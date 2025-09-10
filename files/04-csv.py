import csv
import os
# write
# with open("files/file.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1, 123, "Hello, World!"])
#     writer.writerow([2, 456, "Hello, CSV!"])


# read
# with open("files/file.csv") as file:  # "r" is the default mode
#     reader = csv.reader(file)
#     # [['twit_id', 'user_id', 'text'], ['1', '123', 'Hello, World!'], ['2', '456', 'Hello, CSV!']]
#     print(list(reader))
#     file.seek(0)
#     for row in reader:
#         print(row)

# Update CSV
with open("files/file.csv") as r, open("files/file-temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for row in reader:
        if row[0] == '1':
            writer.writerow([1, 123, "Modified text"])
        else:
            writer.writerow(row)

    # now delete the original file and rename the temp file to the original file name
    os.remove("files/file.csv")
    os.rename("files/file-temp.csv", "files/file.csv")
