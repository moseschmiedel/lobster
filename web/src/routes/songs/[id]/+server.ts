import fs from 'node:fs';
import path from 'node:path';
import { Readable } from 'node:stream';

import { env } from '$env/dynamic/public';

export async function GET({ request, params }) {
	const { id } = params;

	try {
		const song = await getSongById(id);
		const range = checkRangeHeader(song, request.headers.get('Range'));

		if (range.type === 'invalid') {
			return new Response(range.reason, {
				status: 416,
				headers: {
					'Content-Range': `bytes */${song.size}`
				}
			});
		}

		const stream = await streamSongPartially(
			song,
			range.type === 'range' ? range.range : undefined
		);

		if (range.type === 'full') {
			return new Response(stream, {
				status: 206, // Partial Content
				headers: {
					'Content-Type': 'audio/mpeg',
					'Accept-Ranges': 'bytes',
					'Content-Length': String(song.size)
				}
			});
		}

		let { start, end } = range.range;

		return new Response(stream, {
			status: 206, // Partial Content
			headers: {
				'Content-Type': 'audio/mpeg',
				'Accept-Ranges': 'bytes',
				'Content-Range': `bytes ${start}-${end}/${song.size}`,
				'Content-Length': String(end - start + 1)
			}
		});
	} catch (error) {
		console.log(error);
		return new Response(JSON.stringify({ message: 'Song not found' }), { status: 404 });
	}
}

type Song = {
	path: string;
	contentType: string;
	size: number;
};

async function getSongById(id: string): Promise<Song> {
	const songPath = path.join(env.PUBLIC_SONGS_PATH, `${id}.mp3`);
	const stat = await fs.promises.stat(songPath);
	if (!stat.isFile()) {
		return Promise.reject(`Song ${songPath} not found`);
	}

	return {
		size: stat.size,
		contentType: 'audio/mpeg',
		path: songPath
	};
}

type Range = {
	start: number;
	end: number;
};

type CheckRangeHeaderResult =
	| { type: 'range'; range: Range }
	| { type: 'full' }
	| { type: 'invalid'; reason: string };

function checkRangeHeader(song: Song, range: string | null): CheckRangeHeaderResult {
	let start = 0;
	let end = song.size - 1;

	if (!range) return { type: 'full' };

	// Example: "bytes=0-1023"
	const match = /bytes=(\d*)-(\d*)/.exec(range);

	if (match) {
		const rangeStart = match[1] ? parseInt(match[1], 10) : 0;
		const rangeEnd = match[2] ? parseInt(match[2], 10) : song.size - 1;

		start = Number.isNaN(rangeStart) ? 0 : rangeStart;
		end = Number.isNaN(rangeEnd) ? song.size - 1 : rangeEnd;

		// Clamp
		if (start > end || start >= song.size) {
			return {
				type: 'invalid',
				reason: 'Range Not Satisfiable'
			};
		}
	}

	return { type: 'range', range: { start, end } };
}

async function streamSongPartially(song: Song, range?: Range): Promise<ReadableStream> {
	const stream = fs.createReadStream(song.path, {
		start: range?.start,
		end: range?.end
	});

	// Convert Node stream to Web ReadableStream
	return Readable.toWeb(stream) as unknown as ReadableStream;
}
