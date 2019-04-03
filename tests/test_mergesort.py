from unittest import TestCase
from testdata import unsorted_list
from mergesort import merge_sort


class MergesortTest(TestCase):
    def test_mergesort_returns_sorted_list(self):
        list_to_sort = list(unsorted_list)
        expected_result = sorted(list_to_sort)
        merge_sort(list_to_sort)
        self.assertEqual(list_to_sort, expected_result)
