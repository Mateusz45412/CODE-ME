#1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

items = [13, 17,"word", 2.45, 0]

for i in items:
    try:
        x = 10 / i
        print(x)
    except TypeError:
        print("type error for", i)
    except ZeroDivisionError:
        print("zero div error", i)