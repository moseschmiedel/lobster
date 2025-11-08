<script lang="ts">
	type Props = {
		src: string;
	};
	const { src }: Props = $props();

	let time = $state(0);
	let duration = $state(0);
	let paused = $state(true);

	function format(time: number) {
		if (isNaN(time)) return '...';

		const minutes = Math.floor(time / 60);
		const seconds = Math.floor(time % 60);

		return `${minutes}:${seconds < 10 ? `0${seconds}` : seconds}`;
	}
</script>

<div class={['player', { paused }]}>
	<audio
		{src}
		bind:currentTime={time}
		bind:duration
		bind:paused
		onloadstart={() => {
			console.log('loading', src);
		}}
		oncanplay={(e) => {
			console.log('playing', src);
			e.currentTarget?.play();
		}}
		onended={() => {
			time = 0;
		}}
	></audio>

	<button
		class="play shadow"
		aria-label={paused ? 'play' : 'pause'}
		onclick={() => (paused = !paused)}
	></button>

	<div class="info">
		<div class="time">
			<span>{format(time)}</span>
			<div
				class="slider"
				onpointerdown={(e) => {
					const div = e.currentTarget;

					function seek(e: PointerEvent) {
						const { left, width } = div.getBoundingClientRect();

						let p = (e.clientX - left) / width;
						if (p < 0) p = 0;
						if (p > 1) p = 1;

						time = p * duration;
					}

					seek(e);

					window.addEventListener('pointermove', seek);

					window.addEventListener(
						'pointerup',
						() => {
							window.removeEventListener('pointermove', seek);
						},
						{
							once: true
						}
					);
				}}
			>
				<div class="progress" style="--progress: {time / duration}%"></div>
			</div>
			<span>{duration ? format(duration) : '--:--'}</span>
		</div>
	</div>
</div>

<style>
	:root {
		--fg: var(--color-amber-500);
		--bg: var(--color-amber-100);
		--text-color: var(--color-gray-600);
		--slider-color: var(--color-gray-100);
	}
	.player {
		display: grid;
		grid-template-columns: 2.5em 1fr;
		align-items: center;
		gap: 1em;
		padding: 0.5em 1em 0.5em 0.5em;
		border-radius: 2em;
		background: var(--bg);
		transition: filter 0.2s;
		color: var(--fg);
		user-select: none;
	}

	.player:not(.paused) {
		color: var(--text-color);
		filter: drop-shadow(0.5em 0.5em 1em rgba(0, 0, 0, 0.1));
	}

	button {
		width: 100%;
		aspect-ratio: 1;
		background-repeat: no-repeat;
		background-position: 50% 50%;
		border-radius: 50%;
		background-color: var(--fg);
	}

	[aria-label='pause'] {
		background-image: url(./pause.svg);
	}

	[aria-label='play'] {
		background-image: url(./play.svg);
	}

	.info {
		overflow: hidden;
		color: var(--text-color);
	}

	.time {
		display: flex;
		align-items: center;
		gap: 0.5em;
	}

	.time span {
		font-size: 0.7em;
	}

	.slider {
		flex: 1;
		height: 0.5em;
		background: var(--slider-color);
		border-radius: 0.5em;
		overflow: hidden;
	}

	.progress {
		width: calc(100 * var(--progress));
		height: 100%;
		background: var(--fg);
	}
</style>
