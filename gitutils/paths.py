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
Helper utilities to determine Git root.
"""

import os.path


def path_to_git_repo(start_path=os.path.abspath('.')):
    """
    Searches from the current working directory all the way to root
    recursively for the '.git' repo.

    :param start_path: Optional starting path (CWD by default)
    :return: Full path to '.git' or EnvironmentError exception
    """
    if start_path == '/':
        raise EnvironmentError('No git repo found')

    git_repo_path = os.path.join(start_path, '.git')

    if os.path.exists(git_repo_path):
        return git_repo_path

    parent_path = os.path.normpath(os.path.join(start_path, '..'))

    return path_to_git_repo(parent_path)


def path_to_git_root(full_path_to_git_repo):
    """
    Strips the path of '.git' at the end.

    :param full_path_to_git_repo: Full path to git repo.
    :return: Full path to git root.
    """
    if not full_path_to_git_repo.endswith('.git'):
        raise EnvironmentError('No git repo found')

    return os.path.normpath(os.path.join(full_path_to_git_repo, '..'))
