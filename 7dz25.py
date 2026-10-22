from pathlib import Path
directory = input()
ext = input()
root = Path(directory)
if not root.is_dir():
    print("directory not found")
else:
    for p in root.rglob(f"*{ext}"):
        if p.is_file():
            print(p, p.stat().st_size)