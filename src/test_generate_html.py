import unittest
from generate_html import (
    extract_title,
)


class TestGenerateHTML(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        expected = "Hello"
        result = extract_title(markdown)
        self.assertEqual(result, expected)

    def test_extract_title_no_h1(self):
        with self.assertRaises(ValueError) as context:
            extract_title("## Hello")
        self.assertEqual(context.exception.args[0], "Invalid markdown: no h1 found")


if __name__ == "__main__":
    unittest.main()
