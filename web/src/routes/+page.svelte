<script lang="ts">
	import '@fontsource/pacifico';
	import '@fontsource/rammetto-one';

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

<div class="flex h-screen w-full flex-col items-center justify-center gap-4 bg-amber-50 p-4">
	<div>
		<h1
			class="bg-linear-to-br from-amber-500 to-amber-200 bg-clip-text p-2 font-[Pacifico] text-5xl font-extrabold text-transparent"
		>
			Lobster
		</h1>
	</div>
	<div class="flex w-full justify-center">
		{#if gameStarted}
			<div class="w-fit overflow-clip rounded-2xl">
				{#if !song}
					<QRScanner height={400} onScan={parseQRCode} />
				{:else}
					<div
						class="flex h-[400px] w-[336px] flex-col items-center justify-center bg-gray-300 px-1"
					>
						<button
							class="cursor-pointer rounded-md border-s-stone-400 bg-amber-500 p-2 shadow shadow-amber-300 hover:bg-amber-400"
							onclick={scanNewSong}>Nächsten Song scannen</button
						>
					</div>
				{/if}
			</div>
		{:else}
			<button
				class="cursor-pointer rounded-md bg-linear-to-br from-emerald-400 to-lime-300 p-4 font-[Rammetto_One] text-2xl text-white shadow-md shadow-lime-400 hover:from-emerald-300"
				onclick={startGame}>Spiel starten!</button
			>
		{/if}
	</div>
	{#if song}
		<div class="w-full">
			<AudioPlayer src={song.streamUrl} />
		</div>
	{/if}
</div>
