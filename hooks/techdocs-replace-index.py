#!/usr/bin/env python3
import os
def main():
    os.system('cp readme.md docs/index.md')
    print("Copying the File")
    textToSearch = "(docs/images/"
    textToReplace = "(images/"
    docs_file="docs/index.md"
    # Read in the file
    with open(docs_file, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(textToSearch, textToReplace)

    # Write the file out again
    with open(docs_file, 'w') as file:
        file.write(filedata)
        
    print("Replaced paths on readme for techdocs")