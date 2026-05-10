Usage: jj next [OPTIONS] [OFFSET]

Arguments:
  [OFFSET]
          How many revisions to move forward. Advances to the next child by default
          
          [default: 1]

Options:
  -e, --edit
          Instead of creating a new working-copy commit on top of the target commit (like `jj new`),
          edit the target commit directly (like `jj edit`)
          
          Takes precedence over config in `ui.movement.edit`; i.e. will negate `ui.movement.edit =
          false`

  -n, --no-edit
          The inverse of `--edit`
          
          Takes precedence over config in `ui.movement.edit`; i.e. will negate `ui.movement.edit =
          true`

      --conflict
          Jump to the next conflicted descendant

  -h, --help
          Print help (see a summary with '-h')
