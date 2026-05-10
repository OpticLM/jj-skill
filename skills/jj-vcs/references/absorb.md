## Usage

jj absorb [OPTIONS] [FILESETS]...

## Arguments

* [FILESETS]...
  Move only changes to these paths (instead of all paths)

## Options

* -f, --from <REVSET>
  Source revision to absorb from
  [default: @]

* -t, --into <REVSETS>
  Destination revisions to absorb into
  Only ancestors of the source revision will be considered.
  [default: mutable()] [aliases: --to]

* -h, --help
  Print help (see a summary with '-h')
