# New general-purpose simulation benchmark suites for VLA / generalist manipulation policies (2024 – October 2026)

Scope note: broad task suites and platform-style benchmarks only. Diagnostic / stress-test suites (LIBERO-Plus/PRO/X, VLABench, GemBench, RoboMME, RMBench, AGNOSTOS, INSIGHT Bench, RoboCerebra, MIKASA-Robo) were left to the diagnostic researcher. Entries already in `already_listed.txt` (RoboLab-120, X2Real, MolmoSpaces, Genie Sim 3.0, REALM, RobotArena ∞, Colosseum V2, RoboDojo-RealEval, DuoBench, RoboTwin Dual-Arm Collaboration Challenge, AgiBot World Challenge) were not re-catalogued. Machine-readable entries (34) are in `new_sim_suites.entries.json`. Verification status is stated per finding; "as extracted" means the number came from a fetched page summary and was not cross-checked against a second source.

## 1. Tabletop / bimanual suites (RoboTwin 1.0 and 2.0, RoboCasa365, RoboVerse, RLBench2 / PerAct2, BiGym, RoboDojo simulation, RoboEval, BiCoord, LBM Eval, GenManip, RoboFactory)

### Takeaway
RoboTwin 2.0 (ICML 2026) and RoboCasa365 (ICLR 2026) are the two 2024–2026 suites that function as main-results tables for VLA papers and have official leaderboards with third-party entries; RoboDojo's 42-task simulation suite (July 2026) is the hardest current one (best policy 8.8% success). The remaining bimanual suites (PerAct2/RLBench2, BiGym, RoboEval, BiCoord, LBM Eval, RoboFactory) are used mostly by their originating labs or by non-VLA policy papers.

### Cited Findings

**RoboTwin (1.0)**
- "RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins" (Mu, Chen, et al.) is listed as CVPR 2025 Highlight; an early version (arXiv 2409.02920) was presented at an ECCV 2024 workshop — [arXiv 2504.13059](https://arxiv.org/abs/2504.13059); [arXiv HTML](https://arxiv.org/html/2504.13059). The repo README states the early version received a Best Paper Award at the ECCV workshop — [RoboTwin README](https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/README.md)
- 15 tasks on the AgileX COBOT Magic platform (four arms, four RealSense D435 cameras); expert data comes from 3D generative models (digital twins from a single 2D image) plus LLM-generated task code; baselines are DP3 and Diffusion Policy trained with 20/50/100 demos — [arXiv HTML](https://arxiv.org/html/2504.13059)
- Real-robot part is sim-to-real transfer: pretraining on 300 simulated samples and fine-tuning on 20 real samples improved success by about 70% (single-arm) and 40% (dual-arm) over real-only training — [arXiv 2504.13059](https://arxiv.org/abs/2504.13059)

**RoboTwin 2.0**
- Accepted as an ICML 2026 poster — [ICML 2026 poster page](https://icml.cc/virtual/2026/poster/62192); arXiv first posted June 2025 — [arXiv 2506.18088](https://arxiv.org/abs/2506.18088)
- 50 dual-arm tasks, five embodiments (Franka, Piper, UR5, ARX-X5, Aloha-AgileX), RoboTwin-OD object library with 731 objects in 147 categories, 100,000+ expert trajectories, five domain-randomization axes (clutter, background textures, lighting, tabletop height, language) — [arXiv HTML](https://arxiv.org/html/2506.18088)
- Simulator is SAPIEN; the standard protocol uses Aloha-AgileX (14-D joint actions; head, left and right cameras), 50 `demo_clean` demos per task for training, 100 episodes per task, reported separately as Easy (clean) and Hard (randomized) — [LeRobot RoboTwin docs](https://huggingface.co/docs/lerobot/robotwin)
- Paper baselines (Easy / Hard average): RDT 34.5 / 13.7, π0 46.4 / 16.3, ACT 29.7 / 1.7, DP 28.0 / 0.6, DP3 55.2 / 5.0 (as extracted) — [arXiv HTML](https://arxiv.org/html/2506.18088)
- Official leaderboard ranks by the average of clean-to-clean and clean-to-random scores, with a fixed training set of 50 clean trajectories × 50 tasks on Aloha-AgileX and 100 trials per task; listing requires released code, weights and a technical report — [RoboTwin leaderboard](https://robotwin-platform.github.io/leaderboard)
- XPolicyLab (August 2026) integrates 42 policies and reports a top-10 RoboTwin table (10 Aug 2026): FastWAM 77.8% clean, Spatial Forcing 77.2%, π0.5 70.7%, X-WAM 70.0%, X-VLA 68.0% (as extracted) — [XPolicyLab arXiv 2608.09892](https://arxiv.org/html/2608.09892v1)
- A second protocol is in use: InternVLA-A1 fine-tunes on 2,500 clean plus 25,000 randomized episodes (50 + 500 per task) and reports 89.4% Easy / 89.6% Hard — [InternVLA-A1 arXiv 2601.02456](https://arxiv.org/html/2601.02456)
- Real-robot part is sim-to-real transfer on a COBOT-Magic (4 tasks): 10 real demos vs 10 real + 1,000 synthetic vs synthetic-only; the abstract reports 367% relative improvement (few-shot) and 228% (zero-shot) — [arXiv 2506.18088](https://arxiv.org/abs/2506.18088)
- Derived suites: BiCoord (18 long-horizon coordination tasks) and RMBench (memory) are built on RoboTwin 2.0 — [BiCoord arXiv](https://arxiv.org/html/2604.05831v1); [RMBench repo](https://github.com/RoboTwin-Platform/RMBench)

**RoboCasa365**
- ICLR 2026, authors Nasiriany, Nasiriany, Maddukuri, Zhu — [arXiv 2603.04356](https://arxiv.org/abs/2603.04356)
- 365 tasks (65 atomic, 300 composite across 60 activity categories), 2,500 kitchens (50 layouts × 50 styles), 30,000 human pretraining demos (404 h), 600,000 MimicGen demos (1,615 h), 25,000 human target demos (208 h); MuJoCo; Franka Panda on Omron mobile base; three 256×256 RGB views; 12-D actions; three protocols (multi-task, foundation-model training, lifelong learning) — [arXiv HTML](https://arxiv.org/html/2603.04356)
- Paper results on 50 target tasks (atomic / composite-seen / composite-unseen / average): Diffusion Policy 15.7 / 0.2 / 1.25 / 6.1; π0 36.3 / 5.2 / 0.7 / 15.0; π0.5 39.6 / 7.1 / 1.2 / 16.9; GR00T N1.5 43.0 / 9.6 / 4.4 / 20.0 (as extracted) — [arXiv HTML](https://arxiv.org/html/2603.04356)
- Leaderboard (published April 2026; 15 entries on 2026-10-02): Paimon-0 58.1, Xiaomi-Robotics-1 57.4, Phasor-m7 56.8, ABot-M0.6 46.6, ABot-M0.5 40.3, PRTS 39.6, RLDX-1 36.0, WorldDreamer 35.3, GR00T N1.5 23.9, LY-GWM 23.6, GR00T N1.6 21.9, GigaWorld-Policy 0.1 20.7, π0.5 16.9, π0 14.8, Diffusion Policy 6.1; splits are 18 atomic-seen, 16 composite-seen, 16 composite-unseen tasks; models train on Human300 pretraining data — [RoboCasa365 leaderboard](https://robocasa.ai/leaderboard.html)
- Real-robot part is sim-and-real co-training on a DROID Panda arm in a real kitchen (4 tasks, 20 trials each): 79.8% with co-training vs 61.8% real-only — [arXiv HTML](https://arxiv.org/html/2603.04356)

**RoboVerse**
- README states acceptance at RSS 2025; MetaSim core over Isaac Lab/Sim, Isaac Gym, MuJoCo, SAPIEN, PyBullet, Genesis, CoppeliaSim (via PyRep) — [RoboVerse README](https://raw.githubusercontent.com/RoboVerseOrg/RoboVerse/main/README.md)
- About 1,000 tasks (276 manipulation task categories), ~500k trajectories, ~5,500 assets; benchmark levels 0–3 (task space, environment randomization, camera randomization, lighting/reflection randomization); sections on direct sim-to-real transfer (IL) and sim-to-sim-to-real (RL) — [arXiv HTML](https://arxiv.org/html/2504.18904)

**PerAct2 / RLBench2**
- Extends RLBench to bimanual manipulation with 13 new tasks and 23 variations; baselines ACT, RVT-LF, PerAct-LF, PerAct2 — [arXiv 2407.00278](https://arxiv.org/abs/2407.00278); [project page](https://bimanual.github.io/)

**BiGym**
- CoRL 2024 — [CoRL 2024 listing](https://mlanthology.org/corl/2024/chernyadev2024corl-bigym/); 40 tasks, MuJoCo, Unitree H1 with two Robotiq 2F-85 grippers, 50 VR-teleoperated demos per task, whole-body (23-D) or bimanual (16-D) action modes; baselines BC, ACT, Diffusion Policy, DrQ-v2, AWAC, IQL, CQN; ACT best at 46.3% average (as extracted); no real-robot experiments — [arXiv HTML](https://arxiv.org/html/2407.07788)

**RoboDojo (simulation suite)**
- 42 simulation tasks on ARX X5 (Isaac Sim / Isaac Lab): Generalization 12, Memory 6, Long-Horizon 8, Precision 8, Open 8; 3,500 training trajectories (20.66 h); 50 episodes per task; 30 policies evaluated; best policy (Hy-Embodied-0.5-VLA) 8.80% average success vs 76.03% for human experts — [arXiv HTML](https://arxiv.org/html/2607.04434v1)
- The paper notes "partial but not complete alignment" between the simulation and real leaderboards; π0.5 is strong in both but relative ordering changes for several policies — [arXiv HTML](https://arxiv.org/html/2607.04434v1)

**RoboEval**
- 8 bimanual tasks, 28 variations, 3,000+ human demos; MuJoCo; bimanual Franka Panda; behavioral metrics for efficiency, safety/stability and coordination — [arXiv 2507.00435](https://arxiv.org/abs/2507.00435); [RoboEval repo](https://github.com/Robo-Eval/RoboEval)
- v2 (May 2026) evaluates ACT, Diffusion Policy, GR00T N1.6, X-VLA and π0.5; no real-robot experiments — [arXiv HTML](https://arxiv.org/html/2507.00435)

**BiCoord**
- 18 long-horizon bimanual tasks built on RoboTwin 2.0, 100 trajectories per task; DP 33.1%, RDT 39.5%, OpenVLA-OFT 40.5%, π0 46.4% (as extracted); simulation only — [arXiv HTML](https://arxiv.org/html/2604.05831v1)

**LBM Eval (TRI)**
- Open-source Drake benchmark with 49 tasks, gRPC policy interface, MIT/Apache licence, 124 stars — [lbm_eval repo](https://github.com/ToyotaResearchInstitute/lbm_eval)
- In the LBM paper: two Franka FR3 arms; 16 seen and 8 unseen simulated tasks; 200 rollouts per task per policy; Bayesian analysis; 3 seen tasks evaluated in both sim and real with discrepancies noted, no systematic correlation — [arXiv HTML](https://arxiv.org/html/2507.05331v1)
- TRI's VLA Foundry evaluates Foundry-VLA-1.7B and Foundry-Qwen3VLA-2.1B on 16 seen + 3 held-out lbm_eval tasks — [VLA Foundry arXiv](https://arxiv.org/html/2604.19728)

**GenManip / GenManip-Bench**
- CVPR 2025 — [CVPR poster](https://cvpr.thecvf.com/virtual/2025/poster/33632); Isaac Sim, single Franka, 200 human-refined scenarios, 10K assets; CoPA best modular system at 23.0%; GR-1 and ACT as end-to-end policies; simulation only — [arXiv HTML](https://arxiv.org/html/2506.10966v1)

**RoboFactory**
- ICCV 2025 — [RoboFactory repo](https://github.com/MARS-EAI/RoboFactory); ManiSkill, 11 tasks with 1–4 Franka arms, 150 demos per task, Diffusion Policy 49% (1 agent) to 10% (4 agents); simulation only — [arXiv HTML](https://arxiv.org/html/2503.16408)

### Inferences
- RoboTwin 2.0 scores are not comparable across papers unless the protocol is stated: the leaderboard protocol (50 clean demos per task) gives π0.5 about 70% clean, while the 50 + 500 demo protocol gives values near 90% in both settings.
- The RoboCasa365 leaderboard grew from 4 organizer baselines (April 2026) to 15 entries (September 2026), with the top three at 57–58% against 24% for the best organizer baseline, which suggests fast uptake by industrial VLA groups.
- Suites published with only DP / ACT / DP3 baselines (RoboTwin 1.0, BiGym, RoboFactory, PerAct2) have not become VLA results tables; suites that shipped π0 / π0.5 / GR00T baselines and a LeRobot-format dataset have.

### Gaps
- The RoboTwin 2.0 leaderboard table is rendered client-side and did not load; the number of entries and current top scores come only from the XPolicyLab paper.
- RoboVerse baseline names (whether OpenVLA / Octo are evaluated) and real-robot numbers could not be extracted from the arXiv HTML; the PDF exceeded the fetch size limit.
- PerAct2 venue: a search summary says CoRL 2024 workshop; neither arXiv nor the repo README confirms it. Robot model and demo counts were not captured.
- RoboCasa365: GR00T N1.5 and π0 values differ between the paper extraction (20.0, 15.0) and the leaderboard (23.9, 14.8); not resolved.
- BiCoord's π0 value (46.4%) is identical to RoboTwin 2.0's π0 Easy score; possible extraction error.

## 2. Humanoid and whole-body suites (HumanoidBench, RoboCasa GR-1 Tabletop, DexMimicGen, BEHAVIOR Challenge, Isaac Lab-Arena, SIMPLE, HumanoidGen, Labimus)

### Takeaway
The RoboCasa GR-1 Tabletop Tasks (24 tasks, introduced with GR00T N1 in March 2025) is the de facto humanoid row in VLA result tables; the BEHAVIOR Challenge (50 tasks in 2025, 100 in 2026) is the main long-horizon whole-body test, where the top 2025 entries were both π0.5 fine-tunes at about 0.26 q-score. SIMPLE (June 2026) is the first large loco-manipulation suite with VLA and world-action-model baselines.

### Cited Findings

**RoboCasa GR-1 Tabletop Tasks / GR00T simulation evaluation**
- GR00T N1 uses three simulation benchmarks: RoboCasa Kitchen (24 tasks, Franka), DexMimicGen Cross-Embodiment Suite (9 tasks) and GR-1 Tabletop Tasks (24 tasks, newly introduced; GR-1 with dexterous hands, egocentric camera, joint-space actions for arms, hands, waist, neck; 1,000 demos per task). At 100 demos per task: BC-Transformer 26.3 / 53.9 / 16.1, Diffusion Policy 25.6 / 56.1 / 32.7, GR00T-N1-2B 32.1 / 66.5 / 50.0 (as extracted) — [GR00T N1 arXiv HTML](https://arxiv.org/html/2503.14734v1)
- The repo provides 24 tabletop tasks, a teleop simulation dataset with 1,000 demos per task and a 240k-trajectory tabletop dataset; built on RoboCasa/robosuite — [robocasa-gr1-tabletop-tasks README](https://raw.githubusercontent.com/robocasa/robocasa-gr1-tabletop-tasks/main/README.md)
- Third-party use: StarVLA-α evaluates on LIBERO, SimplerEnv, RoboTwin 2.0 and RoboCasa-GR1 and reports 53.8% on RoboCasa-GR1 — [StarVLA-α arXiv HTML](https://arxiv.org/html/2604.11757)
- GR00T N1.7 documentation lists refreshed results on RoboCasa, RoboCasa GR1 tabletop tasks and SimplerEnv — [Isaac-GR00T README](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/main/README.md)

**DexMimicGen**
- ICRA 2025; 21K demos from 60 human demos; 9 tasks over bimanual Panda (grippers), bimanual Panda (dexterous hands) and GR-1 humanoid; MuJoCo/robosuite; baselines BC-RNN and Diffusion Policy — [arXiv 2410.24185](https://arxiv.org/abs/2410.24185); [arXiv HTML](https://arxiv.org/html/2410.24185)
- Real-robot part is real-to-sim-to-real: GR-1 can sorting reaches 90% with generated data vs 0% with source demos only — [arXiv HTML](https://arxiv.org/html/2410.24185)

**HumanoidBench**
- RSS 2024 — [RSS 2024 paper page](https://roboticsconference.org/2024/program/papers/61/); MuJoCo; Unitree H1 with two Shadow Hands (Digit and Robotiq variants supported); 27 tasks; proprioceptive, egocentric visual and tactile observations; RL baselines; simulation only — [HumanoidBench project page](https://humanoid-bench.github.io/); [arXiv 2403.10506](https://arxiv.org/abs/2403.10506)

**BEHAVIOR Challenge**
- 2025 edition: held at the "Foundation Models Meet Embodied Agents" challenge at NeurIPS 2025 (7 Dec 2025, San Diego); 50 full-length household tasks; 10,000 teleoperated demos (1,200+ h); OmniGibson on Isaac Sim; standard and privileged-information tracks; metric is task success with partial credit over BDDL goal predicates; baselines ACT, Diffusion Policy, BC-RNN, WB-VIMA, OpenVLA, π0 — [2025 challenge archive](https://behavior.stanford.edu/challenge/archive/2025/index.html)
- 2025 final top five (q-score): Robot Learning Collective 0.2599, NVIDIA Comet 0.2514, SimpleAI Robot 0.1591, Huawei CRI EAI 0.1204, Embodied Intelligence 0.0947; the winner builds on π0.5; tasks average 6.6 min; 10 evaluation episodes per task — [1st-place report arXiv 2512.06951](https://arxiv.org/html/2512.06951v2)
- The 2nd-place report (Openpi Comet, NVIDIA) also builds on π0.5 and reports a post-challenge validation q-score of 0.345 — [arXiv 2512.10071](https://arxiv.org/abs/2512.10071)
- 2026 edition: 100 tasks, 20,000 teleoperation demos (1,950 h), 7 scenes (4 new), single track with RGB + depth + proprioception, baselines π0.5 and GR00T N1.7, launch 2 July 2026, deadline 16 Oct 2026, winners 4 Nov 2026 — [BEHAVIOR challenge page](https://behavior.stanford.edu/challenge)

**Isaac Lab-Arena and suites on it**
- NVIDIA blog (5 Jan 2026): open-source framework co-developed with Lightwheel; environments compiled from Object, Scene, Embodiment and Task blocks; Lightwheel-RoboCasa-Tasks and Lightwheel-LIBERO-Tasks give 250+ tasks; GR1 and Franka embodiments; GR00T N1.5, π0, SmolVLA supported; integrated in the LeRobot Environment Hub — [NVIDIA blog](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/)
- IsaacLabEvalTasks: two GR1-T2 industrial tasks (nut pouring, exhaust pipe sorting) for benchmarking GR00T N1 in Isaac Lab — [IsaacLabEvalTasks repo](https://github.com/isaac-sim/IsaacLabEvalTasks)
- RoboFinals-100 (Lightwheel, announced 4 Dec 2025): 100 household / factory / retail tasks on Isaac Lab-Arena; not publicly available; Qwen named as user — [RoboFinals page](https://lightwheel.ai/robofinals)

**SIMPLE**
- USC PSI Lab, arXiv 6 June 2026; MuJoCo physics with Isaac Sim rendering; Unitree G1; 60 whole-body tasks, 50 indoor scenes, 1,000+ objects; baselines Ψ0, DreamZero, π0.5, GR00T N1.6, InternVLA, H-RDT, EgoVLA, DP, ACT at three randomization levels; zero-shot sim-to-real on two tasks (90% → 80%, 100% → 80%) — [arXiv HTML](https://arxiv.org/html/2606.08278); [project page](https://psi-lab.ai/SIMPLE)

**HumanoidGen (HGen-Bench)** and **Labimus**
- HGen-Bench: 20 tasks, SAPIEN, Unitree H1-2 with Inspire hands, 100 demos per task, DP and DP3 baselines — [arXiv HTML](https://arxiv.org/html/2507.00833v2)
- Labimus: Isaac Sim, Tianyi 2.0 humanoid with BrainCo Revo 2 hands, 7 chemistry-lab tasks, 100 demos per task, ACT / DP / π0, simulation only — [arXiv HTML](https://arxiv.org/html/2606.31037)

### Inferences
- Humanoid evaluation in VLA papers is dominated by fixed-base upper-body tabletop tasks (RoboCasa GR-1, DexMimicGen); legged loco-manipulation suites with VLA baselines only appeared in 2026 (SIMPLE); the BEHAVIOR Challenge uses a mobile-base bimanual robot rather than a legged humanoid.
- BEHAVIOR Challenge scores (top q-score about 0.26 in 2025) show that long-horizon household tasks remain far from solved even with 200 demos per task.

### Gaps
- No organizer report paper for the 2025 BEHAVIOR Challenge was found; the robot model name (Galaxea R1 Pro in the brief) was not stated on the pages opened.
- The Hugging Face 2026 leaderboard was not opened; no 2026 scores captured.
- SIMPLE venue (a search result mentions CoRL 2026) is unconfirmed; the project page states 100,000+ demonstrations while the paper text extracted states 6,000+ episodes.
- HumanoidBench's 15 manipulation / 12 locomotion split comes from a search snippet of the RSS paper; no VLA results on HumanoidBench were found.
- GR00T N1.5 / N1.6 / N1.7 numeric results on GR-1 Tabletop were not captured.

## 3. Mobile manipulation and household suites (ManiSkill-HAB, EBench, MobileManiBench, AgentWorld, RoboBenchMart, RoboCasa365, BEHAVIOR)

### Takeaway
EBench (June 2026) and MobileManiBench (ECCV 2026) are the new mobile-manipulation suites with π0 / π0.5 baselines; both are simulation-only and report low absolute success (π0.5: 41.0% on EBench, 18.8% on MobileManiBench). ManiSkill-HAB (ICLR 2025) remains an RL/IL benchmark without VLA results.

### Cited Findings
- ManiSkill-HAB: ICLR 2025; GPU implementation of the Home Assistant Benchmark; TidyHouse, PrepareGroceries, SetTable with Pick / Place / Open / Close subtasks; datasets of 18K, 18K, 8K episodes; RL and IL baselines do not solve the tasks; no real-robot experiments — [MS-HAB project page](https://arth-shukla.github.io/mshab/); [arXiv 2412.13211](https://arxiv.org/abs/2412.13211)
- EBench: Isaac Sim at 60 Hz; dual-arm mobile robot; 26 tasks (10 mobile pick-and-place, 9 mobile long-horizon, 7 tabletop dexterous/precise); 9 scene categories; 5 capability dimensions and 4 generalization dimensions (background, object, instruction, mix); 6,600 episodes / 91.4 h; 510 test episodes; test success π0 34.4%, π0.5 41.0%, X-VLA 24.7%, InternVLA-A1 27.6%; authors state they do not claim simulation scores predict real performance; hosted leaderboard — [arXiv HTML](https://arxiv.org/html/2606.18239)
- MobileManiBench: ECCV 2026 (Microsoft Research Asia); Isaac Sim; AgiBot G1 with gripper and XHand robot with 12-DoF hand; 630 objects, 20 categories, 5 skills, 100+ tasks, 100 scenes, 300K RL-generated trajectories; OpenVLA 4.5%, CogACT 6.8%, π0 11.2%, π0.5 18.8%, MobileManiVLA 28.2% — [arXiv 2602.05233](https://arxiv.org/abs/2602.05233); [arXiv HTML](https://arxiv.org/html/2602.05233v2); no real-robot results on the project page — [project page](https://dexhand.github.io/MobileManiBench/)
- AgentWorld: CoRL 2025; Isaac Sim; Unitree G1/H1, Franka on wheeled base, DOBOT X-Trainer; 150 scenes, 9,000+ assets, 1,000+ trajectories; BC / ACT / DP / π0 baselines (π0 64–82% basic, 18–30% multistage); sim-and-real co-training with 100 simulated + 9 real demos gives 29.3% real pick-and-place — [arXiv 2508.07770](https://arxiv.org/abs/2508.07770); [arXiv HTML](https://arxiv.org/html/2508.07770v2)
- RoboBenchMart: ManiSkill3; Fetch; 5 atomic + 2 composite retail tasks; 370 products; Octo, SmolVLA, π0, π0.5; all models score 0% on composite tasks; no real-robot experiments — [arXiv HTML](https://arxiv.org/html/2511.10276)
- Kitchen-R ("Mind and Motion Aligned"): Isaac Sim kitchen benchmark with 500+ language instructions that evaluates task planning, low-level control and the combined system for a mobile manipulator — [arXiv 2508.15663](https://arxiv.org/abs/2508.15663)

### Inferences
- New mobile suites report π0.5 as the strongest open baseline, consistent across EBench, MobileManiBench and RoboBenchMart, but absolute numbers stay below 45%.

### Gaps
- BEHAVIOR-1K simulator/asset updates in 2025 beyond the challenge were not investigated (BEHAVIOR-1K itself is assigned to another researcher).
- ManiSkill-HAB robot model was not captured in this session; no VLA results were found for it.
- MobileManiBench's arXiv text refers to real-robot results in an appendix that was not visible.
- Kitchen-R baselines beyond "VLM planner + Diffusion Policy" were not checked; it is not in the JSON file.

## 4. Dexterous-hand and contact-rich suites (DexVerse, DexJoCo, DexMimicGen, Assemble Bench, GarmentLab, DexGarmentLab)

### Takeaway
Two 2026 dexterous-hand suites report VLA baselines: DexVerse (100 tasks, Isaac Lab; π0.5 34%, OpenVLA 19% on a 19-task subset) and DexJoCo (11 tasks, MuJoCo; π0.5 and GR00T N1.5 both 40.2%, below ACT at 54.1%). In both, VLAs do not outperform small imitation policies.

### Cited Findings
- DexVerse (arXiv 9 July 2026): Isaac Lab; 3 arms (Franka Research 3, UR10e, xArm 7) and 6 hands (Sharpa Wave, WUJI, Shadow, Inspire, Allegro, LEAP); 100 tasks in 8 categories; 3,180 Apple Vision Pro demos; on 19 tasks with 50 episodes each: π0.5 34%, DP3 34%, DP 32%, OpenVLA 19%; no real-robot experiments — [arXiv 2607.08751](https://arxiv.org/abs/2607.08751); [arXiv HTML](https://arxiv.org/html/2607.08751v1)
- DexJoCo (arXiv 15 May 2026): MuJoCo; Franka Panda with Allegro Hand; 11 tasks; 1.1K trajectories; rand-obj success ACT 54.1%, DP-T 50.4%, DP-C 47.6%, π0.5 40.2%, GR00T N1.5 40.2%; simulation only — [arXiv 2605.16257](https://arxiv.org/abs/2605.16257); [arXiv HTML](https://arxiv.org/html/2605.16257v2)
- Assemble Bench (HUD, 31 July 2026): 14 peg / gear / nut tasks based on NIST Assembly Task Boards on Isaac Lab-Arena with the DROID platform; 1,355 scripted demos; π0.5 with BC and CG-DAgger; one real-robot video — [HUD page](https://www.hud.ai/research/assemble-benchmark)
- GarmentLab: NeurIPS 2024; garment / deformable benchmark with FEM and PBD simulation, sim-to-real algorithms and a real-world benchmark — [arXiv 2411.01200](https://arxiv.org/abs/2411.01200)
- DexGarmentLab: NeurIPS 2025 Spotlight; 15 bimanual dexterous garment task scenarios — [arXiv 2505.11032](https://arxiv.org/abs/2505.11032)

### Inferences
- On dexterous-hand suites, pretrained VLAs are at or below ACT / DP3, which matches the note in a 2026 sim-to-real study that VLA pretraining does not confer an advantage in high-DoF hand control (seen only in a search snippet for arXiv 2603.22876, not opened).

### Gaps
- No tactile simulation benchmark with VLA results was found (ManiSkill-ViTac is already listed as a competition).
- GarmentLab and DexGarmentLab were verified at abstract level only; simulator names, baselines and any VLA results were not checked.

## 5. Other suites found by active search (domain-specific labs, retail, platforms)

### Takeaway
A cluster of 2025–2026 domain-specific suites applies π0-class policies to laboratory automation (AutoBio, LabUtopia, Labimus, Pipette, LabDex); these are small (7–24 tasks), simulation-only except LabDex, and not adopted as general VLA results tables.

### Cited Findings
- AutoBio: MuJoCo with thread / detent / liquid plugins and Blender rendering; ALOHA and UR5e; 16 tasks at 3 levels; 100 demos per task; π0 and RDT (about 83–86% easy, 1–21% medium, 4–8% hard); simulation only — [arXiv HTML](https://arxiv.org/html/2505.14030v3)
- LabUtopia: NeurIPS 2025; Isaac Sim; 4 levels (10 basic, 6 combined, 6 generalization, 2 long-sequence tasks per README); ACT and Diffusion Policy baselines — [LabUtopia repo](https://github.com/Rui-li023/LabUtopia)
- Pipette: Isaac Sim 5.1 / Isaac Lab 2.3; 12 wet-lab tasks; 30 human demos per task; ACT, SmolVLA, π0; simulation only — [arXiv HTML](https://arxiv.org/html/2606.12936v3)
- LabDex (arXiv 19 Aug 2026): Franka Research 3 with XHand; hierarchical real + simulation lab benchmark; reported results are real-world (π0.5 0.57 overall on atomic skills, ACT 0.34, DP 0.02; 50 trials per task) — [arXiv HTML](https://arxiv.org/html/2608.18618v1)
- RoboPlayground (April 2026; Wang, Ung, Gubarev, Tan, Srinivasa, Fox): language-driven authoring of evaluation tasks in a structured block-manipulation domain — [arXiv 2604.05226](https://arxiv.org/abs/2604.05226)
- RoboChess Challenge (CoRL 2026 workshop on GPU-accelerated simulation): sim (Isaac Lab, MuJoCo, Genesis) plus real evaluation of chess-piece manipulation with VLA baselines — [workshop page](https://sites.google.com/view/corl-workshop-robochess) (seen in search results only)

### Inferences
- LabDex and the RoboChess Challenge fit the real-world / competition categories better than this simulation category; flagged for the gap-check researcher.

### Gaps
- IndustrialVLA-Bench (arXiv 2609.25562) is a multi-axis evaluation over LIBERO, LIBERO-Plus and LIBERO-Para, not a new suite; left to the diagnostic researcher — [arXiv HTML](https://arxiv.org/html/2609.25562)
- Not opened and therefore not catalogued: GRUtopia, FetchBench, Mimicking-Bench, M3Bench, PARTNR, MuJoCo Playground, Meta-World+, MuBlE, WOLF-VLA benchmark, LeVERB.

## 6. VLA results, leaderboards and adoption

### Takeaway
Official leaderboards exist for RoboTwin 2.0, RoboCasa365, RoboDojo, EBench, RoboEval (project-page section), SIMPLE (stated) and the BEHAVIOR Challenge. Cross-benchmark tooling (vla-eval, XPolicyLab, StarVLA, LeRobot) has converged on RoboTwin 2.0, RoboCasa / RoboCasa365 and BEHAVIOR-1K as the new suites worth integrating.

### Cited Findings
- The AllenAI vla-eval harness supports LIBERO, LIBERO-Pro/Plus/Mem, SimplerEnv, CALVIN, ManiSkill2, RoboCasa, RoboCasa365, RoboCerebra, VLABench, MIKASA-Robo, RoboTwin 2.0, RLBench, Kinetix, MolmoSpaces-Bench, DuoBench, RoboDojo, BEHAVIOR-1K (2025), FurnitureBench — [vla-evaluation-harness repo](https://github.com/allenai/vla-evaluation-harness)
- The vla-eval paper reports that 81% of 509+ models were evaluated on a single benchmark and 6% on three or more — [vla-eval arXiv 2603.13966](https://arxiv.org/html/2603.13966)
- XPolicyLab integrates 42 policies across RoboTwin 2.0, RoboDojo simulation and RoboDojo-RealEval (8 Aug 2026) — [XPolicyLab arXiv](https://arxiv.org/html/2608.09892v1)
- Policies with published results per suite: RoboTwin 2.0 — π0, RDT, π0.5, X-VLA, InternVLA-A1, StarVLA-α, GR00T N1.6 ([RoboTwin 2.0](https://arxiv.org/html/2506.18088); [StarVLA-α](https://arxiv.org/html/2604.11757); [InternVLA-A1](https://arxiv.org/html/2601.02456)); RoboCasa365 — see leaderboard ([leaderboard](https://robocasa.ai/leaderboard.html)); RoboDojo — 30 policies including π0, π0.5, X-VLA, GR00T N1.7, OpenVLA-OFT, RDT-1B, SmolVLA ([RoboDojo](https://arxiv.org/html/2607.04434v1)); EBench — π0, π0.5, X-VLA, InternVLA-A1 ([EBench](https://arxiv.org/html/2606.18239)); SIMPLE — Ψ0, π0.5, GR00T N1.6, InternVLA, H-RDT, EgoVLA, DreamZero ([SIMPLE](https://arxiv.org/html/2606.08278)); RoboEval — GR00T N1.6, X-VLA, π0.5 ([RoboEval](https://arxiv.org/html/2507.00435))
- X-VLA evaluates on LIBERO, SimplerEnv, VLABench, RoboTwin 2.0, CALVIN and NAVSIM — [X-VLA arXiv](https://arxiv.org/html/2510.10274)

### Inferences
- Adoption tiers (author's judgement from the evidence above): high — RoboTwin 2.0, RoboCasa GR-1 Tabletop, RoboCasa365, BEHAVIOR Challenge; emerging with leaderboard — RoboDojo, EBench, SIMPLE, RoboEval; originating-lab only — LBM Eval, GenManip, BiCoord, DexVerse, DexJoCo, MobileManiBench, AgentWorld, RoboBenchMart, lab suites; RL-oriented with no VLA uptake — HumanoidBench, ManiSkill-HAB, BiGym.

### Gaps
- The vla-eval literature leaderboard is client-rendered and did not load, so per-benchmark model counts are unavailable.
- StarVLA-α and X-VLA per-benchmark numbers on RoboTwin 2.0 were returned inconsistently by the fetch tool and are not reported here.
- OpenVLA-OFT results on RoboTwin 2.0 are indicated only as a baseline in StarVLA-α and in a search snippet; exact numbers unverified.

## 7. Real-robot experiments: type per suite

### Takeaway
None of the suites in this slice reports a paired sim-versus-real evaluation with a correlation statistic. Real-robot content, where present, is sim-to-real or co-training transfer; RoboDojo and LBM Eval run the same policies in both domains but describe agreement only qualitatively.

### Cited Findings
- (i) Sim-to-real or co-training transfer: RoboTwin 1.0 ([source](https://arxiv.org/abs/2504.13059)); RoboTwin 2.0 ([source](https://arxiv.org/html/2506.18088)); RoboCasa365 co-training ([source](https://arxiv.org/html/2603.04356)); DexMimicGen real-to-sim-to-real ([source](https://arxiv.org/html/2410.24185)); RoboVerse ([source](https://arxiv.org/html/2504.18904)); AgentWorld co-training ([source](https://arxiv.org/html/2508.07770v2)); SIMPLE zero-shot on two tasks ([source](https://arxiv.org/html/2606.08278)); Assemble Bench single video ([source](https://www.hud.ai/research/assemble-benchmark))
- (ii-partial) Same policies evaluated in sim and real without a reported correlation coefficient: RoboDojo ("partial but not complete alignment") ([source](https://arxiv.org/html/2607.04434v1)); LBM Eval (3 tasks, discrepancies noted) ([source](https://arxiv.org/html/2507.05331v1)); SIMPLE claims "strong correlation" from two tasks ([source](https://arxiv.org/html/2606.08278))
- (iii) None: BiGym ([source](https://arxiv.org/html/2407.07788)); HumanoidBench ([source](https://humanoid-bench.github.io/)); ManiSkill-HAB ([source](https://arth-shukla.github.io/mshab/)); EBench ([source](https://arxiv.org/html/2606.18239)); RoboEval ([source](https://arxiv.org/html/2507.00435)); BiCoord ([source](https://arxiv.org/html/2604.05831v1)); DexVerse ([source](https://arxiv.org/html/2607.08751v1)); DexJoCo ([source](https://arxiv.org/html/2605.16257v2)); GenManip ([source](https://arxiv.org/html/2506.10966v1)); RoboFactory ([source](https://arxiv.org/html/2503.16408)); RoboBenchMart ([source](https://arxiv.org/html/2511.10276)); AutoBio ([source](https://arxiv.org/html/2505.14030v3)); Labimus ([source](https://arxiv.org/html/2606.31037)); Pipette ([source](https://arxiv.org/html/2606.12936v3)); BEHAVIOR Challenge ([source](https://behavior.stanford.edu/challenge/archive/2025/index.html))
- RoboFinals states Real2Sim calibration of its asset library but publishes no real-robot comparison — [RoboFinals page](https://lightwheel.ai/robofinals)

### Inferences
- The suites that do report sim-real correlation are the ones already catalogued as real-validated proxies (RoboLab-120, X2Real, REALM, etc.); the broad task suites in this slice are evidence of simulation performance only.

### Gaps
- Unclear or unverified: PerAct2 (project page mentions real-world use without detail), HumanoidGen (appendix not read), MobileManiBench (appendix not visible), GarmentLab and DexGarmentLab (abstract only), RoboCasa GR-1 Tabletop (GR00T N1's real GR-1 experiments were not read for a sim-real pairing).
