<script lang="ts">
	import '@fontsource/rammetto-one';
	import '@fontsource/cinzel';
	import '@fontsource/antonio';
	import confetti from 'canvas-confetti';
	import AudioPlayer from '$lib/components/AudioPlayer/AudioPlayer.svelte';
	import QRScanner from '$lib/components/QRScanner.svelte';
	import imageSrc from '$lib/assets/lobster-vinyl.png';

	type Song = {
		title: string;
		streamUrl: string;
		coverUrl?: string;
	};

	let gameStarted = $state(false);

	function startGame() {
		gameStarted = true;
	}

	function fireConfetti(event: MouseEvent) {
		const target = event.currentTarget as HTMLElement;
		const rect = target.getBoundingClientRect();
		const x = (rect.left + rect.width / 2) / window.innerWidth;
		const y = (rect.top + rect.height / 2) / window.innerHeight;
		
		confetti({
			particleCount: 100,
			spread: 360,
			origin: { x, y },
			colors: ['#ff6b35', '#e63946', '#ffb347', '#ffd700']
		});
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
			<div class="w-fit overflow-clip rounded-2xl shadow-2xl shadow-primary/20">
				{#if !song}
					<QRScanner height={400} onScan={parseQRCode} />
				{:else}
					<div
						class="flex h-[400px] w-[336px] flex-col items-center justify-center bg-primary/20 px-1"
					>
						<button
							class="neon-button neon-shadow"
							onclick={scanNewSong}>Nächsten Song scannen</button>
					</div>
				{/if}
			</div>
		{:else}
			<div class="flex flex-col items-center gap-6">
				<div class="relative flex items-center justify-center my-12">
					<!-- Pulsing circles for beat visualization -->
					<div class="absolute h-56 w-56 rounded-full border-2 border-primary/10 animate-[ping_2s_ease-out_infinite]"></div>
					<!-- Glow effect -->
					<div class="absolute h-48 w-48 rounded-full bg-secondary/40 blur-xl animate-[pulse_1.5s_ease-in-out_infinite]"></div>
					<div class="absolute h-40 w-40 rounded-full bg-secondary blur-lg animate-[pulse_1s_ease-in-out_0.25s_infinite]"></div>
					<!-- Rotating vinyl -->
					<button type="button" onclick={fireConfetti} class="cursor-pointer bg-transparent border-none p-0">
						<img src={imageSrc} alt="Dancing Lobster" class="relative z-10 h-48 w-auto hover:scale-105 transition-transform animate-[spin_5s_linear_infinite] drop-shadow-[0_0_15px_rgba(255,107,53,0.5)]" />
					</button>
				</div>
				<a
					href="/anleitung"
					class="neon-shadow cursor-pointer font-[Antonio] text-3xl font-thin tracking-widest text-white opacity-80 transition-opacity hover:opacity-100"
				>
					SPIELANLEITUNG
				</a>
				<button
					class="neon-button neon-shadow"
					onclick={startGame}>Spiel starten!</button>
			</div>
		{/if}
	</div>
	{#if song}
		<div class="w-full">
			<AudioPlayer src={song.streamUrl} />
		</div>
	{/if}
</div>
