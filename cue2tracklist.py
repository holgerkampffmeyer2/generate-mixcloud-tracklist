#!/usr/bin/env python3
"""Parse Rekordbox CUE file and generate Mixcloud tracklist template."""

import re
import sys
from pathlib import Path

DJ_HULK_BIO = """Electronic Music DJ from Stuttgart, Germany. I am the co-founder of the DJ collective ToMaTe Stuttgart n.e.V.
I have performed at notable venues such as Romy S., EX-Club Zollamt, Mrs. Jones
I love playing House and Tech House music. Sometimes spicing it up with Techno and DnB.
You can find my weekly mixes on Mixcloud. You can also hear me on the web radio stations Couchradio, JDK Radio and 365 FM Radio

Mixcloud: https://www.mixcloud.com/holger-kampffmeyer/
Instagram: https://www.instagram.com/holgerkampffmeyer/"""

DEFAULT_STATION = 'Vertic Club Radio'


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


def dedupe_tracks(tracks):
    seen = set()
    unique = []
    for t in tracks:
        key = (t['performer'].strip().lower(), t['title'].strip().lower())
        if key in seen:
            continue
        seen.add(key)
        unique.append(t)
    return unique


def make_mix_title(global_title, global_performer):
    if global_title:
        return global_title
    return f"{global_performer} Mix"


import html


def track_lines(filtered):
    lines = []
    for t in filtered:
        perf = t['performer'] if t['performer'] else '<unknown>'
        lines.append(f"{perf} - {t['title']} {t['index']}")
    return lines


def write_tracklist(path, mix_title, filtered, dj_name):
    tracks = track_lines(filtered)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {mix_title}\n\n")
        f.write("TEASER:\n")
        f.write("<Teaser text – max 250 characters, catchy hook for notifications/previews>\n\n")
        f.write("POST:\n")
        f.write("## <Engaging description – 2-3 sentences, make listeners curious>\n\n")
        f.write("If you enjoy, please fav, repost, comment!\n")
        f.write(f"✨**{dj_name}** ✨\n\n")
        f.write("---\n\n")
        f.write("TRACKLIST:\n")
        for line in tracks:
            f.write(line + "\n")
        f.write("\nTAGS:\n")
        f.write("<tag1>, <tag2>, <tag3>, <tag4>, <tag5>\n")

    html_path = Path(path).with_suffix('.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f"<h1>{html.escape(mix_title)}</h1>\n\n")
        f.write("<h2>TEASER</h2>\n")
        f.write("<p>&lt;Teaser text – max 250 characters, catchy hook for notifications/previews&gt;</p>\n\n")
        f.write("<h2>POST</h2>\n")
        f.write("<h3>&lt;Engaging description – 2-3 sentences, make listeners curious&gt;</h3>\n")
        f.write("<p>If you enjoy, please fav, repost, comment!<br>✨<strong>" + html.escape(dj_name) + "</strong> ✨</p>\n\n")
        f.write("<hr>\n\n")
        f.write("<h3>TRACKLIST</h3>\n")
        f.write("<pre>" + html.escape("\n".join(tracks)) + "</pre>\n\n")
        f.write("<h2>TAGS</h2>\n")
        f.write("<p>&lt;tag1&gt;, &lt;tag2&gt;, &lt;tag3&gt;, &lt;tag4&gt;, &lt;tag5&gt;</p>\n")


def write_guestmix(path, mix_title, filtered, station, dj_name):
    tracks = track_lines(filtered)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {mix_title}\n\n")
        f.write("TEASER:\n")
        f.write("<Teaser text – max 250 characters, catchy hook for notifications/previews>\n\n")
        f.write("POST:\n")
        f.write(f"## Guest Mix for {station}\n\n")
        f.write("<Engaging description, 2-3 sentences, mention the vibe and why listeners should tune in>\n\n")
        f.write("If you enjoy, please fav, repost, comment!\n")
        f.write(f"✨**{dj_name}** ✨\n\n")
        f.write("---\n\n")
        f.write("TRACKLIST:\n")
        for line in tracks:
            f.write(line + "\n")
        f.write("\n---\n\n")
        f.write(f"### About {dj_name}\n")
        f.write(DJ_HULK_BIO + "\n")

    html_path = Path(path).with_suffix('.html')
    bio_html = "<br>".join(html.escape(line) for line in DJ_HULK_BIO.splitlines())
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f"<h1>{html.escape(mix_title)}</h1>\n\n")
        f.write("<h2>TEASER</h2>\n")
        f.write("<p>&lt;Teaser text – max 250 characters, catchy hook for notifications/previews&gt;</p>\n\n")
        f.write("<h2>POST</h2>\n")
        f.write(f"<h3>Guest Mix for {html.escape(station)}</h3>\n")
        f.write("<p>&lt;Engaging description, 2-3 sentences, mention the vibe and why listeners should tune in&gt;</p>\n")
        f.write("<p>If you enjoy, please fav, repost, comment!<br>✨<strong>" + html.escape(dj_name) + "</strong> ✨</p>\n\n")
        f.write("<hr>\n\n")
        f.write("<h3>TRACKLIST</h3>\n")
        f.write("<pre>" + html.escape("\n".join(tracks)) + "</pre>\n\n")
        f.write("<hr>\n\n")
        f.write(f"<h3>About {html.escape(dj_name)}</h3>\n")
        f.write(f"<p>{bio_html}</p>\n")


def print_usage():
    print("Usage: cue2tracklist.py <input.cue> [--guestmix [--station NAME]]", file=sys.stderr)
    print("Options:", file=sys.stderr)
    print("  --guestmix          Generate a guest mix text (description, tracklist, bio)", file=sys.stderr)
    print("  --station NAME      Radio station name for the guest mix (default: Vertic Club Radio)", file=sys.stderr)
    print("  -h, --help          Show this help", file=sys.stderr)


def parse_args(argv):
    guestmix = False
    station = DEFAULT_STATION
    cue_path = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in ('-h', '--help'):
            print_usage()
            sys.exit(0)
        elif arg == '--guestmix':
            guestmix = True
        elif arg == '--station':
            i += 1
            if i >= len(argv):
                print("Error: --station requires a name", file=sys.stderr)
                sys.exit(1)
            station = argv[i]
        elif arg.startswith('-'):
            print(f"Error: unknown option: {arg}", file=sys.stderr)
            print_usage()
            sys.exit(1)
        else:
            cue_path = arg
        i += 1
    return cue_path, guestmix, station


def main():
    cue_arg, guestmix, station = parse_args(sys.argv[1:])

    if not cue_arg:
        print_usage()
        sys.exit(1)

    cue_path = Path(cue_arg)
    if not cue_path.exists():
        print(f"Error: file not found: {cue_path}", file=sys.stderr)
        sys.exit(1)

    global_title, global_performer, tracks = parse_cue(str(cue_path))
    mix_title = make_mix_title(global_title, global_performer)
    non_jingle = [t for t in tracks if not is_jingle(t['title'])]
    filtered = dedupe_tracks(non_jingle)
    jingle_count = len(tracks) - len(non_jingle)
    duplicate_count = len(non_jingle) - len(filtered)

    if not filtered:
        print("Error: no tracks remain after filtering jingles", file=sys.stderr)
        sys.exit(1)

    dj_name = global_performer if global_performer else 'DJ Hulk'
    suffix = '-guestmix.txt' if guestmix else '-tracklist.txt'
    out_path = cue_path.with_name(cue_path.stem + suffix)

    if guestmix:
        write_guestmix(str(out_path), mix_title, filtered, station, dj_name)
    else:
        write_tracklist(str(out_path), mix_title, filtered, dj_name)

    html_path = out_path.with_suffix('.html')
    notes = []
    if jingle_count:
        notes.append(f"{jingle_count} jingle{'s' if jingle_count != 1 else ''} filtered")
    if duplicate_count:
        notes.append(f"{duplicate_count} duplicate{'s' if duplicate_count != 1 else ''} removed")
    note = f" ({', '.join(notes)})" if notes else ""
    print(f"✓ {out_path.name}, {html_path.name} ({len(filtered)} tracks{note})")


if __name__ == '__main__':
    main()