#Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8)

n =int(input("wpisz silnie z dowlolnej liczby "))
s=1
if n<=8:
    for i in range (1,n+1):
     s *= i
     print(s)
    print("silnia z ",n,"wynosi",s)
else:
    print("wprowadź liczbę nie większą niż 8 ")

