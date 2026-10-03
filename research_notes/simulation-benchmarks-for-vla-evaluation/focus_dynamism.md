# Dynamism / fast-reaction benchmarks for VLA and generalist robot policies (2023 – Oct 2026)

Scope: benchmarks NOT in `already_listed.txt` that test fast reaction, timing, inference latency, control frequency or real-time execution. Companion file: `focus_dynamism.entries.json` (11 entries). Facts below were read from the arXiv PDFs (text extracted locally) or from the pages linked, in this session. Web search stopped early: the session's search budget ran out after the queries listed under "Gaps" in the last section, so coverage of obscure 2026 preprints is incomplete.

## Real-time execution and latency evaluation suites (RTC, VLASH, A2C2, DynamicVLA, "Faster and Better?", VLAQuantBench, SmolVLA async)

### Takeaway
Only one of these is a reusable, widely adopted latency benchmark: the 12-task Kinetix suite released with Real-Time Chunking, now reused by at least 14 follow-up papers; the rest are either real-robot protocols that cannot be copied without the same tasks (RTC injected delay, VLASH ping-pong, SmolVLA async) or benchmarks that do not model latency at all ("Faster and Better?", VLAQuantBench).

### Cited Findings
- RTC builds "a benchmark of 12 dynamic tasks in Kinetix, which uses force-based control, so inference delay necessitates asynchronous execution (there is no concept of 'holding position')": 10 existing environments plus 2 new ones, Gaussian action noise, 4-layer MLP-Mixer flow policies with prediction horizon H=8, delays d=0–4 control steps, 2,048 rollouts per data point, metric = binary solve rate versus delay and versus execution horizon — [RTC paper](https://arxiv.org/abs/2506.07339)
- RTC's stated motivation: "Most simulated imitation learning benchmarks are quasi-static, and standard chunked execution with a long enough execution horizon can achieve near-perfect success rates" — [RTC paper](https://arxiv.org/abs/2506.07339)
- RTC real-robot protocol: pi0.5 (H=50, 20 ms control period) on a bimanual system with two 6-DoF arms; six tasks (light candle with a match, plug ethernet, make bed, shirt folding, batch folding, dishes in sink); model latency 76 ms (baselines) / 97 ms (RTC) plus 10–20 ms LAN; +100 ms and +200 ms injected latency (d≈11 and 16); 10 trials per task and method, 480 episodes, 28 hours; metric = average throughput (proportion of task completed / episode duration). RTC shows no degradation with injected delay, synchronous inference degrades linearly, and both temporal-ensembling variants trigger protective stops at +100/+200 ms — [RTC paper](https://arxiv.org/abs/2506.07339)
- RTC is listed as published at NeurIPS 2025 — [arXiv listing](https://arxiv.org/abs/2506.07339). The Kinetix code is public (MIT licence, checkpoints and data on a GCS bucket, also contains the training-time RTC experiments) — [GitHub](https://github.com/Physical-Intelligence/real-time-chunking-kinetix)
- Papers opened in this session that evaluate on the RTC Kinetix benchmark: training-time RTC ([2512.05964](https://arxiv.org/abs/2512.05964)), A2C2 ([2509.23224](https://arxiv.org/abs/2509.23224)), VLASH ([2512.01031](https://arxiv.org/abs/2512.01031)), Masked Action Chunking, ICLR 2026 ([2601.20130](https://arxiv.org/abs/2601.20130)), Legato ([2602.12978](https://arxiv.org/abs/2602.12978)), FASTER ([2603.19199](https://arxiv.org/abs/2603.19199)), async-inference comparison ([2605.08168](https://arxiv.org/abs/2605.08168)), DEFLECT ([2605.19294](https://arxiv.org/abs/2605.19294)), real-time autoregressive policies ([2606.13355](https://arxiv.org/abs/2606.13355)), Action ControlNet ([2606.25985](https://arxiv.org/abs/2606.25985)), Reflex streaming inference, ICML 2026 ([2607.14695](https://arxiv.org/abs/2607.14695)), FutureRTC ([2607.24008](https://arxiv.org/abs/2607.24008)), Real-Time EXPO-FT ([2609.18207](https://arxiv.org/abs/2609.18207)), DSDyn-VLA ([2609.39198](https://arxiv.org/abs/2609.39198))
- FASTER notes the limitation: "the policy used in this benchmark is a simple 4-layer MLP rather than a VLA model, so it is not the primary focus of our study" — [FASTER](https://arxiv.org/abs/2603.19199)
- "Understanding Asynchronous Inference Methods for VLA Models" (single author, bachelor thesis, 4 May 2026) puts inference-time RTC, training-time RTC, VLASH and A2C2 in two unified codebases: Kinetix (10 environments, H∈{16,30}, d up to 15, 2,048 rollouts) and LIBERO with SmolVLA (40 tasks, 10 rollouts per task per delay, d∈{0,1,2,4,8,15,20}, s=50). A2C2 holds above 90% solve rate up to d=8 on Kinetix and leads on LIBERO from d≥4; at d=0 on LIBERO inference-time RTC is about 75% and A2C2 about 70%. It argues earlier work stopped at d=4, i.e. 80 ms at 50 Hz, while cloud inference can reach d=13 or more — [paper](https://arxiv.org/abs/2605.08168); code: [GitHub](https://github.com/TheAyos/async-vla-inference)
- A2C2 evaluates on "the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial" with injected delay and reports +23 and +7 percentage points over RTC; no real-robot experiment appears in the text ("All experiments were conducted on publicly available datasets"); Kinetix code released — [A2C2](https://arxiv.org/abs/2509.23224)
- VLASH: Kinetix (delays 0–4) and LIBERO in simulation; real robots Galaxea R1 Lite and SO-101; maximum reaction latency for pi0.5 (K=25 at 50 Hz) is 546.4 ms synchronous vs 46.4 ms VLASH on an H100 (11.8×); real dynamic tasks with pi0.5: ping-pong single-return hit rate 11/20 (55%) vs 0/20 for sync, naive async and RTC; whack-a-mole average score 28.8 vs 3.2 (sync), 8.6 (naive async), 11.0 (RTC) — [VLASH](https://arxiv.org/abs/2512.01031); code: [GitHub](https://github.com/mit-han-lab/vlash)
- FASTER introduces a reactivity metric, Time to First Action (TTFA), models reaction time as a uniform random variable set by TTFA and the execution horizon, compares methods by the probability of reacting faster than sync/async on RTX 4090 and 4060, and demonstrates a real table-tennis task with pi0.5 and X-VLA — [FASTER](https://arxiv.org/abs/2603.19199)
- DynamicVLA's DOM benchmark is already catalogued; its real-world part uses a second robot arm to launch objects along predefined trajectories, 20 trials × 3 motion–position configurations per task, 960 real trials per method on Franka and AgileX PiPER — [DynamicVLA](https://arxiv.org/abs/2601.22153)
- SmolVLA async evaluation (three real-world tasks; the paper's real datasets use SO-100 and SO-101 arms): success sync 78.3% vs async 73.3% averaged over pick-place, stacking, sorting; task completion time 13.75 s (sync) vs 9.70 s (async); cubes moved in a fixed time window 1.8 (sync) vs 3.8 (async) — [SmolVLA](https://arxiv.org/abs/2506.01844)
- "Faster and Better?" (arXiv 2609.37771, 29 Sep 2026) is an audit, not a latency protocol: it finds 22 bugs and 4 design limitations across seven benchmarks (RoboTwin, LIBERO-Plus, VLABench, LIBERO-PRO named in the text) that make training-free acceleration methods appear better than the baseline; it revises success checkers, corrects object masses and adds a motion-aware score; fixing a bug raises the baseline by 52.8 points on one LIBERO-PRO task and a mass fix moves the baseline from 21 points behind to 5 points ahead on a RoboTwin task — [paper](https://arxiv.org/abs/2609.37771)
- VLAQuantBench (arXiv 2609.25376): 409 runs and 94,574 simulation episodes measuring closed-loop success of post-training-quantized VLAs (four models on LIBERO; X-VLA on three more benchmark families) plus physical-robot precision comparisons; in its kernel measurements on an RTX 4090 "all quantized paths are slower than BF16" — [paper](https://arxiv.org/abs/2609.25376); code: [GitHub](https://github.com/jiuyixu25/VLAQuantBench)
- "Toward Real-Time VLAs" (Magiclab, 30 Sep 2026) compares six execution methods (naive async, temporal smoothing, inference-time RTC, training-time RTC, VLASH, Legato) on one physical bimanual garment-folding task with pi0.5, 30 trials per method (180 total), after calibrating camera, communication and actuation latency. Legato 29/30 (73.56 s, 47.31 successful tasks/h), VLASH 28/30 (43.22/h), temporal smoothing 23/30 (29.38/h), training-time RTC and naive async 19/30; "A higher replanning rate alone therefore does not guarantee better task performance" — [paper](https://arxiv.org/abs/2609.39822); code: [GitHub](https://github.com/MagiclabRobotics/Inference)
- VLA-Perf is an analytical roofline model of VLA inference latency and throughput across hardware and network settings; it explicitly excludes task success ("performance always refers to inference latency and throughput, rather than task success rate") — [VLA-Perf](https://arxiv.org/abs/2602.18397)
- vla.cpp reports real-robot success against round-trip latency: SmolVLA on a UR10e cup pick-and-place, S=25 actions at 20 Hz with blocking execution, latency 111.4–3,652.9 ms across four backends (effective rate 17.7 → 5.0 Hz), 20 episodes per backend — [vla.cpp](https://arxiv.org/abs/2606.08094)
- SmolVLA-on-LIBERO deployment study: PyTorch+AMP 70.0%/88.0% (Spatial/Object) at 1,181 ms p99 vs ONNX exports at 601/532 ms p99 with Spatial success falling to 41.0%/40.0%; latency is reported next to success but the simulator is the standard LIBERO loop — [paper](https://arxiv.org/abs/2609.14146)

### Inferences
- Reusable by others today: RTC Kinetix (code + data), async-vla-inference (code), Magiclab framework (code, but one task on their robot). Protocol-only (copyable idea, not copyable tasks): RTC injected delay, VLASH ping-pong / whack-a-mole, SmolVLA sync-vs-async, FASTER TTFA.
- The Kinetix suite measures delay robustness of the execution scheme, not of a VLA: no vision, no language, tiny policies. A benchmark that combines Kinetix-style forced asynchrony with image-conditioned VLAs is what MotionForge, ReflexBench and DynamicManip (below) are attempting.
- LIBERO-with-injected-delay (A2C2, VLASH, DEFLECT, async-vla-inference) only makes the robot's own state stale; the scene is quasi-static, so it under-tests reaction to external motion. FASTER and the Reflex paper say this directly about LIBERO.
- "Faster and Better?" and VLAQuantBench are about whether acceleration preserves success under a paused simulator; neither rewards being faster.

### Gaps
- Venues for A2C2, VLASH, FASTER, DEFLECT and Legato were not confirmed (arXiv only in what I opened).
- RTC real-task throughput values are only in a figure; no table was available to quote.
- I did not find a public leaderboard for any latency benchmark.

## Real-world dynamic manipulation benchmarks (conveyor, catching, ball games, handover, disturbance)

### Takeaway
No standing real-world benchmark for fast-reaction VLA evaluation was found outside the already-catalogued ones; real dynamic evaluation of VLAs lives in per-paper task sets (conveyor picking, rolling balls, ping-pong, catching), and the only reproducible fast-object competitions (Robot Air Hockey) have no VLA entries.

### Cited Findings
- Robot Air Hockey Challenge (NeurIPS 2023 competition; retrospective in the NeurIPS 2024 Datasets and Benchmarks track): two KUKA LBR iiwa 14 arms, 1000 Hz simulation and 50 Hz control; sub-tasks Hit, Defend, Prepare, then full games; a deployability score penalises constraint violations and "Computation Time [0.5-2 pts]: The computation time at each step should be shorter than 0.02 s"; qualifying stage runs 1,000 episodes per sub-task; top three teams were deployed on the real table and "for every team, the performance in the real robot system was considerably worse than in the simulated setting". The authors frame it as "removing the typical assumption of quasi-static motions of other real-world benchmarks" — [retrospective](https://arxiv.org/abs/2411.05718)
- A 2025 edition exists: qualifying to 21 Sep 2025, simulated tournament to 12 Oct 2025, real-world finals 3–16 Nov 2025 for the top four teams, award ceremony at an IROS workshop, organisers from TU Darmstadt and Huawei, public code and leaderboard — [challenge site](https://air-hockey-challenge.robot-learning.net/); code: [GitHub](https://github.com/AirHockeyChallenge/air_hockey_challenge)
- Robot Air Hockey testbed (Chuck et al., May 2024): UR5 arm with 60 Hz overhead camera, Box2D and robosuite simulators plus real robot; "five tasks on the real robot, six tasks in Robosuite, and ten tasks in Box2D"; evaluated with behaviour cloning, offline RL and RL from scratch; the authors note "maintaining low latency is challenging" and that at "20Hz or 50ms, even humans can struggle" — [paper](https://arxiv.org/abs/2405.03113)
- AHEAD (CMU, June 2026) real tasks on a UFactory xArm 7 with a frozen OpenVLA plus a world-model wrapper: 29/30–30/30 on two conveyor tasks and a rolling-ball task, 23/30 paddle interception, 19/30 projectile catching with a launcher 2 m away where every baseline scores 0/30; conveyor speed sweep 0–25 cm/s; full pipeline about 158 ms per action step — [AHEAD](https://arxiv.org/abs/2606.02486)
- DSDyn-VLA real dynamic tasks: real-world success rises from 8.4% with pi0.5 to 49.0% — [DSDyn-VLA](https://arxiv.org/abs/2609.39198)
- RLDX-1 (ALLEX humanoid): on conveyor pick-and-place "RLDX-1 reaches a success rate of over 87.5% while π0.5 remains below 29.2%" — [RLDX-1 report](https://arxiv.org/abs/2605.03269)
- ForeTime-VLA conveyor-belt evaluation on a mobile manipulator: 44/90 grasps across three belt speeds vs 23/90 for pi0.5, 11/30 vs 2/30 at the fast speed; dataset of 458 episodes at 15 Hz — [ForeTime-VLA](https://arxiv.org/abs/2608.20735)
- DynamicWAM: 12 real-world tasks with linear, circular and compound target motion, 46.7% average success, 22.9 points above the strongest baseline, using RTC for asynchronous execution — [DynamicWAM](https://arxiv.org/abs/2608.00793)
- Real-Time EXPO-FT (Stanford, Sept 2026): four dynamic real tasks — robot object passing, ball balancing, table soccer kicking, dynamic object picking — average success 42% (12.5/30) → 97% (29/30) with 10 minutes of online data — [paper](https://arxiv.org/abs/2609.18207)
- TEMPO (UC Irvine; the PDF thanks CoRL reviewers): four dynamic real tasks on a bimanual platform — Bottle Handover, Drop Catch, Flick Catch, Wine Pour — 50 trials per task, compared against RTC and VLASH; Bottle Handover improves 44% → 74%. It also releases TEMPO-Bench, "over 50k annotated frames for evaluating motion-aware robot perception" in regression and multiple-choice form, which is a perception benchmark, not a policy benchmark — [TEMPO](https://arxiv.org/abs/2609.16864)
- "Running VLAs at Real-time Speed" (Dexmal): pi0-level VLA at 30 Hz; falling-pen grasp with end-to-end reaction under 200 ms and 100% success, 600 training episodes — [paper](https://arxiv.org/abs/2510.26742); code: [GitHub](https://github.com/Dexmal/realtime-vla)
- HRIBench (July 2026) simulates a human who instructs, hands over to, or interrupts the robot: 13 role-conditioned tasks, 650+ evaluation episodes, metrics include Completion Time, Temporal Synchronization, Response Latency and Disruption Success Rate; GR00T N1.5-LoRA, pi0.5-LoRA and ACT reach best collaboration success of 0.533 (Instructor), 0.500 (Collaborator) and 0.100 (Intruder); real-robot adaptation study raises GR00T N1.5 from 0.10 to 0.43 — [HRIBench](https://arxiv.org/abs/2607.13056)
- DexH2R (ShanghaiTech, arXiv July 2025) is a real-world human-to-robot handover dataset for a dexterous hand (4,282 trials, 39 participants, 56 objects per the search listing) with an offline benchmark of motion-generation methods scored on grasp success under perturbing forces, penetration and trajectory metrics — [DexH2R](https://arxiv.org/abs/2506.23152)
- Human-perturbation protocols found inside method papers: VLA-Corrector evaluates a "Disturbance recovery" task group on an AgileX PiPER where "objects or targets are manually shifted during execution" (pi0.5 40.0% → 68.3%, 3 tasks × 20 trials) — [VLA-Corrector](https://arxiv.org/abs/2607.01804); RePO-VLA's FRBench has real bimanual tasks under "adversarial" human perturbation (10 trials per task) and a RoboTwin part with 46 tasks and 23,453 episodes where a grasp disturbance is injected by holding the gripper open for 30 frames — [RePO-VLA](https://arxiv.org/abs/2605.09410)
- REAL-I Challenge (already catalogued) on-site scenes at ICRA 2026 include "Metal Parts Righting: flip small metal parts from face-down to face-up on a conveyor belt", 2.5 points per part, 10 points maximum, 3 min — [REAL-I lessons paper](https://arxiv.org/abs/2609.13679)

### Inferences
- Which have VLA baselines: AHEAD (OpenVLA, DreamVLA), DSDyn-VLA (pi0.5, RTC, VLASH, DynamicVLA), RLDX-1 (pi0.5, GR00T N1.6), ForeTime-VLA (pi0.5), DynamicWAM, TEMPO (RTC, VLASH on a VLA), VLASH/FASTER (pi0.5, X-VLA), HRIBench (GR00T N1.5, pi0.5), VLA-Corrector and FRBench (pi0, pi0.5). None of these task sets is shared hardware or a hosted service, so numbers are not comparable across papers.
- Air hockey is the only reproducible fast-object competition with explicit per-step compute-time scoring, but it is striking rather than grasping and state-based; it fits the catalog only as a non-VLA dynamic benchmark.
- DexH2R, FRBench and RoboRecover ([2609.28952](https://arxiv.org/abs/2609.28952), recovery from replayed deviation states in RoboTwin and LIBERO) are adjacent to dynamism but do not score reaction speed; I left them out of the JSON.
- Ball-game work with VLAs (VLASH ping-pong, FASTER table tennis) is presented as demonstrations with small trial counts, not as benchmarks.

### Gaps
- No benchmark posing table tennis or badminton as a manipulation-policy benchmark was found. Not searched to exhaustion (search budget ran out).
- 2025 Robot Air Hockey Challenge final results and team count were not on the pages opened.
- Catching / throwing benchmarks ("Catch It!" DCMM environment, GAP-RL's SAPIEN dynamic-grasping benchmark, GenH2R, MobileH2R) appeared in search results; I opened only GAP-RL ([2410.03509](https://arxiv.org/abs/2410.03509)), which is an RL method paper with an in-paper benchmark. The others are unverified and not included.

## Simulation dynamic benchmarks 2024–2026 not yet catalogued

### Takeaway
Five uncatalogued simulation suites test moving-object reaction — DynaGrasp-32, DynamicManip Benchmark, TIDAL Dynamic Interception, AHEAD's 20 scenarios and the RTC Kinetix suite — and only DynamicManip, TIDAL and Kinetix let the world advance during inference.

### Cited Findings
- DynaGrasp-32 (Tsinghua, 1 Jul 2026): 32 Isaac Sim tasks in six families (Base 2, Objects 6, Obstacle 6, Environment 6, plus Amount and Speed), Franka Panda, three 256×256 cameras, 30 Hz environment, 50 closed-loop episodes per task; paired DynaGrasp-1600 dataset of 1,600 teleoperated demonstrations (~510K control steps, 1.53M images). Fine-tuned base VLAs: SmolVLA 62.50%, X-VLA 36.56%, pi0 72.56%, pi0.5 64.63%; coarse-tuned 40.63%, 37.69%, 39.88%, 48.44% — [DynaWM](https://arxiv.org/abs/2607.02604)
- DynamicManip Benchmark (Sun Yat-sen University, 2 Aug 2026): built on RoboTwin 2.0 / SAPIEN with two ARX-X5 arms; five tasks (Dynamic Tapping, Belt Picking, Object Catching, Mole Whacking, Goal Blocking), 200 expert demonstrations each; "evaluation is coupled to the measured policy inference latency ... we advance the simulator by Ndelay = round(tinfer/∆tsim) steps before applying each predicted action. The scene therefore evolves during inference"; DP3 scores 20/78/48/38/42% at 44–61 ms latency versus 42/80/64/44/88% at 31–38 ms for the authors' policy, 100 trials per task; real counterpart with four tasks on AgileX Piper arms, 30 trials each — [DynamicManip](https://arxiv.org/abs/2608.01452)
- TIDAL Dynamic Interception (Jan 2026): RoboCasa GR-1 task where the target "starts with a random cardinal-direction velocity and makes random 90-degree turns at boundaries", Easy and Hard tiers, GR00T N1.5 backbone, 50 Hz control. Paused vs non-paused success: open-loop 0.31 → 0.09, compute-heavy replanning 0.63 → 0.17, TIDAL 0.61 → 0.30 — [TIDAL](https://arxiv.org/abs/2601.14945)
- AHEAD simulation suite: custom MuJoCo Franka environments in four motion categories — constant-velocity transport (conveyor, beam, pole push), gravity-driven (rolling ball), reactive contact (air hockey, ballistic catching), chaotic post-collision (pinball, occlusion deflection, plinko); 5 seeds × 100 rollouts per cell; AHEAD 79–97% versus 31–58% for the strongest baseline; speed sweep 0–40 cm/s — [AHEAD](https://arxiv.org/abs/2606.02486)
- SIDO (Georgia Tech, July 2026) evaluates three MimicGen tasks (Mug, Square, Stack) under five object-motion patterns with the object moving at 2 cm/s, 20 rollouts per cell, plus two real tasks at 1.5 cm/s; policies are Diffusion Policy variants — [SIDO](https://arxiv.org/abs/2607.27890)
- VLA-ULAP adds a latency-aware variant of the already-catalogued LIBERO-Safety: two tasks from its dynamic obstacle-avoidance suite, three control-step delay for the VLA, "The simulator continues stepping during the modeled VLA delay", 200 episodes per task and policy; two-task mean success pi0.5 63.75% vs 77.00% with the local predictor — [VLA-ULAP](https://arxiv.org/abs/2609.18663). LIBERO-Safety itself lists "hardware latency" as something it "cannot fully capture" — [LIBERO-Safety](https://arxiv.org/abs/2606.23686)

### Inferences
- DynaGrasp-32 is the largest uncatalogued moving-object suite with four VLA baselines, but with nothing released and no stated latency model it is closer to DOMINO than to MotionForge in what it proves about action frequency.
- SIDO's 2 cm/s targets are too slow to count as a fast-reaction test; it is listed for completeness and not in the JSON.
- TIDAL's paired paused/non-paused table is the cleanest single piece of evidence that a paused simulator overstates dynamic performance (71–73% relative drops).

### Gaps
- No release was found for DynaGrasp-32, TIDAL Dynamic Interception or the AHEAD suite; DynamicManip has a project page but I did not confirm a code release.
- Object speeds are not stated in the text I read for DynaGrasp-32 and DynamicManip.
- Other 2026 dynamic-VLA method papers seen only as search results (DBC-TFP, GEM "Train once, deploy anywhere", Delay-aware Diffusion Policy, ST-VLA, LaMP, F2F-AP) were not opened.

## Throughput and speed metrics for VLAs

### Takeaway
Beyond the catalogued PhAIL, throughput appears as a metric inside real-time-execution papers rather than as a standalone benchmark: RTC's task-fraction-per-time, the Magiclab study's successful tasks per hour, SmolVLA's cubes per fixed window, and SAIL's throughput-with-regret.

### Cited Findings
- PhAIL (catalogued) defines Human-Relative Throughput on time-to-success CDFs and finds the best of four VLAs "∼7× slower per operation (RMST ratio) than the human reference" — [PhAIL](https://arxiv.org/abs/2605.29710)
- RTC: "average throughput, defined as the proportion of task completed divided by duration of episode averaged over episodes" — [RTC](https://arxiv.org/abs/2506.07339)
- Magiclab: successful-task throughput Q = R_succ · 3600 / mean time, reported with 95% Wilson intervals; Legato 47.31/h vs inference-time-RTC-class methods at ≤63.3% success and >120 s mean time — [paper](https://arxiv.org/abs/2609.39822)
- SmolVLA: 19 vs 9 cubes moved in total over fixed-time runs (async vs sync) — [SmolVLA](https://arxiv.org/abs/2506.01844)
- VLASH reports 1.5–2.0× task-completion speed-up from action quantization — [VLASH](https://arxiv.org/abs/2512.01031)
- SAIL (faster-than-demonstration execution) uses throughput-with-regret (TPR), average time for successful rollouts and speedup-over-demo as primary metrics and sweeps the speed-up factor up to 10× in simulation — [SAIL](https://arxiv.org/abs/2506.11948)
- Realtime-VLA V2 is a deployment report on running a VLA-driven arm "in a speed on par with casual human operation"; it defines no benchmark — [Realtime-VLA V2](https://arxiv.org/abs/2603.26360)
- HRIBench reports Completion Time and Idle Ratio alongside success — [HRIBench](https://arxiv.org/abs/2607.13056)
- REAL-I on-site scenes are scored as points within a 3-minute limit, which makes speed count — [REAL-I lessons paper](https://arxiv.org/abs/2609.13679)

### Inferences
- PhAIL remains the only benchmark whose headline number is a human-relative speed. The Magiclab study is the closest new addition and is in the JSON with the Throughput tag.
- Throughput metrics on static tasks (PhAIL, Magiclab, SmolVLA) measure cycle time, not reaction; they reward async execution but would not catch a policy that cannot track a moving target.

### Gaps
- SAIL's venue (CoRL 2025 according to a search listing) was not confirmed on a page I opened.
- I found no simulated benchmark that scores VLAs by tasks per hour.

## Control-frequency requirements: success versus Hz or execution horizon

### Takeaway
No benchmark reports VLA success directly as a function of control frequency in Hz; what exists are sweeps of inference delay, execution horizon or query cadence, and they consistently show shorter horizons help on dynamic tasks only when the execution scheme keeps chunks consistent.

### Cited Findings
- RTC Kinetix: solve rate versus execution horizon s∈1..7 at fixed d=1; "Only RTC and BID take full advantage of faster updates, showing strictly increasing performance with decreasing execution horizon" — [RTC](https://arxiv.org/abs/2506.07339)
- MotionForge (catalogued): default execution horizon 16 with actions at 30 Hz resampled to 120 Hz; "The best-performing action execution horizon also varies across these policies within the tested range" — [MotionForge](https://arxiv.org/abs/2609.25689)
- ReflexBench (catalogued): studies chunk size and action horizon at a fixed 30 Hz inference frequency; "Larger chunk sizes with shorter action horizons under asynchronous inference generally achieve better performance" — [Reflex](https://arxiv.org/abs/2608.14379)
- LIBERO-MAX (catalogued) runs query-cadence sweeps and measures "stale-action exposure"; "varying query cadence does not eliminate the gap" — [LIBERO-MAX](https://arxiv.org/abs/2609.36518)
- TIDAL: raising the feedback rate by brute-force replanning helps under paused physics (0.63) and collapses under non-paused physics (0.17) — [TIDAL](https://arxiv.org/abs/2601.14945)
- Magiclab: inference at 3 Hz (inference-time RTC) did not beat methods running at 1–2 Hz — [paper](https://arxiv.org/abs/2609.39822)
- vla.cpp: on a static pick-and-place the effective action rate fell from 17.7 to 5.0 Hz across backends, with success reported per backend (20 episodes each) — [vla.cpp](https://arxiv.org/abs/2606.08094)
- DOMINO reports latency separately from success: OpenVLA 166.7 ms / 6.0 Hz, OpenVLA-OFT 76.9 ms / 13.0 Hz, pi0 106.5 ms / 9.4 Hz, pi0.5 103.0 ms / 9.7 Hz, PUMA 103.7 ms / 9.6 Hz on an RTX 4090 — [DOMINO](https://arxiv.org/abs/2603.15620)
- NEBULA reports inference frequency and latency as standalone stress indicators (figure values: GR00T about 17 Hz / 58–61 ms, RDT-1B about 4.8 Hz / 206–215 ms, Diffusion Policy about 1.5 Hz / 657–794 ms, SpatialVLA about 1.9 Hz / 509–529 ms) — [NEBULA](https://arxiv.org/abs/2510.16263)

### Inferences
- "Control frequency" in these papers is really three different knobs — inference delay d, execution horizon s, and control period — and only Kinetix-style sweeps vary d and s independently with enough rollouts (2,048) for tight intervals.
- A Hz-versus-success curve for VLAs on moving-object tasks is a gap a new benchmark could fill; MotionForge's protocol would support it because latency is whatever the model's native pipeline produces.

### Gaps
- NEBULA numbers above are read from a figure flattened to text; mapping of values to models should be rechecked against the figure before quoting.
- I did not find any paper sweeping the physical control rate (e.g. 10/30/50 Hz) of a VLA on a fixed dynamic benchmark.

## Benchmarks hidden inside method papers (no "benchmark" in the title)

### Takeaway
Most uncatalogued dynamic evaluation sets are introduced inside method papers, and of those opened only Kinetix (RTC) shipped as reusable code; DynaGrasp-32, DynamicManip, TIDAL and AHEAD define suites without a confirmed release.

### Cited Findings
- RTC ("Real-Time Execution of Action Chunking Flow Policies") → Kinetix 12-task benchmark, released — [paper](https://arxiv.org/abs/2506.07339), [code](https://github.com/Physical-Intelligence/real-time-chunking-kinetix)
- DynaWM → DynaGrasp-32 and DynaGrasp-1600, no link in the PDF — [paper](https://arxiv.org/abs/2607.02604)
- DynamicManip → DynamicManip Benchmark with a latency-aware evaluator, project page only — [paper](https://arxiv.org/abs/2608.01452)
- TIDAL → Dynamic Interception with paused / non-paused protocols — [paper](https://arxiv.org/abs/2601.14945)
- AHEAD ("Intercepting the Future") → 20 MuJoCo dynamic scenarios plus five real tasks — [paper](https://arxiv.org/abs/2606.02486)
- TEMPO → TEMPO-Bench (motion-perception frames, not a policy benchmark) — [paper](https://arxiv.org/abs/2609.16864)
- RePO-VLA → FRBench (recovery under injected errors and human perturbation) — [paper](https://arxiv.org/abs/2605.09410)
- Already catalogued examples of the same pattern: DSDyn-VLA → DynBench; Reflex → ReflexBench; D2-VLA → DOMINO-Long; PUMA → DOMINO; DynamicVLA → DOM; PhysMani → PhysMani-Bench.
- Method papers opened that add no new suite (they use LIBERO, Kinetix, DOMINO or ad-hoc real tasks): VLASH, A2C2, FASTER, DEFLECT, Legato, FutureRTC, Action ControlNet, Reflex streaming, real-time autoregressive policies, ReactVLA ([2606.14255](https://arxiv.org/abs/2606.14255)), DynamicWAM, ForeTime-VLA, RLDX-1, Real-Time EXPO-FT, VLA-ULAP.

### Inferences
- A catalog entry for an unreleased in-paper suite is of limited use to readers; the JSON marks these in `status` and `note` so they can be filtered out.

### Gaps
- FlashVLA ([2608.27384](https://arxiv.org/abs/2608.27384)), DAM-VLA ([2606.12105](https://arxiv.org/abs/2606.12105)) and "Dynamic Execution Commitment" ([2605.11567](https://arxiv.org/abs/2605.11567)) were downloaded but only skimmed by keyword; none mentions Kinetix or conveyor tasks, so I treated them as LIBERO-only.

## How catalogued dynamic benchmarks treat inference latency

### Takeaway
Of the catalogued dynamic benchmarks, MotionForge, ReflexBench and DOM let the world move while the policy computes; DOMINO, DOMINO-Long, PhysMani-Bench and LIBERO-MAX are step-synchronous (the simulator waits), DynBench and NEBULA do not say, and PhAIL is real-world so latency counts by construction. Only the first group tests action frequency.

### Cited Findings
- MotionForge defines three protocols — R1 "benchmark-controlled and model-agnostic real-time protocol in which the environment evolves independently of policy inference", R2 "asynchronous execution with coarser environment stepping", R3 "step-synchronous evaluation without a standardized benchmark-level latency protocol" — and classifies DOM as R2, DOMINO as R3, PhysMani-Bench as R3 and itself as R1 (Table I) — [MotionForge](https://arxiv.org/abs/2609.25689)
- MotionForge own protocol: "the simulation environment continues to evolve during policy inference with fine-grained environment stepping under a fixed 120-Hz simulation clock ... the evaluator dispatches the current observation to the policy without pausing the environment"; latency is each model's native pipeline with no mitigation; "freezing the environment during inference increases mean success rates by 21.7–27.5 percentage points relative to our real-time protocol" — [MotionForge](https://arxiv.org/abs/2609.25689)
- ReflexBench: "Unlike existing simulation benchmarks that pause the environment during policy inference, ReflexBench decouples simulation from robot control". It uses a "latency blocking mechanism": under synchronous inference the robot stays idle for the specified latency after the query and then executes the chunk; under asynchronous inference the previous chunk keeps executing and the new one arrives in the next control period. Latency can be set manually or derived from measured real latency via the simulator's Real-Time Factor — [Reflex](https://arxiv.org/abs/2608.14379)
- DOM (DynamicVLA): "object motion does not pause during inference"; actions are indexed at the 25 Hz observation timestep with horizon 20, and "the inference latency m is measured at runtime and allowed to vary across hardware and execution cycles" — [DynamicVLA](https://arxiv.org/abs/2601.22153)
- DOMINO: the paper has no statement on pausing; it reports latency in a separate table (above). MotionForge says "Its step-synchronous evaluation, however, excludes policy inference latency", and DynamicWAM says it evaluates "on DOMINO under its native synchronous protocol" — [DOMINO](https://arxiv.org/abs/2603.15620), [MotionForge](https://arxiv.org/abs/2609.25689), [DynamicWAM](https://arxiv.org/abs/2608.00793)
- DOMINO-Long: ten tasks built alongside DOMINO (RoboTwin 2.0 / SAPIEN, Aloha-AgileX embodiment); the D2-VLA paper does not describe any latency model — [D2-VLA](https://arxiv.org/abs/2609.34792)
- PhysMani-Bench: 8 task groups × 2 speeds (normal and high) extending RLBench, 16 tasks; no mention of pausing or latency in the simulation protocol; in the real-world experiments the control frequency is 5 Hz and an action buffer with temporal ensembling decouples inference from execution. MotionForge: "its evaluation does not explicitly account for policy inference latency" — [PhysMani](https://arxiv.org/abs/2607.01938), [MotionForge](https://arxiv.org/abs/2609.25689)
- DynBench (DSDyn-VLA): MuJoCo, Franka Panda, nine tasks (conveyor picking, dynamic dropping, dynamic stacking, mobile pouring, conveyor sorting, insertion into a moving hole, rolling ball, rolling can, green-ball selection), 100 demonstrations and 100 trials per task; pi0.5 9.7%, RTC 19.4%, VLASH 27.1%, DynamicVLA 34.3%, DSDyn-VLA 48.4%. The paper describes simulated delay only for its Kinetix experiments ("an artificial delay δ ∈ {0, 1, 2, 3, 4} steps") and does not say how DynBench couples simulation to inference time — [DSDyn-VLA](https://arxiv.org/abs/2609.39198)
- LIBERO-MAX: paired Base/Dynamic rollouts replay the same action prefix and then inject one event (target or receptacle relocation, camera shift, sensor noise, illumination or theme switch, distractor burst, obstacle insertion); 8,000 pairs, 14 policies, success falls 11.0–25.7 points. Timing is counted in policy steps ("stale-action exposure", query-cadence sweeps); there is no wall-clock or latency model and the paper positions itself against DynamicVLA/DOMINO, which "directly study moving-object manipulation and low-latency reactive control" — [LIBERO-MAX](https://arxiv.org/abs/2609.36518), [repo](https://github.com/liberomax/LIBERO-MAX)
- NEBULA: Dynamic Adaptation tasks range "from object attribute switching (Easy) to predictable moving (Medium) and unpredictable real-time events (Hard)"; Inference Frequency and Latency are separate "single-indicator" stress tests ("Latency quantifies the delay between sensory input and action output, measured in milliseconds"). The paper does not state that the simulator advances during inference — [NEBULA](https://arxiv.org/abs/2510.16263)
- PhAIL: real Franka FR3 picking on a shared station; time-to-success CDFs include all inference and execution time; the task is static-object picking — [PhAIL](https://arxiv.org/abs/2605.29710)
- AgiBot World Challenge: the 2025 manipulation track lists "Pack washing detergent from conveyor" among 10 tasks and describes "packing moving objects"; the 2026 edition used Genie Sim 3.0 online evaluation plus a real-robot final on the AgiBot G2. None of the pages opened states scoring rules, time limits or how latency is handled — [HF dataset card](https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2025), [challenge page](https://opendrivelab.com/challenge2025/), [Robot Report](https://www.therobotreport.com/agibot-holds-world-challenge-2026-see-how-ai-models-perform-real-tasks/)

### Inferences
- Summary table (my reading of the sources above):
  - World runs during inference, latency = real model latency: MotionForge (R1, 120 Hz clock), DOM (R2, coarser stepping), PhAIL (real robot).
  - World runs during inference, latency = configurable injected delay: ReflexBench (manual or RTF-converted measured latency).
  - Simulator waits for the policy: DOMINO, DOMINO-Long (inferred from shared platform, not stated), PhysMani-Bench, LIBERO-MAX.
  - Not stated: DynBench, NEBULA, AgiBot World Challenge conveyor task.
- On step-synchronous benchmarks a slow VLA is not penalised for its inference time; only its open-loop chunk length matters. They therefore test motion prediction and tracking, not action frequency. MotionForge's 21.7–27.5 point and TIDAL's 71–73% relative drops quantify how much a paused simulator overstates performance.
- For the catalog, a "world keeps running during inference: yes / configurable / no / not stated" field would separate these benchmarks more usefully than the Dynamic tag alone.

### Gaps
- DOMINO-Long's protocol is inferred from DOMINO's; neither the D2-VLA paper nor the DOMINO paper states it explicitly. The DOMINO evaluation code was not inspected.
- DynBench and NEBULA code were not inspected; "not stated" refers to the papers only.
- AgiBot World Challenge conveyor task: object speed, scoring and latency handling could not be verified from any page opened.
- Web search budget for the session was exhausted before I could run the remaining planned queries (edge-deployment latency benchmarks, table-tennis/badminton policy benchmarks, catching benchmarks, CoRL/RSS/ICRA 2026 proceedings sweeps). Leads from earlier results that I could not open or search further: GenH2R, MobileH2R, "Catch It!" (DCMM), DBC-TFP, GEM, Delay-aware Diffusion Policy (2512.07697), TurboVLA (2607.27205), VLA-RAIL (2512.24673), "Characterizing VLA models across XPUs" (ICML 2026).
