# Cue to Tracklist Conversion

## Task
Convert CUE files to tracklist text files and save with the same name as input but with "-tracklist.txt" suffix.

## Input
- CUE file with track information including TITLE, PERFORMER, and INDEX (start time)
- Example file showing the expected output format

## Output Format
```
# Mix Title
## Engaging description (2-3 sentences, makes listeners curious)

---

TRACKLIST:

Performer - Title HH:MM:SS
...
```

Rules:
- Format: `Performer - Title HH:MM:SS`
- No track numbering
- Filter out jingle tracks (exclude entries with "Jingle" in the title)
- Use the timestamps from INDEX 01 in the CUE file
- Create an engaging Mixcloud title (e.g., "DJ Name Mix-XXX - Genre")
- Add a catchy 2-3 sentence description that makes listeners curious
- Always add this line at the end of the description: "If you enjoy, please fav, repost, comment!" followed by "✨Your DJ Name ✨"
