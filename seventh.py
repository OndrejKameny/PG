from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            new_pos = (row + 1, col)
        else:
            new_pos = (row - 1, col)

        if self.is_position_on_board(new_pos):
            return [new_pos]
        return[]
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc

        return moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'

class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc

        return moves
    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'



class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc

        return moves
    
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'



class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)

        return moves
    
    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Queen("white", (4, 4))
    print(piece)
    print(piece.possible_moves())
