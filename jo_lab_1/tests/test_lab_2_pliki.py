import unittest
from unittest.mock import patch

import lab_2_pliki


class TestLab2(unittest.TestCase):

    @patch('lab_2_pliki.get_name', return_value='Mike')
    def test_add_name(self, input):
        self.assertEqual(lab_2_pliki.get_name(), 'Mike')

    @patch('lab_2_pliki.get_name', return_value='Mike')
    def test_add_one_line(self, input):
        lines = lab_2_pliki.get_lines_count()
        lab_2_pliki.guest_book()
        self.assertEqual(lab_2_pliki.get_lines_count(), lines + 1)

    @patch('lab_2_pliki.get_name', return_value='Mike')
    def test_is_Hello_Mike_in_last_line(self, input):
        line = lab_2_pliki.get_last_line()
        self.assertTrue("Hello Mike" in line)
