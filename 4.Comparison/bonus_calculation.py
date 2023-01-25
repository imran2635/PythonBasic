"""
less than 3 : 0% Bonus
less than 5 : 50% Bonus
less than 8 : 75% Bonus
more than 8 : 100% Bonus`
"""

while True:
    try:
        number = float(input("Enter Company Affiliation: "))
        if number < 3:
            print("0% Bonus")
            break
        elif number < 5:
            print("50% Bonus")
            break
        elif number < 8:
            print("75% Bonus")
            break
        else:
            print("100% Bonus")
            break
    except ValueError:
        print("Please enter a number.")
        continue

