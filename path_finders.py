from tree import Node

class KnightPathFinder:
    def __init__(self, start):
        self._root = Node(start)
        self._considered_positions = set(start)
        
    def get_valid_moves(self, pos):
        x, y = pos
        if x > 7 or x < 0 or y > 7 or y < 0:
           return "You have fallen off the board. Try Again!"

        # position = []
        moves = (
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2))
        
        for move in moves:
            x, y = pos
            # print(x, y)
            mX, mY = move
            newXPostion = x + mX
            newYPostion = y + mY

            if newXPostion > 7 or newXPostion < 0:
                pass

            elif newYPostion > 7 or newYPostion < 0:
                pass

            else:
                self._considered_positions.add((newXPostion, newYPostion))
        
        return self._considered_positions


    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        return valid_moves


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0))) 