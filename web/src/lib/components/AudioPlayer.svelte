<script lang="ts">
	import { onMount } from 'svelte';

	type Props = {
		src: string;
	};
	const { src }: Props = $props();

	let audio: HTMLAudioElement;

	onMount(() => {
		audio.load();
		audio.play();
	});
</script>

<audio bind:this={audio} controls>
	<source {src} type="audio/mpeg" />
	Your browser does not support the audio element.
</audio>
