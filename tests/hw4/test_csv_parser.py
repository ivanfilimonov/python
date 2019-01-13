import os
from unittest import TestCase

from main.hw4.csv_parser import CsvParser


class TestCsvParser(TestCase):
    def setUp(self):
        self.csv_parser = CsvParser('1000 Sales Records')

    def test_save_as(self):
        file_name = "new_test_file"
        try:
            self.csv_parser.save_as(file_name, '\t')
            self.assertTrue(os.path.exists(self.csv_parser.get_file_path(file_name)))
        finally:
            os.remove(self.csv_parser.get_file_path(file_name))

    def test_sell_over(self):
        bf_greater = ['Brunei', 'Democratic Republic of the Congo', 'Germany', 'Guatemala', 'Guinea', 'Haiti', 'Iran',
                      'Japan', 'Kiribati', 'Lesotho', 'Luxembourg', 'Mali', 'Moldova ', 'Niger', 'Oman', 'Samoa ']
        self.assertEqual(self.csv_parser.sell_over("Baby Food", 8000), bf_greater)
        cosmetics = ['Belgium', 'Burundi', 'India', 'Iran', 'Maldives', 'Moldova ', 'Norway', 'Saint Lucia', 'Sweden',
                    'Turkey']
        self.assertEqual(self.csv_parser.sell_over('Cosmetics', 9000), cosmetics)

    def test_get_country_profit(self):
        self.assertEqual(self.csv_parser.get_country_profit("Nepal"), 1022269.6299999999)
        self.assertEqual(self.csv_parser.get_country_profit("Armenia"), 1827634.7)