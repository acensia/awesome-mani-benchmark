# Established simulation benchmarks used to evaluate VLA / generalist manipulation policies (first released 2023 or earlier)

Scope note: long-standing simulation benchmarks (first released 2023 or earlier; RoboCasa 2024 admitted as instructed) that VLA and generalist-policy papers report on. Variants and successors from 2024 onward (LIBERO-Plus/PRO, RoboCasa365, SimplerEnv, Colosseum, GemBench, RoboTwin 2.0, VLABench, BEHAVIOR Challenge, DexMimicGen, GR-1 Tabletop) are in the other slices and are only named here. Machine-readable entries (16) are in `established_sim_benchmarks.entries.json`. All sources were opened on 2026-10-02 unless a finding says "search snippet" or "aggregate". ManiSkill3 (2024) is included as its own entry because the assignment named it and the RDT benchmark runs on it; drop it if the 2023 cut is strict.

Name collision to keep in mind: two different models are called UniVLA — the latent-action model of Bu et al. ([arXiv 2505.06111](https://arxiv.org/html/2505.06111)) and the "Unified Vision-Language-Action Model" ([arXiv 2506.19850](https://arxiv.org/abs/2506.19850)). The CALVIN leaderboard entry "UniVLA" (4.41 on ABC→D) and the "UniVLA 9B" row in the X-VLA table are the second one.

## 1. Which simulation benchmarks do the major VLA / generalist-policy papers report on?

### Takeaway
LIBERO is by far the most reported simulation benchmark (about 500 of 750 reporting papers in a 2026 aggregate), followed by SimplerEnv and CALVIN, then RoboCasa (24 atomic tasks) and RLBench; Meta-World, ManiSkill, Language-Table and ALOHA sim appear occasionally. π0, π0.5 and Octo report no simulation results in their own papers, and RDT-1B's simulation numbers exist only in its repository.

### Cited Findings

**Benchmark × paper table** (✓ = result in the paper itself; ○ = result or checkpoint only in the official repository / project page; △ = number published by a third party; blank = none found). Benchmarks marked * are 2024+ and belong to the other slices.

| Model (source) | LIBERO | CALVIN | RLBench | Meta-World | ManiSkill | RoboCasa (24 atomic) | Language-Table sim | ALOHA sim | SimplerEnv* | Other* |
|---|---|---|---|---|---|---|---|---|---|---|
| OpenVLA | ✓ 76.5 (App. E) | △ | △ 41 (10 tasks) | | △ 4.8 (MS3) | | | | △ | |
| OpenVLA-OFT | ✓ 97.1 | △ 4.10 | | | | | | | △ | |
| π0 | ○ / △ 94.2 | | △ 55 (10 tasks) | △ 47.9–50.5 | | △ | | ○ | △ | RoboTwin 2.0 △ |
| π0-FAST | ✓ (fig.) / △ 85.5 | | | | | | | | | DROID (real) |
| π0.5 | ○ 96.85 | △ | | | | △ | | | | |
| GR00T N1 | △ 93.9 | | | | | ✓ 32.1 (100 demos) | ○ 52.8 | | △ | DexMimicGen ✓, GR-1 Tabletop ✓ |
| GR00T N1.5 | △ | | | | | ○ 47.5 (30 demos) | ○ 93.2 | | △ | Sim GR-1 ○, DreamGen ○ |
| GR00T N1.6 | ○ 97.0 | | | | | ○ 66.2 | | | ○ | GR-1 Tabletop ○, BEHAVIOR ○ |
| Octo | △ 75.1 | | | | △ 0.0 (MS3) | | | | △ | |
| RDT-1B | | | | | ○ 53.6 (MS3, 5 tasks) | | | | | RoboTwin △ |
| CogACT | △ | | △ 60 (10 tasks) | | △ (MS2) | | | | ✓ | |
| SmolVLA | ✓ 87.3 | △ | | ✓ 57.3 | | △ | | | | |
| X-VLA | ✓ 98.1 | ✓ 4.43 | | | | | | | ✓ | RoboTwin 2.0 ✓, VLABench ✓, NAVSIM ✓ |
| UniVLA (2505.06111) | ✓ 95.2 | ✓ 3.80 | | | | | | | ✓ | R2R (navigation) ✓ |
| FLOWER | ✓ (5 suites) | ✓ 4.53 | | | | | | ✓ 54.0 | ✓ | |
| VLA-Adapter | ✓ 97.3 | ✓ 4.42 | | | | | | | | |
| VLA-0 | ✓ 94.7 | | | | | | | | | |
| MemoryVLA | ✓ 96.5 (5 suites) | | | | | | | | ✓ | MIKASA-Robo ✓ |
| Dita / DiT Policy | ✓ 82.4 | ✓ 3.61 | | | ✓ 65.8 (MS2, 5 tasks) | | | | ✓ | |
| HybridVLA | | | ✓ 74 (10 tasks) | | | | | | | |
| BridgeVLA | | | ✓ 88.2 (18 tasks) | | | | | | | COLOSSEUM ✓, GemBench ✓ |
| LAPA | | | | | | | ✓ | | ✓ | |
| RT-2 | | | | | | | ✓ 90 ± 10 | | | |
| StarVLA-α (ECCV 2026) | ✓ | | | | | ✓ | | | ✓ | RoboTwin ✓ |
| MMaDA-VLA (ACM MM 2026) | ✓ 98.0 | ✓ 4.78 | | | | | | | | |

Sources for the table rows:
- OpenVLA evaluates in simulation only on LIBERO, in Appendix E; the main experiments are real-robot (WidowX, Google Robot, Franka) — [OpenVLA arXiv HTML](https://arxiv.org/html/2406.09246). Its LIBERO numbers (84.7 / 88.4 / 79.2 / 53.7, average 76.5) are reproduced in the OpenVLA-OFT table — [OpenVLA-OFT arXiv HTML](https://arxiv.org/html/2502.19645)
- OpenVLA-OFT evaluates only LIBERO in simulation: 97.6 / 98.4 / 97.9 / 94.5, average 97.1 (Spatial / Object / Goal / Long), 500 trials per suite (10 tasks × 50 episodes), one policy per suite; same table: π0 fine-tuned 94.2, π0 + FAST 85.5, DiT Policy 82.4, OpenVLA 76.5, Octo fine-tuned 75.1, Diffusion Policy 72.4 — [OpenVLA-OFT arXiv HTML](https://arxiv.org/html/2502.19645)
- The π0 paper reports only real-robot experiments (UR5e, Franka, Trossen, mobile manipulators); no simulation benchmark — [π0 arXiv HTML](https://arxiv.org/html/2410.24164)
- The FAST paper reports LIBERO (four suites, shown as a bar chart, about 70% for FAST versus near 0% for naive tokenization as extracted) alongside real-robot tasks and zero-shot DROID — [FAST arXiv HTML](https://arxiv.org/html/2501.09747)
- The π0.5 paper evaluates only on real robots in real and mock homes — [π0.5 arXiv HTML](https://arxiv.org/html/2504.16054). The openpi repository ships a π0.5 LIBERO checkpoint ("gets state-of-the-art performance") and an ALOHA simulator example — [openpi README](https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/README.md); the LIBERO example lists π0.5 at 98.8 / 98.2 / 98.0 / 92.4, average 96.85 — [openpi LIBERO example](https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/README.md). LeRobot's reproduction gives 97.0 / 99.0 / 98.0 / 96.0, average 97.5 — [LeRobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- GR00T N1 evaluates on RoboCasa Kitchen (24 tasks), DexMimicGen (9 tasks) and GR-1 Tabletop (24 tasks) with 30 / 100 / 300 demos per task; at 100 demos GR00T-N1-2B scores 32.1 / 66.5 / 50.0 versus Diffusion Policy 25.6 / 56.1 / 32.7 and BC-Transformer 26.3 / 53.9 / 16.1 — [GR00T N1 arXiv HTML](https://arxiv.org/html/2503.14734)
- GR00T N1.5 project page: Language Table 93.2% (N1: 52.8%), Sim GR-1 language 54.4% (36.4%), RoboCasa with 30 demos 47.5 (17.4), Sim GR-1 zero-shot 43.9 (39.6) and 30 demos 47.4 (43.2), 12 DreamGen tasks 38.3% (13.1%) — [GR00T N1.5 project page](https://research.nvidia.com/labs/gear/gr00t-n1_5/)
- GR00T N1.6 repository supports LIBERO, SimplerEnv (bridge and fractal checkpoints), RoboCasa, RoboCasa GR-1 Tabletop and BEHAVIOR (BEHAVIOR-1K checkpoint for Galaxea R1 Pro) — [Isaac-GR00T n1.6-release README](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/n1.6-release/README.md). Its LIBERO example lists Spatial 97.65, Object 98.45, Goal 97.5, LIBERO-10 94.35 (200 episodes each; average about 97.0, computed here) — [N1.6 LIBERO example](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/n1.6-release/examples/LIBERO/README.md); its RoboCasa example lists a 24-task average of 66.22% — [N1.6 RoboCasa example](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/n1.6-release/examples/robocasa/README.md). The current main branch (GR00T N1.7) ships LIBERO and SimplerEnv checkpoints — [Isaac-GR00T README](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/main/README.md)
- Octo publishes no simulation results; all evaluation is on nine real robot platforms — [Octo arXiv HTML](https://arxiv.org/html/2405.12213)
- RDT-1B's paper evaluates only on a real ALOHA robot — [RDT-1B arXiv HTML](https://arxiv.org/html/2410.07864). Its repository adds a ManiSkill benchmark (PegInsertionSide, PickCube, StackCube, PlugCharger, PushCube; 5,000 motion-planned trajectories; 250 trials per method): RDT 53.6%, Diffusion Policy 30.2%, OpenVLA 4.8%, Octo 0.0% mean — [RDT README](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/main/README.md). The evaluation script imports `mani_skill` and uses `-v1` environment IDs, i.e., ManiSkill3 — [RDT eval script](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/main/eval_sim/eval_rdt_maniskill.py)
- CogACT evaluates only SIMPLER in simulation (Google Robot visual matching 74.8, variant aggregation 61.3, WidowX 51.3) — [CogACT arXiv HTML](https://arxiv.org/html/2411.19650)
- SmolVLA: LIBERO 90 / 96 / 92 / 71, average 87.3 (10 trials per task; π0 86.0 in the same table) and Meta-World 50 tasks: 82.5 / 41.8 / 45.0 / 60.0 (easy / medium / hard / very hard), average 57.3; π0 47.9–50.5, TinyVLA 31.6, Diffusion Policy 10.5 — [SmolVLA arXiv HTML](https://arxiv.org/html/2506.01844)
- X-VLA (0.9B): Simpler 80.4 (VM) / 75.7 (VA) / 95.8 (WidowX); LIBERO 98.2 / 98.6 / 97.8 / 97.6, average 98.1; CALVIN ABC→D 4.43; RoboTwin 2.0 70.0 / 39.0; VLABench 51.1; NAVSIM 87.3. The same table lists GR00T-N1 at 93.9 and π0 at 94.1 on LIBERO — [X-VLA arXiv HTML](https://arxiv.org/html/2510.10274)
- UniVLA (2505.06111): LIBERO 96.5 / 96.8 / 95.6 / 92.0, average 95.2; CALVIN average length 3.80 (OpenVLA 3.27 in the same table); SimplerEnv 37.5% (decoder-only variant, as extracted); R2R oracle success 47.1% — [UniVLA arXiv HTML](https://arxiv.org/html/2505.06111)
- FLOWER (CoRL 2025): "190 tasks spanning ten simulation and real-world benchmarks", CALVIN ABC 4.53 — [FLOWER arXiv abstract](https://arxiv.org/abs/2509.04996); LIBERO 97.5 / 99.1 / 96.1 / 94.9 plus LIBERO-90 94.7; ALOHA sim 54.0% average — [FLOWER arXiv HTML](https://arxiv.org/html/2509.04996)
- VLA-Adapter (0.5B): LIBERO 97.8 / 99.2 / 97.2 / 95.0, average 97.3 (Pro variant 98.5); CALVIN ABC→D 4.42 (Pro 4.50); lists OpenVLA-OFT at 4.10 on CALVIN — [VLA-Adapter arXiv HTML](https://arxiv.org/html/2509.09372)
- VLA-0 (NVIDIA): LIBERO only, 97.0 / 97.8 / 96.2 / 87.6, average 94.7, compared with models without large-scale robot pretraining (π0.5-KI 93.3, OpenVLA-OFT 91.9, SmolVLA 88.8) — [VLA-0 arXiv HTML](https://arxiv.org/html/2510.13054)
- MemoryVLA: SimplerEnv-Bridge 71.9, SimplerEnv-Fractal 72.7, LIBERO five suites 96.5 (LIBERO-90: 95.6), MIKASA-Robo 41.2 — [MemoryVLA arXiv HTML](https://arxiv.org/html/2508.19236)
- Dita / Diffusion Transformer Policy: SimplerEnv, LIBERO 82.4, CALVIN ABC→D 3.61, ManiSkill2 five tasks 65.8 — [DiT Policy arXiv HTML](https://arxiv.org/html/2410.15959v6)
- HybridVLA: RLBench, 10 tasks, 100 demonstrations each, 20 rollouts × 3; mean success 74% versus CogACT 60%, π0 55%, OpenVLA 41%, ManipLLM 38% — [HybridVLA arXiv HTML](https://arxiv.org/html/2503.10631)
- BridgeVLA: RLBench 18 tasks 88.2% (RVT-2 81.4%, 3D Diffuser Actor 81.3%, Act3D 65.0%), COLOSSEUM 64.0%, GemBench 50.0% — [BridgeVLA arXiv HTML](https://arxiv.org/html/2506.07961)
- LAPA: Language Table simulation (five task categories) and SIMPLER — [LAPA arXiv HTML](https://arxiv.org/html/2410.11758). RT-2 reports the "Open Source Language Table Benchmark": RT-2-PaLI-3B 90 ± 10, LAVA 77 ± 4, RT-1 74 ± 13, BC-Zero 72 ± 3 — [RT-2 arXiv HTML](https://arxiv.org/html/2307.15818)
- StarVLA-α (accepted to ECCV 2026) evaluates on "LIBERO, SimplerEnv, RoboTwin, and RoboCasa" and notes that existing approaches vary in "benchmark-specific engineering" — [StarVLA-α arXiv abstract](https://arxiv.org/abs/2604.11757)
- MMaDA-VLA (ACM MM 2026 oral per its repository title): 98.0% LIBERO, 4.78 CALVIN ABC→D (search snippet of the arXiv abstract; page not opened) — [MMaDA-VLA arXiv](https://arxiv.org/abs/2603.25406)
- △ cells without a number (π0, π0.5 and SmolVLA on RoboCasa or CALVIN; CogACT on LIBERO and ManiSkill2; SimplerEnv re-runs; GR00T N1.5 on LIBERO) are taken from third-party entries in the vla-eval aggregate, which lists, for example, 110 LIBERO entries for π0 variants and 113 for π0.5 variants, most of them baselines re-run by other papers — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json). π0 and RDT on RoboTwin come from the RoboTwin 2.0 paper baselines recorded in the companion notes `new_sim_suites.md` — [RoboTwin 2.0 arXiv HTML](https://arxiv.org/html/2506.18088)

**Usage frequency**
- A blog review of the 164 VLA submissions to ICLR 2026 (Moritz Reuss, October 2025) states that "90% of papers mentioned in this post all test in either LIBERO, SIMPLER or CALVIN", and that RLBench is gaining popularity for VLAs although "all VLAs are still far away from 3D SOTA methods" — [State of VLA Research at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- The vla-eval leaderboard data file (dated 2026-08-10; "largely maintained by AI ... errors are possible") contains 3,576 results from 750 distinct reporting papers. Entries / reporting papers per benchmark, counted here from its `leaderboard.json`: LIBERO 1,607 / 496; SimplerEnv 482 / 135; CALVIN 443 / 128; RoboCasa (Panda and GR-1) 271 / 80; LIBERO-Plus 239 / 74; RLBench 208 / 64; LIBERO-PRO 83 / 23; ManiSkill2 66 / 18; RoboTwin 1.0 50 / 16; VLABench 42 / 14 — [vla-eval leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/); [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- Reporting papers by arXiv year in the same file (counted here): LIBERO 2 (2023), 15 (2024), 148 (2025), 331 (2026 to August); CALVIN 23 / 48 / 52 for 2024 / 2025 / 2026; RoboCasa 3 / 20 / 57; RLBench 19 / 21 / 18; ManiSkill2 5 / 5 / 8 — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- The same project's coverage file counts citing papers: LIBERO 1,437, RLBench 1,027, CALVIN 720, SimplerEnv 499, RoboCasa 463, ManiSkill2 395 — [coverage.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/coverage.json)
- The vla-eval harness integrates LIBERO, CALVIN, SimplerEnv, ManiSkill2, RoboCasa, RLBench, BEHAVIOR-1K and newer suites (18 benchmarks in the repository README) — [vla-evaluation-harness repository](https://github.com/allenai/vla-evaluation-harness); [vla-eval arXiv HTML](https://arxiv.org/html/2603.13966v1)
- LeRobot's landing page names LIBERO and Meta-World as the simulation benchmarks to evaluate against — [LeRobot docs](https://huggingface.co/docs/lerobot/index)

### Inferences
- The frontier-lab models with the strongest real-world claims (π0, π0.5, Octo, RDT-1B) did not publish simulation numbers in their papers; their LIBERO / ManiSkill numbers come from repositories or from other groups' re-runs, so cross-paper comparisons mix first-party and third-party fine-tuning.
- Benchmark choice follows lineage: OpenVLA / π-family follow-ups report LIBERO; GR00T-family models report RoboCasa and GR-1 Tabletop; 3D or keyframe VLAs report RLBench; LeRobot-family models add Meta-World; Google-lineage and latent-action models report Language-Table.
- RoboCasa's share is growing fastest (3 → 20 → 57 reporting papers per year), while RLBench and ManiSkill2 are flat.

### Gaps
- Meta-World, Language-Table, ALOHA sim, VIMA-Bench, ARNOLD, Franka Kitchen and robomimic are not tracked by the vla-eval aggregate, so their usage frequency could not be quantified.
- The vla-eval data are AI-curated; counts were computed from the JSON and not cross-checked against the cited papers. The paper version of vla-eval reports different totals (657 results, 17 benchmarks) than the current data file.
- GR00T N1.5 has no paper; only the project page and README were found. StarVLA-α and MMaDA-VLA scores per benchmark were not read from the full text.

## 2. What does each established benchmark measure, and how is it set up?

### Takeaway
Six of the sixteen verified benchmarks carry almost all VLA reporting (LIBERO, CALVIN, RoboCasa, RLBench, Meta-World, ManiSkill); the rest (robomimic, Franka Kitchen, VIMA-Bench, ARNOLD, Push-T, MimicGen, ALOHA sim, Language-Table, BEHAVIOR-1K) are established policy-learning benchmarks that VLA papers rarely or never report. None was designed for VLAs: LIBERO targets lifelong learning, Meta-World meta-RL, RLBench general robot learning, robomimic offline imitation.

### Cited Findings

**LIBERO** (NeurIPS 2023 Datasets and Benchmarks)
- Liu, Zhu, Gao, Feng, Liu, Zhu, Stone; published in the NeurIPS 2023 Datasets and Benchmarks track — [arXiv 2306.03310](https://arxiv.org/abs/2306.03310); [NeurIPS proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf)
- Built to study knowledge transfer in lifelong learning (declarative, procedural or mixed), policy architectures, algorithms, task-order robustness and pretraining effects — [arXiv 2306.03310](https://arxiv.org/abs/2306.03310)
- 130 tasks: LIBERO-Spatial, LIBERO-Object and LIBERO-Goal with 10 tasks each; LIBERO-100 split into 90 short-horizon tasks (LIBERO-90) and 10 long-horizon tasks (LIBERO-Long); 50 human demonstrations per task; built on robosuite; tasks generated from PDDL-style specifications with instructions drawn from Ego4D activities; metrics FWT, NBT, AUC; baselines ER, EWC, PackNet with ResNet-RNN, ResNet-T, ViT-T — [LIBERO arXiv HTML](https://arxiv.org/html/2306.03310)
- VLA interface as packaged by LeRobot: agent-view and wrist cameras (256×256), 8-D proprioceptive state, 7-D action (6-D end-effector delta plus gripper); the four-suite training set has 1,693 episodes / 273,465 frames / 40 tasks — [LeRobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- No real-robot experiment and no held-out test tasks appear in the paper (as extracted) — [LIBERO arXiv HTML](https://arxiv.org/html/2306.03310)

**CALVIN** (IEEE RA-L 2022)
- Mees, Hermann, Rosete-Beas, Burgard; RA-L vol. 7 no. 3, 2022; RA-L Best Paper Award 2022 per the repository — [arXiv 2112.03227](https://arxiv.org/abs/2112.03227); [CALVIN README](https://raw.githubusercontent.com/mees/calvin/main/README.md)
- 34 tasks in four environments A–D that share functional elements but differ in textures and positions of the sliding door, drawer, button and switch; about 24 hours of teleoperated play data (about 2.4M steps), of which 1% is language-annotated; 7-DoF Franka Panda in PyBullet; static and gripper RGB-D, tactile, proprioception; 30 Hz control — [CALVIN ar5iv](https://ar5iv.labs.arxiv.org/html/2112.03227)
- Protocols: MTLC (single tasks, 10 rollouts each) and LH-MTLC (1,000 chains of five instructions); splits D→D, ABC→D, ABCD→D; the MCIL baseline completed five-instruction chains 0.08% of the time — [CALVIN ar5iv](https://ar5iv.labs.arxiv.org/html/2112.03227); [CALVIN README](https://raw.githubusercontent.com/mees/calvin/main/README.md)

**RLBench and the PerAct 18-task subset** (RA-L 2020; CoRL 2022)
- James, Ma, Arrojo, Davison; 100 hand-designed tasks, RGB / depth / segmentation from over-the-shoulder stereo and eye-in-hand cameras, motion-planned demonstrations in unlimited supply; aimed at RL, imitation, multi-task and few-shot learning — [arXiv 1909.12271](https://arxiv.org/abs/1909.12271)
- Built on CoppeliaSim v4.1.0 and PyRep; Franka Panda is the benchmarking arm; accepted to RA-L with presentation at ICRA — [RLBench README](https://raw.githubusercontent.com/stepjam/RLBench/master/README.md)
- PerAct (CoRL 2022) fixed the common protocol: 18 tasks with 249 variations, 10 or 100 demonstrations per task, 25 evaluation episodes per task, four 128×128 RGB-D cameras, next-keyframe actions executed by a motion planner; PerAct itself also ran 7 real-world tasks — [PerAct arXiv](https://arxiv.org/abs/2209.05451); [PerAct ar5iv](https://ar5iv.labs.arxiv.org/html/2209.05451)

**Meta-World** (CoRL 2019)
- Yu, Quillen, He, Julian, et al.; 50 Sawyer manipulation tasks for meta-RL and multi-task RL; seven algorithms struggled even with ten training tasks — [arXiv 1910.10897](https://arxiv.org/abs/1910.10897)
- MuJoCo; 39-D state observation; action = 3-D end-effector displacement plus gripper effort; modes ML1, MT1, ML10 and ML45 (5 held-out test tasks each), MT10, MT50; no real-robot experiment — [Meta-World ar5iv](https://ar5iv.labs.arxiv.org/html/1910.10897)
- LeRobot's imitation protocol: 50 tasks grouped as easy 28, medium 11, hard 6, very hard 5; one 480×480 corner camera plus 4-D state; 4-D action; MT50 with fixed object / goal positions; 10 episodes per task — [LeRobot Meta-World docs](https://huggingface.co/docs/lerobot/metaworld)

**ManiSkill2 and ManiSkill3** (ICLR 2023; RSS 2025)
- ManiSkill2: 20 task families, 2,000+ object models, 4M+ demonstration frames; rigid and soft-body, stationary and mobile, single- and dual-arm — [arXiv 2302.04659](https://arxiv.org/abs/2302.04659)
- Task families include soft-body (Fill, Hang, Excavate, Pour, Pinch, Write), pick-and-place (PickCube, StackCube, PickSingleYCB, PickSingleEGAD, PickClutterYCB), assembly (PegInsertionSide, PlugCharger, AssemblingKits) and articulated / mobile tasks (OpenCabinetDrawer, OpenCabinetDoor, PushChair, MoveBucket); SAPIEN plus a Warp-based MPM simulator — [ManiSkill2 arXiv HTML](https://arxiv.org/html/2302.04659)
- ManiSkill3 (first posted October 2024, published at RSS 2025): GPU-parallel simulation and rendering at 30,000+ FPS, 12 task domains, millions of demonstration frames; ManiSkill2 code is kept at tag v0.5.3 — [arXiv 2410.00425](https://arxiv.org/abs/2410.00425); [ManiSkill README](https://raw.githubusercontent.com/haosulab/ManiSkill/main/README.md)

**robomimic / robosuite** (CoRL 2021 oral; arXiv 2020)
- "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation": six offline algorithms on five simulated and three real-world tasks — [arXiv 2108.03298](https://arxiv.org/abs/2108.03298)
- Tasks Lift, Can, Square, Transport, Tool Hang in robosuite / MuJoCo; datasets: PH (200 demos per task, one proficient operator), MH (300 demos from six operators), MG (RL-generated, Lift and Can); 50 rollouts per evaluation; real Lift, Can, Tool Hang on a Franka with 200 demos each — [robomimic ar5iv](https://ar5iv.labs.arxiv.org/html/2108.03298)
- robosuite is a MuJoCo-based modular framework with benchmark environments; the arXiv entry was revised in January 2025 to describe v1.5 — [arXiv 2009.12293](https://arxiv.org/abs/2009.12293)

**RoboCasa** (RSS 2024)
- Nasiriany, Maddukuri, Zhang, Parikh, Lo, Joshi, Mandlekar, Zhu; 100 tasks, 150+ object categories, human demonstrations plus automated trajectory generation — [arXiv 2406.02523](https://arxiv.org/abs/2406.02523)
- 25 atomic tasks (eight skills) and 75 LLM-guided composite tasks; 10 floor plans × 12 styles = 120 kitchens; 2,509 objects in 153 categories; MuJoCo via robosuite; three cameras; 50 human demos per atomic task; 3,000 MimicGen demos per task for 24 atomic tasks; BC-Transformer 28.8% (50 human demos) to 47.6% (3,000 generated) on atomic tasks — [RoboCasa arXiv HTML](https://arxiv.org/html/2406.02523)

**BEHAVIOR-1K** (CoRL 2022; extended arXiv 2024)
- 1,000 everyday activities in 50 scenes with 9,000+ annotated objects, on OmniGibson; a preliminary version appeared at CoRL 2022 — [arXiv 2403.09227](https://arxiv.org/abs/2403.09227)
- Activities grounded in a survey of 1,461 participants; BDDL definitions; Omniverse / PhysX 5; baselines on three activities: visuomotor RL 0.0 success, RL with action primitives 0.42–0.88 — [BEHAVIOR-1K arXiv HTML](https://arxiv.org/html/2403.09227)

**Franka Kitchen** (CoRL 2019; D4RL 2020)
- Introduced with Relay Policy Learning (Gupta, Kumar, Lynch, Levine, Hausman) as a "challenging kitchen simulation environment" for multi-stage long-horizon tasks — [arXiv 1910.11956](https://arxiv.org/abs/1910.11956)
- 9-DoF Franka, joint-velocity actions, 59-D observation, MuJoCo, sparse reward, 280-step episodes; maintained in Gymnasium-Robotics — [Gymnasium-Robotics Franka Kitchen](https://robotics.farama.org/envs/franka_kitchen/franka_kitchen/)
- D4RL kitchen datasets from human demonstrations: complete (3,680 transitions), partial (136,950) and mixed (136,950) — [D4RL ar5iv](https://ar5iv.labs.arxiv.org/html/2004.07219); [arXiv 2004.07219](https://arxiv.org/abs/2004.07219)

**VIMA-Bench** (ICML 2023)
- Multimodal-prompt manipulation; thousands of procedurally generated tasks, 600K+ expert trajectories, four-level generalization protocol — [arXiv 2210.03094](https://arxiv.org/abs/2210.03094)
- 17 task templates in six categories on the Ravens simulator (PyBullet); frontal and top-down RGB with segmentation; pick-and-place and wipe primitives; levels L1 placement, L2 combinatorial, L3 novel object, L4 novel task; 50K trajectories per task (650K total); no real-robot experiment — [VIMA arXiv HTML](https://arxiv.org/html/2210.03094)

**ARNOLD** (ICCV 2023)
- 8 language-conditioned tasks with continuous goal states — [arXiv 2304.04321](https://arxiv.org/abs/2304.04321)
- Isaac Sim / PhysX 5; Franka Panda; five 128×128 RGB-D cameras; 20 scenes, 40 objects, 10k demonstrations; splits Novel Object / Scene / State and Any State; PerAct about 55% on the test split and 5.25% on Novel State — [ARNOLD arXiv HTML](https://arxiv.org/html/2304.04321)

**Language-Table** (RA-L 2023)
- "Interactive Language: Talking to Robots in Real Time" (Lynch et al.), nearly 600,000 language-labelled trajectories — [arXiv 2210.06407](https://arxiv.org/abs/2210.06407); published in IEEE RA-L, July 2023 (search result for the IEEE Xplore record; the arXiv page itself lists no venue) — [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10182264/)
- Real setup: xArm6 with cylindrical end-effector, 8 blocks, 2-D delta Cartesian actions; simulated benchmark: five task families spanning 696 task conditions in PyBullet — [Interactive Language ar5iv](https://ar5iv.labs.arxiv.org/html/2210.06407)
- Released data: 442,226 real episodes, 181,020 simulated episodes plus task-specific simulated sets — [language-table README](https://raw.githubusercontent.com/google-research/language-table/main/README.md)

**ALOHA simulation tasks** (RSS 2023)
- ACT paper (Zhao, Kumar, Levine, Finn; RSS 2023 proceedings, paper 16) — [arXiv 2304.13705](https://arxiv.org/abs/2304.13705); [RSS proceedings PDF](https://www.roboticsproceedings.org/rss19/p016.pdf)
- Two MuJoCo tasks, Cube Transfer and Bimanual Insertion, 50 demonstrations each from scripted or human data; ACT 97% / 82% (transfer, scripted / human) and 90% / 60% (insertion); 3 seeds × 50 evaluations — [ACT ar5iv](https://ar5iv.labs.arxiv.org/html/2304.13705)
- gym-aloha: 14-D absolute joint-position actions for two ViperX arms — [gym-aloha README](https://raw.githubusercontent.com/huggingface/gym-aloha/main/README.md)

**Push-T** (RSS 2023)
- Diffusion Policy evaluates 12 tasks from 4 benchmarks (robomimic, Push-T, Multimodal Block Pushing, Franka Kitchen); Push-T is "adapted from IBC", scored by target-area coverage, 200 human demonstrations; Diffusion Policy 0.95 (state) and 0.91 (image, CNN) — [arXiv 2303.04137](https://arxiv.org/abs/2303.04137); [Diffusion Policy ar5iv](https://ar5iv.labs.arxiv.org/html/2303.04137)
- gym-pusht: pymunk physics, 2-D target-position actions, solved at 95% coverage — [gym-pusht README](https://raw.githubusercontent.com/huggingface/gym-pusht/main/README.md)

**MimicGen** (CoRL 2023)
- Over 50K demonstrations across 18 tasks from about 200 human demonstrations; robosuite (MuJoCo) and Isaac Gym Factory; Panda, Sawyer, IIWA, UR5e; also run on real Stack and Coffee tasks — [arXiv 2310.17596](https://arxiv.org/abs/2310.17596); [MimicGen project page](https://mimicgen.github.io/)

### Inferences
- The VLA protocol on LIBERO (fine-tune on the 40 tasks' demonstrations, test on the same 40 tasks) is not the lifelong-learning protocol the benchmark was designed for; the same holds for Meta-World (imitation on MT50 rather than meta-RL) and RLBench (the PerAct subset rather than the 100 tasks).
- Benchmarks with high-level action interfaces (RLBench keyframes, VIMA-Bench primitives, ARNOLD two-phase keyframes) fit 3D and planner-based policies better than closed-loop VLAs, which helps explain their low VLA uptake.

### Gaps
- No VLA results were found for robomimic, Franka Kitchen, VIMA-Bench, ARNOLD, Push-T or MimicGen in the papers opened. A search snippet claimed TraceVLA results on Franka Kitchen; this was not verified and is not used.
- LIBERO observation resolution and the action controller in the original paper were not extracted; the interface above is LeRobot's packaging.
- The original BEHAVIOR-1K simulated robot embodiments (Fetch) were not confirmed from the paper text.

## 3. How saturated is each benchmark, and what critiques exist?

### Takeaway
LIBERO is saturated (hundreds of entries at 97–99%, a 0.54M-parameter policy at 95.1%, a language-blind probe at 92–100%) and CALVIN ABC→D is close (4.5–4.78 of 5); RLBench-18 is at 88–94%. RoboCasa (top about 80% on 24 tasks), ManiSkill subsets and Meta-World still separate models. A June 2026 audit finds that only about 20% of state-of-the-art claims on LIBERO and CALVIN are statistically significant.

### Cited Findings

**Top scores**
- LIBERO four-suite averages: OpenVLA-OFT 97.1 — [OpenVLA-OFT](https://arxiv.org/html/2502.19645); X-VLA 98.1 — [X-VLA](https://arxiv.org/html/2510.10274); VLA-Adapter-Pro 98.5 — [VLA-Adapter](https://arxiv.org/html/2509.09372); CAC-VLA 98.9 — [CAC-VLA arXiv](https://arxiv.org/abs/2607.04816); LaST-R1 99.9 with RL post-training after one-shot supervised warm-up — [LaST-R1 arXiv](https://arxiv.org/abs/2604.28192)
- In the vla-eval aggregate (2026-08-10), of 1,251 LIBERO entries with a four-suite average the median is 94.1; 538 are ≥ 95, 288 ≥ 97, 122 ≥ 98 and 18 ≥ 99 (counted here) — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- CALVIN ABC→D: official leaderboard top is FLOWER 4.53 (then UniVLA 4.41, Seer-Large 4.28, GR-MG 4.04, MoDE 4.01); ABCD→D top FLOWER 4.67; D→D top FLOWER 4.35 — [CALVIN leaderboard](http://calvin.cs.uni-freiburg.de/). Papers report higher: MMaDA-VLA 4.78 (search snippet) — [arXiv 2603.25406](https://arxiv.org/abs/2603.25406); aggregate lists Xiaomi-Robotics-0 4.75, VITA 4.73, NS-VLA 4.72; of 301 ABC→D entries the median is 3.89, 141 are ≥ 4.0 and 20 ≥ 4.5 (counted here) — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- "Higher than 4 score for ABC is standard now and above 4.5 is sota regime"; "LIBERO is basically solved and showing 99% vs 98% is not very helpful"; CALVIN "almost saturated"; SIMPLER "hard to interpret across setups; success spans 40–99% on Bridge" — [State of VLA Research at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- RLBench 18 tasks: BridgeVLA 88.2 — [BridgeVLA](https://arxiv.org/html/2506.07961); ActiveVLA 91.8 (search snippet; not in abstract) — [ActiveVLA arXiv](https://arxiv.org/abs/2601.08325); aggregate lists BridgeVLA++ 93.7 and SAM2Act 86.8; of 64 18-task entries the median is 77.3 and 4 are ≥ 90 (counted here) — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- RoboCasa 24 atomic tasks (Panda): GR00T N1 32.1 → N1.6 66.2 — [GR00T N1](https://arxiv.org/html/2503.14734); [N1.6 RoboCasa example](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/n1.6-release/examples/robocasa/README.md); aggregate lists Z-1 RL 80.6, X-WAM 79.2, Xiaomi-Robotics-1 74.5 with differing demo counts (50 human, 300 generated, or 1,199 public demos) — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json)
- Meta-World 50 tasks: SmolVLA 57.3 — [SmolVLA](https://arxiv.org/html/2506.01844); FabriVLA 90.0 on MT50 — [FabriVLA arXiv](https://arxiv.org/abs/2607.08575)
- ManiSkill2 five-task set: DiT Policy / Dita 65.8 — [DiT Policy](https://arxiv.org/html/2410.15959v6); aggregate lists GeoVLA 77.0 — [leaderboard.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/leaderboard.json). ManiSkill3 five-task set: RDT 53.6 — [RDT README](https://raw.githubusercontent.com/thu-ml/RoboticsDiffusionTransformer/main/README.md)

**Critiques**
- LIBERO-PRO (arXiv October 2025): LIBERO's "training and evaluation settings are problematic, often leading to inflated performance estimates"; models with over 90% standard accuracy "collapse to 0.0% under our generalized setting"; models keep grasping when the target object is replaced and outputs stay unchanged under corrupted instructions — [arXiv 2510.03827](https://arxiv.org/abs/2510.03827)
- LIBERO-Plus (arXiv October 2025): performance drops "from 95% to below 30% under modest perturbations" of camera viewpoint and robot initial state; models "tend to ignore language instructions completely" — [arXiv 2510.13626](https://arxiv.org/abs/2510.13626)
- MINERVA (arXiv September 2026): a 0.54M-parameter policy reaches 95.1% over 2,000 rollouts on the four LIBERO suites; shuffling task-ID mappings drops success to near chance (instruction conditioning acts as a task lookup); flow matching gives no detectable advantage over L1 regression; LIBERO-Plus perturbations reduce it to 46–56% — [arXiv 2609.03715](https://arxiv.org/abs/2609.03715)
- "What Are We Actually Benchmarking in Robot Manipulation?" (Jiang et al., arXiv June 2026) audits LIBERO, CALVIN, SimplerEnv, RoboCasa (RSS 2024 24-task protocol) and RoboTwin 2.0 with four diagnostics (shortcut solvability, statistical significance, creeping overfitting, data-source dependence) — [arXiv 2606.04233](https://arxiv.org/html/2606.04233v1). Findings as extracted:
  - A language-blind probe (DINOv2 encoder plus MLP, about 0.09B parameters) scores 99.0 / 100.0 / 98.8 / 92.4 on LIBERO Spatial / Object / Goal / Long and completes over 3.1 tasks per CALVIN chain, but 0% on SimplerEnv, 18.8% on RoboCasa and about 60% on RoboTwin 2.0
  - Share of published state-of-the-art gains that are provably significant at the 5% level (paired Wald test from aggregate scores): LIBERO 19.8%, CALVIN 19.7%, RoboCasa 53.3%, RoboTwin 2.0 73.7% (the SimplerEnv figure was extracted inconsistently and is not reported here)
  - CALVIN: resampling block poses within the training range lowers average tasks completed by 1.03 for X-VLA, 0.75 for GR-1 and 0.50 for RoboFlamingo
  - LIBERO: redrawing initial states moves success by less than 1%; instructions come "from a fixed public set", enabling task lookup
  - Recommendations: wider test distributions, documented significance thresholds, per-instance outcome reporting, and restrictions or disclosure on training-data sources
- vla-eval (arXiv March 2026): published protocols are not comparable — "SimplerEnv spans three incomparable robot configurations", "CALVIN ABC→D and ABCD→D splits are not comparable", "LIBERO papers report 4 or 5 suites"; reproducing one model found undocumented requirements (ambiguous termination in SimplerEnv, hardcoded observation normalization in CALVIN) and LIBERO deviations of −2.2 to +1.4 points — [vla-eval arXiv HTML](https://arxiv.org/html/2603.13966v1)
- Trial counts differ across papers: OpenVLA-OFT uses 50 episodes per task (500 per suite) — [OpenVLA-OFT](https://arxiv.org/html/2502.19645); SmolVLA and LeRobot use 10 episodes per task (400 total), and LeRobot notes success "may vary by a few percent across evaluation seeds" — [SmolVLA](https://arxiv.org/html/2506.01844); [LeRobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- ManiSkill2: the aggregate counts 14+ task-subset combinations across papers, the most common five-task set covering about 24% of entries; RLBench: "multi-variation vs single-variation significantly affects scores" — [benchmarks.json](https://allenai.github.io/vla-evaluation-harness/leaderboard/benchmarks.json)
- Meta-World+: since Meta-World's introduction "there have been numerous undocumented changes which inhibit a fair comparison of algorithms" — [arXiv 2505.11289](https://arxiv.org/abs/2505.11289)
- Reuss: "you don't need VLAs and large-scale pretraining to get competitive results" on LIBERO; "sim-only is hard to trust" — [State of VLA Research at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- General practice critique: robot learning papers commonly report success rates with little information on number of runs, initial conditions or statistical analysis (search snippet of the abstract; page not opened) — [Kress-Gazit et al., arXiv 2409.09491](https://arxiv.org/abs/2409.09491)
- StarVLA-α notes that VLA approaches differ in "benchmark-specific engineering" and argues a strong VLM backbone with minimal design suffices on LIBERO, SimplerEnv, RoboTwin and RoboCasa — [StarVLA-α arXiv abstract](https://arxiv.org/abs/2604.11757)

### Inferences
- With 500 trials per LIBERO suite, a 1-point difference near 98% is inside binomial noise; this is consistent with the audit's 19.8% significance figure and with LeRobot's "few percent across seeds" remark. Differences below about 2 points on LIBERO and below about 0.1 on CALVIN should not be read as ranking evidence.
- LIBERO scores above about 95% no longer discriminate between a 0.5M-parameter policy, a language-blind probe and a 7B VLA, so the benchmark now works as an integration check rather than a measure of generalist capability; the diagnostic variants (LIBERO-Plus / PRO, in the other slice) are where spread remains.
- RoboCasa's lower probe score (18.8%) and higher significance share (53.3%) suggest it is currently the most discriminating of the established targets, but its results are split across at least three demonstration regimes.

### Gaps
- No critique paper specific to RLBench or Meta-World in the VLA setting was found beyond protocol-variation notes.
- The audit's number of claims examined per benchmark and its SimplerEnv significance share were not reliably extracted.
- Top scores taken from the AI-curated aggregate (BridgeVLA++ 93.7, Xiaomi-Robotics-0 4.75, Z-1 RL 80.6, GeoVLA 77.0) were not confirmed in the papers' full text; their abstracts do not state the numbers.

## 4. Does any established benchmark include real-robot validation or sim–real correlation?

### Takeaway
None of the established benchmarks reports a correlation between simulated and real policy rankings. LIBERO, CALVIN, RLBench, Meta-World, VIMA-Bench and Franka Kitchen are simulation-only; ManiSkill2, BEHAVIOR-1K, ARNOLD, RoboCasa, robomimic, MimicGen and Language-Table include real-robot components, but as sim-to-real transfer, co-training or parallel real tasks.

### Cited Findings
- LIBERO: no real-robot experiment (as extracted) — [LIBERO arXiv HTML](https://arxiv.org/html/2306.03310)
- CALVIN: no real-robot experiment — [CALVIN ar5iv](https://ar5iv.labs.arxiv.org/html/2112.03227)
- Meta-World: no real-robot experiment — [Meta-World ar5iv](https://ar5iv.labs.arxiv.org/html/1910.10897)
- VIMA-Bench: no real-robot experiment — [VIMA arXiv HTML](https://arxiv.org/html/2210.03094)
- RLBench: the benchmark paper describes a simulated environment only — [arXiv 1909.12271](https://arxiv.org/abs/1909.12271); PerAct, which defined the 18-task subset, separately ran 7 real-world tasks (18 variations) — [PerAct arXiv](https://arxiv.org/abs/2209.05451)
- ManiSkill2: a PickCube policy scored 91.0% in simulation and 60.0% on a real ROKAE arm; Pinch soft-body trajectories were compared between simulation and the real world — [ManiSkill2 arXiv HTML](https://arxiv.org/html/2302.04659)
- BEHAVIOR-1K: CollectTrash on a real Tiago in a mock apartment — about 40% in simulation, about 22% in reality with an optimal (oracle) policy and 0% with the trained vision policy; gap attributed to grasping failures, visual mismatch and navigation error — [BEHAVIOR-1K arXiv HTML](https://arxiv.org/html/2403.09227)
- RoboCasa: real Franka in a kitchen, three pick-and-place tasks; real-only 13.6% versus real plus simulation co-training 24.4% (seen objects), 2.6% versus 9.3% (unseen objects); no sim–real correlation metric — [RoboCasa arXiv HTML](https://arxiv.org/html/2406.02523)
- robomimic: three of the tasks (Lift, Can, Tool Hang) were also run on a real Franka with 200 demonstrations each — [robomimic ar5iv](https://ar5iv.labs.arxiv.org/html/2108.03298)
- ARNOLD: "preliminary Sim2Real transfer" on a Franka, with the authors noting real manipulation "continues to struggle because of the Sim2Real gap" (as extracted) — [ARNOLD arXiv HTML](https://arxiv.org/html/2304.04321)
- Language-Table: the headline result (93.5% over 87,588 instructions) is real-robot; the simulated environment is built to "roughly match our real world setup" — [Interactive Language ar5iv](https://ar5iv.labs.arxiv.org/html/2210.06407)
- MimicGen: also run on real-robot Stack and Coffee tasks — [MimicGen project page](https://mimicgen.github.io/)
- ManiSkill3 additionally offers "Real2sim environments for scalably evaluating real-world policies" (the SIMPLER ports, catalogued separately) — [ManiSkill README](https://raw.githubusercontent.com/haosulab/ManiSkill/main/README.md)
- The audit shows that even SimplerEnv, built for sim–real correlation, can be matched by a 22M-parameter model trained on 120 scripted demonstrations collected next to the test conditions (94.8% versus X-VLA's reported 95.8%) — [arXiv 2606.04233](https://arxiv.org/html/2606.04233v1)

### Inferences
- A high score on any established benchmark is evidence about fine-tuning in that simulator only; the real-robot components above test transfer of a policy or of data, not whether simulated rankings predict real rankings.
- This is the gap the proxy-evaluation slice (SIMPLER and later real-to-sim suites) was built to fill.

### Gaps
- No study was found that measures correlation between LIBERO / CALVIN / RLBench scores and real-robot performance across models.
- ARNOLD's and MimicGen's real-robot numbers were not extracted.

## 5. Is each benchmark maintained, and is there an official leaderboard?

### Takeaway
Only CALVIN has an official leaderboard, and it lags the literature; RoboCasa's official leaderboard belongs to its 2026 successor. Maintenance is active for Meta-World, ManiSkill, robosuite / robomimic, RoboCasa, BEHAVIOR-1K and Gymnasium-Robotics, while the LIBERO, RLBench and VIMA-Bench repositories have seen no pushes since early 2025 or 2023.

### Cited Findings
- CALVIN official leaderboard with D→D, ABC→D and ABCD→D tables; its top ABC→D entry (FLOWER 4.53) is below results published since (page reachable over HTTP only) — [CALVIN leaderboard](http://calvin.cs.uni-freiburg.de/)
- RoboCasa: the RoboCasa365 leaderboard was published in April 2026; RoboCasa365 launched in February 2026; the site lists Diffusion Policy, π0 and GR00T as supported policies — [robocasa.ai](https://robocasa.ai/)
- LIBERO README mentions no leaderboard — [LIBERO README](https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/README.md); RLBench README mentions none — [RLBench README](https://raw.githubusercontent.com/stepjam/RLBench/master/README.md)
- Third-party aggregate leaderboard covering LIBERO, CALVIN, SimplerEnv, RoboCasa, RLBench, ManiSkill2 and newer suites, updated monthly and "largely maintained by AI" — [vla-eval leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/)
- Last repository push (GitHub API, read 2026-10-02): LIBERO 2025-03-15 — [repo](https://github.com/Lifelong-Robot-Learning/LIBERO); CALVIN 2025-09-08 — [repo](https://github.com/mees/calvin); RLBench 2025-01-25 — [repo](https://github.com/stepjam/RLBench); Meta-World 2026-09-12 — [repo](https://github.com/Farama-Foundation/Metaworld); ManiSkill 2026-08-04 (now under the mani-skill organization) — [repo](https://github.com/haosulab/ManiSkill); robosuite 2026-07-11 — [repo](https://github.com/ARISE-Initiative/robosuite); robomimic 2026-08-09 — [repo](https://github.com/ARISE-Initiative/robomimic); RoboCasa 2026-09-25 — [repo](https://github.com/robocasa/robocasa); BEHAVIOR-1K 2026-09-29 — [repo](https://github.com/StanfordVL/BEHAVIOR-1K); VIMA-Bench 2023-09-26 — [repo](https://github.com/vimalabs/VIMABench); ARNOLD 2025-03-16 — [repo](https://github.com/arnold-benchmark/arnold); Language-Table 2026-09-16 — [repo](https://github.com/google-research/language-table); gym-aloha and gym-pusht 2026-09-24 — [gym-aloha](https://github.com/huggingface/gym-aloha), [gym-pusht](https://github.com/huggingface/gym-pusht); Gymnasium-Robotics (Franka Kitchen) 2026-09-07 — [repo](https://github.com/Farama-Foundation/Gymnasium-Robotics)
- Meta-World is maintained by the Farama Foundation (v3 environments; Meta-World+ accepted at NeurIPS 2025 Datasets and Benchmarks) — [Meta-World README](https://raw.githubusercontent.com/Farama-Foundation/Metaworld/master/README.md); [arXiv 2505.11289](https://arxiv.org/abs/2505.11289)
- LIBERO and Meta-World are packaged for evaluation in LeRobot, and LIBERO in openpi and Isaac-GR00T — [LeRobot LIBERO docs](https://huggingface.co/docs/lerobot/libero); [LeRobot Meta-World docs](https://huggingface.co/docs/lerobot/metaworld); [openpi README](https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/README.md); [Isaac-GR00T README](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/main/README.md)

### Inferences
- For LIBERO, upkeep has moved from the original repository to downstream packagers (LeRobot, openpi, Isaac-GR00T, vla-eval) and to the variant benchmarks, which is why protocol details (episodes per task, control mode, dataset revision) now differ by toolkit.
- Without official leaderboards, the de facto record for LIBERO, RLBench and ManiSkill is each paper's own comparison table, where baseline numbers are frequently copied from earlier papers rather than re-run.

### Gaps
- Push dates show repository activity, not benchmark-protocol maintenance; issue backlogs and release notes were not inspected.
- Whether paperswithcode-style community leaderboards for these benchmarks are current was not checked.
