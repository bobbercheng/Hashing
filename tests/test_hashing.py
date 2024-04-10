import unittest
from hashing import Hashing

class TestHashing(unittest.TestCase):
    def test_sha256(self):
        self.assertEqual(
            Hashing.sha256_int("Hello, World!"),
            560004575
        )

if __name__ == '__main__':
    unittest.main()