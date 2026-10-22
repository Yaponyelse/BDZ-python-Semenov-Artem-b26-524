from pathlib import Path
root = Path(".")
files = [p for p in root.iterdir() if p.is_file()]
dirs = [p for p in root.iterdir() if p.is_dir()]
py_files = [p for p in root.rglob("*.py")]
total_size = sum(p.stat().st_size for p in root.rglob("*") if p.is_file())
print(len(files))
print(len(dirs))
for p in py_files:
    print(p)
print(total_size)