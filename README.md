# MKVMagiq — Fix Default Audio & Subtitles in MKV Files

MKVMagiq is a simple Python tool that helps you clean up your video files by:

- Setting English audio as the default
- Disabling all subtitle tracks
- Recursively scanning folders (including subfolders)
- Editing files directly — no re-encoding needed
- Showing a progress bar while working through files

---

## Requirements

Before using MKVMagiq, you'll need the following:

### 1. Python (3.7 or higher)

- Download from: https://www.python.org/downloads/
- During installation, make sure to check **"Add Python to PATH"**

### 2. MKVToolNix

- Download from: https://mkvtoolnix.download/downloads.html
- During installation, ensure `mkvpropedit` and `mkvmerge` are added to your system’s **PATH**.
- If not added automatically:
  - Find the install location (e.g., `C:\Program Files\MKVToolNix`)
  - Add that folder to your system’s Environment Variables → `Path`

### 3. tqdm (for progress bar)

Install via pip:

```bash
pip install tqdm
```

---

## How to Use

### Step 1: Download or Clone the Repo

```bash
git clone https://github.com/yourusername/mkvmagiq.git
cd mkvmagiq
```

Or download the ZIP file and extract it.

---

### Step 2: Run the Script

Open your terminal (Command Prompt or PowerShell) and run:

#### To process a single video file:

```bash
python mkvmagiq.py "C:\Path\To\Your\File.mkv"
```

#### To process all video files in a folder (and subfolders):

```bash
python mkvmagiq.py "C:\Path\To\Your\Folder"
```

The script will:

- Set the **English audio** track as the default (if found)
- Disable all **subtitle tracks**
- Display a progress bar as it works

---

## Notes

- Close any apps (like VLC) that might be using the video files while the script runs.
- Ensure the files are **not write-protected** and you have **edit permissions**.
- No re-encoding is done — the script simply modifies metadata (fast and lossless).

---

## License

MIT — free to use, modify, and share.

---

## Support

Feel free to open an issue or discussion on the GitHub repo if you run into trouble or have questions.

I wonder if this will useful to anyone else :)
Angelo
