import subprocess
import json
import os
import sys
from tqdm import tqdm

def set_english_audio_as_default(filepath, tracks):
    for track in tracks:
        if track['type'] != 'audio':
            continue

        track_number = track['id'] + 1
        current_language = track.get('properties', {}).get('language', '').lower()
        is_english = current_language in ['eng', 'english']

        cmd = [
            'mkvpropedit', filepath,
            '--edit', f'track:{track_number}',
            '--set', f'flag-default={"1" if is_english else "0"}'
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def disable_all_subtitles(filepath, tracks):
    for track in tracks:
        if track['type'] != 'subtitles':
            continue

        track_number = track['id'] + 1
        cmd = [
            'mkvpropedit', filepath,
            '--edit', f'track:{track_number}',
            '--set', 'flag-default=0',
            '--set', 'flag-forced=0'
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def process_file(filepath):
    result = subprocess.run(['mkvmerge', '-J', filepath], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"\n[ERROR] {os.path.basename(filepath)}: {result.stderr.strip()}")
        return

    mkvjson = json.loads(result.stdout)
    tracks = mkvjson.get('tracks', [])

    set_english_audio_as_default(filepath, tracks)
    disable_all_subtitles(filepath, tracks)

def process_all_videos_recursive(folder):
    video_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(('.mkv', '.mp4', '.avi', '.m4v')):
                full_path = os.path.join(root, f)
                video_files.append(full_path)

    for filepath in tqdm(video_files, desc="Processing videos"):
        process_file(filepath)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python asd.py <file-or-folder-path>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        process_all_videos_recursive(path)
    else:
        print(f"Error: The path '{path}' is neither a file nor a folder.")
        sys.exit(1)
