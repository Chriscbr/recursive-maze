# pylint: disable=missing-docstring
import queue
from enum import Enum

"""
The direction a path follows (to enter a recursively deeper or shallower
copy/layer of the puzzle) is represented by a value of either
OUT, A, B, or C, where OUT is leaving the current layer outwards.
"""
class Direction(Enum):
    OUT = 0
    A = 1
    B = 2
    C = 3

    def __repr__(self):
        return str(self)

"""
Holds a list of connections between search states in the puzzle.
Each inner set contains a tuples of (gate, direction) pairs representing
state changes that can be traversed between.
Gates are numbered 1-16 clockwise starting at the top-left.
"""
CONNECTIONS = [
    [(1, Direction.OUT), (15, Direction.OUT),
     (16, Direction.OUT), (1, Direction.A)],
    [(2, Direction.OUT), (4, Direction.A)],
    [(3, Direction.OUT), (5, Direction.A),
     (1, Direction.C), (7, Direction.B), (12, Direction.OUT)],
    [(4, Direction.OUT), (1, Direction.B)],
    [(5, Direction.OUT), (4, Direction.B)],
    [(6, Direction.OUT), (8, Direction.B)],
    [(7, Direction.OUT), (3, Direction.A), (6, Direction.C)],
    [(8, Direction.OUT), (10, Direction.OUT),
     (13, Direction.OUT), (11, Direction.A)],
    [(9, Direction.OUT), (3, Direction.B)],
    [(11, Direction.OUT), (14, Direction.OUT), (14, Direction.A)],
    [(8, Direction.A), (16, Direction.B)],
    [(9, Direction.A), (13, Direction.C)],
    [(16, Direction.A), (10, Direction.A)],
    [(11, Direction.B), (4, Direction.C)],
    [(14, Direction.B), (15, Direction.C)],
    [(7, Direction.C), (8, Direction.C)]
]


class PuzzleState(object):

    def __init__(self, layer_list=None, gate=0):
        """
        layer_list is a list of "layers" the state has gone into

        gate is the current outward "connection" the state is in
        """
        if layer_list is None:
            self.layer_list = []
        else:
            self.layer_list = layer_list
        self.gate = gate

    def get_neighbors(self):
        curr_layer = self.layer_list[-1] if self.layer_list else None
        candidates = []
        for group in CONNECTIONS:
            match = False
            for gate, direction in group:
                if gate == self.gate and direction is curr_layer:
                    match = True
                if (gate == self.gate and direction is Direction.OUT and
                        self.layer_list):
                    match = True
            if match:
                candidates = candidates + group

        # remove candidates that crate self-loops
        self_states = [(self.gate, curr_layer), (self.gate, Direction.OUT)]
        candidates = list(set(candidates).difference(self_states))

        # final list of neighbors must be list of PuzzleStates
        def tuple_to_puzzle_state(tup):
            gate, direction = tup
            layer_list = self.layer_list
            if direction is Direction.OUT:
                layer_list = layer_list[:-1]
            else:
                layer_list = layer_list + [direction]
            return PuzzleState(layer_list, gate)
        neighbors = list(map(tuple_to_puzzle_state, candidates))
        return neighbors

    def __repr__(self):
        return 'PuzzleState({}, {})'.format(repr(self.layer_list),
                                            repr(self.gate))


def breadth_first_search(init_state, goal_state):
    node = init_state
    if node == goal_state:
        return node
    frontier = queue.Queue()
    frontier.put(node)
    explored = set()
    while not frontier.empty():
        # print('frontier:', frontier)
        # print('explored:', explored)
        node = frontier.get()
        explored.add(node)
        for neighbor in node.get_neighbors():
            if neighbor not in explored:
                if neighbor == goal_state:
                    return neighbor
                frontier.put(neighbor)
    return None


def main():
    start = PuzzleState(['+', Direction.C], 10)
    print(start.get_neighbors())
    # next_state = PuzzleState([Direction.OUT], 8)
    # print(next_state.get_neighbors())

    goal = PuzzleState(['-', Direction.A], 12)

    # print(breadth_first_search(start, goal))

if __name__ == '__main__':
    main()
