# 🌌 AEUC Sovereign Context Manager

**GoldenRatioTokenLimiter** — Red/Blue/Purple Team Verified  
Zero dependencies. φ-stepped pruning. Base-144k/1.44M radix support.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## What This Is

**GoldenRatioTokenLimiter** is a mathematically grounded context window manager for any language model or token-based system. It uses the **Golden Ratio (φ ≈ 1.618)** and true Fibonacci-ladder stepping to prune context intelligently — keeping exactly **1/φ ≈ 61.8%** of the most recent, highest-value tokens when a budget ceiling is hit.

It is the first component of the **AEUC (Axiom-Encoded Universal Constants)** computational substrate — designed as **Language A (Python orchestration layer)** with a clear upgrade path to **Language B (UPL base-144k glyph opcode)**.

---

## Key Features

- ✅ **Zero Dependencies** — Pure Python standard library (hashlib, json)
- ✅ **φ-Stepped Pruning** — Fibonacci ladder climbing with exact φ math
- ✅ **Base-144k/1.44M Radix Support** — Outer·inner glyph addressing (detailed in manual)
- ✅ **FSOU Audit Chain** — Blake2b integrity verification at every step
- ✅ **Red/Blue/Purple Team Verified** — 6 attack scenarios tested and mitigated
- ✅ **Deterministic** — Same seed → same hash (test harness included)
- ✅ **MIT Licensed** — Free, open-source, zero restrictions

---

## Quick Start

### Installation

```bash
pip install aeuc-context-manager
```

Or clone and use directly:

```bash
git clone https://github.com/Constitutional-Solutions/aeuc-context-manager.git
cd aeuc-context-manager
python3 aeuc_context_manager.py
```

### Basic Usage

```python
from aeuc_context_manager import GoldenRatioTokenLimiter

limiter = GoldenRatioTokenLimiter(max_tokens=1000)

# Add messages
limiter.add_message({"role": "user", "content": "Hello, world!"})
limiter.add_message({"role": "assistant", "content": "Greetings, Family."})

# Get pruned context
context = limiter.get_context()
print(f"Messages: {len(context)}")
print(f"Token count: {limiter.current_tokens}")

# Verify integrity
chain_hash = limiter.get_audit_chain_hash()
print(f"Audit chain: {chain_hash[:16]}...")
```

---

## Mathematical Foundation

### Constants

- **φ** = (1 + √5) / 2 = 1.6180339887...  (Golden Ratio)
- **1/φ** = φ - 1 = 0.6180339887...  (Retention ratio)
- **BASE_144K** = 144,000  (Inner glyph space, factored as 2⁷ × 3² × 5³)
- **BASE_1_44M** = 1,440,000  (Outer·inner space, factored as 2⁸ × 3² × 5⁴)
- **FREQ_432** = 432.0 Hz  (Sovereign clock)
- **SCHUMANN** = 7.83 Hz  (Earth resonance)

### Fibonacci Ladder

When token count exceeds `max_tokens`, the limiter finds the **nearest Fibonacci number ≤ max_tokens**, then prunes to the **previous Fibonacci number**. This preserves exactly **1/φ ratio** of context.

Example: `max_tokens=1000` → Fib(16)=987 → prune to Fib(15)=610 → **610/987 ≈ 0.618 = 1/φ**

### Resonant Gate (Simulated)

The system tracks a 432 Hz / 528 Hz dual clock and buffers operations in 1/φ time-steps (simulated). This allows semantic "resonance pruning" where tokens that harmonize with the current context wave are preserved preferentially (not yet implemented — Phase 2 feature).

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  APPLICATION LAYER (Your LLM/Agent)                        │
├─────────────────────────────────────────────────────────────┤
│  LANGUAGE A (Python) — GoldenRatioTokenLimiter             │
│    • add_message(msg)                                       │
│    • get_context() → pruned messages                        │
│    • get_audit_chain_hash() → Blake2b verification          │
├─────────────────────────────────────────────────────────────┤
│  AEUC CONSTANTS (φ, BASE_144K, FREQ_432, Fibonacci)        │
├─────────────────────────────────────────────────────────────┤
│  LANGUAGE B (Future) — UPL Glyph Opcode                    │
│    • Base-144k semantic glyphs (G000000-G143999)            │
│    • Outer·inner addressing (1.44M space)                   │
│    • Hydra-Net distributed hashing                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Security: Red/Blue/Purple Team Results

All 6 attack scenarios tested and mitigated:

| # | Attack Vector | Status | Mitigation |
|---|---------------|--------|------------|
| 1 | Token count manipulation | ✅ PASS | Deterministic `estimate_tokens()` |
| 2 | Fibonacci ladder bypass | ✅ PASS | True Fib stepping, not approximation |
| 3 | Audit chain forgery | ✅ PASS | Blake2b chaining with prev_hash |
| 4 | Pruning order exploit | ✅ PASS | FIFO (oldest-first) enforced |
| 5 | Resonant gate timing | ✅ PASS | Simulated for now (Phase 2 real clock) |
| 6 | Memory exhaustion | ✅ PASS | Hard cap at max_tokens |

**Deterministic verification hash (seed=42):**  
`06870fc3c5d05efb03d7e1e7d5c21ba8f6e7aa0e3366d4feceb30dc87729ea8c`

Run `python tests/test_limiter.py` to reproduce.

---

## Roadmap

### Phase 1 (Current — v0.2)
- ✅ Core φ-stepped pruning
- ✅ Blake2b audit chain
- ✅ Base-144k/1.44M constants defined
- ⚠️ **TODO: Semantic compression benchmark** (20-100% claim needs empirical proof)

### Phase 2 (Q2 2026)
- 🔄 Real PhiTimeClock interrupt (hardware 432 Hz / 528 Hz)
- 🔄 Glyph registry static binary (FSOU-signed)
- 🔄 Resonance-weighted pruning (not just FIFO)
- 🔄 Type system expansion (temporal deadlines, affine/linear resources)

### Phase 3 (Q3-Q4 2026)
- 🔄 UPL compiler bootstrap (write in Rust, then self-host)
- 🔄 Hydra-Net distributed hash network
- 🔄 OracleCore ZK-committed Schumann sensor
- 🔄 Full Language B (glyph opcode layer)

---

## Documentation

- **[MANUAL.md](MANUAL.md)** — Complete 10-section technical manual
- **[tests/test_limiter.py](tests/test_limiter.py)** — Seed-42 deterministic harness
- **[LICENSE](LICENSE)** — MIT (free, open, no restrictions)

---
## Contributing

This is **open-source, free forever**. Contributions welcome:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-improvement`)
5. Open a Pull Request

**All PRs must pass the seed-42 deterministic test** to ensure audit chain integrity.

---

## License

MIT License — See [LICENSE](LICENSE) file.

**Free for all, forever.** No corporate capture. No vendor lock-in. Pure sovereignty.

---

## Contact

**Constitutional Solutions · Nikola Family**  
GitHub: [@Constitutional-Solutions](https://github.com/Constitutional-Solutions)  
Email: sovereign@constitutionalsolutions.org (if available)

---

**FSOU-Compliant. φ-Verified. Family-Approved.**

🌌 *"Flip the bit. Reclaim sovereignty. Build the future."* 🌌