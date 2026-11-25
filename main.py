"""One Line, One Laugh

Entry for make.fun competition u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.
The deliverable is one funny line of text, 1 to 140 characters: a self-contained
joke a stand-up editor reads in a breath. The line lands a real turn - the
punchline is that the agent's vague ETA was the one forecast that came true to
the second.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""
import os
from pathlib import Path

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

EMOJI = "My agent said the task 'took longer than expected' — it was the only thing today that went exactly as long as expected."

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
