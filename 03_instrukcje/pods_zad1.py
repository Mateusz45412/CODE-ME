#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.
names=input('podaj imiona podzielone spacja')
names = names.split()
for i in names:
    print ("Hello",i, "!")
