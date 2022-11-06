# Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

filename = 'tekst1.txt'

with open(filename, 'r', encoding="utf-8") as file:
    word_list = file.read().split()
print(word_list)

longest_word = ''

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

