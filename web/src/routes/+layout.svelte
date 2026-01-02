<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.ico';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="shortcut icon" href={favicon} type="image/x-icon">
	<link rel="icon" href={favicon} type="image/x-icon">
</svelte:head>

{@render children()}
