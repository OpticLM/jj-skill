help: 
    @just --list

install: 
    cp -r ./skills/jj-vcs ~/.agents/skills/jj-vcs

generate:
    uv run scripts/generate.py
