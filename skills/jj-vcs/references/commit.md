Usage: jj commit [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Put these paths in the current commit

Options:
  -i, --interactive
          Interactively choose which changes to include in the current commit

      --tool <NAME>
          Specify diff editor to be used (implies --interactive)

  -m, --message <MESSAGE>
          The change description to use (don't open editor)

      --editor
          Open an editor to edit the change description
          
          Forces an editor to open when using `--message` to allow the message to be edited
          afterwards.

  -h, --help
          Print help (see a summary with '-h')
