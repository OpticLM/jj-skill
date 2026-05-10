Usage: jj split [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Files matching any of these filesets are put in the selected changes

Options:
  -i, --interactive
          Interactively choose which parts to split
          
          This is the default if no filesets are provided.

      --tool <NAME>
          Specify diff editor to be used (implies --interactive)

  -r, --revision <REVSET>
          The revision to split
          
          [default: @]

  -o, --onto <REVSETS>
          The revision(s) to rebase the selected changes onto (can be repeated to create a merge
          commit)
          
          Extracts the selected changes into a new commit based on the given revision(s). The
          remaining changes stay in the original commit's location.
          
          [aliases: -d, --destination]

  -A, --insert-after <REVSETS>
          The revision(s) to insert after (can be repeated to create a merge commit)
          
          Extracts the selected changes into a new commit inserted after the given revision(s). The
          remaining changes stay in the original commit's location.
          
          [aliases: --after]

  -B, --insert-before <REVSETS>
          The revision(s) to insert before (can be repeated to create a merge commit)
          
          Extracts the selected changes into a new commit inserted before the given revision(s). The
          remaining changes stay in the original commit's location.
          
          [aliases: --before]

  -m, --message <MESSAGE>
          The change description to use for the selected changes (don't open editor)
          
          Sets the description for the revision containing the selected changes. The other revision
          will keep its original description, if any.

      --editor
          Open an editor to edit the change description(s)
          
          Forces an editor to open when using `--message` to allow the message to be edited
          afterward.

  -p, --parallel
          Split the revision into two parallel revisions instead of a parent and child

  -h, --help
          Print help (see a summary with '-h')
