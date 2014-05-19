#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Common functionality for file watchers."""

import os


# Directories that we should not watch at all.
_IGNORED_DIRS = ('.git', '.hg', '.svn')

# File prefixes that should be ignored.
_IGNORED_FILE_PREFIXES = (
  # Emacs
  '.#',
)

# File suffixes that should be ignored.
_IGNORED_FILE_SUFFIXES = (
    # Python temporaries
    '.pyc',
    '.pyo',
    # Backups
    '~',
    # Emacs
    '#',
    # Vim
    '.swp',
    '.swo',
)


def ignore_file(filename):
  """Report whether a file should not be watched."""
  basename = os.path.basename(filename)
  return (
    any(basename.startswith(prefix) for prefix in _IGNORED_FILE_PREFIXES) or
    any(basename.endswith(suffix) for suffix in _IGNORED_FILE_SUFFIXES))


def ignore_dir(dirname):
  """Report whether a directory should not be watched."""
  while dirname:
    dirname, tail = os.path.split(dirname)
    if not tail:
      break
    if tail in _IGNORED_DIRS:
      return True
  return False


def remove_ignored_dirs(dirs):
  """Remove directories from dirs that should not be watched."""
  for d in _IGNORED_DIRS:
    if d in dirs:
      dirs.remove(d)
