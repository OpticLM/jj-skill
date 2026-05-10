## Usage

jj revert [OPTIONS] --revision <REVSETS> <--onto <REVSETS>|--insert-after <REVSETS>|--insert-before <REVSETS>>

## Options

* -r, --revision <REVSETS>
  The revision(s) to apply the reverse of

* -o, --onto <REVSETS>
  The revision(s) to apply the reverse changes on top of
  [aliases: -d, --destination]

* -A, --insert-after <REVSETS>
  The revision(s) to insert the reverse changes after (can be repeated to create a merge commit)
  [aliases: --after]

* -B, --insert-before <REVSETS>
  The revision(s) to insert the reverse changes before (can be repeated to create a merge commit)
  [aliases: --before]

* -h, --help
  Print help (see a summary with '-h')
