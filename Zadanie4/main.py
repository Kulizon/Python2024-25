# ZADANIE 4.2

def make_ruler(n):
    if n < 0:
        raise ValueError("Długość miarki musi być liczbą nieujemną.")
    ruler_top = "|".join("...." for _ in range(n)) + "|"
    ruler_bottom = "".join(f"{str(i).ljust(5)}" for i in range(n + 1))
    return f"|{ruler_top}\n{ruler_bottom}"

assert make_ruler(12) == (
    "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
    "0    1    2    3    4    5    6    7    8    9    10   11   12   "
)

def make_grid(rows, cols):
    if rows < 1 or cols < 1:
        raise ValueError("Wymiary muszą być liczbami dodatnimi.")
    row = "+---" * cols + "+\n"
    cell = "|   " * cols + "|\n"
    return (row + cell) * rows + row

assert make_grid(2, 4) == (
    "+---+---+---+---+\n"
    "|   |   |   |   |\n"
    "+---+---+---+---+\n"
    "|   |   |   |   |\n"
    "+---+---+---+---+\n"
)

# ZADANIE 4.3
def factorial(n):
    if n < 0:
        raise ValueError("Argument musi być liczbą nieujemną.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

assert factorial(5) == 120

# ZADANIE 4.4
def fibonacci(n):
    if n < 0:
        raise ValueError("Argument musi być liczbą nieujemną.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

assert fibonacci(7) == 13

# ZADANIE 4.5
# Wersja iteracyjna
def reverse_iter(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Indeksy są poza zakresem listy lub left > right.")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

# Wersja rekurencyjna
def reverse_recur(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Indeksy są poza zakresem listy lub left > right.")
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_recur(L, left + 1, right - 1)
    return L

L1 = [1, 2, 3, 4, 5]
assert reverse_iter(L1, 1, 3) == [1, 4, 3, 2, 5]

L2 = [1, 2, 3, 4, 5]
assert reverse_recur(L2, 1, 3) == [1, 4, 3, 2, 5]

# ZADANIE 4.6
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
        else:
            raise ValueError("Sekwencja zawiera niepoprawny typ danych.")
    return total

assert sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == 45

# ZADANIE 4.7
def flatten(sequence):
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
assert flatten(seq) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
