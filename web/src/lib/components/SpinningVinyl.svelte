<script lang="ts">
	import confetti from 'canvas-confetti';
	import imageSrc from '$lib/assets/lobster-vinyl.png';

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
