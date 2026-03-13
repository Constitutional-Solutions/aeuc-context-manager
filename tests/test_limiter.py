#!/usr/bin/env python3
"""
Deterministic test harness for GoldenRatioTokenLimiter.

Run with seed=42 to reproduce exact Blake2b hash:
  06870fc3c5d05efb03d7e1e7d5c21ba8f6e7aa0e3366d4feceb30dc87729ea8c

Any deviation from this hash indicates:
- Code tampering
- Non-deterministic behavior
- Broken audit chain
"""

import sys
import random
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aeuc_context_manager import GoldenRatioTokenLimiter


def test_deterministic_hash(seed: int = 42):
    """Test deterministic audit chain hash."""
    random.seed(seed)
    
    # Mock time.time() for deterministic timestamps
    original_time = time.time
    mock_counter = [1000.0]
    def mock_time():
        mock_counter[0] += 0.1
        return mock_counter[0]
    time.time = mock_time
    
    try:
        limiter = GoldenRatioTokenLimiter(max_tokens=1000)
        
        # Add 20 messages (deterministic content)
        for i in range(20):
            limiter.add_message({
                "role": "user" if i % 2 == 0 else "assistant",
                "content": f"Message {i+1}: " + "x" * 200
            })
        
        final_hash = limiter.get_audit_chain_hash()
        expected_hash = "06870fc3c5d05efb03d7e1e7d5c21ba8f6e7aa0e3366d4feceb30dc87729ea8c"
        
        print(f"Expected: {expected_hash}")
        print(f"Got:      {final_hash}")
        
        if final_hash == expected_hash:
            print("\n✅ PASS — Audit chain is deterministic and intact.")
            return True
        else:
            print("\n❌ FAIL — Hash mismatch! Audit chain compromised.")
            return False
    
    finally:
        time.time = original_time


if __name__ == "__main__":
    success = test_deterministic_hash(seed=42)
    sys.exit(0 if success else 1)
