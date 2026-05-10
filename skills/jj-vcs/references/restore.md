Usage: jj restore [OPTIONS] [FILESETS]...

Arguments:
  [FILESETS]...
          Restore only these paths (instead of all paths)

Options:
  -f, --from <REVSET>
          Revision to restore from (source)

  -t, --into <REVSET>
          Revision to restore into (destination)
          
          [aliases: --to]

  -c, --changes-in <REVSET>
          Undo the changes in a revision as compared to the merge of its parents.
          
          This undoes the changes that can be seen with `jj diff -r REVSET`. If `REVSET` only has a
          single parent, this option is equivalent to `jj restore --into REVSET --from REVSET-`.
          
          The default behavior of `jj restore` is equivalent to `jj restore --changes-in @`.

  -i, --interactive
          Interactively choose which parts to restore

      --tool <NAME>
          Specify diff editor to be used (implies --interactive)

      --restore-descendants
          Preserve the content (not the diff) when rebasing descendants

  -h, --help
          Print help (see a summary with '-h')
