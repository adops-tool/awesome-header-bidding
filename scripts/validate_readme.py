#!/usr/bin/env python3
"""Validate README.md formatting and link hygiene for awesome-header-bidding.

Usage (from anywhere in the repository):

    python3 scripts/validate_readme.py [path/to/README.md]

Checks performed:

1.  Every entry line matches the documented shape:
    `![icon](image/file.png) [Name](https://url) - Description.`
2.  Only the known icons are used, each with its own file, and the icon matches
    the link target: `github` for github.com links, `web` for everything else.
3.  No URL appears twice in the document.
4.  Every `##` category has a Table of Contents entry, and every Table of
    Contents entry resolves to a real heading.
5.  Every `##` category is followed by a one-line italic description.
6.  Relative links (icons, LICENSE, CODE_OF_CONDUCT.md) point at files that
    exist, and every absolute link is https with no tracking parameters.
7.  Descriptions start capitalized, end with a period, stay short, and contain
    no promotional wording.
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "README.md")

ICONS = {"github": "image/alg_R.png", "web": "image/alg_I.png"}
GITHUB_HOSTS = {"github.com", "www.github.com"}
MIN_ENTRIES = 50
MAX_DESC = 320

BANNED = re.compile(
    r"\b(best|world'?s.?best|leading|revolutionary|revolutioni[sz]e|ultimate|"
    r"#1|unmatched|incomparable|amazing|awesome|cutting[- ]edge|next[- ]gen|"
    r"next[- ]generation|innovative|seamless|effortless|guaranteed revenue|"
    r"free money|cheapest|top[- ]rated)\b",
    re.I,
)
TRACKING_PARAMS = re.compile(
    r"([?&])(ref|ref_src|utm_[a-z]+|aff|affiliate|gclid|fbclid|msclkid|mc_eid|referral)", re.I
)

ENTRY_RE = re.compile(
    r"^!\[(?P<icon>[a-z]+)\]\((?P<iconpath>[^)]+)\)\s+\[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)"
    r"\s+-\s+(?P<desc>.+?)\.?$"
)
HEADING_RE = re.compile(r"^(?P<hashes>#{2,3})\s+(?P<title>.+?)\s*$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)\s]+)")
TOC_RE = re.compile(r"^\s*-\s+\[[^\]]+\]\(#(?P<anchor>[^)]+)\)")
META_HEADINGS = {"table of contents", "contributing", "license"}


def anchor(title: str) -> str:
    """GitHub-style anchor: lowercase, punctuation dropped, spaces to hyphens."""
    slug = re.sub(r"[^\w\s-]", "", title.strip().lower())
    return re.sub(r"\s+", "-", slug.strip())


def main() -> int:
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")

    problems: list[str] = []
    urls: list[str] = []
    entries = 0
    icon_mismatches = 0
    headings: dict[str, str] = {}
    levels: dict[str, int] = {}
    toc_anchors: set[str] = set()

    in_code = False
    for num, line in enumerate(lines, start=1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        heading = HEADING_RE.match(line)
        if heading:
            title = heading.group("title")
            key = anchor(title)
            if key in headings:
                problems.append(f"line {num}: duplicate heading anchor '{key}'")
            headings[key] = title
            levels[key] = len(heading.group("hashes"))
            continue

        toc = TOC_RE.match(line)
        if toc:
            toc_anchors.add(toc.group("anchor"))
            continue

        for target in LINK_RE.findall(line):
            if target.startswith(("http://", "https://")):
                parsed = urlparse(target)
                if parsed.scheme != "https":
                    problems.append(f"line {num}: link must be https: {target}")
                if TRACKING_PARAMS.search(parsed.query):
                    problems.append(f"line {num}: URL carries a tracking or referral parameter: {target}")
            elif target.startswith("#"):
                if target[1:] not in headings:
                    problems.append(f"line {num}: in-page link #{target[1:]} has no matching heading")
            elif not target.startswith("mailto:"):
                local = os.path.join(ROOT, target.split("#")[0])
                if not os.path.exists(local):
                    problems.append(f"line {num}: local path does not exist: {target}")

        if not line.startswith("!["):
            continue

        entry = ENTRY_RE.match(line.rstrip())
        if not entry:
            problems.append(f"line {num}: entry does not match the required format")
            continue

        entries += 1
        icon = entry.group("icon")
        iconpath = entry.group("iconpath")
        url = entry.group("url")
        desc = entry.group("desc")
        name = entry.group("name")
        urls.append(url)

        if icon not in ICONS:
            problems.append(f"line {num}: unknown icon type '{icon}' (use {' or '.join(ICONS)})")
            continue
        if iconpath != ICONS[icon]:
            problems.append(f"line {num}: '{icon}' entries must use {ICONS[icon]}, found {iconpath}")

        host = urlparse(url).netloc.lower()
        if (icon == "github") != (host in GITHUB_HOSTS):
            icon_mismatches += 1
            problems.append(f"line {num}: '{name}' uses the {icon} icon but links to {host or 'a relative path'}")

        first_word = re.match(r"[^\s]+", desc).group(0)
        if first_word.strip("`\"“’.,()") and not any(char.isupper() for char in first_word):
            problems.append(f"line {num}: description must start capitalized: {name}")
        if not line.rstrip().endswith("."):
            problems.append(f"line {num}: description must end with a period: {name}")
        if len(desc) > MAX_DESC:
            problems.append(f"line {num}: description longer than {MAX_DESC} characters: {name}")
        if re.search(r"\s-\s", desc):
            problems.append(f"line {num}: description contains a stray ' - ' separator: {name}")
        if re.search(r"[.!?]\s+[A-Z]", desc):
            problems.append(f"line {num}: description should be one sentence: {name}")
        banned = sorted(set(BANNED.findall(desc)))
        if banned:
            problems.append(f"line {num}: promotional wording in description: {', '.join(banned)}")

    for url, count in Counter(urls).items():
        if count > 1:
            problems.append(f"URL listed {count} times: {url}")

    for toc in sorted(toc_anchors - set(headings)):
        problems.append(f"Table of Contents points at missing heading: #{toc}")
    for key, title in headings.items():
        if levels[key] == 2 and title.lower() not in META_HEADINGS and key not in toc_anchors:
            problems.append(f"category '{title}' is missing from the Table of Contents")

    for i, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        title = line[3:].strip()
        if title.lower() in META_HEADINGS:
            continue
        following = [x for x in lines[i + 1 : i + 4] if x.strip()]
        if not following or not re.fullmatch(r"\*[^*].*[^*]\*", following[0].strip()):
            problems.append(f"category '{title}' needs a one-line italic description after the heading")

    if entries < MIN_ENTRIES:
        problems.append(f"suspiciously few entries found ({entries}, minimum {MIN_ENTRIES}); is the file complete?")

    print(
        f"{os.path.relpath(README, ROOT)}: {entries} entries, {len(headings)} headings, "
        f"{len(toc_anchors)} TOC links, {icon_mismatches} icon mismatches"
    )
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("OK: format, icons, links, and Table of Contents are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
