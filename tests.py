# tests.py

import unittest
from functions.get_files_info import get_files_info


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
    unittest.main()
