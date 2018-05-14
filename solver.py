"""
This module solves the solution to a recursive maze puzzle.
"""
import queue

"""
Holds a list of connections between search states in the puzzle.
Each inner list contains a group of nodes that are all pairwise connected
in the maze (defined according to the PuzzleState class).
"""
CONNECTIONS = [
    [('E', 1), ('E', 15), ('E', 16), ('A', 1)],
    [('E', 2), ('A', 4)],
    [('E', 3), ('A', 5), ('C', 1), ('B', 7), ('E', 12)],
    [('E', 4), ('B', 1)],
    [('E', 5), ('B', 4)],
    [('E', 6), ('B', 8)],
    [('E', 7), ('A', 3), ('C', 6)],
    [('E', 8), ('E', 10), ('E', 13), ('A', 11)],
    [('E', 9), ('B', 3)],
    [('E', 11), ('E', 14), ('A', 14)],
    [('A', 8), ('B', 16)],
    [('A', 9), ('C', 13)],
    [('A', 16), ('A', 10)],
    [('B', 11), ('C', 4)],
    [('B', 14), ('C', 15)],
    [('C', 7), ('C', 8)]
]


class PuzzleState(object):
    """
    Represents a state of the maze puzzle.

    Describes a location of the puzzle in terms of a node, and
    how many smaller copies of the maze that have been recursed into.

    Attributes:
        layer_list: a list of layers (either 'A', 'B', 'C') indicating what
            order the puzzle has recursed into smaller copies of itself.
            An empty list represents the outermost layer.
        node: the point location within the current layer of the puzzle.
            This is a tuple containing two elements: the first is the general
            vicinity (the outside edge 'E', or outside of box 'A', 'B', or
            'C'), and the specific node in that area (an integer from 1-16).
    """

    def __init__(self, layer_list=None, node=0):
        """Inits PuzzleState with a layer list and node."""
        if layer_list is None:
            self.layer_list = []
        else:
            self.layer_list = layer_list
        self.node = node

    def get_neighbors(self):
        """
        Generates a list of neighboring PuzzleState instances.

        A PuzzleState instance is a neighbor if it is one direct move away,
        which is either moving between two nodes on the same layer
        connected by a line, or switching between layers by adding or removing
        a layer from the layer_list and changing the node appropriately.
        """
        return []

    def __repr__(self):
        return 'PuzzleState({}, {})'.format(repr(self.layer_list),
                                            repr(self.node))


def breadth_first_search(init_state, goal_state):
    """
    Performs a BFS for a given start and goal state.

    This BFS begins with the init_state and ends when it reaches a state
    equal to the goal_state. It relies on states being hashable to check if
    they have been explored or not, and for states to have a get_neighbors()
    method for generating their incident states.
    """
    node = init_state
    if node == goal_state:
        return node
    frontier = queue.Queue()
    frontier.put(node)
    explored = set()
    while not frontier.empty():
        node = frontier.get()
        explored.add(node)
        for neighbor in node.get_neighbors():
            if neighbor not in explored:
                if neighbor == goal_state:
                    return neighbor
                frontier.put(neighbor)
    return None


def main():
    """
    Calculates the solution of the puzzle.
    """
    start = PuzzleState([], ('C', 10))
    goal = PuzzleState([], ('A', 12))

    # print(breadth_first_search(start, goal))

if __name__ == '__main__':
    main()
