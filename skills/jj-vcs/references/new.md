Usage: jj new [OPTIONS] [REVSETS]...

Arguments:
  [REVSETS]...
          Parent(s) of the new change [default: @] [aliases: -o, -r]

Options:
  -m, --message <MESSAGE>
          The change description to use

      --no-edit
          Do not edit the newly created change

  -A, --insert-after <REVSETS>
          Insert the new change after the given commit(s)
          
          Example: `jj new --insert-after A` creates a new change between `A` and
          its children:
          
          ```text
                          B   C
                           \ /
              B   C   =>    @
               \ /          |
                A           A
          ```
          
          Specifying `--insert-after` multiple times will relocate all children of
          the given commits.
          
          Example: `jj new --insert-after A --insert-after X` creates a change
          with `A` and `X` as parents, and rebases all children on top of the new
          change:
          
          ```text
                          B   Y
                           \ /
              B  Y    =>    @
              |  |         / \
              A  X        A   X
          ```
          
          [aliases: --after]

  -B, --insert-before <REVSETS>
          Insert the new change before the given commit(s)
          
          Example: `jj new --insert-before C` creates a new change between `C` and
          its parents:
          
          ```text
                             C
                             |
                C     =>     @
               / \          / \
              A   B        A   B
          ```
          
          `--insert-after` and `--insert-before` can be combined.
          
          Example: `jj new --insert-after A --insert-before D`:
          
          ```text
          
              D            D
              |           / \
              C          |   C
              |    =>    @   |
              B          |   B
              |           \ /
              A            A
          ```
          
          Similar to `--insert-after`, you can specify `--insert-before` multiple
          times.
          
          [aliases: --before]

  -h, --help
          Print help (see a summary with '-h')
