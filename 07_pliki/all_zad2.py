#2▹ Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.
import os
lista = os.listdir(".") #kropka sprawdza aktualny folder a dwie folder wyżej
print(lista)

print(os.path.isfile(".")) #sprawdza czy jest plikiem
print(os.path.isdir(".")) #sprawdza czy jest folderem
# os.rename("cos.txt", "test.txt") #zmienia nazwe
# os.remove("usuwa plik")
# os.rmdir("usuwa folder")

filename = 'rozmiar.txt'

with open(filename, 'r', encoding="utf-8") as f:
  content = f.read()
  print(os.stat('rozmiar.txt').st_size)
