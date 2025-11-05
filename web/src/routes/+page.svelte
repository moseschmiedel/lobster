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
		const audioURl = parseURL(data);
		song = {
			title: 'Scanned Song',
			streamUrl: audioURl
		};
	}
</script>

<QRScanner onScan={parseQRCode} />

{#if song}
	<AudioPlayer src={song.streamUrl} />
{/if}
