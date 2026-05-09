#!/usr/bin/env python3
"""Parse Rekordbox CUE file and generate Mixcloud tracklist template."""

import re
import sys
from pathlib import Path


def parse_cue(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    global_title = ''
    global_performer = ''
    for line in content.splitlines():
        if not line.startswith('\t') and not line.startswith(' '):
            m = re.match(r'TITLE\s+"(.+)"', line)
            if m:
                global_title = m.group(1)
            m = re.match(r'PERFORMER\s+"(.+)"', line)
            if m:
                global_performer = m.group(1)

    track_blocks = re.split(r'\n\s+TRACK\s+\d+\s+AUDIO\s*\n', content)
    tracks = []
    for block in track_blocks[1:]:
        title = ''
        performer = ''
        index_time = ''
        for line in block.splitlines():
            m = re.match(r'\s+TITLE\s+"(.+)"', line)
            if m:
                title = m.group(1)
            m = re.match(r'\s+PERFORMER\s+"(.+)"', line)
            if m:
                performer = m.group(1)
            m = re.match(r'\s+INDEX\s+01\s+(\d+:\d+:\d+)', line)
            if m:
                index_time = m.group(1)
        if title and index_time:
            tracks.append({
                'title': title,
                'performer': performer,
                'index': index_time,
            })

    return global_title, global_performer, tracks


def is_jingle(title):
    return 'Jingle' in title


def make_mix_title(global_title, global_performer):
    if global_title:
        return global_title
    return f"{global_performer} Mix"


def main():
    if len(sys.argv) < 2:
        print("Usage: cue2tracklist.py <input.cue>", file=sys.stderr)
        sys.exit(1)

    cue_path = Path(sys.argv[1])
    if not cue_path.exists():
        print(f"Error: file not found: {cue_path}", file=sys.stderr)
        sys.exit(1)

    global_title, global_performer, tracks = parse_cue(str(cue_path))
    mix_title = make_mix_title(global_title, global_performer)
    filtered = [t for t in tracks if not is_jingle(t['title'])]
    skip_count = len(tracks) - len(filtered)

    if not filtered:
        print("Error: no tracks remain after filtering jingles", file=sys.stderr)
        sys.exit(1)

    out_path = cue_path.with_name(cue_path.stem + '-tracklist.txt')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# {mix_title}\n")
        f.write("## <Engaging description – 2-3 sentences, make listeners curious>\n\n")
        f.write("If you enjoy, please fav, repost, comment!\n")
        f.write("✨<Your DJ Name> ✨\n\n")
        f.write("---\n\n")
        f.write("TRACKLIST:\n\n")
        for t in filtered:
            perf = t['performer'] if t['performer'] else '<unknown>'
            f.write(f"{perf} - {t['title']} {t['index']}\n")
        f.write("\nTAGS:\n")
        f.write("<tag1>, <tag2>, <tag3>, <tag4>, <tag5>\n")

    jingle_note = f" ({skip_count} jingle{'s' if skip_count != 1 else ''} filtered)" if skip_count else ""
    print(f"✓ {out_path.name} ({len(filtered)} tracks{jingle_note})")


if __name__ == '__main__':
    main()
