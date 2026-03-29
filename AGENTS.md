# Cue to Tracklist Conversion

## Task
Convert CUE files to tracklist text files and save with the same name as input but with "-tracklist.txt" suffix.

## Input
- CUE file with track information including TITLE, PERFORMER, and INDEX (start time)
- Example file showing the expected output format

## Output Format
```
Performer - Title HH:MM:SS
```

Rules:
- Format: `Performer - Title HH:MM:SS`
- No track numbering
- Filter out jingle tracks (exclude entries with "Jingle" in the title)
- Use the timestamps from INDEX 01 in the CUE file
