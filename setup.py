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

from distutils.core import setup

setup(
    name='PyGitUtils',
    version='0.1',
    packages=['gitutils'],
    url='https://github.com/jsodini/PyGitUtils',
    license='Apache 2.0',
    author='James Sodini',
    author_email='james@sodini.io',
    description='Python Git Utility Library and Helper Scripts',
    setup_requires=['pytest-runner', 'fudge', 'gitpython'],
    tests_require=['pytest'],
    scripts=[
        'bin/git-add-all-files',
        'bin/git-add-all-tracked-files',
        'bin/git-add-modified-files',
        'bin/git-add-new-files',
        'bin/git-add-untracked-files',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux'
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities',
    ],
)
