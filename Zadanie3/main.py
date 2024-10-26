# ZADANIE 3.1
# - w Pythonie każda instrukcja powinna być w nowej linii lub w bloku kodu

x = 2
y = 3
if x > y:
    result = x
else:
    result = y
result  # Poprawione rozwiązanie

# ZADANIE 3.2
# Poprawność kodu:
# - L.sort() zwraca None, więc przypisanie L = L.sort() daje L = None, .sort() sortuje in-place
# - przypisanie trzech wartości do dwóch zmiennych
# - krotki są niemutowalne, więc X[1] = 4 jest niedozwolone
# - lista X ma tylko 3 elementy, więc X[3] = 4 wywoła IndexError, indeksowanie od 0
# - łańcuchy znaków są niemutowalne, więc X.append("d") jest błędem
# - map(pow, range(8)) wymaga drugiego argumentu, np. 2 dla kwadratów

# ZADANIE 3.3
result = [i for i in range(31) if i % 3 != 0]
assert result == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]

# ZADANIE 3.4
def cube_loop():
    result = []
    while True:
        x = input("Enter a number or 'stop' to quit: ")
        if x.lower() == 'stop':
            break
        try:
            num = float(x)
            result.append((num, num ** 3))
        except ValueError:
            result.append("Error: Input must be a number")
    return result

# ZADANIE 3.5
def draw_ruler(length):
    ruler_top = "|".join("...." for _ in range(length)) + "|"
    ruler_bottom = "".join(f"{str(i).ljust(5)}" for i in range(length + 1))
    result = f"|{ruler_top}\n{ruler_bottom}"
    return result

print(draw_ruler(12))
assert draw_ruler(12) == (
    "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
    "0    1    2    3    4    5    6    7    8    9    10   11   12   "
)

# ZADANIE 3.6
def draw_rectangle(rows, cols):
    row = "+---" * cols + "+\n"
    cell = "|   " * cols + "|\n"
    rectangle = (row + cell) * rows + row
    return rectangle

print(draw_rectangle(2, 4))
assert draw_rectangle(2, 4) == "+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n"

# ZADANIE 3.8
def sequences_intersection_union(seq1, seq2):
    intersection = list(set(seq1) & set(seq2))
    union = list(set(seq1) | set(seq2))
    return intersection, union

assert sequences_intersection_union([1, 2, 3], [2, 3, 4]) == ([2, 3], [1, 2, 3, 4])

# ZADANIE 3.9
def sum_sequences(sequences):
    return [sum(seq) for seq in sequences]

assert sum_sequences([[], [4], (1, 2), [3, 4], (5, 6, 7)]) == [0, 4, 3, 7, 18]

# ZADANIE 3.10
roman_dict = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def roman2int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

assert roman2int("XIV") == 14
assert roman2int("MCMXCIV") == 1994
