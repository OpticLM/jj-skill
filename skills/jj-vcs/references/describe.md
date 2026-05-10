Usage: jj describe [OPTIONS] [REVSETS]...

Arguments:
  [REVSETS]...
          The revision(s) whose description to edit (default: @) [aliases: -r]

Options:
  -m, --message <MESSAGE>
          The change description to use (don't open editor)
          
          If multiple revisions are specified, the same description will be used for all of them.

      --stdin
          Read the change description from stdin
          
          If multiple revisions are specified, the same description will be used for all of them.

      --editor
          Open an editor to edit the change description
          
          Forces an editor to open when using `--stdin` or `--message` to allow the message to be
          edited afterwards.

  -h, --help
          Print help (see a summary with '-h')
