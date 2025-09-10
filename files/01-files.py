from pathlib import Path
from time import ctime

file = Path("files/test-file.txt")

# print(file.stat())

print("access:", ctime(file.stat().st_atime))
print("created at:", ctime(file.stat().st_ctime))
print("modified at:", ctime(file.stat().st_mtime))
