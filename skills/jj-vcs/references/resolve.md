## Usage

jj resolve [OPTIONS] [FILESETS]...

## Arguments

* [FILESETS]...
  Only resolve conflicts in these paths. You can use the `--list` argument to find paths to use here

## Options

* -r, --revision <REVSET>
  [default: @]

* -l, --list
  Instead of resolving conflicts, list all the conflicts

* --tool <NAME>
  Specify 3-way merge tool to be used
  The built-in merge tools `:ours` and `:theirs` can be used to choose side #1 and side #2 of the conflict respectively.

* -h, --help
  Print help (see a summary with '-h')
