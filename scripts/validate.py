"""Run stable, offline checks for the Awesome Math repository."""

from collections import Counter
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))

import build_toc  # noqa: E402


ENTRY_PATTERN = re.compile(
    r"^\s*\* \[[^\]]+\]\(https://[^)]+\) - .+\.$"
)
HEADING_PATTERN = re.compile(r"^#{2,} .+$", re.MULTILINE)
URL_PATTERN = re.compile(r"https?://[^)\s]+")
START_TOC = "<!-- START_TOC -->"
END_TOC = "<!-- END_TOC -->"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_toc(readme):
    require(readme.count(START_TOC) == 1,
            "README must contain one start-of-TOC marker")
    require(readme.count(END_TOC) == 1,
            "README must contain one end-of-TOC marker")
    with tempfile.TemporaryDirectory() as directory:
        copy = Path(directory) / "README.md"
        copy.write_text(readme, encoding="utf-8")
        build_toc.gen_toc(copy)
        require(copy.read_text(encoding="utf-8") == readme,
                "README table of contents is out of date")


def check_entries(readme):
    body = readme.split(END_TOC, maxsplit=1)[1]
    entries = [line for line in body.splitlines()
               if re.match(r"^\s*\* \[", line)]
    invalid = [line for line in entries if not ENTRY_PATTERN.fullmatch(line)]
    require(not invalid,
            "Invalid resource entry format:\n" + "\n".join(invalid))
    return len(entries)


def check_urls(readme):
    urls = URL_PATTERN.findall(readme)
    require(all(url.startswith("https://") for url in urls),
            "README contains a plain HTTP URL")
    duplicates = sorted(url for url, count in Counter(urls).items()
                        if count > 1)
    require(not duplicates,
            "Duplicate README URLs:\n" + "\n".join(duplicates))
    return len(urls)


def check_headings(readme):
    headings = HEADING_PATTERN.findall(readme)
    duplicates = sorted(heading for heading, count
                        in Counter(headings).items() if count > 1)
    require(not duplicates,
            "Duplicate README headings:\n" + "\n".join(duplicates))
    anchors = [build_toc._anchor(heading.split(" ", maxsplit=1)[1])
               for heading in headings]
    duplicate_anchors = sorted(anchor for anchor, count
                               in Counter(anchors).items() if count > 1)
    require(not duplicate_anchors,
            "Duplicate README anchors:\n" + "\n".join(duplicate_anchors))


def main():
    readme = README.read_text(encoding="utf-8")
    require(readme.endswith("\n"), "README must end with a newline")
    check_toc(readme)
    entry_count = check_entries(readme)
    url_count = check_urls(readme)
    check_headings(readme)
    print(f"Validated {entry_count} resource entries and {url_count} URLs.")


if __name__ == "__main__":
    main()
