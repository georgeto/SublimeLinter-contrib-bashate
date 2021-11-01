#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ben Stoutenburgh
# Copyright (c) 2016 Ben Stoutenburgh
#
# License: MIT
#

"""This module exports the Bashate plugin class."""

from SublimeLinter.lint import Linter
import os


class Bashate(Linter):
    """Provides an interface to bashate."""

    cmd = 'bashate'
    defaults = {
        'selector': 'source.shell.bash',
        '--ignore=,': '',
        '--warn=,': '',
        '--error=,': ''
    }
    regex = (
        r'^.+:(?P<line>\d+):1: (?:(?P<error>E)|(?P<warning>W))(?P<code>\d{3}) (?P<message>.+)'
    )
    tempfile_suffix = 'sh'

    def tmpfile(self, cmd, code, suffix=''):
        """
        Run an external executable using a temp file to pass code and return its output.

        We override this to have the tmpfile extension match what is being
        linted so E005 is valid.
        """

        filename, extension = os.path.splitext(self.filename)
        extension = '.missingextension' if not extension else extension
        return super().tmpfile(cmd, code, extension)
