# -*- coding: utf-8 -*-

"""
direct Python Toolbox
All-in-one toolbox to encapsulate Python runtime variants
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?dpt;settings

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
unittest
"""

from os import path
import unittest

from dpt_settings import Settings

class TestSettings(unittest.TestCase):
    """
Unittest for Settings

:since: v1.0.0
    """

    def test_paths(self):
        """
Tests the calculated paths.
        """

        settings = Settings()

        self.assertTrue(settings.get("path_system")
                        == path.sep.join(path.abspath(__file__).split(path.sep)[:-2] + [ "src" ])
                       )
    #
#

if (__name__ == "__main__"):
    unittest.main()
#
