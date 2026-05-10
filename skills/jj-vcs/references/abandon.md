Usage: jj abandon [OPTIONS] [REVSETS]...

Arguments:
  [REVSETS]...
          The revision(s) to abandon (default: @) [aliases: -r]

Options:
      --retain-bookmarks
          Do not delete bookmarks pointing to the revisions to abandon
          
          Bookmarks will be moved to the parent revisions instead.

      --restore-descendants
          Do not modify the content of the children of the abandoned commits

  -h, --help
          Print help (see a summary with '-h')
