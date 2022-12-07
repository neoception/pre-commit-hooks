#!/usr/bin/env python3
from pathlib import Path
import os
import shutil

dir_src = "./"

for filename in os.listdir("."):
    if filename.lower().startswith("readme"):
        shutil.copyfile(dir_src + filename, "./docs/index.md")

print("Copying the File")
textToSearch = "(docs/images/"
textToReplace = "(images/"
destination_file = "docs/index.md"
# Read in the file
with open(destination_file, "r") as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace(textToSearch, textToReplace)

# Write the file out again
with open(destination_file, "w") as file:
    file.write(filedata)

print("Replaced paths on readme for techdocs")
