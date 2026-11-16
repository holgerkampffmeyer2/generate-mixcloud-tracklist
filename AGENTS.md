# Cue to Tracklist Conversion

## Task
Convert CUE files to tracklist text files with "-tracklist.txt" suffix.

## Workflow

Run the script THEN immediately fill in the creative parts — both steps are required, never stop after step 1.

### 1. Run the parser script
```bash
python3 cue2tracklist.py <input.cue>
```
This generates `*-tracklist.txt` and `*-tracklist.html` with placeholders for teaser, post text, DJ name, and tags.

For a radio station guest mix (e.g., Vertic Club Radio):
```bash
python3 cue2tracklist.py <input.cue> --guestmix [--station "Vertic Club Radio"]
```
This generates `*-guestmix.txt` and `*-guestmix.html` with placeholders for teaser and post text, the tracklist, and the DJ Hulk bio.

### 2. AI fills creative parts (English, immediately after step 1)
Replace the placeholders in both generated files (`.txt` and `.html`):
- **Teaser**: short hook for Mixcloud's separate teaser field, max 250 characters
- **Post/Description**: 2-3 engaging English sentences that make listeners curious (post text supports headings, **bold**, *italic*; keep `.html` formatted with `<h3>/<p>/<strong>/<em>` so it can be pasted into rich fields)
- **DJ Name**: e.g., `DJ Hulk`
- **Tags**: exactly 5 genre tags (tracklist output)

## Input
- CUE file with track information including TITLE, PERFORMER, and INDEX (start time)

## Output Format (tracklist)
```
# Mix Title

TEASER:
<max 250 characters>

POST:
## Engaging description (2-3 sentences, makes listeners curious)

If you enjoy, please fav, repost, comment!
✨**DJ Hulk** ✨

---

TRACKLIST:
Performer - Title HH:MM:SS
...

TAGS:
tag1, tag2, tag3, tag4, tag5
```

## Output Format (guest mix)
```
# Mix Title

TEASER:
<max 250 characters>

POST:
## Guest Mix for <Station>

<Engaging description, 2-3 sentences>

If you enjoy, please fav, repost, comment!
✨**DJ Hulk** ✨

---

TRACKLIST:
Performer - Title HH:MM:SS
...

---

### About DJ Hulk
<bio>
```

## Mixcloud Guidelines

### Teaser (separate field)
- Max 250 characters
- First thing followers see in notifications/previews; make it compelling

### Post text (supports heading, bold, italic)
- Explain the mood, concept or setting of the mix
- Make listeners curious - why should they press play?
- Include relevant keywords naturally (genre names, vibe descriptors)
- Use headings/bold/italic where helpful
- End with: "If you enjoy, please fav, repost, comment!" + "✨**DJ Name** ✨"

### Tags (tracklist output)
- Exactly 5 genre tags required for generated outputs
- Mix broad genres (House, Techno) and specific (Tech House, Deep House)
- Listed in the `TAGS:` section, comma-separated

## Rules
- Format: `Performer - Title HH:MM:SS`
- Teaser, post text, DJ name, and other creative text must be written in English
- Teaser must be <= 250 characters
- No track numbering
- Filter out jingle tracks (exclude entries with "Jingle" in the title)
- Use the timestamps from INDEX 01 in the CUE file
- Create an engaging Mixcloud title (e.g., "DJ Name Mix-XXX - Genre")
- Add a teaser (max 250 chars) and a catchy 2-3 sentence post description
- Keep the generated tracklist block compact (no extra blank lines inside TRACKLIST section) to paste cleanly into Mixcloud
- Include exactly 5 genre tags as a `TAGS:` section after the TRACKLIST in tracklist outputs, following Mixcloud SEO tag guidelines
