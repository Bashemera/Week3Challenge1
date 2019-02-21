import unittest
from list_sort import sort_list


class listsortTest(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(sort_list(5), 'Invalid Input')

if __name__ == '__main__':
    unittest.main()
