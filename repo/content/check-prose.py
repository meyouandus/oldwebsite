#!/usr/bin/env python3
"""
check-prose.py - hunt the tells listed in language.md.

    python3 check-prose.py FILE [FILE ...]

Exit code 0 means nothing found. Exit code 1 means there are tells to look at.

Covers the rules a machine can see. Rules 3, 5, 7 and the terminology lock still need a human
reading, because they turn on meaning rather than shape. Skips fenced code blocks, inline code
and markdown tables, so quoted examples of bad writing do not fail their own document.
"""

import re
import sys

RULES = [
    ("em dash", r"—", "Rule: punctuation. Use a spaced hyphen or rewrite."),
    ("'This' opener", r"(?m)^\s{0,3}(?:[-*]\s+|\d+\.\s+)?This\s+(?:means|is|gives|makes|lets|allows|creates|matters|gets|gave|gets|gives)\b",
     "Rule 10. 'This means the build is simpler' becomes 'The build gets simpler.'"),
    ("colon then list", r"(?m):\s*$(?=\n\s*(?:[-*]\s|\d+\.\s))", "Punctuation. Write it as prose or use a heading."),
    ("not only", r"(?i)\bnot only\b", "Rule 11. Split into two sentences."),
    ("crucial", r"(?i)\bcrucial(?:ly)?\b", "Rule 12. Use 'matters' or state the thing."),
    ("critical", r"(?i)\bcritical(?:ly)?\b", "Rule 16. Cut it or replace it with the consequence."),
    ("significant", r"(?i)\bsignificant(?:ly)?\b", "Rule 16. Cut it or give the number."),
    ("count before list", r"(?i)\b(?:two|three|four|five|six|seven|eight|nine|ten)\s+(?:\w+\s+){0,2}(?:things?|ways?|reasons?|points?|problems?|layers?|steps?)\b",
     "Rule 15. Drop the number and write the items."),
    ("intensifier", r"(?i)\b(?:strongly|materially|significantly|substantially|dramatically|vastly)\s+\w+",
     "Rule 17. Cite it, count it, or delete the adverb."),
    ("claim verb", r"(?i)\b(?:constitutes|represents|serves as)\b", "Rule 18. Make the claim instead of announcing it."),
    ("self-congratulation", r"(?i)(?:and that matters|that's the part everyone misses|which is exactly the point|that'?s a real find|nice find|worth the effort)",
     "Rule 4. Delete it. Nothing is lost."),
    ("warm-up opener", r"(?i)(?:here'?s the thing|let me be clear|the truth is|it'?s worth noting|at its core|in today'?s landscape)",
     "Rule 6. Start one sentence later."),
    ("summary ending", r"(?i)(?:^|\n)\s*(?:in short|at the end of the day|to sum up|in summary)\b",
     "Rule 9. Stop typing instead."),
    ("range not number", r"(?i)\b\d+\s*(?:to|-)\s*\d+\s*(?:minutes?|hours?|days?|weeks?|seconds?)\b",
     "Rule 8. Say the number. Defined bands in applications are exempt."),
    ("not X that's Y", r"(?i)(?:isn'?t|is not|aren'?t|are not|wasn'?t)\s+[^.!?\n]{2,40}[.]\s+(?:It'?s|That'?s|They'?re)\s",
     "Rule 1. Write only the second half."),
    ("X, not Y definition", r"(?i),\s+not\s+(?:a\s+|an\s+|the\s+)?\w+(?:\s+\w+){0,3}[.,]",
     "Rule 14. One per section. State the positive claim on its own."),
    ("suspect word", r"(?i)\b(?:delve|leverage|robust|holistic|tapestry|testament|unlock|elevate|harness)\b",
     "Clusters in machine writing. Second look."),
]

FENCE = re.compile(r"(?ms)^```.*?^```")
INLINE = re.compile(r"`[^`\n]*`")
TABLE = re.compile(r"(?m)^\s*\|.*\|\s*$")
QUOTED = re.compile(r'"[^"\n]{0,120}"')


def strip_non_prose(text):
    """Blank out code, tables and quoted examples, keeping line numbers intact."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    for pat in (FENCE, INLINE, TABLE, QUOTED):
        text = pat.sub(blank, text)
    return text


def scan(path):
    raw = open(path, encoding="utf-8").read()
    if "## Forbidden patterns" in raw and "House rules for written output" in raw:
        return []  # the rules file quotes every tell as an example
    prose = strip_non_prose(raw)
    lines = raw.split("\n")
    hits, seen = [], set()
    for name, pattern, advice in RULES:
        for m in re.finditer(pattern, prose):
            n = prose[:m.start()].count("\n") + 1
            if (n, name) in seen:
                continue
            seen.add((n, name))
            hits.append((n, name, lines[n - 1].strip()[:100], advice))
    hits.sort()
    return hits


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    total = 0
    for path in sys.argv[1:]:
        hits = scan(path)
        total += len(hits)
        print(f"\n{path}  {len(hits) or 'clean'}")
        if hits:
            print("-" * (len(path) + 12))
        seen = set()
        for n, name, line, advice in hits:
            print(f"  L{n:<5} {name:<22} {line}")
            if name not in seen:
                print(f"  {'':<5} {'':<22} {advice}")
                seen.add(name)
    if total:
        print(f"\n{total} across {len(sys.argv) - 1} file(s). Rules 3, 5, 7 and the "
              f"terminology lock still need reading by a person.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
