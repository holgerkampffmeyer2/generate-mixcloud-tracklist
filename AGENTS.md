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

If you enjoy, please fav, repost, comment!
✨DJ Hulk ✨

---

TRACKLIST:

Performer - Title HH:MM:SS
...
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

### Tags (add in description or separate note)
- Up to 5 genre tags recommended
- Use combination of broad genres (House, Techno) AND specific (Tech House, Deep House)
- This helps appear in Mixcloud Charts and Discover pages

## Rules
- Format: `Performer - Title HH:MM:SS`
- No track numbering
- Filter out jingle tracks (exclude entries with "Jingle" in the title)
- Use the timestamps from INDEX 01 in the CUE file
- Create an engaging Mixcloud title (e.g., "DJ Name Mix-XXX - Genre")
- Add a catchy 2-3 sentence description that makes listeners curious
