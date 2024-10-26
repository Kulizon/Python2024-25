# Zadanie 2.10
line = "To jest przykładowy\nwielowierszowy napis."
words = line.split()
number_of_words = len(words)
print(number_of_words)

# Zadanie 2.11
word = "Python"
underscored_word = "_".join(word)
print(underscored_word)

# Zadanie 2.12
line = "To jest przykładowy tekst"
words = line.split()
first_letters = "".join([word[0] for word in words])
last_letters = "".join([word[-1] for word in words])
print(first_letters)
print(last_letters)

# Zadanie 2.13
total_length = sum(len(word) for word in words)
print(total_length)

# Zadanie 2.14
longest_word = max(words, key=len)
longest_word_length = len(longest_word)
print(longest_word)
print(longest_word_length)

# Zadanie 2.15
L = [123, 45, 6, 789]
digits_string = "".join(str(num) for num in L)
print(digits_string)

# Zadanie 2.16
line = "Python został stworzony przez GvR"
line_replaced = line.replace("GvR", "Guido van Rossum")
print(line_replaced)

# Zadanie 2.17
words_sorted_alphabetically = sorted(words)
words_sorted_by_length = sorted(words, key=len)
print(words_sorted_alphabetically)
print(words_sorted_by_length)

# Zadanie 2.18
big_number = 100200300400500
zero_count = str(big_number).count('0')
print(zero_count)

# Zadanie 2.19
L = [7, 24, 153]
formatted_blocks = "".join([str(num).zfill(3) for num in L])
print(formatted_blocks)
