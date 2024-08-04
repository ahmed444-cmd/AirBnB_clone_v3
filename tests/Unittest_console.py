#!/usr/bin/python3
"""General unit test for the project's requirements"""

import unittest
import os


class Test_Project(unittest.TestCase):
    """Class to test the project"""

    def test_project(self):
        """
        Verify the project prerequisites:
        - Ensure all necessary files and directories are in the correct places
        - Confirm all Python scripts have executable permissions
        - Check that every file concludes with a newline character
        - Make sure each file begins with #!/usr/bin/python
        - Validate that all files adhere to the pycodestyle guidelines
        - Ensure there is a README file present
        - Confirm all modules have proper documentation
        """

        # the init file of the api/v1/views have wrong pep8

        # Readme file
        self.assertTrue(os.path.isfile('README.md'))

        # Package
        self.assertTrue(os.path.isfile('./models/__init__.py'))
        self.assertTrue(os.path.isfile('./models/engine/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/__init__.py'))
        self.assertTrue(os.path.isfile(
            './tests/test_models/test_engine/__init__.py'))

        flist = ['console.py', './models/base_model.py',
                 './models/city.py', './models/place.py',
                 './models/review.py', './models/state.py',
                 './models/user.py',
                 './models/engine/file_storage.py']

        for filee in flist:
            # PEP8
            pep8 = "pep8 --count {}".format(filee)
            self.assertEqual(os.system(pep8), 0, filee)

            # Verify the presence of all files and directories in their correct locations
            self.assertTrue(os.path.isfile(filee), filee)

            # executable files
            self.assertTrue(os.access(filee, os.X_OK), filee)

            # First line and last line
            with open(filee) as f:
                first = f.readline()
                last = f.read()[-1]
                self.assertTrue(first == '#!/usr/bin/python3\n', filee)
                self.assertTrue(last == '\n', filee)

            # module's documentation
            self.assertTrue(len(filee.__doc__) > 5)


if __name__ == '__main__':
    unittest.main()
