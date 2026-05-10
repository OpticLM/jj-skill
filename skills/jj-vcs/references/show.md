## Usage

jj show [OPTIONS] [REVSET]

## Arguments

* [REVSET]
  Show changes in this revision, compared to its parent(s) [default: @] [aliases: -r]

## Options

* -T, --template <TEMPLATE>
  Render a revision using the given template
  You can specify arbitrary template expressions using the [built-in keywords]. See [`jj help -k templates`] for more information.
  [built-in keywords]: https://docs.jj-vcs.dev/latest/templates/#commit-keywords
  [`jj help -k templates`]: https://docs.jj-vcs.dev/latest/templates/

* -h, --help
  Print help (see a summary with '-h')

## Diff Formatting Options

* -s, --summary
  For each path, show only whether it was modified, added, or deleted

* --stat
  Show a histogram of the changes

* --types
  For each path, show only its type before and after
  The diff is shown as two letters. The first letter indicates the type before and the second letter indicates the type after. '-' indicates that the path was not present, 'F' represents a regular file, `L' represents a symlink, 'C' represents a conflict, and 'G' represents a Git submodule.

* --name-only
  For each path, show only its path
  Typically useful for shell commands like: `jj diff -r @- --name-only | xargs perl -pi -e's/OLD/NEW/g`

* --git
  Show a Git-format diff

* --color-words
  Show a word-level diff with changes indicated only by color

* --tool <TOOL>
  Generate diff by external command
  A builtin format can also be specified as `:<name>`. For example, `--tool=:git` is equivalent to `--git`.

* --context <CONTEXT>
  Number of lines of context to show

* -w, --ignore-all-space
  Ignore whitespace when comparing lines

* -b, --ignore-space-change
  Ignore changes in amount of whitespace when comparing lines

* --no-patch
  Do not show the patch
