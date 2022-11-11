e = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com"]
my_e = input("wpisz szukanego maila ")


def search_email(my_email, emails):
    return print("email jest na liście") if my_email in emails else print("False")


search_email(my_e, e)
