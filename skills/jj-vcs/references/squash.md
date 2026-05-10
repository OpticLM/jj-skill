Usage: jj squash [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Move only changes to these paths (instead of all paths)

Options:
  -r, --revision <REVSET>
          Revision to squash into its parent (default: @). Incompatible with the experimental
          `-o`/`-A`/`-B` options

  -f, --from <REVSETS>
          Revision(s) to squash from (default: @)

  -t, --into <REVSET>
          Revision to squash into (default: @)
          
          [aliases: --to]

  -o, --onto <REVSETS>
          (Experimental) The revision(s) to use as parent for the new commit (can be repeated to
          create a merge commit)
          
          [aliases: -d, --destination]

  -A, --insert-after <REVSETS>
          (Experimental) The revision(s) to insert the new commit after (can be repeated to create a
          merge commit)
          
          [aliases: --after]

  -B, --insert-before <REVSETS>
          (Experimental) The revision(s) to insert the new commit before (can be repeated to create
          a merge commit)
          
          [aliases: --before]

  -m, --message <MESSAGE>
          The description to use for squashed revision (don't open editor)

  -u, --use-destination-message
          Use the description of the destination revision and discard the description(s) of the
          source revision(s)

      --editor
          Open an editor to edit the change description
          
          Forces an editor to open when using `--message` to allow the message to be edited
          afterwards.

  -i, --interactive
          Interactively choose which parts to squash

      --tool <NAME>
          Specify diff editor to be used (implies --interactive)

  -k, --keep-emptied
          The source revision will not be abandoned

  -h, --help
          Print help (see a summary with '-h')
