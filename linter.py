#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ben Stoutenburgh
# Copyright (c) 2015 Ben Stoutenburgh
#
# License: MIT
#

"""This module exports the Bashate plugin class."""

from SublimeLinter.lint import Linter, util


class Bashate(Linter):

    """Provides an interface to bashate."""

    syntax = 'shell-unix-generic'
    cmd = 'bashate'
    regex = (
        r'^(?:(?P<error>[E])|(?P<warning>[W]))\d+: '
        r'(?P<message>.+): \'(?P<near>.+)\'\n - '
        r'(?P<file>.+) : L(?P<line>\d+)'
    )
    multiline = True
    tempfile_suffix = '-'
    check_version = False
