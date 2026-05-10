Usage: jj duplicate [OPTIONS] [REVSETS]...

Arguments:
  [REVSETS]...
          The revision(s) to duplicate (default: @) [aliases: -r]

Options:
  -o, --onto <REVSETS>
          The revision(s) to duplicate onto (can be repeated to create a merge commit)
          
          [aliases: -d, --destination]

  -A, --insert-after <REVSETS>
          The revision(s) to insert after (can be repeated to create a merge commit)
          
          [aliases: --after]

  -B, --insert-before <REVSETS>
          The revision(s) to insert before (can be repeated to create a merge commit)
          
          [aliases: --before]

  -h, --help
          Print help (see a summary with '-h')
