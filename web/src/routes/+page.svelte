<script lang="ts">
	import '@fontsource/rammetto-one';
	import '@fontsource/cinzel';
	import '@fontsource/antonio';
	import AudioPlayer from '$lib/components/AudioPlayer/AudioPlayer.svelte';
	import QRScanner from '$lib/components/QRScanner.svelte';
	import SpinningVinyl from '$lib/components/SpinningVinyl.svelte';

	type Song = {
		title: string;
		streamUrl: string;
		coverUrl?: string;
	};

	let gameStarted = $state(false);

	function startGame() {
		gameStarted = true;
	}

	let song: Song | null = $state(null);
	let scannedURL: string[] = $state([]);

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
		if (scannedURL.includes(data)) {
			console.warn('URL already scanned:', data);
			return;
		}
		song = {
			title: 'Scanned Song',
			streamUrl: audioURl
		};
		scannedURL.push(data);
	}

	function scanNewSong() {
		song = null;
		scannedURL = [];
	}
</script>

<div class="flex h-screen w-full flex-col p-8">
	<h1
		class="neon-title neon-shadow inline-block text-center text-6xl md:text-8xl mb-8"
		data-text="Lobster"
	>
		Lo<span class="flicker-slow">b</span>s<span class="flicker-fast">t</span>er
	</h1>
	<div class="relative z-20 flex w-full justify-center pb-12">
		{#if gameStarted}
			{#if !song}
				<div class="w-fit overflow-clip rounded-2xl">
					<QRScanner height={400} onScan={parseQRCode} />
				</div>	
			{:else}
				<div class="flex flex-col items-center justify-center gap-6">
					<SpinningVinyl />
					<div class="w-full">
						<AudioPlayer src={song.streamUrl} />
					</div>
					<button
						class="neon-button"
						onclick={scanNewSong}>Nächsten Song scannen</button>
				</div>
			{/if}
		{:else}
			<div class="flex flex-col items-center gap-6">
				<SpinningVinyl />
				<a
					href="/anleitung"
					class="neon-shadow cursor-pointer font-[Antonio] text-3xl font-thin tracking-widest text-white opacity-80 transition-opacity hover:opacity-100"
				>
					SPIELANLEITUNG
				</a>
				<button
					class="neon-button"
					onclick={startGame}>Spiel starten!</button>
			</div>
		{/if}
	</div>
</div>
