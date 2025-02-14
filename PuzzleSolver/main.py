import time
import pygame
import random
pygame.font.init()

pentomino = [
# F piece
[
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 0]
],
# I piece
[
    [1, 1, 1, 1, 1]
],
# L piece
[
    [1, 0, 0, 0],
    [1, 1, 1, 1]
],
# N piece
[
    [0, 0, 1, 1],
    [1, 1, 1, 0]
],
# P piece
[
    [1, 1],
    [1, 1],
    [1, 0]
],
# T piece
[
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0]
],
# U piece
[
    [1, 0, 1],
    [1, 1, 1],
],
# V piece
[
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1]
],
# W piece
[
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
],
# X piece
[
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
],
# Y piece
[
    [0, 1, 0, 0],
    [1, 1, 1, 1]
],
# Z piece
[
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]
]

colors = {
    0: (220, 220, 220),
    1: (0, 255, 0),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (255, 69, 0),
    5: (153, 50, 204),
    6: (0, 206, 209),
    7: (255, 20, 147),
    8: (139, 69, 19),
    9: (70, 130, 180),
    10: (178, 34, 34),
    11: (34, 139, 34),
    12: (255, 0, 0),
    13: (255, 140, 0)
}

BOARD_WIDTH = 10
BOARD_HEIGHT = 5

SCREEN_WIDTH_PX = 1200
SCREEN_HEIGHT_PX = 600

SCREEN_PADDING = 20
PIECE_PADDING = 5

SOLVED_BOARD_CELL_SIZE = 35
PIECE_DISPLAY_CELL_SIZE = 25

PIECE_DISPLAY_OFFSET_Y = 50
PIECE_DISPLAY_OFFSET_Y = 50
PIECE_DISPLAY_PADDING = 20

sleep_debug = False

def draw_board(screen, board, used_pieces):
    screen.fill((20, 20, 20))

    offset_x = (SCREEN_WIDTH_PX - (BOARD_WIDTH * SOLVED_BOARD_CELL_SIZE)) // 2
    offset_y = SCREEN_PADDING

    for row_cell, row in enumerate(board):
        for col in range(len(row)):
            piece_index = row[col]

            rect = pygame.Rect(offset_x + col * (SOLVED_BOARD_CELL_SIZE + PIECE_PADDING), 
                               offset_y + row_cell * (SOLVED_BOARD_CELL_SIZE + PIECE_PADDING), 
                               SOLVED_BOARD_CELL_SIZE, 
                               SOLVED_BOARD_CELL_SIZE)

            pygame.draw.rect(screen, colors[piece_index], rect) 

    offset_y += (BOARD_HEIGHT * (SOLVED_BOARD_CELL_SIZE + PIECE_PADDING)) + PIECE_DISPLAY_OFFSET_Y
    offset_x = SCREEN_PADDING

    START_X = (SCREEN_WIDTH_PX - (3.5 * (PIECE_DISPLAY_CELL_SIZE + PIECE_PADDING) + PIECE_DISPLAY_PADDING) * 6) // 2

    drawn_pieces = 0
    current_piece_x = START_X
    current_piece_y = 0
    current_max_piece_height = 0

    for piece_index, used in enumerate(used_pieces):
        if used:
            continue

        if drawn_pieces % 6 == 0:
            current_piece_x = START_X
            current_piece_y += PIECE_DISPLAY_CELL_SIZE * current_max_piece_height + PIECE_DISPLAY_PADDING
            current_max_piece_height = 0

        piece = pentomino[piece_index]

        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell != 0:
                    rect = pygame.Rect(offset_x + current_piece_x + x * (PIECE_DISPLAY_CELL_SIZE + PIECE_PADDING), 
                                       offset_y + current_piece_y + y * (PIECE_DISPLAY_CELL_SIZE + PIECE_PADDING), 
                                       PIECE_DISPLAY_CELL_SIZE, 
                                       PIECE_DISPLAY_CELL_SIZE)

                    pygame.draw.rect(screen, colors[piece_index + 1], rect)

        current_piece_x += len(piece[0]) * (PIECE_DISPLAY_CELL_SIZE + PIECE_PADDING) + PIECE_DISPLAY_PADDING
        current_max_piece_height = max(current_max_piece_height, len(piece))
        drawn_pieces += 1

    pygame.display.flip()

    global sleep_debug
    if sleep_debug:
        sleep_debug = False
        time.sleep(5)


def place_piece(board_x, board_y, piece, piece_index):
    if not can_place_piece(board_x, board_y, piece):
        return False

    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                board[board_y + y][board_x + x] = piece_index + 1 
    return True

def remove_piece(board_x, board_y, piece):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                board[board_y + y][board_x + x] = 0 

def has_unfillable_gaps(board):
    def flood_fill(x, y):
        if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT or board[y][x] != 0:
            return 0
        board[y][x] = -1
        return 1 + flood_fill(x + 1, y) + flood_fill(x - 1, y) + flood_fill(x, y + 1) + flood_fill(x, y - 1)

    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x] == 0:
                gap_size = flood_fill(x, y)
                if gap_size % 5 != 0:
                    return True
    return False

def can_place_piece(board_x, board_y, piece):
    if board_y + len(piece) > BOARD_HEIGHT:
        return False
    if board_x + len(piece[0]) > BOARD_WIDTH:
        return False

    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0 and board[board_y + y][board_x + x] != 0:
                return False
            
    temp_board = [row[:] for row in board]
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                temp_board[board_y + y][board_x + x] = 1

    if has_unfillable_gaps(temp_board):
        # global sleep_debug
        # sleep_debug = True
        return False

    return True

def rotate_piece(piece):
    return [list(row) for row in zip(*reversed(piece))]

def get_unique_pieces(pieces):
    unique_pieces = []
    for piece in pieces:
        if piece not in unique_pieces:
            unique_pieces.append(piece)
    return unique_pieces

def get_piece_variations(piece):
    rotations = []
    for _ in range(4):
        rotations.append(piece)
        piece = rotate_piece(piece)

    mirrored_piece = get_mirrored_piece(piece)
    for _ in range(4):
        rotations.append(mirrored_piece)
        mirrored_piece = rotate_piece(mirrored_piece)

    return get_unique_pieces(rotations)

def get_mirrored_piece(piece):
    return [list(reversed(row)) for row in piece]

def solve(board, used_pieces, depth=0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

    if all(used_pieces) or not any(0 in row for row in board):
        draw_board(screen, board, used_pieces)
        return True

    def update_board(piece_index, added):
        used_pieces[piece_index] = added
        draw_board(screen, board, used_pieces)
        time.sleep(1)

    draw_board(screen, board, used_pieces)

    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x] == 0:
                for piece_index, piece in enumerate(pentomino):
                    if used_pieces[piece_index]:
                        continue

                    rotations = get_piece_variations(piece)

                    for rotation in rotations:
                        if place_piece(x, y, rotation, piece_index):
                            update_board(piece_index, True)
                            if solve(board, used_pieces, depth + 1):
                                return True

                            remove_piece(x, y, rotation)
                            update_board(piece_index, False)

                return False
    return False

def randomize_pentomino(pentomino):
    randomized_pentomino = pentomino[:]
    random.shuffle(randomized_pentomino)
    return randomized_pentomino

pentomino = randomize_pentomino(pentomino)

screen = pygame.display.set_mode((SCREEN_WIDTH_PX + SCREEN_PADDING, SCREEN_HEIGHT_PX + SCREEN_PADDING))
board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
used_pieces = [False] * len(pentomino)

if BOARD_HEIGHT * BOARD_WIDTH % 5 != 0:
    raise ValueError("Board size must be divisible by 5")

solve(board, used_pieces)

time.sleep(15)
