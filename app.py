from datetime import date
import pickle

# Data set
swimmers = {
    "Kyaw Za Yan Naing": {
        "name": "Kyaw Za Yan Naing",
        "gender": "Male",
        "age": "18",
        "status": "inactive",
    },
    "Jayden Smith": {
        "name": "Jayden Smith",
        "gender": "Male",
        "age": "19",
        "status": "active",
    },
}

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


end_program = "No"
while end_program == "No":
    options = getInput(
        prompt="Enter 1 for registeration. \nEnter 2 to print data. \nEnter -> ",
        cast=int,
        condition=lambda x: x == 1 or x == 2,
        errorMessage="You can only enter 1 or 2.",
    )
    if options == 1:
        # Looping register process
        end_register = "No"
        while end_register == "No":
            # Divided the register into creating and deleting user
            create_delete = getInput(
                prompt="Enter 1 to create user. \nEnter 2 to delete user. \nEnter -> ",
                cast=int,
                condition=lambda x: x == 1 or x == 2,
                errorMessage="You can only enter 1 or 2.",
            )
            if create_delete == 1:
                # Registration process (creating new user)
                # Name validated
                swimmer_name = str
                swimmer_name = name_validate(swimmer_name)

                # Gender validated
                swimmer_gender = getInput(
                    prompt="Enter your gender: ",
                    condition=lambda x: x == "Male" or x == "Female" or x == "Others",
                    errorMessage="Only accept Male, Female and Others",
                )

                # Date of birth validate
                while True:
                    inputDate = input("Enter the date of birth(YYYY/MM/DD): ")
                    year, month, day = inputDate.split("/")

                    if int(year) > 2022:
                        print("Year has to be less than 2022.")
                        continue
                    elif int(month) > 12:
                        print("Month has to be less than 12.")
                        continue
                    elif int(day) > 31:
                        print("Day has to be less than 31.")
                        continue
                    else:
                        break

                # Calculate age
                age = age(date(int(year), int(month), int(day)))
                swimmer_age = str(age)

                # Status
                swimmer_status = "active"
                # Adding data and checking user's existence
                if swimmer_name in swimmers:
                    if swimmer_name == swimmers[swimmer_name]["name"]:
                        if swimmers[swimmer_name]["status"] == "inactive":
                            print("User already existed and status is updated to active.")
                            swimmers[swimmer_name]["status"] = "active"
                        else:
                            print("Status is already active.")
                else:
                    # Add user data to the dictionary
                    new_data = add_user(swimmer_name, swimmer_gender, swimmer_age, swimmer_status)
                    swimmers[swimmer_name] = new_data
                    print(f"New user {swimmer_name} registered successfully.")

            elif create_delete == 2:
                # Deleting the searched user
                delete_swimmer = str
                delete_swimmer = name_validate(delete_swimmer)
                if swimmers[delete_swimmer]["status"] == "active":
                    swimmers[delete_swimmer]["status"] = "inactive"
                    print(f"{delete_swimmer}'s status has been updated to inactive.")
                else:
                    print(f"{delete_swimmer} doesn't exist or already inactive.")

            end_register = getInput(
                prompt="Do you want to end the registeration?(Yes or No): ",
                condition=lambda x: x == "Yes" or x == "No",
                errorMessage="You can only enter Yes or No.",
            )

    elif options == 2:
        # Printing data
        print("{0:21} {1:21} {2:21} {3:}".format("Name", "Gender", "Age", "Status"))
        loop_dic(swimmers)

    end_program = getInput(
        prompt="Do you want to end the program? (Yes or No): ",
        condition=lambda x: x == "Yes" or x == "No",
        errorMessage="You can only enter Yes or No.",
    )
