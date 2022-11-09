def calculate_bmi():
    while True:
        try:
            h = float(input('Height[m]:'))
            w = float(input("Weight[kg]: "))
            bmi = w / (h ** 2)
            print('BMI result:', round(bmi, 2))
            return bmi
        except ValueError:
            print("Błąd wartości")
        except ZeroDivisionError:
            print("nie może być wartości zerowej")


def get_bmi_state(bmi):
    try:
        if bmi < 18:
            return 'underweight'
        elif bmi <= 25:
            return 'standard'
        elif bmi <= 30:
            return 'overweight'
        else:
            return 'obesity'
    except TypeError:
        print("TypeError")



def main():

    result_bmi = calculate_bmi()
    status = get_bmi_state(result_bmi)
    print(status)


main()
