Usage: jj prev [OPTIONS] [OFFSET]

Arguments:
  [OFFSET]
          How many revisions to move backward. Moves to the parent by default
          
          [default: 1]

Options:
  -e, --edit
          Edit the parent directly, instead of moving the working-copy commit
          
          Takes precedence over config in `ui.movement.edit`; i.e. will negate `ui.movement.edit =
          false`

  -n, --no-edit
          The inverse of `--edit`
          
          Takes precedence over config in `ui.movement.edit`; i.e. will negate `ui.movement.edit =
          true`

      --conflict
          Jump to the previous conflicted ancestor

  -h, --help
          Print help (see a summary with '-h')
