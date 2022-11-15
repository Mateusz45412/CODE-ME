#Zadanie: Otwórz dowolny plik np. tekst.txt.txt i wklej do niego fragment inwokacji Pana Tadeusza

filename = 'tekst1.txt'

with open(filename, 'r', encoding="utf-8") as f:
  content = f.readlines()
print(content)