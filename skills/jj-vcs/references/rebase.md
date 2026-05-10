## Usage

jj rebase [OPTIONS] <--onto <REVSETS>|--insert-after <REVSETS>|--insert-before <REVSETS>>

## Options

* -b, --branch <REVSETS>
  Rebase the whole branch relative to destination's ancestors (can be repeated)
  `jj rebase -b=br -o=dst` is equivalent to `jj rebase '-s=roots(dst..br)' -o=dst`.
  If none of `-b`, `-s`, or `-r` is provided, then the default is `-b @`.

* -s, --source <REVSETS>
  Rebase specified revision(s) together with their trees of descendants (can be repeated)
  Each specified revision will become a direct child of the destination revision(s), even if some of the source revisions are descendants of others.
  If none of `-b`, `-s`, or `-r` is provided, then the default is `-b @`.

* -r, --revision <REVSETS>
  Rebase the given revisions, rebasing descendants onto this revision's parent(s)
  Unlike `-s` or `-b`, you may `jj rebase -r` a revision `A` onto a descendant of `A`.
  If none of `-b`, `-s`, or `-r` is provided, then the default is `-b @`.

* -o, --onto <REVSETS>
  The revision(s) to rebase onto (can be repeated to create a merge commit)
  [aliases: -d]

* -A, --insert-after <REVSETS>
  The revision(s) to insert after (can be repeated to create a merge commit)
  [aliases: --after]

* -B, --insert-before <REVSETS>
  The revision(s) to insert before (can be repeated to create a merge commit)
  [aliases: --before]

* --skip-emptied
  If true, when rebasing would produce an empty commit, the commit is abandoned. It will not be abandoned if it was already empty before the rebase. Will never skip merge commits with multiple non-empty parents

* --keep-divergent
  Keep divergent commits while rebasing
  Without this flag, divergent commits are abandoned while rebasing if another commit with the same change ID is already present in the destination with identical changes.

* --simplify-parents
  Simplify parents of rebased commits, like `jj simplify-parents`, while rebasing them. Any parents that are ancestors of other parents will be removed

* -h, --help
  Print help (see a summary with '-h')
