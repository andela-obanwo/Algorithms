from testdata import graph
from unittest import TestCase
from dfs import dfs



class DFSTest(TestCase):
    def test_dfs_returns_all_vertices(self):
        expexted_result = sorted(graph.keys())
        dfs_result = dfs(graph, 'A')
        self.assertEqual(expexted_result, sorted(dfs_result))

    def test_dfs_returns_results_in_correct_order(self):
        start = 'A'
        expected_result = [start, 'F', 'G', 'C', 'E', 'B', 'D']
        dfs_result = dfs(graph, start)
        self.assertEqual(expected_result, dfs_result)

