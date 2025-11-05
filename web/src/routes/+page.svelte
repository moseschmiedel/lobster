<script lang="ts">
	import AudioPlayer from '$lib/components/AudioPlayer.svelte';
	import QRScanner from '$lib/components/QRScanner.svelte';

	type Song = {
		title: string;
		streamUrl: string;
		coverUrl?: string;
	};

	let song: Song | null = $state(null);

	function parseURL(maybeURL: string): string {
		if (maybeURL.startsWith('lobster://')) {
			return `/songs/${maybeURL.replace('lobster://', '')}`;
		}
		if (!maybeURL.startsWith('http://') && !maybeURL.startsWith('https://')) {
			throw new Error('Not a valid URL');
		}
		return maybeURL;
	}

	function parseQRCode(data: string) {
		console.log('Scanned QR Code:', data);
		const audioURl = parseURL(data);
		song = {
			title: 'Scanned Song',
			streamUrl: audioURl
		};
	}

	function scanNewSong() {
		song = null;
	}
</script>

{#if song}
	<AudioPlayer src={song.streamUrl} />
{:else}
	<QRScanner onScan={parseQRCode} />
{/if}

<button
	class="cursor-pointer rounded-md border-s-stone-400 bg-amber-500 p-2 shadow shadow-amber-300 hover:bg-amber-400 hover:shadow-2xl"
	onclick={scanNewSong}>Nächsten Song scannen</button
>
