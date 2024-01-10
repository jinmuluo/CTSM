#!/usr/bin/env python3
"""
Unit tests for NeonSite

You can run this by:
    python -m unittest test_unit_NeonSite.py
"""

import unittest
import tempfile
import shutil
import os
import sys

# -- add python/ctsm  to path (needed if we want to run the test stand-alone)
_CTSM_PYTHON = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir)
sys.path.insert(1, _CTSM_PYTHON)

# pylint: disable=wrong-import-position
from ctsm import unit_testing
from ctsm.site_and_regional.NeonSite import FUNCTION_NAME

# pylint: disable=invalid-name


class TestNeonSite(unittest.TestCase):
    """
    Basic class for testing NeonSite.py.
    """

    def setUp(self):
        """
        Make /_tempdir for use by these tests.
        """
        self._tempdir = tempfile.mkdtemp()

    def tearDown(self):
        """
        Remove temporary directory
        """
        shutil.rmtree(self._tempdir, ignore_errors=True)

    def test_function(self):
        """
        Test that NeonSite class is working properly...
        """
        #valid_neon_sites = ["ABBY", "BART"]
        #previous_dir = os.getcwd()
        #os.chdir(self._tempdir)  # cd to tempdir
        #available_list = check_neon_listing(valid_neon_sites)
        #self.assertEqual(
        #    available_list[0].name, "ABBY", "available list of actual sites not as expected"
        #)
        #self.assertEqual(
        #    available_list[1].name, "BART", "available list of actual sites not as expected"
        #)
        # change to previous dir once listing.csv file is created in tempdir and test complete
        #os.chdir(previous_dir)
        continue


if __name__ == "__main__":
    unit_testing.setup_for_tests()
    unittest.main()
