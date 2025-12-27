<script lang="ts">
	import '@fontsource/pacifico';
	import '@fontsource/antonio';
	import '@fontsource/rammetto-one';

	import cardsIcon from '$lib/assets/instructions/cards.png';
	import peopleIcon from '$lib/assets/instructions/people.png';
	import noMusicIcon from '$lib/assets/instructions/no_music.png';
	import lobsterIcon from '$lib/assets/instructions/lobster.png';

	let activeTab = $state('basics');

	const tabs = [
		{ id: 'basics', label: 'THE BASICS', title: 'Der Spielablauf' },
		{ id: 'extras', label: 'EXTRAS', title: 'Sonderregeln & Spielideen' }
	];
</script>

<div
	class="flex min-h-screen w-full flex-col items-center bg-lobster-yellow/10 p-4 font-[Antonio]"
>
	<!-- Header -->
	<header class="mb-8 mt-4 flex w-full max-w-4xl flex-col items-center">
		<a href="/" class="mb-8 font-[Pacifico] text-4xl text-lobster-red no-underline transition-transform hover:scale-105">
			Lobster
		</a>
		<h1 class="text-center text-4xl font-thin tracking-widest text-lobster-red uppercase sm:text-6xl md:text-7xl">
			SPIELANLEITUNG
		</h1>
	</header>

	<!-- Tabs -->
	<div class="mb-12 flex w-full max-w-4xl flex-wrap justify-center gap-4">
		{#each tabs as tab}
			<button
				class="rounded-full px-8 py-3 text-xl font-light tracking-wide transition-all uppercase
        {activeTab === tab.id
					? 'bg-lobster-red text-white shadow-lg shadow-lobster-red/30'
					: 'bg-white text-lobster-orange hover:bg-lobster-orange/10'}"
				onclick={() => (activeTab = tab.id)}
			>
				{tab.label}
			</button>
		{/each}
	</div>

	<!-- Content -->
	<div class="relative w-full max-w-2xl">
		{#each tabs as tab}
			{#if activeTab === tab.id}
				<div
					class="w-full animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white p-8 rounded-3xl shadow-xl shadow-lobster-orange/10 border border-lobster-orange/10"
				>
					<h2
						class="mb-6 bg-linear-to-r from-lobster-red to-lobster-orange bg-clip-text text-4xl font-bold text-transparent"
					>
						{tab.title}
					</h2>

					<div class="space-y-6 text-xl leading-relaxed text-stone-600 font-sans">
						{#if tab.id === 'basics'}
							<div class="space-y-6">
								<p>
									Jede:r von euch bekommt eine Startkarte, die er oder sie offen vor sich hinlegen
									darf und einen Lobster-Point. Scannt dann den QR-Code mit der App auf der nächsten
									Musikkarte und startet den Song.
								</p>
								<p>
									Es beginnt die Person, die als letztes irgendetwas mit Hummern zu tun gehabt hat.
									Danach geht es der Reihe nach weiter.
								</p>
								<p>
									Ratet, wann der jeweilige Song erschienen ist, und legt die Karte an die richtige
									Position auf eurem Musik-Zeitstrahl.
								</p>
								<div class="rounded-xl bg-orange-50 p-4 shadow-inner">
									<p class="mb-2 font-bold text-lobster-red">ACHTUNG:</p>
									<p class="mb-2">
										Die gesungene Sprache ist für das Erscheinungsdatum relevant. <br />
										<span class="italic text-stone-500"
											>Beispiel: „Our God“ von Chris Tomlin ist 2010 erschienen, die deutsche
											Übersetzung „So bist nur du“ 2011.</span
										>
									</p>
									<p>
										Außerdem ist es sehr schwer zu jedem christlichen Lied eine Originalaufnahme zu
										finden. Findet ihr dieses Symbol <img
											src={noMusicIcon}
											alt="Cover Symbol"
											class="inline-block h-8 w-auto align-middle"
										/> auf der Vorderseite der Karte, bedeutet das, dass diese Version des Songs nicht
										von der oder dem originalen Künstler:in stammt. Findet ihr kein Symbol auf der Vorderseite,
										ist es eine Originalaufnahme oder zumindest eine Aufnahme von der oder dem jeweiligen
										Künstler:in.
									</p>
								</div>
								<div>
									<h3 class="font-[Antonio] text-2xl uppercase text-lobster-red">Lobstern</h3>
									<p>
										Alle Mitspielenden haben die Chance ihre Lobster-Points einzusetzen, falls sie
										denken, dass die Karte falsch einsortiert ist. Bevor die Karte umgedreht wird,
										dürfen sie ihren Lobster-Point an die entsprechende Stelle legen, bei der sie
										denken, dass die Karte hingehören würde. Liegen sie richtig, gehört die Karte
										ihnen und sie dürfen sie auf ihrem eigenen Zeitstrahl einordnen. Alle
										eingesetzten Lobster-Points kommen danach zurück in die Verpackung.
									</p>
								</div>
								<div>
									<h3 class="font-[Antonio] text-2xl uppercase text-lobster-red">Gewinnen</h3>
									<p>
										Ihr könnt Lobster-Points gewinnen, indem ihr während eures Zuges den richtigen
										Titel des Songs und mindestens einen der Namen der Künstler:innen nennt. Ein
										Lobster-Point kann auch gewonnen werden, wenn die Karte nicht richtig auf dem
										Zeitstrahl einsortiert wurde.
									</p>
									<p class="mt-4 font-bold">
										Gewonnen hat die Person, die zuerst 8 Karten auf ihrem Zeitstrahl liegen hat.
									</p>
								</div>
								<p class="text-sm italic text-stone-400">
									Übrigens: Das Spiel hat immer Recht. Zu manchen Songs existieren unterschiedliche
									Erscheinungsdaten, wir haben uns nach einem ausgeklügelten Auswahlsystem für
									bestimmte Daten entschieden und damit hat das Spiel immer Recht.
								</p>
							</div>
						{:else if tab.id === 'extras'}
							<div class="space-y-8">
								<p class="font-bold text-stone-800">
									Sonderregeln und Spielideen, um das Spiel beliebig zu erweitern:
								</p>

								<!-- Zusätzliche Lobster- Points -->
								<div>
									<h3 class="mb-2 font-[Antonio] text-2xl uppercase text-lobster-red">
										Zusätzliche Lobster-Points
									</h3>
									<p class="mb-2 text-sm italic text-stone-500">
										Gilt immer nur für die Person, die an der Reihe ist.
									</p>
									<ul class="list-disc space-y-2 pl-6 marker:text-lobster-red">
										<li>
											Falls man nur den Titel oder Künstler:in kennt, kann man trotzdem einen
											Lobster-Point gewinnen, indem man einen coolen Tanzmove macht.
										</li>
										<li>
											Man kann einen Lobster-Point gewinnen, indem man den kompletten Chorus ohne
											Musik richtig singt. Wichtig dafür ist, dass der Chorus nicht angehört und der
											Song vorher pausiert wurde.
										</li>
									</ul>
								</div>

								<!-- Hummer-Lobster-Point -->
								<div>
									<h3 class="mb-2 flex items-center gap-2 font-[Antonio] text-2xl uppercase text-lobster-red">
										Hummer-Lobster-Point <img
											src={lobsterIcon}
											alt="Lobster"
											class="h-10 w-auto object-contain"
										/>
									</h3>
									<p class="mb-2">
										Sobald eine Person ihre sechste Karte auf dem Zeitstrahl anlegt, bekommt die
										Person mit den wenigsten Karten auf dem Zeitstrahl den Hummer-Lobster-Point.
									</p>
									<p class="mb-2 text-sm italic text-stone-500">
										Sollte es mehrere Personen mit gleich wenig Karten geben, bekommen alle einen
										Hummer-Lobster-Point. Sollten das mehr als drei Leute sein, muss darum
										geschnickt werden.
									</p>
									<p class="mt-4 font-bold text-lobster-red">Die Funktion:</p>
									<p>
										Mit diesem Hummer-Lobster-Point hat man die Chance Karten zu klauen. Ist man
										nicht an der Reihe, aber nennt schneller den Titel des Songs, als die Person,
										die an der Reihe ist, darf man die Karte auf dem eigenen Zeitstrahl
										einsortieren. Das Datum muss nicht erkannt werden. Danach kommt der
										Hummer-Lobster-Point aus dem Spiel.
									</p>
									<p class="mt-2 text-sm font-bold text-stone-500">
										Falls ein falscher Titel genannt wird, verfällt der Hummer-Lobster-Point
										sofort und wird aus dem Spiel genommen.
									</p>
								</div>

								<!-- Würfeledition -->
								<div>
									<h3 class="mb-4 font-[Antonio] text-2xl uppercase text-lobster-red">
										Würfeledition
									</h3>
									<p class="mb-4">
										Vor jedem Zug wird gewürfelt und die Runde entsprechend angepasst. Nach
										Ausführen der verschiedenen Aktionen, ist die nächste Person an der Reihe und
										würfelt.
									</p>
									<div class="grid gap-4 sm:grid-cols-2">
										<div class="rounded-xl border border-stone-200 bg-white p-4">
											<h4 class="mb-2 font-bold text-stone-400">⬜ Leere Seite</h4>
											<p>Ganz normales Spiel.</p>
										</div>
										<div class="rounded-xl border border-lobster-yellow bg-lobster-yellow/10 p-4">
											<h4 class="mb-2 flex items-center gap-2 font-bold text-lobster-orange">
												<img src={peopleIcon} alt="Menschen" class="h-8 w-8 object-contain" /> Menschen
											</h4>
											<p>
												Hier geht es um die Wurst – alle dürfen mitraten, wer zuerst den Songtitel
												errät, darf die Karte bei sich auf den Zeitstrahl legen. Das Datum muss nicht
												erraten werden. Bei einem Stechen muss zusätzlich der oder die Künstler:in
												genannt werden.
											</p>
										</div>
										<div class="rounded-xl border border-lobster-red bg-lobster-red/10 p-4">
											<h4 class="mb-2 flex items-center gap-2 font-bold text-lobster-red">
												<img src={lobsterIcon} alt="Lobster" class="h-8 w-auto object-contain" /> Hummer
											</h4>
											<p>
												Zunächst wird die Runde wie gewohnt gespielt, falls die Karte richtig auf
												dem Zeitstrahl eingeordnet wurde oder eine Person richtig mit ihrem
												Lobster-Point gelobstert hat, gilt folgende Regel: Die Person, die richtig
												lag, darf von einer anderen mitspielenden Person eine Karte aus dem
												Zeitstrahl klauen und sie auf einem anderen Zeitstrahl einsortieren. <br />
												<strong class="text-xs uppercase tracking-wide text-lobster-red"
													>Wichtig: Die Karte darf NICHT auf dem eigenen Zeitstrahl angelegt
													werden.</strong
												>
											</p>
										</div>
										<div class="rounded-xl border border-purple-200 bg-purple-50 p-4">
											<h4 class="mb-2 flex items-center gap-2 font-bold text-purple-600">
												<img src={cardsIcon} alt="Zwei Karten" class="h-8 w-8 object-contain" /> Zwei
												Karten
											</h4>
											<p>
												Hier darf in die nächsten beiden Songs vom Stapel reingehört werden, danach
												muss sich für eine der beiden Karten entschieden werden, um sie wie gewohnt
												auf dem eigenen Zeitstrahl einzusortieren.
											</p>
										</div>
									</div>
								</div>

								<!-- Memory -->
								<div>
									<h3 class="mb-2 font-[Antonio] text-2xl uppercase text-lobster-red">
										Memory
									</h3>
									<p>
										Übrigens - Jedes Foto kommt genau zweimal vor. Was könnte man wohl damit spielen?
									</p>
								</div>
							</div>
						{/if}
					</div>
				</div>
			{/if}
		{/each}
	</div>

	<a
		href="/"
		class="mt-12 text-lg text-lobster-red/60 hover:text-lobster-red transition-colors"
	>
		Zurück zum Start
	</a>
</div>
