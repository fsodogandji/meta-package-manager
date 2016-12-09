# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Kevin Deldycke <kevin@deldycke.com>
#                    and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import unittest
from subprocess import PIPE, Popen

from meta_package_manager import bitbar


class TestBitBarPlugin(unittest.TestCase):

    def test_simple_call(self):
        process = Popen([bitbar.__file__], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        print(output)
        print(error)
        self.assertEqual(process.returncode, 0)
        self.assertFalse(error)
        self.assertIn(" | dropdown=false\n---\n", output.decode('utf-8'))