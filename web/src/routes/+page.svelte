<script lang="ts">
	import AudioPlayer from '$lib/components/AudioPlayer/AudioPlayer.svelte';
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

<div class="flex h-screen w-full flex-col items-center justify-center gap-4 p-4">
	<h1 class="font-mono text-2xl font-bold">Lobster</h1>
	<div class="overflow-clip rounded-2xl">
		{#if !song}
			<QRScanner height={400} onScan={parseQRCode} />
		{:else}
			<div class="flex h-[400px] flex-col items-center justify-center bg-gray-300 p-4">
				<button
					class="cursor-pointer rounded-md border-s-stone-400 bg-amber-500 p-2 shadow shadow-amber-300 hover:bg-amber-400"
					onclick={scanNewSong}>Nächsten Song scannen</button
				>
			</div>
		{/if}
	</div>
	{#if song}
		<div class="w-[400px]">
			<AudioPlayer src={song.streamUrl} />
		</div>
	{/if}
</div>
