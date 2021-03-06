# Copyright (C) 2014 Brian J. Stucky
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# To use this to compile the calign module, from the folder containing this file, run
# the following distutils command.
#
#     python setup.py build_ext --inplace
#

from distutils.core import setup
from distutils.extension import Extension

setup(
    name='calign',
    author='Brian J. Stucky',
    license='GNU General Public License (GPL) version 3',
    ext_modules = [
        Extension('calign', ['calign.c'])
        ]
)

