# Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
L_test2 = [1, 2, 3, 4]
#################################
L_test.append("i")
print("append", L_test)
L_test.extend(L_test2)
print("extend",L_test)
L_test.insert(2,"oo")
print("insert",L_test)
L_test.remove(2) #działa dla seta nie działa dla krotek
print("remove",L_test)
index=L_test.index(2) #działa dla krotek nie działa dla seta
print("index",index)
c = L_test.count("oo") #działa dla krotek nie działa dla seta
print("count",c)
p=L_test.pop(1)
print("pop",p)
L_test.reverse()
print("reverse",L_test)

# T_test = (1, 2, 3, 4)
# S_test = {1, 2, 3, 4}