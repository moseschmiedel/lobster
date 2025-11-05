import fs from 'node:fs/promises';

import { env } from '$env/dynamic/public';

export async function GET({ params }) {
	const { id } = params;

	try {
		const song = await getSongById(id);
		return new Response(song, {
			headers: {
				'Content-Type': 'audio/mpeg'
			}
		});
	} catch (error) {
		console.log(error);
		return new Response(JSON.stringify({ message: 'Song not found' }), { status: 404 });
	}
}

async function getSongById(id: string) {
	const path = `${env.PUBLIC_SONGS_PATH}/${id}.mp3`;
	const stat = await fs.stat(path);
	if (!stat.isFile()) {
		return Promise.reject(`Song ${path} not found`);
	}
	return fs.readFile(path);
}
