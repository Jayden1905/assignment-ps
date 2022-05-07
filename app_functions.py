from datetime import date

# Loop throught the dictionary and output as a table
def loop_dic(dic):
    for index in dic:
        for keys, values in dic[index].items():
            print("{0:21}".format(values), end=" ")
        print("")


# Validate the input
def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt).capitalize())
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid Input!")


# Name validation
def name_validate(name):
    while True:
        name = input("Enter your name: ").title()
        if all(x.isalpha() or x.isspace() for x in name):
            return name
            break
        else:
            print("Invalid name, you can only enter alphabets.")
            continue


# Calc age from date of birth
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Adding new users
def add_user(name, gender, age, status):
    new_data_set = {
        "name": name,
        "gender": gender,
        "age": age,
        "status": status,
    }
    return new_data_set
