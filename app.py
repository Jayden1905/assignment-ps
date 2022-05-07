from datetime import date
import app_functions

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

end_program = "No"
while end_program == "No":
    options = app_functions.getInput(
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
            create_delete = app_functions.getInput(
                prompt="Enter 1 to create user. \nEnter 2 to delete user. \nEnter -> ",
                cast=int,
                condition=lambda x: x == 1 or x == 2,
                errorMessage="You can only enter 1 or 2.",
            )
            if create_delete == 1:
                # Registration process (creating new user)
                # Name validated
                swimmer_name = str
                swimmer_name = app_functions.name_validate(swimmer_name)

                # Gender validated
                swimmer_gender = app_functions.getInput(
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
                age = app_functions.age(date(int(year), int(month), int(day)))
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
                    new_data = app_functions.add_user(swimmer_name, swimmer_gender, swimmer_age, swimmer_status)
                    swimmers[swimmer_name] = new_data
                    print(f"New user {swimmer_name} registered successfully.")

            elif create_delete == 2:
                # Deleting the searched user
                delete_swimmer = str
                delete_swimmer = app_functions.name_validate(delete_swimmer)
                if swimmers[delete_swimmer]["status"] == "active":
                    swimmers[delete_swimmer]["status"] = "inactive"
                    print(f"{delete_swimmer}'s status has been updated to inactive.")
                else:
                    print(f"{delete_swimmer} doesn't exist or already inactive.")

            end_register = app_functions.getInput(
                prompt="Do you want to end the registeration?(Yes or No): ",
                condition=lambda x: x == "Yes" or x == "No",
                errorMessage="You can only enter Yes or No.",
            )

    elif options == 2:
        # Printing data
        print("{0:21} {1:21} {2:21} {3:}".format("Name", "Gender", "Age", "Status"))
        app_functions.loop_dic(swimmers)

    end_program = app_functions.getInput(
        prompt="Do you want to end the program? (Yes or No): ",
        condition=lambda x: x == "Yes" or x == "No",
        errorMessage="You can only enter Yes or No.",
    )
