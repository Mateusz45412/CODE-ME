import io

filename = 'plikl.txt'
try:
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Nie ma takiego pliku !!")

filename1 = 'plik.txt'
try:
    with open(filename1, 'w', encoding="utf-8") as f:
            print(f.read())
except io.UnsupportedOperation:
    print("ma być tryb 'r' a nie 'w' ")

filename2 = 'plik.txt'
try:
    with open(filename2, 'w', encoding="utf-8") as f:
            print(f.read())
except io.UnsupportedOperation:
    print("tryb X")