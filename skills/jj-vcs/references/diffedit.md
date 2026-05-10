## Usage

jj diffedit [OPTIONS] [FILESETS]...

## Arguments

* [FILESETS]...
  Edit only these paths (unmatched paths will remain unchanged)

## Options

* -r, --revision <REVSET>
  The revision to touch up
  Defaults to @ if neither --to nor --from are specified.

* -f, --from <REVSET>
  Show changes from this revision
  Defaults to @ if --to is specified.

* -t, --to <REVSET>
  Edit changes in this revision
  Defaults to @ if --from is specified.

* --tool <NAME>
  Specify diff editor to be used

* --restore-descendants
  Preserve the content (not the diff) when rebasing descendants
  When rebasing a descendant on top of the rewritten revision, its diff compared to its parent(s) is normally preserved, i.e. the same way that descendants are always rebased. This flag makes it so the content/state is preserved instead of preserving the diff.

* -h, --help
  Print help (see a summary with '-h')
