from unittest import TestCase
from testdata import unsorted_list
from quicksort import quick_sort


class QuicksortTest(TestCase):
    def test_quicksort_returns_sorted_list(self):
        list_to_sort = list(unsorted_list)
        expected_result = sorted(list_to_sort)
        quick_sort(list_to_sort, 0, len(list_to_sort) - 1)
        self.assertEqual(list_to_sort, expected_result)
