import pygame
import time
import random

class PentominoSolver:
    # x - liczba kolumn
    # y - liczba wierszy
    # randomize - czy losować początkową kolejność klocków 

    # x * y musi być podzielne przez 5
    def __init__(self, x, y, randomize=False):
        self.board_width = x
        self.board_height = y

        if x * y % 5 != 0:
            raise ValueError("x * y must be divisible by 5")

        # reprezentacją planszy jest macierz x na y, gdzie 0 oznacza puste pole, a liczba większa od 0 oznacza konkretny klocek
        self.board = [[0] * x for _ in range(y)]
        self.pieces = self.get_pentomino_pieces()
        self.randomize = randomize 

        # zmienne dla pygame z pozycjami i kolorami
        pygame.init()
        self.cell_size = 40
        self.window_size = (900, 700)
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.colors = self.generate_unique_colors(len(self.pieces))
        self.board_x = (self.window_size[0] - self.board_width * self.cell_size) // 2
        self.board_y = 20
        self.shapes_list_y = self.board_y + self.board_height * self.cell_size + 120

        # lista śledząca, które klocki zostały już umieszczone na planszy
        self.placed_pieces = set() 

    def get_pentomino_pieces(self):
        pieces = {
            "F": [[(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)]],
            "I": [[(0, i) for i in range(5)]],
            "L": [[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]],
            "N": [[(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]],
            "P": [[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]],
            "T": [[(0, i) for i in range(3)] + [(1, 1)] + [(2, 1)]],
            "U": [[(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]],
            "V": [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]],
            "W": [[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]],
            "X": [[(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]],
            "Y": [[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]],
            "Z": [[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]]
        }
        # dla każdego klocka generujemy wszystkie możliwe rotacje
        return {k: self.get_rotations(v) for k, v in pieces.items()}

    def get_rotations(self, shapes):
        rotations = set()
        # każdy klocek obracamy 4 razy o 90 stopni, a następnie symetrycznie względem osi x i y
        # dopuszczamy obracanie wokół osi x i y, ponieważ klocki nie są symetryczne
        # dla ułatwienia zadania
        for shape in shapes:
            for _ in range(4):
                shape = [(y, -x) for x, y in shape]
                rotations.add(tuple(sorted(shape)))
                shape = [(x, -y) for x, y in shape]
                rotations.add(tuple(sorted(shape)))
        return [list(r) for r in rotations]

    def generate_unique_colors(self, num_colors):
        # generujemy num_colors kolorów, które będą używane do rysowania klocków
        return [pygame.Color(i * 20 % 255, (i * 70) % 255, (i * 150) % 255) for i in range(1, num_colors + 1)]

    # funkcja sprawdzająca, czy klocek może zostać umieszczony na planszy
    # do postawienia klocków zdefiniowałem parę warunków poprawiających wydajność algorytmu:
    # - pierwszy klocek musi dotykać ściany planszy
    # - każdy kolejny klocek musi być przylegający do innego klocka (ograniczmamy liczbę bezużytecznych kombinacji)
    # - klocki nie mogą się nakładać na siebie
    # - klocki nie mogą wychodzić poza planszę
    def can_place(self, shape, x, y):
        is_first_piece = all(all(cell == 0 for cell in row) for row in self.board)
        adjacent_found = False # zmienna sprawdzadjąca, czy klocek przylega do innego klocka
        touches_wall = False # zmienna sprawdzająca, czy klocek dotyka ściany planszy

        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            # sprawdzamy, czy klocek wychodzi poza planszę, czy koliduje z innym klockiem
            if nx < 0 or ny < 0 or nx >= self.board_width or ny >= self.board_height or self.board[ny][nx] != 0:
                return False
            # sprawdzamy, czy klocek dotyka ściany planszy (dla pierwszego klocka)
            if nx == 0 or ny == 0 or nx == self.board_width - 1 or ny == self.board_height - 1:
                touches_wall = True
            # sprawdzamy, czy klocek przylega do innego klocka (dla kolejnych klocków)
            if not is_first_piece and self.is_adjacent(nx, ny):
                adjacent_found = True

        if is_first_piece:
            return touches_wall
        return adjacent_found

    # funkcja umieszczająca klocek na planszy
    # podmienia 0 na jedynki w miejscach, gdzie znajduje się klocek
    # rysuje nową planszę
    def place(self, shape, x, y, piece_id):
        for dx, dy in shape:
            self.board[y + dy][x + dx] = piece_id
        self.placed_pieces.add(piece_id) 
        self.draw_board()
        pygame.display.update()
        time.sleep(0.01)

    # funkcja usuwająca klocek z planszy
    # podmienia "id klocka" na zera w miejscach, gdzie się znajdował
    def remove(self, shape, x, y, piece_id):
        for dx, dy in shape:
            self.board[y + dy][x + dx] = 0
        self.placed_pieces.remove(piece_id)

    # funkcja sprawdzająca, czy na planszy są niezapełnione luki
    # w takich przypadkach algorytm nie będzie mógł znaleźć rozwiązania, więc
    # aby zaoszczędzić czas, sprawdzamy to wcześniej i ograniczamy liczbę kombinacji
    # funkcja szuka, czy istnieje puzzel, który może zapełnić lukę
    def has_unfillable_gaps(self, pieces):
        visited = [[False] * self.board_width for _ in range(self.board_height)]

        def dfs(x, y):
            stack = [(x, y)]
            cells = []
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < self.board_width and 0 <= cy < self.board_height and not visited[cy][cx] and self.board[cy][cx] == 0:
                    visited[cy][cx] = True
                    cells.append((cx, cy))
                    stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])
            return cells

        for y in range(self.board_height):
            for x in range(self.board_width):
                if self.board[y][x] == 0 and not visited[y][x]:
                    gap = dfs(x, y)
                    if not self.can_fill_gap_with_pieces(gap, pieces):
                        return True
        return False

    # funkcja sprawdzająca, czy możliwe jest umieszczenie klocka
    # funkcja podobna do can_place, ale ignoruje część zdefiniowanych warunków
    def can_fill_gap_with_pieces(self, gap, pieces):
        for piece_id, shapes in pieces:
            for shape in shapes:
                for gx, gy in gap:
                    if all((gx + dx, gy + dy) in gap for dx, dy in shape):
                        return True
        return False

    # funkcja rysująca planszę
    # idzie po wszystkich komórkach macierzy i rysuje odpowiedni kwadraty z siatką
    # rysuje również klocki, które można umieścić na planszy
    def draw_board(self):
        self.screen.fill((240, 240, 240))
        colors = [(255, 255, 255)] + self.colors
        for y in range(self.board_height):
            for x in range(self.board_width):
                rect = pygame.Rect(self.board_x + x * self.cell_size, self.board_y + y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, colors[self.board[y][x]], rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        piece_start_x = 80 
        piece_start_y = 0 
        piece_offset = 30 
        piece_counter = 0 
        piece_scale = 6
        for i, (name, shapes) in enumerate(self.pieces.items()):
            if i + 1 in self.placed_pieces:
                continue

            shape = shapes[0] 
            for dx, dy in shape:
                piece_width = max(dx for dx, dy in shape) + 1
                piece_height = max(dy for dx, dy in shape) + 1

                pygame.draw.rect(self.screen, self.colors[i],
                                pygame.Rect(piece_start_x + piece_offset + dx * (self.cell_size - piece_scale),
                                            self.shapes_list_y + dy * (self.cell_size - piece_scale) + piece_start_y - (piece_height * self.cell_size) / 2,
                                            (self.cell_size - piece_scale), (self.cell_size - piece_scale)))

            piece_start_x += piece_width * (self.cell_size - piece_scale) + piece_offset
            piece_counter += 1

            if piece_counter % 6 == 5:
                piece_start_x = 80
                piece_start_y += 5 * (self.cell_size - piece_scale) + piece_offset


    # funkcja pomocnicza sprawdzająca, czy klocek przylega do innego klocka
    def is_adjacent(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.board_width and 0 <= ny < self.board_height and self.board[ny][nx] != 0:
                return True
        return False

    # funkcja rekurencyjna rozwiązująca problem
    # próbuje umieścić wszystkie klocki na planszy
    # jeśli uda się umieścić wszystkie klocki, zwraca True
    # jeśli nie, cofa ostatnie umieszczenie klocka i próbuje ponownie
    def solve(self, pieces):
        if all(all(cell != 0 for cell in row) for row in self.board):
            return True

        for i in range(len(pieces)):
            piece_id, shapes = pieces[i]
            for y in range(self.board_height):
                for x in range(self.board_width):
                    for shape in shapes:
                        if self.can_place(shape, x, y):
                            self.place(shape, x, y, piece_id)
                            remaining_pieces = pieces[:i] + pieces[i + 1:]
                            if not self.has_unfillable_gaps(remaining_pieces) and self.solve(remaining_pieces):
                                return True
                            self.remove(shape, x, y, piece_id)

            pieces.append(pieces.pop(i))
        return False

    # funkcja od której startuje program
    def run(self):
        piece_list = list(enumerate(self.pieces.values(), 1))
        if self.randomize:
            random.shuffle(piece_list)
        self.solve(piece_list)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

if __name__ == "__main__":
    solver = PentominoSolver(5, 5, randomize=False)
    solver.run()
