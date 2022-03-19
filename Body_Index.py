weight = float(input("Write your weight: "))
height = float(input("Write your height: "))
age = float(input("Write your age: "))
body_index = weight/(height**2)


if age < 18:
    print("You're too young for this")
else:
    if body_index < 18.5:
        print("You are slim")
    elif body_index >= 18.5 and body_index <= 25:
        print("You are normal")
    elif body_index >= 25 and body_index < 30:
        print("You are overweight")
    else: print("You are obese")



