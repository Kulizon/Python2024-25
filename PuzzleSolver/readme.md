# PentominoSolver

## Wymagania

Wymagane jest środowisko Pythona w wersji **3.12.8** lub nowszej oraz biblioteka **pygame** w wersji **2.6.1**.

```bash
pip install pygame
```

## Opis

Klasa `PentominoSolver` jest implementacją rozwiązania problemu układania klocków pentomino na planszy o wymiarach x na y. Klocki pentomino to figury składające się z pięciu kwadratowych pól, które muszą zostać umieszczone na planszy, przestrzegając kilku zasad:

- Pierwszy klocek musi dotykać ścian planszy.
- Kolejne klocki muszą być przylegające do innego już umieszczonego klocka.
- Klocki nie mogą się nakładać.
- Klocki nie mogą wychodzić poza planszę.

## Konstruktor

Konstruktor klasy przyjmuje następujące parametry:

- `x` – liczba kolumn w planszy,
- `y` – liczba wierszy w planszy,
- `randomize` – flaga określająca, czy początkowa kolejność klocków ma być losowa.

Plansza jest reprezentowana jako macierz o wymiarach x na y, gdzie 0 oznacza puste pole, a liczba większa od 0 oznacza konkretne miejsce zajęte przez konkretny klocek.

Jeśli x * y nie jest podzielne przez 5, podnosi wyjątek `ValueError`. Warunek ten wynika z charakteru klocków pentomino. 

## Metody

### `get_pentomino_pieces()`

Zwraca klocki pentomino wraz ze wszystkimi ich możliwymi rotacjami. 
Rotacje są przeprowadzane zarówno o 90 stopni, jak i symetrycznie względem osi X i Y.

### `generate_unique_colors(num_colors)`

Generuje unikalne kolory dla klocków pentomino.

### `can_place(shape, x, y)`

Sprawdza, czy klocek o danym kształcie może zostać umieszczony na planszy w określonym miejscu. Warunki, które są sprawdzane to:

- Czy klocek nie wychodzi poza planszę.
- Czy klocek nie nakłada się na inne klocki.
- Dla pierwszego klocka – czy dotyka ściany planszy.
- Dla kolejnych klocków – czy przylega do innego klocka (ograniczenie liczby sprawdzanych możliwośći).

### `place(shape, x, y, piece_id)`

Umieszcza klocek na planszy w danym miejscu i rysuje zaktualizowaną planszę. Po umieszczeniu klocka, jego identyfikator jest dodawany do zbioru `placed_pieces`.

### `remove(shape, x, y, piece_id)`

Usuwa klocek z planszy, podmieniając "id klocka" na 0 w miejscach, gdzie był umieszczony. Po usunięciu, identyfikator klocka jest usuwany ze zbioru `placed_pieces`.

### `has_unfillable_gaps(pieces)`

Sprawdza, czy na planszy znajdują się luki, które nie mogą zostać wypełnione przez dostępne klocki. Luki są analizowane za pomocą algorytmu DFS, który przeszukuje wszystkie puste komórki i sprawdza, czy możliwe jest ich wypełnienie odpowiednimi klockami. Sprawdzanie luk, których nie da się wypełnić ograncza bezsensowne rozwiązania.

### `can_fill_gap_with_pieces(gap, pieces)`

Sprawdza, czy dane luki mogą zostać wypełnione dostępnymi klockami. Jest to funkcja pomocnicza dla metody `has_unfillable_gaps`.

### `draw_board()`

Rysuje planszę na ekranie. Każde pole na planszy jest rysowane jako kwadrat, a klocki są przedstawiane w odpowiednich kolorach. Dodatkowo, rysowane są klocki, które można umieścić na planszy.

### `is_adjacent(x, y)`

Sprawdza, czy podane pole przylega do innego klocka na planszy. Funkcja ta jest używana w metodzie `can_place`.

### `solve(pieces)`

Rekurencyjna funkcja rozwiązująca problem układania klocków. Próbuję umieścić wszystkie klocki na planszy. Jeśli uda się umieścić wszystkie klocki, zwraca wartość True. W przeciwnym przypadku cofa ostatnie umieszczenie klocka i próbuje ponownie.

### `run()`

Funkcja startowa, która uruchamia rozwiązywanie problemu. Inicjalizuje odpowiednie ustawienia i wywołuje metodę `solve`.

## Użycie

Aby rozpocząć rozwiązywanie problemu, należy stworzyć obiekt klasy `PentominoSolver` z odpowiednimi parametrami i wywołać metodę `run()`.

```python
solver = PentominoSolver(5, 3, randomize=False)
solver.run()
```