Usage: jj log [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Show revisions modifying the given paths

Options:
  -r, --revision <REVSETS>
          Which revisions to show
          
          If no paths nor revisions are specified, this defaults to the `revsets.log` setting.

  -n, --limit <LIMIT>
          Limit number of revisions to show
          
          Applied after revisions are filtered and reordered topologically, but before being
          reversed.

      --reversed
          Show revisions in the opposite order (older revisions first)

  -G, --no-graph
          Don't show the graph, show a flat list of revisions

  -T, --template <TEMPLATE>
          Render each revision using the given template
          
          Run `jj log -T` to list the built-in templates.
          
          You can also specify arbitrary template expressions using the [built-in keywords]. See
          [`jj help -k templates`] for more information.
          
          If not specified, this defaults to the `templates.log` setting.
          
          [built-in keywords]: https://docs.jj-vcs.dev/latest/templates/#commit-keywords
          
          [`jj help -k templates`]: https://docs.jj-vcs.dev/latest/templates/

  -p, --patch
          Show patch

      --count
          Print the number of commits instead of showing them

  -h, --help
          Print help (see a summary with '-h')

Diff Formatting Options:
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

      --ignore-all-space
          Ignore whitespace when comparing lines

      --ignore-space-change
          Ignore changes in amount of whitespace when comparing lines
