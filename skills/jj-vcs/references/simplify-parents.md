Usage: jj simplify-parents [OPTIONS]

Options:
  -s, --source <REVSETS>
          Simplify specified revision(s) together with their trees of descendants (can be repeated)

  -r, --revision <REVSETS>
          Simplify specified revision(s) (can be repeated)
          
          If both `--source` and `--revisions` are not provided, this defaults to the
          `revsets.simplify-parents` setting, or `reachable(@, mutable())` if it is not set.

  -h, --help
          Print help (see a summary with '-h')
