Usage: jj fix [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Fix only these paths

Options:
  -s, --source <REVSETS>
          Fix files in the specified revision(s) and their descendants. If no revisions are
          specified, this defaults to the `revsets.fix` setting, or `reachable(@, mutable())` if it
          is not set

      --include-unchanged-files
          Fix unchanged files in addition to changed ones. If no paths are specified, all files in
          the repo will be fixed

  -a, --all-lines
          Format all lines instead of only modified lines.
          
          If the formatter doesn't support formatting only modified lines, then this option has no
          effect since the formatter always formats all lines.

  -h, --help
          Print help (see a summary with '-h')
