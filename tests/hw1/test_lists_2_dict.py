import unittest

from main.hw1.lists_2_dict import lists_2_dict


class TestLists2Dict(unittest.TestCase):

    def test_lists_2_dict(self):
        self.assertEqual(lists_2_dict(["Name", "Age", "Job Title"], ["Jane", 44, "Python Developer"]),
                         {"Name": "Jane", "Age": 44, "Job Title": "Python Developer"})

        with self.assertRaises(TypeError, msg=""):
            lists_2_dict(["Name", "Age", {77.2, }], ["Jane", 44, "Python Developer"])


if __name__ == "__main__":
    unittest.main()