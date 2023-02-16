# Pre Commit Hooks

This repository contains some pre-commit hooks used by Neoception.

## Requirements

- Install [pre-commit](https://pre-commit.com/)

```bash
brew install pre-commit
```

- Add the hook to your `.pre-commit-config.yaml` (see instructions below)

## Usage
If you wish to run `pre-commit` before actually committing use `pre-commit run --all-files`. If you think the `pre-commit` hook is not working properly, clean and install again with:

```bash
pre-commit clean && pre-commit install
```

## Techdocs-Replace-Index

This pre-commit hook script searches for files in the current directory whose filenames start with `readme`, copies the first file found to a file named `index.md` in a `docs` subdirectory, and then replaces instances of the string `(docs/images/` in the new `index.md` file with the string `(images/`

The script can be used to prepare a project for publishing to a documentation site that uses a specific folder structure. When run as a pre-commit hook, the script ensures that the changes are made automatically before committing.

Add to your existing `.pre-commit-config.yaml` with:

```yaml
repos:
  - repo: https://github.com/neoception/pre-commit-hooks
    rev: v0.0.3
    hooks:
      - id: techdocs-replace-index
```
