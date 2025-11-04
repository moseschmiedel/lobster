<script lang="ts">
	import QRScanner from 'qr-scanner';

	type Song = {
		title: string;
		streamUrl: URL;
		coverUrl?: URL;
	};

	let video: HTMLVideoElement | null = $state(null);
	let song: Song | null = $state({
		title: 'Test Song',
		streamUrl: new URL('https://www.youtube.com/watch?v=ssKmVgTtMnc')
	});

	function parseURL(maybeURL: string): URL {
		if (!maybeURL.startsWith('http://') && !maybeURL.startsWith('https://')) {
			throw new Error('Not a valid URL');
		}
		const url = new URL(maybeURL);
		song = {
			title: url.searchParams.get('title') || 'Unknown Title',
			streamUrl: url
		};
		return url;
	}

	function parseQRCode(qrResult: QRScanner.ScanResult) {
		const url = parseURL(qrResult.data);
	}

	$effect(() => {
		if (video) {
			const scanner = new QRScanner(video, parseQRCode, {
				preferredCamera: 'environment',
				highlightScanRegion: true
			});
			scanner.start();

			return () => {
				scanner.stop();
				scanner.destroy();
			};
		}
	});
</script>

{#await QRScanner.hasCamera() then hasCamera}
	{#if !hasCamera}
		<p>No camera found on this device.</p>
	{:else if song}
		<h2>Now Playing: {song.title}</h2>
		<video src={song.streamUrl.toString()} controls autoplay><track kind="captions" /></video>
	{:else}
		<p>Point your camera at a QR code to scan a song.</p>
		<video bind:this={video} muted></video>
	{/if}
{/await}
