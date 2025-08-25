# tests.py

import unittest
from functions.get_files_info import get_files_info, get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_calculator_main(self):
        result = get_file_content("calculator", "main.py")
        print(f"\n{result}")
        self.assertTrue(result.startswith("# main.py"))

    def test_calculator_pkg_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(f"\n{result}")
        self.assertTrue(result.startswith("# calculator.py"))

    def test_not_a_regular_file(self):
        result = get_file_content("calculator", "pkg")
        print(f"\n{result}")
        self.assertEqual(result, ''f'Error: File not found or is not a regular file: "pkg"')

    def test_doesnt_exist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"\n{result}")
        self.assertEqual(result, ''f'Error: File not found or is not a regular file: "pkg/does_not_exist.py"')

    def test_outside_working_dir(self):
        result = get_file_content("calculator", "/bin/cat")
        print(f"\n{result}")
        self.assertEqual(result, 'Error: Cannot list "/bin/cat" as it is outside the permitted working directory')

    def test_more_than_10k_characters(self):
        result = get_file_content("calculator", "lorem.txt")
        print(f"\n{result}")
        self.assertTrue(result.startswith("Lorem ipsum dolor sit amet,"))
        self.assertTrue(result.endswith("characters]"))


class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_files(self):
        result = get_files_info("calculator", ".")
        print(f"\n{result}")
        self.assertEqual(result,
            " - main.py: file_size=576 bytes, is_dir=False\n" +
            " - pkg: file_size=160 bytes, is_dir=True\n" +
            " - tests.py: file_size=1343 bytes, is_dir=False")

    def test_calculator_pkg_files(self):
        result = get_files_info("calculator", "pkg")
        print(f"\n{result}")
        self.assertEqual(result,
            " - __pycache__: file_size=128 bytes, is_dir=True\n" +
            " - calculator.py: file_size=1738 bytes, is_dir=False\n" +
            " - render.py: file_size=767 bytes, is_dir=False")

    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        print(f"\n{result}")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_calculator_parent_directory(self):
        result = get_files_info("calculator", "../")
        print(f"\n{result}")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

    def test_not_a_directory(self):
        result = get_files_info("calculator", "doesnt_exist")
        print(f"\n{result}")
        self.assertEqual(result, ''f'Error: "doesnt_exist" is not a directory')


if __name__ == "__main__":
    unittest.main(defaultTest="TestGetFileContent")
