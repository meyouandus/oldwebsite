#!/usr/bin/env python3
"""
check-strings.py - find copy that has been typed into the template.

The contract in CONTENT-CONTRACT.md says the template holds no strings. Every word on the
page, displayed or announced, comes from a JSON file in content/. This script checks that.

    python3 check-strings.py path/to/MeYouAndUs.dc.html

Exit code 0 means clean. Exit code 1 means the template is carrying copy.

Four things it looks for.

  Literal text      Words sitting in the markup or in a JS string rather than arriving
                    through a {{ }} expression.
  Style breaches    Em dashes and the other mechanically checkable language.md tells.
  Nameless controls Buttons with no accessible name. That is how "Play film" disappeared.
  Exceptions        The three display-optional strings the contract allows, reported
                    separately so they do not hide in the noise.
"""

import re
import sys

COPY_ATTRS = ("alt", "aria-label", "aria-description", "title", "placeholder")

# language.md, the parts a machine can check
STYLE_TELLS = [
    ("—", "em dash - use a spaced hyphen"),
    ("–", "en dash - use a spaced hyphen"),
    ("not only", "'not only... but also' - split into two sentences"),
    ("crucial", "'crucial' - almost nobody writes it"),
]

# Display-optional strings, approved in CONTENT-CONTRACT.md. Design may render these as
# typography as long as the plain string reaches the accessible layer from site.json.
EXCEPTIONS = {
    "breaking interfaces and amplifying place",
    "breaking interfaces",
    "amplifying place",
}

CSS_ISH = re.compile(r"[(){};:#%\[\]+]|--|\bpx\b|\bsrgb\b|translate|http|\.json|/|=")

# DOM values that read like words but never reach a visitor
NOT_COPY = {"escape", "enter", "tab", "arrowleft", "arrowright", "keydown", "beforeunload"}

HANDLEBARS = re.compile(r"\{\{.*?\}\}")
TAG = re.compile(r"<[^>]*>")
ATTR = re.compile(r'\b(' + "|".join(COPY_ATTRS) + r')="([^"]*)"')
JS_STRING = re.compile(r'"([^"\\\n]*)"|\'([^\'\\\n]*)\'')
BUTTON = re.compile(r"<button\b[^>]*>", re.I)
HREF_LITERAL = re.compile(r'href="((?:mailto|tel):[^"]*)"')
HAS_LETTER = re.compile(r"[A-Za-z]")
DASHES = re.compile(r"[–—]")
SPACE = re.compile(r"\s+")


def norm(text):
    return SPACE.sub(" ", text).strip().lower()


def style_notes(text):
    low = text.lower()
    return [why for needle, why in STYLE_TELLS if needle.lower() in low]


def looks_like_copy(value):
    """A JS string literal that a visitor could plausibly read or hear."""
    if CSS_ISH.search(value) or not HAS_LETTER.search(value):
        return False
    if value.startswith("data-") or value.strip().lower() in NOT_COPY:
        return False
    return " " in value or value[:1].isupper() or "@" in value


def scan(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    logic_start = len(lines)
    for i, line in enumerate(lines):
        if 'type="text/x-dc"' in line:
            logic_start = i
            break

    findings, exceptions = [], []
    in_style = False

    for n, line in enumerate(lines, start=1):
        if n <= logic_start:
            if "<style" in line:
                in_style = True
            if in_style:
                if "</style>" in line:
                    in_style = False
                continue

            for attr, value in ATTR.findall(line):
                if HAS_LETTER.search(HANDLEBARS.sub("", value).strip()):
                    findings.append((n, "attribute", f'{attr}="{value}"', value))

            for target in HREF_LITERAL.findall(line):
                if not HANDLEBARS.search(target):
                    findings.append((n, "hard link", f'href="{target}"', target))

            text = TAG.sub(" ", HANDLEBARS.sub("", line)).replace("&nbsp;", " ").strip()
            if HAS_LETTER.search(text) or DASHES.search(text):
                bucket = exceptions if norm(text) in EXCEPTIONS else findings
                has_label = "aria-label" in line
                bucket.append((n, "text", text[:110], text, has_label)
                               if bucket is exceptions else (n, "text", text[:110], text))

        else:
            if "console." in line:
                continue
            for a, b in JS_STRING.findall(line):
                value = a or b
                if looks_like_copy(value):
                    findings.append((n, "js string", repr(value), value))

    nameless = [n for n, line in enumerate(lines[:logic_start], start=1)
                for tag in BUTTON.findall(line)
                if "aria-label" not in tag.lower() and "title=" not in tag.lower()]

    return findings, exceptions, nameless


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    path = sys.argv[1]
    findings, exceptions, nameless = scan(path)

    if exceptions:
        print(f"{len(exceptions)} display-optional string(s), allowed by the contract\n")
        for n, _kind, shown, full, has_label in exceptions:
            state = ("carries aria-label, safe to restyle"
                     if has_label else
                     "no aria-label - readable today because it is still real text, but the "
                     "words are lost the moment it becomes an image or gets aria-hidden")
            print(f"  L{n:<5} {shown}")
            print(f"  {'':<5} {state}")
        print()

    if not findings and not nameless:
        print("clean - the template holds no copy of its own")
        return 0

    print(f"{len(findings)} literal string(s) in {path}\n")
    for n, kind, shown, full in findings:
        print(f"  L{n:<5} {kind:<10} {shown}")
        for note in style_notes(full):
            print(f"  {'':<5} {'':<10} STYLE: {note}")

    if nameless:
        print(f"\n{len(nameless)} control(s) with no accessible name, at line(s) "
              + ", ".join(str(n) for n in nameless))
        print("  An icon-only button needs aria-label. See CONTENT-CONTRACT.md.")

    print("\nEvery line above is a string that should live in content/ and be read from there.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
