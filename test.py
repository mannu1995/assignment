import unittest
from dict2 import Dict2

class TestDict2(unittest.TestCase):
    def test_storing_key_value_pairs(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)

    def test_accessing_values(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        self.assertEqual(obj['a'], 1)

    def test_custom_exception(self):
        obj = Dict2()
        with self.assertRaises(KeyError):
            val = obj['a']

    def test_iteration(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        keys = [k for k in obj]
        self.assertEqual(keys, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()