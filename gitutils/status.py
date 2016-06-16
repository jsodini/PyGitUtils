# Copyright 2016 James Sodini
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

"""
Helper utilities to parse 'git status' command response.
"""

import re

import git

import gitutils.paths as paths


class GitStatus(object):

    GIT_STATUS_NEW_REGEX = re.compile('new file:\s*(.*?)\\n')
    GIT_MODIFIED_REGEX = re.compile('modified:\s*(.*?)\\n')
    GIT_UNTRACKED_REGEX = re.compile('^Untracked files:$')

    def __init__(self, path_to_git_repo=paths.path_to_git_repo()):
        """
        Git Status wrapper object constructor. If a path to git repo is not
        entered, it will search upwards from the current working directory.

        :param path_to_git_repo: Path to the project .git directory.
        """
        self._path_to_git_repo = path_to_git_repo

    @property
    def status(self):
        """
        Automatically discovers files as shown from the "git status" command.

        :return: String format representation of "git status".
        """
        git_repo = git.Repo(self._path_to_git_repo)
        return git_repo.git.status()

    @property
    def new_files(self):
        """
        Searches for all New Files via 'git status' in list format.

        :return: List of files found (empty list when nothing found).
        """
        return GitStatus.GIT_STATUS_NEW_REGEX.findall(self.status)

    @property
    def modified_files(self):
        """
        Searches for all Modified Files via 'git status' in list format.

        :return: List of files found (empty list when nothing found).
        """
        return GitStatus.GIT_MODIFIED_REGEX.findall(self.status)

    @property
    def untracked_files(self):
        """
        Searches for all Untracked Files via 'git status' in list format.

        :return: List of files found (empty list when nothing found).
        """
        untracked_files = []
        untracked_scope = False

        for line in self.status.split('\n'):
            if untracked_scope:
                line_data = line.split()
                if len(line_data) == 1:
                    untracked_files.append(line_data[0])
            else:
                # Only search when we've entered the right context of output.
                untracked_scope = GitStatus.GIT_UNTRACKED_REGEX.match(line)

        return untracked_files
