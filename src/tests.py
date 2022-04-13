import unittest

import prepare
import backup

class TestBackup(unittest.TestCase):
    _backup = backup("../tests/test_target/", "../tests/test_source/")
    def test_archive(self):
        self.assertEqual()
