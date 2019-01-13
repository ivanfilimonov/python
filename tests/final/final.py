import os
from unittest import TestCase

import main.final_task.final


class Final(TestCase):

    def test_final(self):
        # link = "https://imdb.com/chart/top"
        try:
            main.final_task.final.run_full_console_scenario()
            self.assertTrue(os.path.exists("log.log"))
        finally:
            os.remove("log.log")
