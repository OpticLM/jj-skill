---
name: jj-vcs
description: Using jj for version control
allowed-tools: Bash(jj:*)
license: MIT
metadata:
  author: OpticLM
  version: "0.41.0.0"
---

## Core concepts

jj is a new version control system that supports various VCSes, including Git, as file system backends. Therefore, while you may still be able to use Git commands, this is no longer recommended; you should use jj instead.

In jj, history is organized in units called changes (also known as revisions; in jj, revision and change are synonymous). Each change is a diff based on one or more ancestor changes. Every change has a change ID that remains fixed. You can make changes to files within a change, resulting in a new commit hash, but the change ID will remain the same. This aligns with the concept of changes evolving over time.

The current workspace resides in a revision we commonly refer to as the working copy. The ultimate ancestor of all revisions is the root revision with change ID zzzzzzzz.

When you need to save the current diff as a revision, simply create a new revision based on the current revision (or any other revision).

```sh
$ jj log
@  abcdefgh [author] [time]
│  (no description set)
◆  zzzzzzzz root() 00000000
$ jj new abcdefgh
Working copy  (@) now at: qwertyui [hash] (empty) (no description set)
Parent commit (@-)      : abcdefgh [hash] (no description set)
```

There is no concept of a `git commit` here. There is no staging area. To ignore a file, add it to `.gitignore` and then use `jj file untrack`.

You could:
* `jj new a` Create a new revision based on `a` revision
* `jj squash` or `jj squash -f a -t b` Squash diffs of a revision into b revision
* `jj describe -m [message] a` Describe revision a. **This is necessary before pushing the revision to remote.**
* `jj commit -m [message]` Equivalent to `jj describe -m [message] && jj new`
* `jj edit a` Switch the workspace to the state of revision `a`. At this point, any changes made to the workspace will be reflected in the diff for revision `a`. It is recommended to use `jj new a` and then, after review, use `jj squash` as needed.
** `jj diff --git` Get a git-style diff to prevent

## Resources

- references/
  - help.md: All commands
  - global-options.md: Global options for jj CLI tool
  - [command-name].md: E.g. abandon.md for `jj abandon` command

## Quick Start

* **Clone a repository** `jj git clone` (same as `git clone`)
* **Push** `jj git push`
* **Manage remotes** `jj git remote add origin ...`
* **Status of current working copy** `jj st`
* **List all revisions** `jj log -r "all()"`

## Branches or Bookmarks

jj does not use branches; instead, it uses bookmarks. Each bookmark points to a revision. Use `jj bookmark track [bookmark name] --remote=[remote name]`, for example `jj bookmark track main --remote=origin`, to bind a bookmark to a branch in a remote Git repository.

Here’s how bookmarks work: Suppose the bookmark `main` and `main@origin` both point to revision `a`. After the user creates several revisions, the latest (non-empty) revision becomes `b`. If the user wants to push this to the remote, they would run:

```sh
jj bookmark move --to=b main
# or
jj b m -t=b main
```

At this point, `main@origin` still points to `a`, but `main` points to `b`. Therefore, `jj git push` will resolve the Git commits intended for the `main` branch and push them.

Because of this design, in a tree-like revision branch structure, you only need to move the bookmark; you don’t need to worry about branch management.
