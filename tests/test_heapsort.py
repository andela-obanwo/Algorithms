from unittest import TestCase
from testdata import unsorted_list
from heapsort import heap_sort


class HeapsortTest(TestCase):
    def test_heapsort_returns_sorted_list(self):
        list_to_sort = list(unsorted_list)
        expected_result = sorted(list_to_sort)
        heap_sort(list_to_sort, len(list_to_sort))
        self.assertEqual(list_to_sort, expected_result)
