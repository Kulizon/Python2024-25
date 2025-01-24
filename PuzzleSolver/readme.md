# PentominoSolver

## Wymagania

Wymagane jest środowisko Pythona w wersji **3.12.8** lub nowszej oraz biblioteka **pygame** w wersji **2.6.1**.

```bash
pip install pygame
```

## Opis

Klasa `PentominoSolver` jest implementacją rozwiązania problemu układania klocków pentomino na planszy o wymiarach x na y. Klocki pentomino to figury składające się z pięciu kwadratowych pól, które muszą zostać umieszczone na planszy, przestrzegając kilku zasad:

- Postawienie klocka nie może stworzyć niewypełnialnej przestrzeni.
- Klocki nie mogą się nakładać.
- Klocki nie mogą wychodzić poza planszę.

Plansza jest reprezentowana jako macierz o wymiarach x na y, gdzie 0 oznacza puste pole, a liczba większa od 0 oznacza konkretne miejsce zajęte przez konkretny klocek.

Jeśli x * y nie jest podzielne przez 5, podnosi wyjątek `ValueError`. Warunek ten wynika z charakteru klocków pentomino. 

## Metody

### `randomize_pentomino()`

Zwraca klocki pentomino w losowej kolejności w celu randomizacji rozwiąząń.

### `can_place_piece(board_x, board_y, piece)`

Sprawdza, czy klocek o danym kształcie może zostać umieszczony na planszy w określonym miejscu. Warunki, które są sprawdzane to:

- Czy klocek nie wychodzi poza planszę.
- Czy klocek nie nakłada się na inne klocki.
- Czy umieszczenie klocka nie tworzy niewypełnialnej przestrzeni.

###  `has_unfillable_gaps(temp_board)`

Sprawdza, czy na planszy istnieją luki, których nie można wypełnić.

Funkcja używa algorytmu flood fill do zidentyfikowania i zmierzenia rozmiaru każdej luki na planszy. Jeśli rozmiar luki nie jest wielokrotnością 5, funkcja zwraca `True`, co oznacza, że istnieje luka, której nie można wypełnić. W przeciwnym razie zwraca `False`.

### `place_piece(board_x, board_y, piece, piece_index)`

Umieszcza klocek na planszy w danym miejscu. Po umieszczeniu klocka, jego identyfikator jest dodawany do zbioru `used_pieces` (już poza funkcją).

### `remove_piece(board_x, board_y, piece)`

Usuwa klocek z planszy, podmieniając "id klocka" na 0 w miejscach, gdzie był umieszczony. Po usunięciu, identyfikator klocka jest usuwany ze zbioru `used_pieces` (już poza funkcją).

### `draw_board()`

Rysuje planszę na ekranie. Każde pole na planszy jest rysowane jako kwadrat, a klocki są przedstawiane w odpowiednich kolorach. Dodatkowo, rysowane są klocki, które można umieścić na planszy.

### `solve(pieces)`

Rekurencyjna funkcja rozwiązująca problem układania klocków. Próbuję umieścić wszystkie klocki na planszy. Jeśli uda się umieścić wszystkie klocki, zwraca wartość True. W przeciwnym przypadku cofa ostatnie umieszczenie klocka i próbuje ponownie.

### `get_unique_pieces(pieces)`

Usuwa duplikaty z listy kształtów klocków, zwracając tylko unikalne kształty.

### `rotate_piece(piece)`

Zwraca nową wersję klocka, która jest jego obrotem o 90 stopni zgodnie z ruchem wskazówek zegara.

### `get_piece_rotations(piece)`

Tworzy listę wszystkich możliwych rotacji i odbić lustrzanych danego klocka, eliminując duplikaty, aby uniknąć powtórzeń.

### `get_mirrored_piece(piece)`

Zwraca odbicie lustrzane danego klocka w osi pionowej.

## Użycie

Wywołujemy funkcję `solve` z ewentualną zmianą wymiarów planszy.

```python
BOARD_WIDTH = 5
BOARD_HEIGHT = 10

solve(board, used_pieces)
```