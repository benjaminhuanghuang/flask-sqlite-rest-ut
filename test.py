import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from tests.app.test import AppTest


if __name__ == '__main__':
    unittest.main()