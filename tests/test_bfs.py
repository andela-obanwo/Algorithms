from testdata import graph
from unittest import TestCase
from bfs import bfs



class BFSTest(TestCase):
    def test_bfs_returns_all_vertices(self):
        expexted_result = sorted(graph.keys())
        bfs_result = bfs(graph, 'A')
        self.assertEqual(expexted_result, sorted(bfs_result))

    def test_bfs_returns_results_in_correct_order(self):
        start = 'A'
        expected_result = [start, 'B', 'C', 'G', 'F', 'D', 'E']
        bfs_result = bfs(graph, start)
        self.assertEqual(expected_result, bfs_result)

