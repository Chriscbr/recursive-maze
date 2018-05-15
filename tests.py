#pylint: disable=missing-docstring
import unittest
import solver

class TestMazeSolver(unittest.TestCase):
    def test_puzzle_state_eq(self):
        state1 = solver.PuzzleState([], ('C', 10))
        state2 = solver.PuzzleState([], ('C', 10))
        self.assertEqual(state1, state2)

        state1 = solver.PuzzleState([], ('B', 10))
        state2 = solver.PuzzleState([], ('E', 10))
        self.assertNotEqual(state1, state2)

        state1 = solver.PuzzleState(['B', 'C', 'A'], ('C', 10))
        state2 = solver.PuzzleState(['B', 'C', 'A'], ('C', 10))
        self.assertEqual(state1, state2)

        state1 = solver.PuzzleState(['B', 'C', 'B'], ('C', 10))
        state2 = solver.PuzzleState(['B', 'C', 'A'], ('C', 10))
        self.assertNotEqual(state1, state2)

    def test_puzzle_state_hash(self):
        state1 = solver.PuzzleState(['A', 'C', 'B'], ('C', 10))
        items = {state1}
        state2 = solver.PuzzleState(['A', 'C', 'B'], ('C', 10))
        self.assertIn(state2, items)

        state1 = solver.PuzzleState(['A', 'C', 'B'], ('C', 10))
        items = {state1}
        state2 = solver.PuzzleState(['B', 'A', 'C'], ('C', 10))
        self.assertNotIn(state2, items)

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

    def test_get_neighbors_intermediate(self):
        # neighbors must be compared with sets since they may contain
        # elements in a different order
        state = solver.PuzzleState(['C'], ('E', 10))
        neighbors = set([solver.PuzzleState(['C'], ('E', 8)),
                         solver.PuzzleState(['C'], ('E', 13)),
                         solver.PuzzleState(['C'], ('A', 11)),
                         solver.PuzzleState([], ('C', 10))])
        self.assertEqual(set(state.get_neighbors()), neighbors)

if __name__ == '__main__':
    unittest.main()
