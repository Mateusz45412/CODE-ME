#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
txt='abrakadabra'
lenght=len(txt) #ilość liter w wyrazie
index_center = lenght // 2 #wyznaczam środek wyrazu
index_prev = index_center -1
index_next = index_center +1
print(txt[index_prev]+txt[index_center]+txt[index_next])