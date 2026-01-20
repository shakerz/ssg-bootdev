import unittest

from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# This is my title"
        title = extract_title(md)
        self.assertEqual(title, "This is my title")

    def test_extract_real_title(self):
        md = (
            "## This is not the real title\n"
            "# This is the real title"
        )


        title = extract_title(md)
        self.assertEqual(title, "This is the real title")

    def test_extract_no_real_title(self):
        md = (
            "## This is not a real title"
        )
        with self.assertRaises(Exception):
            extract_title(md)






if __name__ == "__main__":
    unittest.main()