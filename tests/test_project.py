#!/usr/bin/python3
"""Unit test for overall project requirements."""

import unittest
import os


class Test_Project(unittest.TestCase):
    """Testing class for the project."""

    def test_project(self):
        """Check the project requirements:"""

        # The __init__.py file in api/v1/views doesn't follow PEP 8 guidelines

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

            # Check the presence & positioning of all files and directories.
            self.assertTrue(os.path.isfile(filee), filee)

            # files are exec
            self.assertTrue(os.access(filee, os.X_OK), filee)

            # 1st and last line
            with open(filee) as f:
                first = f.readline()
                last = f.read()[-1]
                self.assertTrue(first == '#!/usr/bin/python3\n', filee)
                self.assertTrue(last == '\n', filee)

            # doc of module
            self.assertTrue(len(filee.__doc__) > 5)


if __name__ == '__main__':
    unittest.main()
