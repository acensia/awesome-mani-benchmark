# What each real-world manipulation benchmark targets

For every benchmark in [real-world-manipulation-evaluation-benchmarks.md](real-world-manipulation-evaluation-benchmarks.md), this file records two things:

- **Evaluates**: the capability, skill, or system the benchmark measures.
- **Improves**: the problem in evaluation practice the benchmark was built to fix (cost, reproducibility, access, scoring, and so on).

Both columns are summarized from the research notes in `research_notes/real-world-manipulation-evaluation-benchmarks/`, which recorded each work's abstract, project page, and design. The papers were not re-opened for this file, so read the "Improves" column as a summary of the stated aim or design, not as a quotation. Verification caveats for individual entries (preprint status, unconfirmed venues) are in the main report.

Methodology papers (STEP, STAR-Gen, the TRI best-practice protocol, and similar) are not benchmarks and are left in the main report.

## 1. Physical benchmarks a lab reproduces on its own robot

### Classic object sets and protocols (2015–2026)

| Benchmark | Evaluates | Improves | Link |
|---|---|---|---|
| YCB Object and Model Set | Grasping, pick-and-place, in-hand, bimanual and assembly on 77 everyday objects that vary in shape, size, texture, weight and rigidity | Gives labs a shared physical object set plus a protocol template, so results from different robots can be compared | [arXiv 1502.03143](https://arxiv.org/abs/1502.03143) |
| ACRV Picking Benchmark (APB) | Complete shelf-picking systems (perception plus manipulation) | Reproducible scene setup: 42 objects, a widely available shelf, and stencils that fix object arrangement | [arXiv 1609.05258](https://arxiv.org/abs/1609.05258) |
| RA-L 2020 Special Issue protocols (14) | One protocol each for gripper strength and repeatability, grasp resilience, grasp planning, bin picking, Rubik's cube, small-parts assembly, bimanual cloth, semi-deformable objects, in-hand manipulation, aerial manipulation, and handover | The absence of any widely adopted manipulation benchmark; every paper had to use standard objects, a common protocol template, and baseline results | [Introduction PDF](https://cpb-us-w2.wpmucdn.com/wp.wpi.edu/dist/f/375/files/2022/03/Introduction-to-the-Special-Issue-on-Benchmarking-Protocols-for-Robotic-Manipulation.pdf) |
| GRASPA 1.0 / GRASPA-fying the Panda | Grasp planning pipelines on a robot arm | The lack of a common protocol and metrics for grasping; scores are normalized to each platform's workspace and payload so different robots can be compared | [arXiv 2002.05017](https://arxiv.org/abs/2002.05017) |
| NIST Assembly Task Boards (ATB 1–4) | Small-parts assembly systems: peg insertion, gear meshing, connectors, nut threading, belts, cable routing, wire harnesses | Standard fabricable boards with CAD, scoring and analysis guidelines, so industrial assembly results are measured the same way everywhere | [NIST](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/assembly) |
| Box and Blocks Test benchmark | Speed of pick-and-place in clutter (blocks moved per unit time) | Borrows a clinical dexterity test, giving a robot-agnostic score that is compared against human norms | [project](https://robotpilab.github.io/publication/benchmarking-cluttered-robot-pick-and-place-manipulation-with-the-box-and-blocks-test/) |
| Benchmarking In-Hand Manipulation | Planning and control for changing the pose of a held object using fingers, the environment, or both | Common task definitions (initial and goal poses on YCB meshes) and a shared pose-error metric | [arXiv 2001.03070](https://arxiv.org/abs/2001.03070) |
| Benchmarking Bimanual Cloth Manipulation | Tablecloth spreading, towel folding and dressing, at several difficulty levels with quality measures | Runs on any bimanual platform with standardized, easy-to-buy cloth objects | [Semantic Scholar](https://www.semanticscholar.org/paper/Benchmarking-Bimanual-Cloth-Manipulation-Garcia-Camacho-Aleny%C3%A0/5291ca085e97ff10839d6da7e8099958b30929f7) |
| Household Cloth Object Set (HCOS) | Deformable-object manipulation: folding, piling, table setting, bed making | A cloth object set that can be distributed among research groups, the cloth counterpart of a rigid object set | [arXiv 2111.01527](https://arxiv.org/abs/2111.01527) |
| ICRA 2024 Cloth Competition dataset | Grasp selection for unfolding garments | Turns a one-off competition into a reusable dataset and offline benchmark (679 attempts, 34 garments) | [arXiv 2508.16749](https://arxiv.org/abs/2508.16749) |
| Cluttered Environment Picking Benchmark (CEPB) | Perception, planning, control and grasping in sequential bin picking | Separate protocols per pipeline stage for warehouse-style picking, on a fixed 40-object set | [site](http://cepbbenchmark.eu/) |
| EGAD! | Grasping systems across a controlled range of shape complexity and grasp difficulty | 49 3D-printable objects, so anyone can reproduce the test set without sourcing products | [arXiv 2003.01314](https://arxiv.org/abs/2003.01314) |
| SceneReplica | Full grasping pipelines (perception, planning, execution) on pick-and-place in clutter, with failures attributed to each stage | Replicable scenes without markers: operators rebuild each scene by overlaying a reference image on the live camera | [arXiv 2306.15620](https://arxiv.org/abs/2306.15620) |
| Robothon / euROBIN task board (DR.J) | Speed and completion of electronic task-board subtasks (e-waste disassembly, device testing) | The board scores itself with onboard electronics and reports to a web dashboard, building a shared performance database | [GitHub](https://github.com/peterso/robotlearningblock) |
| AHAP | Grasping ability of anthropomorphic hands across 10 grip patterns | A hand-level protocol with 25 household objects | [CORE](https://core.ac.uk/outputs/270088295/) |
| Benchmarking Multi-Object Grasping | Grasping several objects at once from piles and surfaces | Three protocols for a capability that single-object grasp benchmarks do not cover | [arXiv 2503.20820](https://arxiv.org/abs/2503.20820) |
| GRAB | Grasping in clutter for food-waste sorting, across three gripper types and four clutter levels | Graspability metrics that describe pre-grasp conditions, on a domain existing benchmarks skip | [arXiv 2602.18835](https://arxiv.org/abs/2602.18835) |

### Learning-era benchmarks with a fixed robot cell (2019–2025)

| Benchmark | Evaluates | Improves | Link |
|---|---|---|---|
| REPLAB | Learned grasping (plus an RL reaching baseline) | Cost and reproducibility: a self-contained arm, camera and workspace for about $2,000 that assembles in hours | [arXiv 1905.07447](https://arxiv.org/abs/1905.07447) |
| ROBEL | Reinforcement learning for dexterous manipulation (D'Claw) and locomotion (D'Kitty) on real hardware, including hardware-safety metrics | Low-cost open-source robots so results can be replicated across institutions | [arXiv 1909.11639](https://arxiv.org/abs/1909.11639) |
| TriFinger | Dexterous manipulation by control and learning methods | An inexpensive open platform that can run autonomously and safely for long periods | [arXiv 2008.03596](https://arxiv.org/abs/2008.03596) |
| DeepClaw | Tic-Tac-Toe, bin clearing and jigsaw tasks across three hardware configurations | A reconfigurable cell and shared task hierarchy that accept arms, grippers and cameras from different vendors | [arXiv 2005.02588](https://arxiv.org/abs/2005.02588) |
| RB2 | Learning algorithms on pouring, scooping, zipping and insertion | Cross-lab variance: the same experiment differed by 20% between labs, so local results are pooled into one global ranking instead of comparing absolute numbers | [arXiv 2203.08098](https://arxiv.org/abs/2203.08098) |
| FurnitureBench | Long-horizon, complex furniture assembly (grasping, inserting, screwing) | A reproducible real-world setup: 3D-printed furniture, a setup guide and systematic initialization, checked by 10 independent reproductions | [arXiv 2305.12821](https://arxiv.org/abs/2305.12821) |
| FMB | Multi-stage, contact-rich functional manipulation (grasping, repositioning, insertion, assembly), including held-out objects | 3D-printable objects with stated tolerances, a large dataset, and per-skill trial protocols | [arXiv 2401.08553](https://arxiv.org/abs/2401.08553) |
| RAMP | Assembly that needs both manipulation and planning (beams joined with pegs into goal structures) | Parts that are 3D-printed or easy to obtain, with CAD and a digital twin | [arXiv 2305.09644](https://arxiv.org/abs/2305.09644) |
| IndustReal | Sim-to-real transfer of RL policies for contact-rich assembly | Releases the hardware and software tools needed to reproduce the system | [arXiv 2305.17110](https://arxiv.org/abs/2305.17110) |
| REASSEMBLE | Contact-rich assembly and disassembly (pick, insert, remove, place) learned from multimodal data | A dataset built on NIST Task Board 1, so it inherits that board's physical standard | [arXiv 2502.05086](https://arxiv.org/abs/2502.05086) |
| HomeRobot OVMM | Open-vocabulary mobile manipulation: pick any object in an unseen home and place it where commanded | A paired sim and real benchmark on one low-cost mobile manipulator (Hello Robot Stretch) | [arXiv 2306.11565](https://arxiv.org/abs/2306.11565) |
| THE COLOSSEUM | Robustness of policies to perturbations in color, texture, size, lighting, distractors, physical properties and camera pose | Systematic generalization testing, with printable objects to replicate the perturbations on a real robot | [arXiv 2402.08191](https://arxiv.org/abs/2402.08191) |
| λ (LAMBDA) | Language-conditioned, long-horizon, multi-room mobile pick-and-place, with a focus on data efficiency | A sim and real benchmark for a setting where tabletop benchmarks do not apply | [arXiv 2412.05313](https://arxiv.org/abs/2412.05313) |

### VLA-era benchmarks (2025–2026)

| Benchmark | Evaluates | Improves | Link |
|---|---|---|---|
| VLA-REPLICA | VLA and imitation policies on 10 tabletop tasks, in-distribution and out-of-distribution scenes | Cost and cross-setup reproducibility: a roughly $1,050 cell with fixed lighting, calibrated cameras and overlay resets, offered as an alternative to remote evaluation | [arXiv 2605.20774](https://arxiv.org/abs/2605.20774) |
| Benchmarking VLA Models on SO-101 | How VLA policies fail and whether they recover, on four tasks | Goes beyond success rate with a failure taxonomy and recovery-aware metrics; defines a common SO-101 action space | [arXiv 2606.08881](https://arxiv.org/abs/2606.08881) |
| GM-100 | Breadth of skill: 100 detail-oriented tasks on two bimanual platforms | Task coverage; the authors frame it as a first step toward a "robot learning Olympics" | [arXiv 2601.11421](https://arxiv.org/html/2601.11421v1) |
| ATOM-Bench | Atomic skills and whether they compose: 30 atomic tasks and 24 held-out compositional tasks | Diagnoses where compositional failures come from (Compositional Failure Share), with mask-guided placement and fixed test seeds | [arXiv 2606.16826](https://arxiv.org/abs/2606.16826) |
| LongBench | Long-horizon tasks, split into those that need memory of earlier context and those that do not | Stage-wise scoring that separates the mechanisms behind long-horizon failure | [arXiv 2604.16788](https://arxiv.org/abs/2604.16788) |
| UMI-Bench 1.0 | Policies trained on UMI-style handheld-gripper data, using wrist cameras only | One local protocol covering data collection, scene reset, execution, logging and task-factor analysis | [arXiv 2606.10382](https://arxiv.org/abs/2606.10382) |
| Experiences from Benchmarking VLA Models | VLA policies on a mobile bimanual robot under spatial and object shifts | Adds time-to-success and instruction-adherence metrics next to success rate | [arXiv 2511.11298](https://arxiv.org/html/2511.11298v1) |
| DuoBench | Bimanual coordination in four categories: asymmetric support, joint manipulation, sequential handoff, parallel execution | Stage-based scoring and real-world task recipes with printable assets | [arXiv 2606.11901](https://arxiv.org/abs/2606.11901) |
| BusyBox | Affordance generalization: whether a policy can still operate switches, sliders, buttons and dials when the modules are rearranged | An instrumented, 3D-printed box that reports its own state, giving automatic success detection | [arXiv 2602.05441](https://arxiv.org/abs/2602.05441) |
| POMDAR | Dexterity of anthropomorphic robot hands across 18 manipulation and grasping tasks, scored against a human baseline | A fully 3D-printed test apparatus for comparing hand designs | [arXiv 2604.09294](https://arxiv.org/html/2604.09294v1) |
| TactiDex | Tactile-guided dexterous manipulation | A dataset aligning whole-hand tactile signals with motion and object state, plus standard metrics | [arXiv 2607.09190](https://arxiv.org/abs/2607.09190) |
| Peg-in-Bench | High-precision insertion across peg shapes and clearances (0.1, 1 and 3 mm) | A modular, printable insertion kit with specified tolerances | [arXiv 2609.00906](https://arxiv.org/html/2609.00906) |
| Industrial Dexterity Benchmark | Industrial tasks: datacenter cable plugging, cable-harness routing, planetary gearbox assembly | Three open boards with CAD, bill of materials and scoring | [arXiv 2607.14021](https://arxiv.org/abs/2607.14021) |

## 2. Hosted and remote platforms, where someone else runs the robot

| Platform | Evaluates | Improves | Link |
|---|---|---|---|
| RoboArena | Generalist policies on open-ended tasks and scenes chosen by evaluators, on the DROID setup | Scalability of centralized evaluation: a network of labs runs double-blind pairwise comparisons and a ranking model aggregates them; model weights stay private | [arXiv 2506.18123](https://arxiv.org/abs/2506.18123) |
| AutoEval | Generalist policies on a few Bridge tabletop tasks | Human labor: learned success detection and learned resets let a cell run around the clock with almost no supervision | [arXiv 2503.24278](https://arxiv.org/abs/2503.24278) |
| RoboChallenge Table30 / V2 | VLA policies on 30 tabletop tasks across four robot types, per-task and generalist tracks; V2 adds multi-task, zero-shot and out-of-domain tests | Online access to a real robot fleet at scale without handing over model weights | [arXiv 2510.17950](https://arxiv.org/abs/2510.17950) |
| ManipulationNet | Physical skills (peg-in-hole, cable management, grasping in clutter) and embodied reasoning (language-conditioned tabletop tasks, block arrangement) on any robot | Realism, accessibility and authenticity together: standard kits are mailed out, tasks run locally, and a server verifies results | [arXiv 2603.04363](https://arxiv.org/abs/2603.04363) |
| RoboDojo-RealEval | Generalist policies on long-horizon, precision, memory and generalization tasks across three bimanual robots | A unified sim and real suite with remote evaluation and double-blind scoring by three evaluators | [arXiv 2607.04434](https://arxiv.org/abs/2607.04434) |
| ManipArena | Tabletop execution, tabletop semantic reasoning and mobile manipulation, each with in-domain, shifted and held-out trials | Controlled conditions: a green-screen facility with fixed lighting, cameras and workspace | [arXiv 2603.28545](https://arxiv.org/abs/2603.28545) |
| FolDeX / FoldChallenge | Garment folding across more than 10 robot types | A score that combines success, fold quality and efficiency, with held-out garments and double-blind submission | [arXiv 2609.10243](https://arxiv.org/html/2609.10243v1) |
| ArmnetBench v0.1 | Imitation and VLA policies on 12 single-arm and bimanual tasks | Cost per evaluation: low-cost arm cells where one operator supervises several at once | [arXiv 2607.24481](https://arxiv.org/abs/2607.24481) |
| PhAIL | Speed and throughput of VLA policies on order picking, relative to a human operator | Statistical reporting: time-to-success distributions, confidence intervals, blind scheduling and public run audit | [arXiv 2605.29710](https://arxiv.org/abs/2605.29710) |
| Humanoid Everyday cloud evaluation | Manipulation policies on humanoid robots across task categories | Access to humanoid hardware: described as the first cloud evaluation platform for humanoids | [arXiv 2510.08807](https://arxiv.org/abs/2510.08807) |
| Real Robot Challenge | Dexterous manipulation on TriFinger robots; the 2022 edition tested offline RL on pushing and lifting | Access: participants submit code that runs on a remote robot cluster | [arXiv 2109.10957](https://arxiv.org/abs/2109.10957) |
| OCRTOC | Table organization (grasping and rearranging objects into a target layout) | Fair comparison on identical robot setups reached through the cloud | [arXiv 2104.11446](https://arxiv.org/abs/2104.11446) |
| CloudGripper | Planar pushing and rope manipulation on 32 small remote cells | A shared testbed for large-scale benchmarking and data collection | [arXiv 2309.12786](https://arxiv.org/abs/2309.12786) |
| HALTER | Long-horizon manipulation (evaluation tooling, not a benchmark) | Automatic scene reset for long tasks, which earlier automated cells handled poorly | [arXiv 2609.19413](https://arxiv.org/abs/2609.19413) |
| UniBot World Challenge | One model across multiple tabletop tasks (grasping, placing, bimanual coordination) | A hosted leaderboard on real hardware; not yet open | [site](https://unibot.unitree.com/) |
| UMI Arena | Policies trained on handheld-device data, on eight tasks across three robot arms | Queue-based remote evaluation with held-out tasks | [site](https://umi-arena.airoa.io/) |
| AIRoA Mobile Manipulation Challenge | VLA pipelines for mobile manipulation on Toyota HSR | Shared hardware with regular real-robot evaluation rounds | [site](https://icra2026vlapipeline.github.io/) |

### Competitions with a real-robot stage

| Competition | What it targets | Link |
|---|---|---|
| RGMC | Picking from clutter, in-hand manipulation, human-robot handover, mobile manipulation, assembly on task boards, and a remote cloud-robotics track | [site](https://sites.google.com/view/rgmcomp) |
| WBCD | Bimanual systems (teleoperation plus learning from demonstration) on logistics picking, packing, lab work and pallet loading | [site](https://wbcdcompetition.github.io/) |
| Robothon Grand Challenge | Speed on a self-scoring electronic task board that teams receive by mail | [GitHub](https://github.com/peterso/robothon-grand-challenge) |
| euROBIN Manipulation Skill Versatility Challenge | Versatility, speed and transfer of skills on the same task board | [site](https://sites.google.com/view/eurobin-msvc/) |
| ICRA 2024 Cloth Competition | Unfolding garments on a shared robot | [arXiv 2508.16749](https://arxiv.org/abs/2508.16749) |
| World Robot Summit Manufacturing Robotics Challenge | Industrial assembly (2018) and mixed-goods box packing (2025) | [site](https://worldrobotsummit.org/en/wrs2025/mrc/) |
| RoboCup@Home / RoboCup ARM Challenge | Domestic service tasks; ARM tests autonomous manipulation on a real UR5e | [@Home](https://athome.robocup.org/) · [ARM](https://arm.robocup.org/) |
| Amazon Picking / Robotics Challenge | Warehouse picking from shelves and bins (discontinued in 2017) | [arXiv 1601.05484](https://arxiv.org/abs/1601.05484) |
| HomeRobot OVMM Challenge | Open-vocabulary mobile manipulation in a real apartment | [site](https://aihabitat.org/challenge/2023_homerobot_ovmm/) |
| RoboTwin Dual-Arm Collaboration Challenge | Bimanual collaboration, with a real round after two simulation rounds | [arXiv 2506.23351](https://arxiv.org/abs/2506.23351) |
| ManiSkill-ViTac | Vision-tactile manipulation, with top simulation entries checked on a real tactile platform | [arXiv 2411.12503](https://arxiv.org/abs/2411.12503) |
| AgiBot World Challenge | Manipulation on AgiBot robots (shirt folding, conveyor picking, food preparation); 2026 adds supermarket mobile manipulation | [Robot Report](https://www.therobotreport.com/agibot-holds-world-challenge-2026-see-how-ai-models-perform-real-tasks/) |
| REAL-I | Dual-arm humanoid manipulation on logistics-style tasks, with no extra training data allowed | [arXiv 2609.13679](https://arxiv.org/html/2609.13679v1) |
| RoCo Challenge | Dual-arm assembly (gearbox, industrial board, bricks) | [arXiv 2603.15469](https://arxiv.org/abs/2603.15469) |
| LeHome Challenge | Garment manipulation on low-cost SO-ARM101 arms | [site](https://lehome-challenge.com/) |
| RoboSynChallenge | Generalization of policies trained on synthetic data, tested in the real world | [arXiv 2608.12416](https://arxiv.org/abs/2608.12416) |
| ATEC Real-World Extreme Challenge | Fully autonomous operation outdoors, with remote control banned | [BusinessWire](https://secure.businesswire.com/news/home/20251207877880/en/) |
| PhyRC Challenge | Physical caregiving (dressing, bed bathing) on manikins | [site](https://emprise.cs.cornell.edu/rcareworld/challenge/) |
| EBiM | Mobile bimanual manipulation: cable routing, thermal pad placement, assisted feeding | [site](https://ebim-benchmark.github.io/) |
| GigaBrain Challenge 2026 (RoboChallenge track) | Generalist models on a preview of Table30 V2 | [site](https://gigaai-research.github.io/GigaBrain-Challenge-2026/) |
| Intrinsic AI for Industry Challenge | Cable insertion in an industrial workcell, scored on success, precision, safety and cycle time | [site](https://www.intrinsic.ai/events/ai-for-industry-challenge) |
| Robotic Origami Challenge | Paper folding with bimanual arms and dexterous hands in a remote lab | [site](https://robotic-origami-challenge.github.io/) |

## 3. Proxies that predict real-world results without running the robot

Every entry here shares one goal: estimate how real-data-trained policies would rank or score on a real robot, at lower cost. The "Improves" column says which part of that problem each work addresses.

### Simulator digital twins

| Work | Evaluates | Improves | Link |
|---|---|---|---|
| SIMPLER | Generalist policies (RT-1, RT-1-X, RT-2-X, Octo) for the Google Robot and WidowX setups | Established the method: close the control gap with system identification and the visual gap with matched backgrounds and textures; introduced the MMRV ranking metric | [arXiv 2405.05941](https://arxiv.org/abs/2405.05941) |
| ManiSkill3 digital twins | The same SIMPLER environments | Speed: GPU-parallel versions run about 10 times faster | [arXiv 2410.00425](https://arxiv.org/pdf/2410.00425) |
| DROID sim-evals | Policies trained on the real DROID dataset, zero-shot | Simulation scenes that need no separate simulation training data | [GitHub](https://github.com/arhanjain/sim-evals) |
| REALM | Generalization of VLA policies across 15 visual, semantic and behavioral perturbations on the DROID setup | A generalization benchmark whose simulator is validated against paired real rollouts | [arXiv 2512.19562](https://arxiv.org/html/2512.19562) |
| RobotArena ∞ | VLA policies across scenes from several real datasets, with perturbations | Scale: environments are generated automatically from a single image, and scoring uses a VLM plus crowdsourced preferences | [arXiv 2510.23571](https://arxiv.org/html/2510.23571) |
| RoboLab-120 | Generalist policies on 120 pick-and-place tasks graded by difficulty and by visual, procedural and relational demands | Fine-grained analysis of where generalist policies fail | [arXiv 2604.09860](https://arxiv.org/html/2604.09860v3) |
| X2Real | 44 long-horizon tasks across 10 capability dimensions and four robots, in-distribution and out-of-distribution | Hardware-aligned calibration between each simulated and real robot | [arXiv 2609.27449](https://arxiv.org/html/2609.27449v1) |
| VISER | Manipulation policies under physically based, ray-traced rendering | The visual gap: shows how highlights and shadows change measured success | [arXiv 2605.06311](https://arxiv.org/html/2605.06311) |
| MolmoSpaces | Pick, open and close skills across 230,000 procedurally built environments | Scale and diversity of evaluation environments | [arXiv 2602.11337](https://arxiv.org/abs/2602.11337) |
| Genie Sim 3.0 | Policies for AgiBot G1 and G2 robots | Scanned real scenes inside a physics simulator | [arXiv 2601.02078](https://arxiv.org/html/2601.02078v2) |
| Colosseum V2 | Robustness to 19 perturbations for single-arm and bimanual policies | A faster GPU simulator for perturbation testing, checked against real trials | [arXiv 2605.27759](https://arxiv.org/html/2605.27759) |
| H2RBench | Methods that transfer skills from human video to robots | A benchmark for human-to-robot transfer that predicts real results | [arXiv 2609.24778](https://arxiv.org/abs/2609.24778v1) |
| R2S-Eval | VLA policies on a dual-arm humanoid with dexterous hands | A calibrated twin scored by a VLM that produces pairwise preferences | [arXiv 2609.03276](https://arxiv.org/html/2609.03276) |
| A Practical Recipe (sim-and-real correlation) | Existing simulators (VLA-Arena, SIMPLER, REALM) compared on the same real tasks | How to raise agreement with real results, such as a small amount of simulation adaptation | [arXiv 2606.10366](https://arxiv.org/html/2606.10366) |
| SureSim | Any policy with a few real and many simulated rollouts | Statistics: combines both sources into valid confidence intervals with less robot time | [arXiv 2510.04354](https://arxiv.org/abs/2510.04354) |

### Reconstruction-based pipelines

| Work | Evaluates | Improves | Link |
|---|---|---|---|
| PolaRiS | Generalist DROID policies in newly captured environments | Cost of building scenes (a short phone video is enough) and support for wrist cameras | [arXiv 2512.16881](https://arxiv.org/html/2512.16881) |
| Real-to-Sim Policy Evaluation with Gaussian Splatting (soft-body) | Policies on deformable objects: rope routing, plush-toy packing, plus T-block pushing | Deformables, which rigid-body simulators and world models handle poorly | [arXiv 2511.04665](https://arxiv.org/abs/2511.04665) |
| SimFoundry | Generalist policies on single-arm and bimanual setups | Builds a simulation-ready twin from one video and works without adapting the policy | [arXiv 2606.28276](https://arxiv.org/html/2606.28276v3) |
| ReVeal | VLA policies on a humanoid | Shows how reconstruction quality drives agreement with real results | [arXiv 2609.23910](https://arxiv.org/html/2609.23910) |
| GSWorld | Imitation policies on several arms | Photo-realistic closed-loop simulation for reproducible benchmarking | [arXiv 2510.20813](https://arxiv.org/abs/2510.20813) |
| Real-is-Sim | Policy checkpoints on a pushing task | A continuously corrected twin, so checkpoints can be evaluated offline in minutes | [arXiv 2504.03597](https://arxiv.org/html/2504.03597v1) |

### Video world models

| Work | Evaluates | Improves | Link |
|---|---|---|---|
| WorldEval | Imitation and VLA policies on a bimanual robot | Conditions the video model on the policy's own latent actions; also ranks checkpoints and flags unsafe behavior | [arXiv 2505.19017](https://arxiv.org/html/2505.19017) |
| WorldGym | Generalist policies on Bridge and Google Robot tasks | A world model used as the environment, with VLM scoring and out-of-distribution probes made by image editing | [arXiv 2506.00613](https://arxiv.org/html/2506.00613) |
| Ctrl-World | Generalist DROID policies | Multi-view prediction with memory for longer rollouts; also generates data to improve policies | [arXiv 2510.10125](https://arxiv.org/html/2510.10125) |
| Evaluating Gemini Robotics Policies in a Veo World Simulator | Gemini Robotics policies on a bimanual robot, in normal and out-of-distribution scenes | Edited scenes for generalization testing and safety red teaming | [arXiv 2512.10675](https://arxiv.org/html/2512.10675v1) |
| 1X World Model | Policy checkpoints for the NEO humanoid | Checkpoint selection and architecture comparison before real testing | [blog](https://www.1x.tech/discover/redwood-ai-world-model) |
| DreamDojo | A policy on a fruit-packing task (policy evaluation is one application) | A general world model pretrained on large-scale human video | [arXiv 2602.06949](https://arxiv.org/html/2602.06949v1) |
| PlayWorld | 18 policies on the DROID setup | Trains on autonomous play that includes failures, reducing falsely predicted successes | [arXiv 2603.09030](https://arxiv.org/html/2603.09030) |
| Interactive World Simulator | Imitation and VLA policies on bimanual tasks | Stable rollouts of 10 minutes or more for both training and evaluation | [arXiv 2603.08546](https://arxiv.org/abs/2603.08546) |
| dWorldEval | Policies on a bimanual robot and two simulators | A progress token that detects success automatically, plus memory for consistency | [arXiv 2604.22152](https://arxiv.org/html/2604.22152v1) |
| PiL-World | VLA checkpoints on dual-arm tasks | Alternates policy inference and generation to cut hallucination and the gap to real success rates | [arXiv 2606.05773](https://arxiv.org/html/2606.05773) |
| SC3-Eval | Checkpoints of one policy on table bussing | Self-consistency checks that detect drift and reproduce real failure types | [arXiv 2606.18610](https://arxiv.org/abs/2606.18610) |
| RoboWorld | Open policies from the RoboArena leaderboard | Speed: fast enough to replicate the whole leaderboard in about 100 GPU-hours | [arXiv 2607.01060](https://arxiv.org/html/2607.01060v4) |
| Genie Envisioner (GE-Sim) / GE-Sim 2.0 | Policies on AgiBot dual-arm robots | Closed-loop video simulation with a learned success classifier | [arXiv 2605.27491](https://arxiv.org/html/2605.27491) |
| EnerVerse-AC | Policies on AgiBot robots | One world model that serves as both evaluator and data generator | [OpenReview](https://openreview.net/pdf?id=zIiV66Dimq) |
| Scalable Policy Evaluation with Video World Models | Generalist policies on Bridge and RoboMimic tasks | Policy evaluation with a large pretrained video model, with documented failure cases | [arXiv 2511.11520](https://arxiv.org/abs/2511.11520) |
| GigaWorld-1 / WMBench | Seven world models as evaluators, against 2,989 paired real trajectories | Which model designs and which metrics make a world model a reliable evaluator | [arXiv 2607.02642](https://arxiv.org/html/2607.02642v1) |
| IRASim | Policies in LIBERO (the reference is a simulator, not a real robot) | Fine-grained trajectory-conditioned video prediction | [paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_IRASim_A_Fine-Grained_World_Model_for_Robot_Manipulation_ICCV_2025_paper.pdf) |
| Cosmos-Surg-dVRK | Surgical policies on the dVRK robot | Extends world-model evaluation to surgical robotics, using a video classifier to judge outcomes | [arXiv 2510.16240](https://arxiv.org/abs/2510.16240) |
