## Usage

jj metaedit [OPTIONS] [REVSETS]...

## Arguments

* [REVSETS]...
  The revision(s) to modify (default: @) [aliases: -r]

## Options

* --update-change-id
  Generate a new change-id
  This generates a new change-id for the revision.

* -m, --message <MESSAGE>
  Update the change description
  This updates the change description, without opening the editor.
  Use `jj describe` if you want to use an editor.

* --update-author-timestamp
  Update the author timestamp
  This updates the author date to the current time, without modifying the author.

* --update-author
  Update the author to the configured user
  This updates the author name and email. The author timestamp is not modified – use --update-author-timestamp to update the author timestamp.
  You can use it in combination with the JJ_USER and JJ_EMAIL environment variables to set a different author:
  $ JJ_USER='Foo Bar' JJ_EMAIL=foo@bar.com jj metaedit --update-author

* --author <AUTHOR>
  Set author to the provided string
  This changes author name and email while retaining author timestamp for non-discardable commits.
  ```shell $ jj metaedit --author "Foo Bar <foo@bar.com>" ```

* --author-timestamp <AUTHOR_TIMESTAMP>
  Set the author date to the given date
  The date can either be human readable ([RFC2822], eg 'Sun, 23 Jan 2000 01:23:45 PST') or a time stamp ([RFC3339], eg '2000-01-23T01:23:45-08:00').
  [RFC2822]: https://datatracker.ietf.org/doc/html/rfc2822
  [RFC3339]: https://datatracker.ietf.org/doc/html/rfc3339

* --force-rewrite
  Rewrite the commit, even if no other metadata changed
  This updates the committer timestamp to the current time, as well as the committer name and email.
  Even if this option is not passed, the committer name, email, and timestamp will be updated if other metadata is updated. This option just forces every commit to be rewritten whether or not there are other changes.
  You can use it in combination with the `JJ_USER` and `JJ_EMAIL` environment variables to set a different committer:
  $ JJ_USER='Foo Bar' JJ_EMAIL=foo@bar.com jj metaedit --force-rewrite

* -h, --help
  Print help (see a summary with '-h')
