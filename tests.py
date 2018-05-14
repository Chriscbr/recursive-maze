#pylint: disable=missing-docstring
import unittest
import solver

class TestMazeSolver(unittest.TestCase):
    def test_get_neighbors_simple(self):
        # These states are only connected to the plus and minus in the
        # original puzzle, but we don't have representations for those,
        # so the only option should be to recurse into the C and A
        # boxes respectively.
        state = solver.PuzzleState([], ('C', 10))
        neighbors = [solver.PuzzleState(['C'], ('E', 10))]
        self.assertEqual(state.get_neighbors(), neighbors)

        state = solver.PuzzleState([], ('A', 12))
        neighbors = [solver.PuzzleState(['A'], ('E', 12))]
        self.assertEqual(state.get_neighbors(), neighbors)

if __name__ == '__main__':
    unittest.main()
