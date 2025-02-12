import unittest
from nameSorter import fullNameSort

class TestNameSorter(unittest.TestCase):

    def testNameSort(self):
        # Test with a list of names and surnames.
        namesList = [("Jason", "Derulo"), ("Undertaker", "Undertaker"), ("Naruto", "Uzumaki")]
        sortedList = fullNameSort(namesList)
        self.assertEqual(sortedList, [("Jason", "Derulo"), ("Naruto", "Uzumaki"), ("Undertaker", "Undertaker")])

    def testNameSortEmpty(self):
        # Test with an empty list.
        namesList = []
        sortedList = fullNameSort(namesList)
        self.assertEqual(sortedList, [])

    def testNameSortSingle(self):
        # Test with a list containing one name.
        namesList = [("Naruto", "Uzumaki")]
        sortedList = fullNameSort(namesList)
        self.assertEqual(sortedList, [("Naruto", "Uzumaki")])

    def testNameSortSorted(self):
        # Test with an already sorted list.
        namesList = [("Nathan", "Explosion"), ("Orihime", "Kurosaki"), ("Pablo", "Escobar")]
        sortedList = fullNameSort(namesList)
        self.assertEqual(sortedList, [("Nathan", "Explosion"), ("Orihime", "Kurosaki"), ("Pablo", "Escobar")])

    def testNameSortReversed(self):
        # Test with a list that is reverse sorted.
        namesList = [("Zlatan", "Ibrahimovic"), ("Yusuke", "Urameshi"), ("Wayne", "Rooney"), ("Walter", "White")]
        sortedList = fullNameSort(namesList)
        self.assertEqual(sortedList, [("Walter", "White"), ("Wayne", "Rooney"), ("Yusuke", "Urameshi"), ("Zlatan", "Ibrahimovic")])

if __name__ == '__main__':
    unittest.main()
