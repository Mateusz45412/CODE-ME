try:
  x = 5 / 0
except ZeroDivisionError as e:
  print("Nie dziel przez zero! Twój wyjątek to:", e)
  x = 0 # potrzebujemy x więc go nadpiszemy
finally:
  print ("Zawsze się wyświetlę")

print(x + 4)