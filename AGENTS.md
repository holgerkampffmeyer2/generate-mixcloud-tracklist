# Cue to Tracklist Conversion

## Task
Convert CUE files to tracklist text files with "-tracklist.txt" suffix.

## Workflow

Run the script THEN immediately fill in the creative parts — both steps are required, never stop after step 1.

### 1. Run the parser script
```bash
python3 cue2tracklist.py <input.cue>
```
This generates a `*-tracklist.txt` file with placeholders for description, DJ name, and tags.

### 2. AI fills creative parts (English, immediately after step 1)
Replace the placeholders in the generated file:
- **Description**: 2-3 engaging English sentences that make listeners curious
- **DJ Name**: e.g., `DJ Hulk`
- **Tags**: exactly 5 genre tags

## Input
- CUE file with track information including TITLE, PERFORMER, and INDEX (start time)

## Output Format
```
# Mix Title
## Engaging description (2-3 sentences, makes listeners curious)

If you enjoy, please fav, repost, comment!
✨DJ Hulk ✨

---

TRACKLIST:

Performer - Title HH:MM:SS
...

TAGS:
tag1, tag2, tag3, tag4, tag5
```

## Mixcloud SEO Guidelines (for better discoverability)

### Title
- Format: "DJ Name Mix-XXX - Genre" (e.g., "DJ Hulk Mix-178 - Tech House")
- Include mix number and genre for searchability

### Description (2-3 sentences)
- Explain the mood, concept or setting of the mix
- Make listeners curious - why should they press play?
- Include relevant keywords naturally (genre names, vibe descriptors)
- End with: "If you enjoy, please fav, repost, comment!" + "✨Your DJ Name ✨"

### Tags (add as separate TAGS section in output txt)
- Exactly 5 genre tags required for generated outputs
- Use combination of broad genres (House, Techno) AND specific (Tech House, Deep House)
- This helps appear in Mixcloud Charts and Discover pages
- Tags must be listed in the `TAGS:` section of the output text file, comma-separated

## Rules
- Format: `Performer - Title HH:MM:SS`
- Description, DJ name, and other creative text must be written in English
- No track numbering
- Filter out jingle tracks (exclude entries with "Jingle" in the title)
- Use the timestamps from INDEX 01 in the CUE file
- Create an engaging Mixcloud title (e.g., "DJ Name Mix-XXX - Genre")
- Add a catchy 2-3 sentence description that makes listeners curious
- Include exactly 5 genre tags as a `TAGS:` section after the TRACKLIST, following Mixcloud SEO tag guidelines
