Usage: jj diff [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Restrict the diff to these paths

Options:
  -r, --revisions <REVSETS>
          Show changes in these revisions
          
          If there are multiple revisions, then the total diff for all of them will be shown. For
          example, if you have a linear chain of revisions A..D, then `jj diff -r B::D` equals `jj
          diff --from A --to D`. Multiple heads and/or roots are supported, but gaps in the revset
          are not supported (e.g. `jj diff -r 'A|C'` in a linear chain A..C).
          
          If a revision is a merge commit, this shows changes *from* the automatic merge of the
          contents of all of its parents *to* the contents of the revision itself.
          
          If none of `-r`, `-f`, or `-t` is provided, then the default is `-r @`.

  -f, --from <REVSET>
          Show changes from this revision
          
          If none of `-r`, `-f`, or `-t` is provided, then the default is `-r @`.

  -t, --to <REVSET>
          Show changes to this revision
          
          If none of `-r`, `-f`, or `-t` is provided, then the default is `-r @`.

  -h, --help
          Print help (see a summary with '-h')

Diff Formatting Options:
  -T, --template <TEMPLATE>
          Render each file diff entry using the given template
          
          All 0-argument methods of the [`TreeDiffEntry` type] are available as keywords in the
          template expression. See [`jj help -k templates`] for more information.
          
          [`TreeDiffEntry` type]: https://docs.jj-vcs.dev/latest/templates/#treediffentry-type
          
          [`jj help -k templates`]: https://docs.jj-vcs.dev/latest/templates/

  -s, --summary
          For each path, show only whether it was modified, added, or deleted

      --stat
          Show a histogram of the changes

      --types
          For each path, show only its type before and after
          
          The diff is shown as two letters. The first letter indicates the type before and the
          second letter indicates the type after. '-' indicates that the path was not present, 'F'
          represents a regular file, `L' represents a symlink, 'C' represents a conflict, and 'G'
          represents a Git submodule.

      --name-only
          For each path, show only its path
          
          Typically useful for shell commands like: `jj diff -r @- --name-only | xargs perl -pi
          -e's/OLD/NEW/g`

      --git
          Show a Git-format diff

      --color-words
          Show a word-level diff with changes indicated only by color

      --tool <TOOL>
          Generate diff by external command
          
          A builtin format can also be specified as `:<name>`. For example, `--tool=:git` is
          equivalent to `--git`.

      --context <CONTEXT>
          Number of lines of context to show

  -w, --ignore-all-space
          Ignore whitespace when comparing lines

  -b, --ignore-space-change
          Ignore changes in amount of whitespace when comparing lines
