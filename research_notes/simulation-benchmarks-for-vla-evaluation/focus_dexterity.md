# Dexterity / Precise-Action Benchmarks for VLA and Generalist Policies (2023 – Oct 2026)

Scope: benchmarks NOT in `already_listed.txt` that test precise action (tight tolerance, contact-rich, finger dexterity). 20 new entries are in `focus_dexterity.entries.json`. Research date: 2026-10-02. All pages cited below were opened in this session unless marked "search snippet only". Numbers were extracted from arXiv HTML / project pages through an automated page reader; entries where that reading is the only check are flagged.

Reading guide for the 20 JSON entries:
- With VLA / generalist results (11): WireCraft, WorkBenchMark, MetaFine, SurgVLA-Bench, PRISM, DexHoldem, Bench2Dex, NeoSim, ForceBench, Tabero, FACT contact-rich task suite. UniVTAC has VLA numbers only from a later third-party paper.
- Without VLA results (8): ManiFeel, ALOHA sim, DexToolBench, DexCraft, AutoMate, QBIT, VTDexManip, RoboPianist.

## Insertion, assembly and tight tolerance

### Takeaway
Only a few uncatalogued benchmarks both state a clearance and report VLA results: WireCraft (3 mm connector clearance, pi0.5 at 0% insertion) and WorkBenchMark (LEGO Duplo, fine-tuned pi0.5 falling from 82% to 2% across tiers). Most tight-tolerance work with VLAs (0.02–1 mm) still appears as tasks inside method papers or on the already-catalogued NIST / ManipulationNet boards, not as new benchmarks.

### Cited Findings
- WireCraft (University of Toronto, arXiv 2026-06-16) is an Isaac Lab 2.2.1 / Isaac Sim 4.5 benchmark for industrial deformable-linear-object manipulation with three task families: connector insertion (cylinder, cuboid, Ethernet, DisplayPort) at a stated 3 mm plug–socket clearance, clip routing (1–3 clips) and channel seating — [WireCraft](https://arxiv.org/abs/2606.18097)
- WireCraft reports reach success and insertion success separately. On Ethernet insertion: state PPO 95.86% insertion, SACfD 92.40%, vision PPO 17.74%, pi0.5 6.2% reach / 0.0% insertion; a Diffusion Transformer VLA policy reaches 3.13% insertion (search snippet of the same paper). A UR5 real test with ACT reached 4/10 insertions. Code and data are promised "upon acceptance" — [WireCraft](https://arxiv.org/html/2606.18097)
- WorkBenchMark (RWTH Aachen / FH Aachen, arXiv 2026-06-20) has 400 LEGO Duplo assembly tasks in four tiers in MuJoCo (via LIBERO) plus a real subset of 10 tasks per tier on a UR5; metrics are assembly success and execution accuracy (fraction of brick connections at the target relative pose) — [WorkBenchMark](https://arxiv.org/abs/2606.19358); [project](https://workbenchmark.github.io/)
- WorkBenchMark VLA numbers (success by tier 1–4): fine-tuned pi0.5 82 / 63 / 23 / 2%; zero-shot Gemini 2.5 Flash + pi0.5 70 / 59 / 19 / 5%; the authors' planning pipeline 94 / 87 / 67 / 62%. The real UR5 runs (90 / 90 / 70% for tiers 1–3) are for the planning pipeline only — [WorkBenchMark](https://arxiv.org/html/2606.19358)
- AutoMate (NVIDIA / USC, RSS 2024) provides 100 plug-and-socket assemblies that are simulation-compatible and 3D-printable; specialist policies reach about 80%+ on 80 assemblies, a generalist 80%+ on 20; real trials: 200 policy-only trials over 20 assemblies and 100 perception-initialized trials over 5 assemblies with 86–90% mean success. No VLA baseline — [AutoMate](https://arxiv.org/abs/2407.08028); [project](https://bingjietang718.github.io/automate/)
- QBIT (arXiv 2025-03) benchmarks peg-in-hole and USB insertion at 1 mm and 0.1 mm clearance in MuJoCo with randomized contact parameters and on a real UR5e with a SCHUNK force/torque sensor; baselines are position control, impedance control and InsertionNet; 100 real repetitions per method. No VLA baseline — [QBIT](https://arxiv.org/abs/2503.07479); [HTML](https://arxiv.org/html/2503.07479)
- The ALOHA / ACT paper (RSS 2023) defines two simulated fine bimanual tasks with stated clearances: Transfer Cube ("around 1cm" between cube and left gripper) and Bimanual Insertion ("around 5mm in the insertion phase"); ACT reaches 86% / 50% (scripted / human data) on Transfer and 32% / 20% on Insertion, over 3 seeds × 50 rollouts with 50 demonstrations — [ACT paper](https://arxiv.org/abs/2304.13705); venue from [project page](https://tonyzhaozh.github.io/aloha/); tasks distributed as [gym-aloha](https://github.com/huggingface/gym-aloha)
- "The Curse of Precision" (Tsinghua, arXiv 2026-07-25) is a scaling study, not a benchmark: in ManiSkill3 it varies peg-insertion clearance and cuboid-stacking tolerance over 4–10 mm and a ball-rolling target radius over 35–200 mm, trains Diffusion Policy in 100+ runs, and reports that required data grows super-exponentially as the precision target approaches a system-dependent limit. No release is stated — [Curse of Precision](https://arxiv.org/html/2607.23108)
- FurnitureVLA (MERL, arXiv 2026-07-01) extends the FurnitureBench Isaac Gym code to real-scale IKEA furniture (LACK, KALLAX, IVAR) with dual Kinova Gen3 arms and success thresholds of 1–2 cm translation and about 4° rotation; the authors say no new benchmark is introduced. Results: monolithic pi0.5 48% average (91 / 11 / 41%), FurnitureVLA 80%, zero-shot pi0.5 0% — [FurnitureVLA](https://arxiv.org/html/2607.01212v1)
- InsertAnything (arXiv 2026-09) fabricates insertion workpieces with five hole shapes and clearances of 2, 0.5, 0.1 and 0.02 mm and reports "the first perfect score of 20/20" on the ManipulationNet peg-in-hole benchmark under the human-in-the-loop protocol; baselines are classical search and hybrid force/position controllers, not VLAs — [InsertAnything](https://arxiv.org/html/2609.24511v1)

### Inferences
- Where a clearance is stated and a VLA is tested, the VLA is at or near zero: 0.0% insertion at 3 mm for pi0.5 on WireCraft, 20% at 3 mm on NIST ATB M1 (see the catalogued-benchmark section). State-based RL on the same WireCraft task is above 90%, so the gap is in visuomotor precision, not task feasibility.
- No uncatalogued benchmark was found that reports VLA success as a curve over several clearance levels. The boards that have graded clearances (ManipulationNet 3 / 1 / 0.1 / 0.02 mm; Peg-in-Bench 3 / 1 / 0.1 mm) are already catalogued and have no VLA baselines.
- WorkBenchMark's difficulty for VLAs comes mainly from planning horizon; Duplo bricks are described by the authors as mechanically forgiving, so it is a weaker precision test than the others.

### Gaps
- No benchmark for watchmaking or micro-assembly with VLA baselines was found.
- No VLA results were found on AutoMate, QBIT or (in a peer-reviewed table) the two ALOHA sim tasks. Community numbers exist (e.g. a third-party SmolVLA run at 2/20 on AlohaInsertion, search snippet only) but were not verified.
- "A Simulation Benchmark for Dexterous Peg-in-Hole Assembly With Force-Tactile-Based Pose Estimation Across Multiple Embodiments" (IEEE Xplore document 11593873; Isaac Gym; 49.68% average insertion success per a search snippet) could not be opened (HTTP 418), so it is not in the JSON.
- The session's web-search budget (200 queries) ran out before a final sweep; competition results for RGMC 2026 and ManiSkill-ViTac 2026 were not checked.

## Fine bimanual and tool tasks used as VLA precision tests (ALOHA-style, laboratory, electronics, surgical)

### Takeaway
One new surgical VLA benchmark (SurgVLA-Bench, simulation) and one industrial real-robot dataset with a baseline protocol (PRISM) were found. ALOHA-style real tasks (zip-tie threading, battery slotting, shoe lacing) are still reported as per-paper task sets, not as a packaged benchmark.

### Cited Findings
- SurgVLA-Bench (arXiv 2026-06-28) is built on SurRoL (PyBullet) with 8 tasks in three levels: atomic (gauze pick, needle pick, electrocoagulation), conditional (with distractors, vessel clipping) and composite (pick and place, hemostasis). Over 800 trajectories are used for LoRA fine-tuning and each model gets 50 trials per task — [SurgVLA-Bench](https://arxiv.org/abs/2606.29247); [HTML](https://arxiv.org/html/2606.29247)
- SurgVLA-Bench results (per-task ranges): OpenVLA 36–76% on Level 1 and 0% on Level 3; pi0 0–76% on Level 1; pi0.5 0–78% on Level 1, 0–12% on Level 3; SmolVLA 0–8% everywhere. The abstract states that autoregressive models show stronger semantic comprehension and flow-matching models better task precision. No real-robot validation — [SurgVLA-Bench](https://arxiv.org/html/2606.29247)
- PRISM (Peking University and partners; arXiv 2026-08-18; GitHub repository titled "[IROS2026]") is a real dataset of 25 industrial contact-rich tasks (connector plug/unplug, bearing installation, NIST task-board operations, sorting) with 5,000+ trajectories (about 45 h), multi-view RGB-D, 6-axis F/T at 100 Hz and visuotactile images, on Franka, bimanual Realman RM75-6F and a LEJU humanoid — [PRISM](https://arxiv.org/html/2608.17962); [code](https://github.com/Tengbo-Yu/PRISM)
- PRISM baselines (bimanual Realman, 200 demos per task, 20 trials, with pretraining): plug/unplug ACT 10%, DP 10%, pi0 25%; caliper packaging 55 / 55 / 85%; conveyor sorting 30 / 20 / 85% — [PRISM](https://arxiv.org/html/2608.17962)
- The ACT paper's real tasks give dimensions that later papers reuse as precision demands: the zip-tie hole is 4 mm × 1.5 mm for a 0.8 mm × 3.5 mm tie, and stacked cups have 2.5 mm clearance; these are tasks in a method paper, not a benchmark — [ACT paper](https://arxiv.org/abs/2304.13705)
- Facet-0 (NTU PINE Lab, arXiv 2026-09-01) releases ManuFacet-1K, a 1,000-hour force-synchronized corpus (25,153 episodes per the project page) over UR7e, xArm and Franka, and evaluates on sub-millimetre computer-assembly tasks (RAM, CPU, GPU, disk); reported 82% mean success versus 15% for the strongest baseline and 0.5 mm placement accuracy. It is a model and dataset, not a benchmark, and the project page names no VLA baselines — [Facet-0](https://arxiv.org/abs/2609.01596); [project](https://pine-lab-ntu.github.io/facet-0/)

### Inferences
- In SurgVLA-Bench the precision demand is implicit (thin needles, small targets under an endoscope view) and success is binary; it does not report positional error, unlike the already-catalogued SutureBot.
- PRISM's hardest baseline task is the tight-tolerance one: connector plug/unplug stays at 10–25% while the two looser tasks reach 85% with pi0.

### Gaps
- No packaged benchmark of ALOHA-style fine bimanual tasks (thread zip tie, battery insertion, shoe lacing) with a multi-VLA comparison was found; the search snippet for GR-RL (arXiv 2512.01801) reports shoe lacing at 83.3% but that is a method result.
- A multi-policy suture-following evaluation in open surgery (ACT, Diffusion Policy, SmolVLA, pi0; arXiv 2605.28736) appeared in search results but was not opened.
- Laboratory benchmarks found (AutoBio, Labimus, Pipette, LabUtopia, LabDex) are all already catalogued; no new one was found. VLA-Precision (arXiv 2609.04355; nine real chemistry tasks, 98.3% after online RL per a search snippet) is a method paper and was not opened.

## Dexterous multi-fingered hands

### Takeaway
Three new dexterous-hand benchmarks carry VLA or generalist baselines or are designed for them: Bench2Dex (simulation, 12 hands, GR00T N1.5 and pi0.5), DexHoldem (real ShadowHand, pi0.5 / pi0 / RDT), and, without VLA baselines, DexToolBench (real tool use) and DexCraft (simulated articulated tool use). An industry standard, RLWRLD's DexBench, is announced but not released.

### Cited Findings
- Bench2Dex (technical report, arXiv 2026-09-14) is an Isaac Lab benchmark with 26 bimanual tasks, 12 arm–hand embodiments (e.g. UR5+Shadow, Panda+Allegro, xArm7+LEAP, IIWA7+Sharpa), about 1.3K teleoperated demonstrations and a shared tactile image built by ray-casting contact distance — [Bench2Dex](https://arxiv.org/abs/2609.15726); [project](https://bench2dex.github.io/)
- Bench2Dex results over 1,300 rollouts per policy: matched scenes GR00T N1.5 48.5%, ACT 29.5%, pi0.5 27.3%, Diffusion Policy 12.9%; combined perturbations GR00T N1.5 19.8%, pi0.5 19.7%, ACT 13.0%, DP 3.8%. No real-robot experiment; the authors state hand and tactile models are not calibrated to hardware — [Bench2Dex HTML](https://arxiv.org/html/2609.15726). The project page instead quotes 25.5% for pi0.5 under full shift — [project](https://bench2dex.github.io/)
- Bench2Dex task names are mostly household loading, sorting and pouring (e.g. "Tool Box Loading", "Fridge Wine Interhand Pour"), with a few finer ones ("Jigsaw Puzzle Assembly", "Bimanual Piano Melody", "Screwdriver Box & Hammer") — [Bench2Dex HTML](https://arxiv.org/html/2609.15726)
- DexHoldem (arXiv 2605.18727, v3 dated 2026-10-01) is a real-world benchmark on a ShadowHand + UR arm playing Texas Hold'em: 14 primitives over thin cards (about 0.3 mm) and chips, 1,470 teleoperated demonstrations, 80 trials per policy. Task completion / scene-preserving success: pi0.5 61.2% / 47.5%, pi0 57.5% / 47.5%, RDT 46.2% / 30.0%, DP (DINO) 36.2% / 26.2%, smaller models 1.2–20.0%; only 12.1% of 33 closed-loop hands were completed — [DexHoldem](https://arxiv.org/html/2605.18727)
- DexToolBench (Cornell / Stanford, in the SimToolReal paper, arXiv 2602.16863) is a real benchmark with digital twins: KUKA iiwa 14 + 22-DoF Sharpa hand, 24 tasks over 6 tool categories (hammer, marker, eraser, brush, spatula, screwdriver) and 12 object instances; metric is task progress (percentage of goal poses tracked); 120 real rollouts. Baselines are retargeting, fixed grasp and specialist RL; no VLA — [SimToolReal](https://arxiv.org/html/2602.16863)
- DexCraft (CMU, in "From Grasps to Dexterity", arXiv 2606.30749) is a ManiSkill3 benchmark of six articulated tool-use tasks (spray bottle, lighter, dispenser, pliers, stapler, pen) for xArm6 + LEAP Hand; success needs both the tool goal pose and the joint triggered. DP3 reaches 19.1%, the proposed method 64.6%; no VLA baseline — [From Grasps to Dexterity](https://arxiv.org/html/2606.30749)
- VTDexManip (ICLR 2025) is an IsaacGym visual-tactile dexterous benchmark with six tasks (bottle cap turning, faucet screwing, lever sliding, table reorientation, in-hand reorientation, bimanual hand-over) evaluated with RL over 18 pretrained and non-pretrained encoders — [VTDexManip code](https://github.com/LQTS/VTDexManip)
- RoboPianist (CoRL 2023) uses two 24-DoF Shadow hands in MuJoCo on 150 pieces and scores precision, recall and F1 of key presses; the RL baseline reaches F1 0.79 on the Etude-12 subset — [RoboPianist](https://arxiv.org/abs/2304.04150); [project](https://kzakka.com/robopianist/)
- DexArt (CVPR 2023) benchmarks a multi-finger hand on articulated objects with RL and point-cloud inputs — [DexArt](https://arxiv.org/abs/2305.05706)
- RLWRLD announced a "DexBench initiative" with NVIDIA on 2026-06-09: five evaluation domains (grasp diversity, spatial precision, temporal precision, contact precision, context awareness), 18 key atomic tasks, integration with Isaac Lab-Arena; described as in development — [press release](https://www.manilatimes.net/2026/06/09/tmt-newswire/pr-newswire/rlwrld-launches-dexbench-initiative-to-define-next-generation-industry-standards-for-humanoid-ai-in-collaboration-with-nvidia/2361831); site [dexbench.org](http://dexbench.org/)
- A September 2026 review of multifingered-hand dexterity benchmarks describes DexBench (2026) as using six complexity axes with 56 evaluation cases in 18 categories, and lists POMDAR, GM-100, ManipulationNet and DexVerse alongside it — [review](https://arxiv.org/html/2609.05585)
- "Towards High-DoF Dexterous Manipulation through VLA Post-Training" (arXiv 2026-09-17) evaluates on five custom real tasks (bimanual transfer, in-hand reorientation, tool use) and introduces no named benchmark — [paper](https://arxiv.org/abs/2609.19666)

### Inferences
- On dexterous hands, large VLAs do not clearly beat small policies in simulation (GR00T N1.5 leads Bench2Dex, but pi0.5 trails ACT in matched scenes), while on the real ShadowHand in DexHoldem the two pi models lead by a wide margin over ACT and small Diffusion Policy variants. The two results are from different setups and cannot be combined into one ranking.
- No benchmark found tests in-hand reorientation specifically with VLA baselines; VTDexManip has the task but only RL baselines.

### Gaps
- RLWRLD DexBench: no paper, task list with success criteria or results were found; not added to the JSON.
- "RC DexBench / XEbench" (github.com/RoboticsCenter/dexbench; keypress, piano-sequence and pick-place tasks; v0.1.0 alpha) was opened but has no paper or published results and its maintainer could not be assessed; not added — [repo](https://github.com/RoboticsCenter/dexbench)
- DexArt's task list was not confirmed (project page timed out), so it is cited here but not added to the JSON.
- Dexora (ICRA 2026 per its GitHub title; "66.7% vs 51.7% for GR00T N1, 26.7% for pi0" on dexterous tasks) is known only from search snippets; it is a VLA and dataset, not a benchmark.

## Tactile / force-aware benchmarks for VLAs

### Takeaway
Four uncatalogued tactile or force benchmarks relate to VLAs: ForceBench (how to feed wrist force to pi0.5; project page only), Tabero (LIBERO with simulated GelSight and grip-force metrics), NeoSim (12 tactile tasks with six VLA baselines) and UniVTAC (8 tactile tasks; VLA numbers from a later paper). ManiFeel is a tactile policy benchmark without VLA baselines.

### Cited Findings
- ForceBench (PKU-PI Lab; project page updated September 2026; paper and code links not yet active) has eight simulation tasks in three groups — physical-property inference (Weight Sort, CoM Sort), resistance-dependent interaction (two faucet tasks, two stove tasks, Drawer Pull) and contact-rich assembly (Nut Thread) — with 1,600 demonstrations, 16,000 simulation episodes and 800 real trials on a Franka Research 3 with a KWR75B F/T sensor — [ForceBench](https://forcebench-platform.github.io/)
- ForceBench results: pi0.5 without force 23.25% simulation average, best force variant (prompt fusion) 35.31%; real (5 separately trained tasks incl. Plug Insert and Block Insert) 40% versus 63%. The page states "Force observations alone do not guarantee improvement" — [ForceBench](https://forcebench-platform.github.io/)
- Tabero (arXiv 2026-05-27) replays LIBERO tasks in Isaac Lab with Taxim / FOTS GelSight simulation and adds metrics beyond success: average and maximum grip force and applied force. Its pi0-based Tabero-VTLA gets 86% success at 32.4 N average grip force with "firm" instructions and 52% at 3.7 N with "gentle" instructions; simulation only — [Tabero](https://arxiv.org/abs/2605.27886); [code](https://github.com/NathanWu7/Tabero)
- NeoSim (NeoteAI / Fudan, in N0-VTLA, arXiv 2026-07-25) is built in the UniVTAC framework with 12 tasks (single-arm: Pour Ball, Unplug/Plug Charger, Plug USB, Grasp Chip; dual-arm: Insert Screw, Place Gears, stacking, unstacking, handover) and 100 demonstrations per task. Mean success: N0-VTLA 50.8%, pi0.5 45.8%, Xiaomi-Robotics-0 23.4%, StarVLA-alpha 23.2%, GigaWorld-Policy 10.8%, InternVLA-A1 8.6% — [N0-VTLA](https://arxiv.org/html/2607.23782)
- The companion real suite NeoReal (9 tasks in the paper, 10 on the data-report page) gives pi0.5 29.4% versus N0-VTLA 47.2% (paper), or pi0.5 26.5% vision-only versus 32.5% with tactile conditioning (data report) — [N0-VTLA](https://arxiv.org/html/2607.23782); [N0-Foundation report page](https://research.neoteai.com/n0-foundation/)
- UniVTAC (SJTU ScaleLab and partners, arXiv 2026-02-10) is a TacEx / Isaac Sim platform with simulated GelSight Mini, ViTai GF225 and Xense WS sensors and eight tasks (Lift Bottle, Lift Can, Put Bottle in Shelf, Grasp Classify, Insert Hole, Insert HDMI, Insert Tube, Pull Out Key); paper baselines: ACT 30.9%, VITaL 40.5%, ACT + UniVTAC encoder 48.0%; real tests 43.3% → 68.3% — [UniVTAC](https://arxiv.org/html/2602.10093v1); [project](https://univtac.github.io/)
- On the UniVTAC benchmark, the N0-VTLA paper reports 83.1% mean for N0-VTLA and 67.1% for InternVLA-A1 — [N0-VTLA](https://arxiv.org/html/2607.23782)
- ManiFeel (Purdue, arXiv 2025-05; project page lists a Best Paper Award at the Sense of Space workshop, CVPR 2026) is an IsaacGym + TacSL benchmark with insertion (peg, USB, power plug, gear), screwing (nut–bolt, bulb) and exploration tasks, 99 simulation and 44 real setups, and Diffusion Policy, Equivariant Diffusion Policy and Flow Matching baselines; tactile force fields add 26 points on peg insertion — [ManiFeel](https://arxiv.org/html/2505.18472v2); [project](https://zhengtongxu.github.io/manifeel-website/)
- TaF-VLA (arXiv 2026-01-28) releases TaF-Dataset with over 10 million synchronized tactile observations with 6-axis force/torque; the abstract mentions contact-rich tasks but the 8-task suite reported in a search snippet was not confirmed on the page opened — [TaF-VLA](https://arxiv.org/abs/2601.20321)
- RoboTacDex (arXiv 2026-06-30) is a Unitree G1 dexterous-hand visual-tactile dataset (6k trajectories, 19 tasks) evaluated with three imitation models; dataset "will be open-sourced soon" — [RoboTacDex](https://arxiv.org/abs/2606.31836)

### Inferences
- Force and tactile benchmarks for VLAs so far measure the benefit of adding the modality to one backbone (pi0 or pi0.5); only NeoSim compares several independent VLAs, and it comes from the vendor of one of them.
- Tabero and ForceBench are the only two found that score force behaviour (grip force; force-dependent task outcomes) instead of position alone.

### Gaps
- ForceBench has no paper yet; the simulator name is not stated on the project page and all numbers should be treated as preliminary.
- Whether NeoSim's task assets are public was not confirmed.
- ForceVLA (arXiv 2505.22159; five tasks, 244 trajectories, ForceVLA-Data) and its successor dataset are known only from search snippets and are method-paper task sets, not benchmarks.

## Metrics of precision: which benchmarks go beyond binary success

### Takeaway
Among the new entries, nine report something other than a single success bit: staged success (WireCraft, MetaFine, ALOHA sim), per-connection accuracy (WorkBenchMark), goal-pose tracking progress (DexToolBench), force quality (QBIT, Tabero), key-press F1 (RoboPianist) and scene-preserving success (DexHoldem). None reports millimetre placement error for VLAs.

### Cited Findings
- WireCraft separates Reach Success (plug within the socket neighbourhood) from Insert Success (tip seated) — [WireCraft](https://arxiv.org/html/2606.18097)
- MetaFine (Southeast University and partners, arXiv 2026-05-19) rebuilds RoboTwin, CALVIN and LIBERO tasks into a skill graph of 10 atomic skills (including Align and Insert), with position and angle tolerances, stage-wise success, area under the success curve across perturbation levels and a trajectory-smoothness score; the authors report "up to 70% capability inflation" from binary metrics — [MetaFine](https://arxiv.org/html/2605.19986); [project](https://metafine.github.io/)
- MetaFine evaluates ACT, DP3, Octo, OpenVLA, OpenVLA-OFT, pi0 and pi0.5 with 100 demonstrations per task; on the peg-in-hole Align stage Octo gets 4% and OpenVLA-OFT 19%; replacing pi0.5's visual encoder with a multi-scale one raises Align from 0% to 32%. It also combines 20–25 paired real rollouts with simulation through prediction-powered inference (variance 11.5% → 2.6% for pi0.5) — [MetaFine](https://arxiv.org/html/2605.19986)
- WorkBenchMark's execution accuracy is the fraction of brick connections that match the target relative pose; fine-tuned pi0.5 scores 74.5 / 57.2 / 22.3 / 10.2% over tiers 1–4 — [WorkBenchMark](https://arxiv.org/html/2606.19358)
- QBIT defines force energy (axial and lateral), force smoothness and maximum contact force alongside success and completion time — [QBIT](https://arxiv.org/html/2503.07479)
- Tabero reports maximum transient grip force (mean of the top 5% of values), average grip force and maximum / average applied force — [Tabero](https://arxiv.org/html/2605.27886)
- DexHoldem reports Scene-Preserving Success Rate next to Task Completion Rate, penalizing completions that disturb the rest of the table — [DexHoldem](https://arxiv.org/html/2605.18727)
- DexToolBench scores "Task Progress, measuring the percentage of demonstrated goal poses tracked successfully" — [SimToolReal](https://arxiv.org/html/2602.16863)
- RoboPianist scores precision, recall and F1 of key presses — [project](https://kzakka.com/robopianist/)
- For comparison, the already-catalogued Intrinsic AI for Industry Challenge scores task success, precision (connector pose relative to target), safety (collision, force, cable jerk) and cycle time — [Datameister blog](https://datameister.ai/blog/intrinsic-ai-for-industry-challenge-qualifying-first/)

### Inferences
- Success-versus-clearance curves for VLAs exist only as single points today (3 mm in WireCraft; 3 mm and 0.1 mm rows in ReTac-ACT without a pi0.5 number at 0.1 mm). The Curse of Precision study shows how such a curve can be built (4–10 mm) but only for Diffusion Policy.
- MetaFine numbers in the JSON were read through an automated summary of the HTML; they should be checked against the tables before publication.

### Gaps
- No benchmark was found that reports end-effector or object placement error in millimetres for VLA policies.

## Benchmarks introduced inside method papers

### Takeaway
Five of the new entries come from method or model papers whose titles do not contain "benchmark": NeoSim (N0-VTLA), DexToolBench (SimToolReal), DexCraft (From Grasps to Dexterity), the FACT five-task suite, and the ALOHA sim tasks (ACT). Several other precise-manipulation VLA papers were checked and do not release a benchmark.

### Cited Findings
- FACT ("Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them", Stanford IPRL, arXiv 2026-08-02) uses five real tasks (plug, USB and key insertion; button push; board erasing) on a Franka Research 3 with a Bota SensONE F/T sensor, about 2,500 rollouts, and states that a bill of materials and 3D-printable STL files will be released with the code. FACT reaches 66% average versus 40.5% for ForceVLA; pi0.5 and TA-VLA are also compared — [FACT](https://arxiv.org/html/2608.01402v1); [project](https://stanford-iprl-lab.github.io/fact/)
- The same paper attributes precision failures to "a flow-matching policy training mismatch" and force failures to "the distinctive structure of force signals" — [FACT abstract](https://arxiv.org/abs/2608.01402)
- ReactVLA (arXiv 2606.14255) introduces RoboIMI, a MuJoCo dual-arm environment with Peg-in-Socket and Object Transfer tasks scored by episodic reward over 100 rollouts; SmolVLA failed to converge; no public release is documented — [ReactVLA](https://arxiv.org/html/2606.14255)
- "From Reach to Insert" (IROS 2026) tests five hole geometries at three clearances and reports 67% at 0.05 mm, but is an IL+RL method without VLA baselines or a released benchmark — [paper](https://arxiv.org/abs/2605.04649)
- Checked and found to be outside the precision scope despite the name: IndustrialVLA-Bench (arXiv 2026-09-22) evaluates six VLAs only on LIBERO, LIBERO-Plus and LIBERO-Para plus deployability measures — [IndustrialVLA-Bench](https://arxiv.org/html/2609.25562v1)
- Adjacent benchmarks not in `already_listed.txt` that were opened but left out of the JSON because they do not primarily test precise action by learned policies: DLO-Lab (Genesis-based differentiable DLO benchmark, 10 tasks incl. Wiring-post and Wiring-ring, SmolVLA fine-tuning in an appendix) — [DLO-Lab](https://arxiv.org/html/2606.04206); EmbodiedSWE (28 long-horizon dexterous tasks in Isaac Lab incl. nut threading and PC motherboard installation, evaluated mainly with coding agents; SmolVLA 18% → 69% with 10 → 400 generated demos) — [EmbodiedSWE](https://arxiv.org/html/2609.27308v1)
- MimicGen (CoRL 2023; 18 tasks, 50K+ generated demonstrations, including multi-part assembly) was opened only at abstract level; no verified VLA results on its Threading / Three Piece Assembly tasks were found — [MimicGen](https://arxiv.org/abs/2310.17596)

### Inferences
- The two adjacent benchmarks (DLO-Lab, EmbodiedSWE) and IndustrialVLA-Bench are candidates for other catalogue categories (deformable; agentic / long-horizon; robustness) rather than for the precision list.

### Gaps
- Physical Intelligence's "Precise Manipulation with Efficient Online RL" page (pi.website/research/rlt) returned HTTP 429 and was not read.
- VLA-Precision (arXiv 2609.04355), TORL-VLA, CompliantVLA-adaptor, PaCo-VLA and DreamTacVLA appeared in search results as contact-rich VLA method papers; they were not opened, so whether any releases a task suite is unknown.

## VLA results on already-catalogued precision benchmarks

### Takeaway
Published VLA numbers were found for 13 of the catalogued precision benchmarks; they are low wherever tolerance is tight (pi0.5 20% at 3 mm on NIST ATB M1; 0–12% on RoboDojo's Precision dimension; near zero on ManiSkill peg and plug insertion). For RAMP, IndustReal, FMB, Robothon, POMDAR, TactiDex, Peg-in-Bench, ManipulationNet and the Industrial Dexterity Benchmark no VLA result was found.

### Cited Findings
- NIST Assembly Task Board (ATB M1 peg insertion, real, bimanual Realman RM75-6F-V with Xense tactile sensors, 20 trials): at 3 mm clearance ReTac-ACT 90%, ACT 40%, Diffusion Policy 20%, pi0.5 20%; at 0.1 mm ReTac-ACT 80%, ACT 15%, DP 0% (no pi0.5 number given at 0.1 mm) — [ReTac-ACT](https://arxiv.org/html/2603.09565v2)
- NIST-board operations also appear inside the PRISM dataset; its pi0 baseline reaches 25% on connector plug/unplug — [PRISM](https://arxiv.org/html/2608.17962)
- Assemble Bench (HUD, 2026-07-31; 14 tasks modelled on NIST ATB-1 in Isaac Lab Arena): only pi0.5 (DROID-fine-tuned checkpoint) was evaluated systematically; frontier DROID checkpoints started at "0% across all tasks" because of camera-viewport differences; after adaptation pi0.5 did well on round pegs and nuts and "almost none" on square pegs and small / medium gears — [Assemble Bench](https://www.hud.ai/research/assemble-benchmark)
- FurnitureBench (simulation, One-Leg task, 500 demonstrations, 50 trials), per-step success for steps 1–5: OpenVLA 96 / 94 / 78 / 53 / 29%; CogACT 98 / 96 / 96 / 56 / 42%; DAM-VLA 100 / 100 / 100 / 62 / 56% (step 4 is the screwing step, step 5 full success) — [DAM-VLA](https://arxiv.org/html/2603.00926v1)
- ManipulationNet: the paper's baselines are task-specific methods and are labelled preliminary; no VLA model is named. The peg-in-hole board has clearances of 3, 1, 0.1 and 0.02 mm — [ManipulationNet](https://arxiv.org/html/2603.04363v1). InsertAnything (RL, not a VLA) reports the first 20/20 on it under the human-in-the-loop protocol — [InsertAnything](https://arxiv.org/html/2609.24511v1)
- GM-100 (real, Dobot Xtrainer, tasks 1–10 average): partial success rate DP 7.0%, pi0 32.1%, pi0.5 53.9%; full success rate DP 1.6%, pi0 4.4%, pi0.5 24.9%; GR00T is also listed as a baseline — [GM-100](https://arxiv.org/html/2601.11421)
- RoboDojo simulation, Precision dimension (8 tasks), success rate: X-VLA 12.00%, Spatial Forcing 10.58%, Hy-Embodied-0.5-VLA 8.00%, pi0.5 5.50%, pi0 0.75%, GR00T N1.7 0.67%; human teleoperation 64.00% — [RoboDojo](https://arxiv.org/html/2607.04434)
- RoCo Challenge (planetary gearbox assembly): organizer baselines were pi0.5 and ACT; 1st place IIGroup used ARC-VLA (3.6B parameters, pi0.5 backbone) with simulation 0.126, real 0.344, final 0.279; 2nd place RoboCola combined OpenPi and GalaxeaVLA with 0.038 / 0.139 / 0.109 — [RoCo Challenge](https://arxiv.org/html/2603.15469)
- Intrinsic AI for Industry Challenge: a participant's pi0.5 policy trained on about 100 episodes made no successful insertion in the qualifier and was replaced by ACT (about 127 points, position 55, below the cutoff) — [Open Robotics Discourse](https://discourse.openrobotics.org/t/my-first-results-pi0-5-vla-policy/53670). The qualifier winner (Datameister, 293.38 points, about 160 teams) used a sequence of step-specific policies, not a single VLA — [Datameister blog](https://datameister.ai/blog/intrinsic-ai-for-industry-challenge-qualifying-first/)
- DexVerse (19 baseline tasks): pi0.5 0.34, DP3 0.34, Diffusion Policy 0.32, OpenVLA 0.19 mean success — [DexVerse](https://arxiv.org/html/2607.08751v1)
- DexJoCo (11 tasks, 100 demos each, 1,650 episodes per setting), object randomization: ACT 54.1%, DP-T 50.4%, DP-C 47.6%, pi0.5 40.2%; full randomization: ACT 40.3%, pi0.5 30.5%, DP-C 28.4%, DP-T 20.0% — [DexJoCo](https://arxiv.org/html/2605.16257). The extraction returned the same 40.2% for GR00T N1.5, which looks like a copy error; a search snippet of the same paper says pi0.5 has the highest overall success — treat the DexJoCo ranking as unresolved.
- AutoBio (pi0 / RDT-1B): close thermal-cycler lid 99.7 / 100%; pick up centrifuge tube 53.7 / 57.7%; unscrew cap 21.3 / 2.7%; aspirate with pipette 42.7 / 0.3%; screw on cap 2.0 / 8.3%; operate thermal-mixer panel 7.5 / 1.6%; load centrifuge rotor 14.7 / 1.0% — [AutoBio](https://arxiv.org/html/2505.14030)
- Labimus: pi0 is the only VLA, on two Tier-1 tasks: Door Open 47.3 ± 7.4%, Door Close 40.7 ± 3.8% — [Labimus](https://arxiv.org/html/2606.31037)
- Pipette (11 tasks, 30 demos per task): ACT 65.5% average; simulation augmentation raises SmolVLA from 44.1% to 74.7% and pi0 from 40.4% to 46.5% — search snippet of [Pipette](https://arxiv.org/abs/2606.12936) only; the page timed out when opened.
- ManiSkill (catalogued as ManiSkill2 / ManiSkill3), RDT-1B repository table, 250 trials per method: PegInsertionSide RDT 13.2%, OpenVLA 0.0%, Octo 0.0%, Diffusion Policy 0.0%; PlugCharger RDT 1.2%, others 0.0%; five-task mean RDT 53.6%, OpenVLA 4.8%, Octo 0.0%, DP 30.2% — [RDT repository](https://github.com/thu-ml/RoboticsDiffusionTransformer)
- UniVTAC / ManiSkill-ViTac-style tactile insertion: see N0-VTLA numbers above.
- Benchmarks checked with no VLA baseline in their own paper: Industrial Dexterity Benchmark (diffusion-based AG-iDP3 only; best configuration 76% total on datacenter cable cleaning) — [IDB](https://arxiv.org/html/2607.14021); TactiDex (TactiSkill versus a kinematic baseline) — [TactiDex](https://arxiv.org/html/2607.09190); Peg-in-Bench (no learned-policy results; clearances 0.1, 1 and 3 mm) — [Peg-in-Bench](https://arxiv.org/html/2609.00906)

### Inferences
- On benchmarks with graded difficulty, VLA success falls at the contact step: FurnitureBench step 3 → 4 (screwing) drops from 78–100% to 53–62%; AutoBio screwing and panel tasks are in single digits; RoboDojo Precision is the dimension where the best policy reaches 12%.
- pi0.5 is the most frequent VLA baseline across these precision benchmarks (NIST ATB M1, Assemble Bench, GM-100, RoboDojo, RoCo, DexVerse, DexJoCo, AI for Industry), which makes it the practical reference point for a precision comparison table.

### Gaps
- No VLA results found for: RAMP, IndustReal, FMB, REASSEMBLE, Robothon / euROBIN task board, POMDAR, RGMC, ManiSkill-ViTac. Searches for each returned only the benchmark papers; a possible REASSEMBLE-based VLA fine-tuning study (arXiv 2605.30695) timed out and is unverified.
- DexMimicGen and RoboCasa GR-1 Tabletop: the catalogue already holds GR00T N1 numbers; search snippets mention ABot-M0 58.3% and TwinBrainVLA 54.6% on GR-1 Tabletop but these were not opened.
- AI for Industry Challenge Phase 1 / Phase 2 (real hardware) results were not found.
- GM-100, RoboDojo and DexJoCo numbers were read through an automated page reader; verify against the tables before publishing.
