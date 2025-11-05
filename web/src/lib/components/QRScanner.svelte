<script lang="ts">
	import QrScanner from 'qr-scanner';

	type Props = {
		onScan: (result: string) => void;
		disabled?: boolean;
	};

	const { onScan, disabled }: Props = $props();

	let video: HTMLVideoElement | null = $state(null);

	function onDecode(result: QrScanner.ScanResult) {
		onScan(result.data);
	}

	$effect(() => {
		if (video) {
			const scanner = new QrScanner(video, onDecode, {
				preferredCamera: 'environment',
				highlightScanRegion: true
			});
			scanner.start();

			if (disabled) {
				scanner.stop();
			}

			return () => {
				scanner.stop();
				scanner.destroy();
			};
		}
	});
</script>

{#await QrScanner.hasCamera() then hasCamera}
	{#if !hasCamera}
		<p>No camera found on this device.</p>
	{:else}
		<p>Point your camera at a QR code to scan a song.</p>
		<video bind:this={video} muted></video>
	{/if}
{/await}
