# Pre Commit Hooks

This repository contains some pre-commit hooks used by Neoception.

# Techdocs-Replac-Index

This pre-commit hook script searches for files in the current directory whose filenames start with "readme", copies the first file found to a file named "index.md" in a "docs" subdirectory, and then replaces instances of the string "(docs/images/" in the new "index.md" file with the string "(images/". The script can be used to prepare a project for publishing to a documentation site that uses a specific folder structure. When run as a pre-commit hook, the script ensures that the changes are made automatically before committing.