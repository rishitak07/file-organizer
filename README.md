# File Organiser

A simple Python script that automatically sorts the files in a folder into subfolders, either by **file type** or by **last-modified date**. It uses only Python's built-in modules, so there is nothing to install.

## Features

- Sort files by type: Images, Documents, Spreadsheets, Videos, Audio, Code, Archives, or Other
- Sort files by date into `YYYY-MM` folders (for example `2025-03`)
- Preview mode to see what would happen before anything is moved
- Never overwrites files: duplicates are renamed to `file (1).txt`, `file (2).txt`, and so on
- Skips hidden files, existing folders, and the script itself

## Requirements

- Python 3.6 or newer

## How to use

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the script:

   ```
   python main.py
   ```

4. Answer the three questions:
   - Which folder to organise (press Enter to use the current folder)
   - Sort by `1` (type) or `2` (date)
   - Preview only? Type `y` to preview, `n` to move the files

## Example

Before:

```
Downloads/
├── holiday.jpg
├── report.pdf
├── song.mp3
└── script.py
```

After sorting by type:

```
Downloads/
├── Images/
│   └── holiday.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
└── Code/
    └── script.py
```

## Customising

To add or change categories, edit the `categories` dictionary at the top of `main.py`:

```python
categories = {
    "Images": [".jpg", ".png", ".gif"],
    "Ebooks": [".epub", ".mobi"],
}
```

## Tip

Run the script in preview mode first and test it on a copy of a folder before using it on important files.
