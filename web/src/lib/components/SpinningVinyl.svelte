<script lang="ts">
	import confetti from 'canvas-confetti';

	let imageLoaded = false;

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
</script>

<div class="relative flex items-center justify-center my-12 transition-opacity duration-1000 ease-out" class:opacity-0={!imageLoaded} class:pointer-events-none={!imageLoaded}>
	<!-- Pulsing circles for beat visualization -->
	<div class="absolute h-56 w-56 rounded-full border-2 border-primary/10 animate-[ping_2s_ease-out_infinite]"></div>
	<!-- Glow effect -->
	<div class="absolute h-48 w-48 rounded-full bg-secondary/40 blur-xl animate-[pulse_1.5s_ease-in-out_infinite]"></div>
	<div class="absolute h-40 w-40 rounded-full bg-secondary blur-lg animate-[pulse_1s_ease-in-out_0.25s_infinite]"></div>
	<!-- Rotating vinyl -->
	<button
		type="button"
		onclick={fireConfetti}
		aria-label="Celebrate"
		class="cursor-pointer bg-transparent border-none p-0 [&_picture]:block [&_picture]:h-48 [&_img]:h-48 [&_img]:w-auto"
	>
		<enhanced:img
			src="../assets/lobster-vinyl.png?w=384;192"
			alt="Spinning Lobster Vinyl"
			sizes="192px"
			fetchpriority="high"
			onload={() => (imageLoaded = true)}
			onerror={() => (imageLoaded = true)}
			class="relative z-10 hover:scale-105 transition-transform animate-[spin_5s_linear_infinite] drop-shadow-[0_0_15px_rgba(255,107,53,0.5)]"
		/>
	</button>
</div>
