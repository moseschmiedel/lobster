<script lang="ts">
	import '@fontsource/pacifico';
	import '@fontsource/rammetto-one';
	import '@fontsource/cinzel';
	import '@fontsource/antonio';

	import AudioPlayer from '$lib/components/AudioPlayer/AudioPlayer.svelte';
	import QRScanner from '$lib/components/QRScanner.svelte';

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

<div class="flex h-screen w-full flex-col items-center justify-around bg-lobster-yellow/10 p-8 pb-16">
	<div class="relative flex items-center justify-center">
		<div class="ring-container">
			<div class="ring ring-1"></div>
			<div class="ring ring-2"></div>
			<div class="ring ring-3"></div>
			<div class="ring ring-4"></div>
			<div class="ring ring-5"></div>
		</div>
		<h1
			class="relative z-10 p-2 font-[Pacifico] text-6xl font-extrabold text-lobster-red drop-shadow-sm sm:text-8xl lg:text-9xl"
		>
			Lobster
		</h1>
	</div>
	<div class="relative z-20 flex w-full justify-center pb-12">
		{#if gameStarted}
			<div class="w-fit overflow-clip rounded-2xl shadow-2xl shadow-lobster-orange/20">
				{#if !song}
					<QRScanner height={400} onScan={parseQRCode} />
				{:else}
					<div
						class="flex h-[400px] w-[336px] flex-col items-center justify-center bg-lobster-orange/20 px-1"
					>
						<button
							class="w-full cursor-pointer rounded-xl bg-lobster-yellow px-8 py-4 font-bold text-lobster-red shadow-lg shadow-lobster-orange transition-all hover:scale-105 active:scale-95"
							onclick={scanNewSong}>Nächsten Song scannen</button
						>
					</div>
				{/if}
			</div>
		{:else}
			<div class="flex flex-col items-center gap-6">
				<button
					class="cursor-pointer rounded-full bg-linear-to-r from-lobster-red to-lobster-orange px-12 py-6 font-[Rammetto_One] text-2xl text-white shadow-xl shadow-lobster-red/40 transition-all hover:scale-105 hover:shadow-2xl active:scale-95 active:shadow-inner"
					onclick={startGame}>Spiel starten!</button
				>
				<a
					href="/anleitung"
					class="cursor-pointer font-[Antonio] text-3xl font-thin tracking-widest text-lobster-red opacity-80 transition-opacity hover:opacity-100"
				>
					SPIELANLEITUNG
				</a>
			</div>
		{/if}
	</div>
	{#if song}
		<div class="w-full">
			<AudioPlayer src={song.streamUrl} />
		</div>
	{/if}
</div>

<style>
	.ring-container {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		width: 300px;
		height: 300px;
		pointer-events: none;
		z-index: 0;
	}

	.ring {
		position: absolute;
		inset: 0;
		border: 2px solid transparent;
		border-radius: 50%;
		animation: ring-pulse 4s infinite ease-in-out;
	}

	.ring-1 {
		border-color: var(--color-lobster-yellow);
		border-top-color: transparent;
		transform: rotate(45deg);
		animation-delay: 0s;
	}
	.ring-2 {
		border-color: var(--color-lobster-orange);
		border-right-color: transparent;
		border-bottom-color: transparent;
		transform: rotate(-30deg);
		animation-delay: 0.5s;
		width: 92%;
		height: 92%;
		top: 4%;
		left: 4%;
	}
	.ring-3 {
		border-color: var(--color-lobster-orange);
		border-left-color: transparent;
		transform: rotate(120deg);
		animation-delay: 1s;
		width: 84%;
		height: 84%;
		top: 8%;
		left: 8%;
	}
	.ring-4 {
		border-color: var(--color-lobster-red);
		border-bottom-color: transparent;
		border-top-color: transparent;
		transform: rotate(200deg);
		animation-delay: 1.5s;
		width: 76%;
		height: 76%;
		top: 12%;
		left: 12%;
	}
	.ring-5 {
		border-color: var(--color-lobster-red);
		border-left-color: transparent;
		transform: rotate(10deg);
		animation-delay: 2s;
		width: 68%;
		height: 68%;
		top: 16%;
		left: 16%;
	}

	@keyframes ring-pulse {
		0%,
		100% {
			opacity: 0.3;
			transform: scale(1) rotate(0deg);
		}
		50% {
			opacity: 0.6;
			transform: scale(1.05) rotate(10deg);
		}
	}
</style>
