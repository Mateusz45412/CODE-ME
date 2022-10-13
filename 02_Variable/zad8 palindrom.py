#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
txt=input("Give me a sentence to check palindrome ->")
txt=txt.replace(" ","")
txt = txt.lower() #Zmienia wszystkie duże litery na małe w stringu
print('Is palindrome ? ->', txt==txt[::-1])