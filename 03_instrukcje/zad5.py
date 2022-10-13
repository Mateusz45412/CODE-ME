#Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password=input("podaj testowe hasło")

if len(password) < 8 or len(password) > 24:
    print("długość hasła nieprawidłowa, oczekiwana długość między 8 a 24 znaki")
if password.isdigit():
    print("hasło powinno zawierać litery")
if password.isalpha():
    print("hasło powinno zawierać cyfry")
if password.islower():
    print("hasło zawiera tylko małe litery a powinno zawierać conajmniej 1 dużą litere")
if password.isupper():
    print("hasło zawiera tylko duże litery a powinno zawierać conajmniej 1 małą litere")