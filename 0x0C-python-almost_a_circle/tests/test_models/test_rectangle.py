import unittest
from models.rectangle import Rectangle


class RectangleTestSuite(unittest.TestCase):
    """Testing Rectangle subclass"""
    def setUp(self):
        """Initializing objects for test"""
        self.r0 = Rectangle(10, 2)
        self.r1 = Rectangle(2, 10)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(10, 2, 0, 0, -1)

    def test_a_init(self):
        """Test to return self.id from Rectangle"""
        self.assertEqual(self.r0, 1)
        self.assertEqual(self.r1, 2)
        self.assertEqual(self.r2, 12)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(3)
        self.assertEqual(self.r3, -1)

    def tearDown(self):
        """Cleaning up after myself"""
        del self.r0
        del self.r1
        del self.r2
        del self.r3

if __name__ == "__main__":
    unittest.main()
