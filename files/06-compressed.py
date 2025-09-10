from pathlib import Path
from zipfile import ZipFile

# Write a zip file
# with ZipFile("files/file.zip", "w") as zip:
#     for path in Path("files").rglob("*.*"):  # *.* all files
#         # validate not to zip this zip file
#         # print(path)
#         if str(path) != "files/file.zip":
#             zip.write(path)

# Read a zip file
with ZipFile("files/file.zip", "r") as zip:
    # print(zip.namelist())  # list of files in the zip
    info = zip.getinfo("files/06-compressed.py")
    print(info)
    print(info.file_size)  # original file size
    print(info.compress_size)  # compressed file size
    # extract all files
    zip.extractall("files/unzipped")
