#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dan Flettre
# Copyright (c) 2015 Dan Flettre
#
# License: MIT
#

"""This module exports the ModernStandard plugin class."""

from SublimeLinter.lint import NodeLinter


class Standard(NodeLinter):

    """Provides an interface to modern-standard."""

    syntax = ('javascript', 'html', 'javascriptnext', 'javascript 6to5', 'javascript (babel)')
    cmd = 'modern-standard --stdin --verbose'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.7.2'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    selectors = {
        'html': 'source.js.embedded.html'
    }
