from .tree import Node

class KnightPathFinder:
    def __init__(self, start):
        self._root = Node(start)
        self._considered_positions = set(start)
        
    def get_valid_moves(self, pos):
        x, y = pos
        if x > 7 or x < 0 or y > 7 or y < 0:
           return "You have fallen off the board. Try Again!"

        knight-position = []
        knight-moves = (
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2))
       