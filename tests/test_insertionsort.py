from unittest import TestCase
from testdata import unsorted_list
from insertionsort import insertion_sort


class InsertionSortTest(TestCase):
    def test_insertionsort_returns_sorted_list(self):
        list_to_sort = list(unsorted_list)
        expected_result = sorted(list_to_sort)
        insertion_sort(list_to_sort)
        self.assertEqual(list_to_sort, expected_result)
