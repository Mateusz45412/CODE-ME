data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def cal(m):
    cal = dict(data)
    print(list(cal.keys())[m])
    for day in cal[list(cal.keys())[m]]:
        day = day+1
        if day % 7 == 0:
            print(day)

        elif day < 10:
            print("0" + str(day), end="\t")
        else:
            print(day, end="\t")



def main():
    for i in range(12):
        print(cal(i))



main()

