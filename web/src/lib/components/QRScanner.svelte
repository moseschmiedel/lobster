<script lang="ts">
	import QrScanner from 'qr-scanner';

	type Props = {
		width?: number;
		height?: number;
		onScan: (result: string) => void;
	};

	const { onScan, width, height }: Props = $props();

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
		<video bind:this={video} {width} {height} muted class="object-cover object-center"></video>
	{/if}
{/await}
