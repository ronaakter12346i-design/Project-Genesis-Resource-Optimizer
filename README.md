# Project Genesis: Autonomous AI-Driven System Resource Optimizer

An intelligent, autonomous system resource optimization framework built with Python, eBPF, and adaptive feedback loops to dynamically manage CPU and memory performance while maintaining strict safety constraints.

---

## 🚀 Key Features
- **Autonomous Decision Engine:** Continuously monitors CPU and memory usage to decide between caching optimization and process throttling[cite: 3].
- **eBPF Kernel Probing:** Utilizes low-level kernel probes (`kprobe/sys_execve`) for real-time system metrics tracing[cite: 1].
- **Safety Shield Architecture:** Built-in safeguards (`safety_shield.py`) to prevent system instability (e.g., blocking unsafe resource limits)[cite: 6].
- **Experience Logging & Reinforcement Learning:** Tracks past outcomes in `experience_log.json` to adapt and improve future execution efficiency[cite: 2, 3, 4, 7].

---

## 🛠️ Tech Stack & Components
- **Language:** Python, C (`eBPF`)[cite: 1, 3]
- **Core Files:**
  - `genesis_core.py`: Main master decision-making script[cite: 3].
  - `ebpf_probe.c`: Low-level system telemetry probe[cite: 1].
  - `safety_shield.py`: Constraint verification and action gating[cite: 6].
  - `memory_buffer.py` & `trainer.py`: Experience logging and feedback analysis[cite: 4, 7].
  - `reporter.py`: Efficiency and performance metric generator[cite: 5].

---

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Project-Genesis-Resource-Optimizer.git](https://github.com/YOUR_USERNAME/Project-Genesis-Resource-Optimizer.git)
   cd Project-Genesis-Resource-Optimizer
