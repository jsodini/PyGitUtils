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

import gitutils.paths as paths


class PathsTest(unittest.TestCase):

    def test_path_to_git_repo_throws_when_no_git_found(self):
        self.assertRaises(EnvironmentError, paths.path_to_git_repo, '/')

    @fudge.patch('os.path.exists')
    def test_path_to_git_repo_returns_path_when_found(self, mock_exists):
        mock_exists.expects_call().with_args('/wat/.git').returns(True)
        git_path = paths.path_to_git_repo('/wat')
        self.assertEqual('/wat/.git', git_path)

    @fudge.patch('os.path.exists')
    def test_path_to_git_repo_searches_recursively(self, mock_exists):
        mock_exists.expects_call().returns(False).next_call().returns(True)
        git_path = paths.path_to_git_repo('/wat/foo')
        self.assertEqual('/wat/.git', git_path)

    def test_path_to_git_root_throws_when_no_git_found(self):
        self.assertRaises(EnvironmentError, paths.path_to_git_root, '/wat')

    def test_path_to_git_root_strips_git_when_found(self):
        self.assertEqual('/wat', paths.path_to_git_root('/wat/.git'))
