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

import unittest

import fudge

import gitutils.status


TEST_POSITIVE_STATUS = (
    "On branch master\n"
    "Your branch is up-to-date with \'origin/master\'.\n"
    "Changes to be committed:\n"
    "  (use \"git reset HEAD <file>...\" to unstage)\n"
    "\n"
    "\tnew file:   new_file_one\n"
    "\tnew file:   new_file_two\n"
    "\n"
    "Changes not staged for commit:\n"
    "  (use \"git add <file>...\" to update what will be committed)\n"
    "  (use \"git checkout -- <file>...\" to discard "
        "changes in working directory)\n"
    "\n"
    "\tmodified:   modified_file_one\n"
    "\tmodified:   modified_file_two\n"
    "\n"
    "Untracked files:\n"
    "  (use \"git add <file>...\" to include in what will be committed)\n"
    "\n"
    "\tuntracked_file_one\n"
    "\tuntracked_file_two\n"
)

TEST_NEGATIVE_STATUS = (
    "On branch master\n"
    "Your branch is up-to-date with 'origin/master'.\n"
    "nothing to commit, working directory clean\n"
)


class PathsDataTest(gitutils.status.GitStatus):
    """
    Same as GitStatus object with an overridden data source. Easiest way
    to test while preserving @property decorator for lazy evaluation
    attributes.
    """

    def __init__(self, git_status_data, full_path=False):
        gitutils.status.GitStatus.__init__(self, '/wat', full_path)
        self._git_status_data = git_status_data

    @property
    def status(self):
        return self._git_status_data


class PathsTest(unittest.TestCase):

    def test_new_files_found_when_present(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS)
        self.assertEqual(["new_file_one", "new_file_two"],
                         git_status.new_files)

    def test_new_files_found_when_full_path(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS, True)
        self.assertEqual(["/wat/new_file_one", "/wat/new_file_two"],
                         git_status.new_files)

    def test_new_files_empty_when_not_present(self):
        git_status = PathsDataTest(TEST_NEGATIVE_STATUS)
        self.assertFalse(git_status.new_files)

    def test_modified_files_found_when_present(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS)
        self.assertEqual(["modified_file_one", "modified_file_two"],
                         git_status.modified_files)

    def test_modified_files_found_when_full_path(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS, True)
        self.assertEqual(["/wat/modified_file_one", "/wat/modified_file_two"],
                         git_status.modified_files)

    def test_modified_files_empty_when_not_present(self):
        git_status = PathsDataTest(TEST_NEGATIVE_STATUS)
        self.assertFalse(git_status.modified_files)

    def test_untracked_files_found_when_present(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS)
        self.assertEqual(["untracked_file_one", "untracked_file_two"],
                         git_status.untracked_files)

    def test_untracked_files_found_when_full_path(self):
        git_status = PathsDataTest(TEST_POSITIVE_STATUS, True)
        self.assertEqual(["/wat/untracked_file_one",
                          "/wat/untracked_file_two"],
                         git_status.untracked_files)

    def test_untracked_files_empty_when_not_present(self):
        git_status = PathsDataTest(TEST_NEGATIVE_STATUS)
        self.assertFalse(git_status.untracked_files)
