from datetime import date
from random import randrange
import pickle

# Loop throught the dictionary and output as a table
def loop_dic(dic):
    for index in dic:
        for keys, values in dic[index].items():
            print("{0:21}".format(values), end=" ")
        print("")


def loop_tuple(dic):
    for index in dic:
        for value in dic[index]:
            print("{0:21}".format(value), end=" ")
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


# Data set
try:
    swimmers = pickle.load(open("data.pickle", "rb"))
except (OSError, IOError) as e:
    swimmers = {}
    pickle.dump(swimmers, open("data.pickle", "wb"))

try:
    swimmers_record = pickle.load(open("record.pickle", "rb"))
except (OSError, IOError) as e:
    swimmers_record = {}
    pickle.dump(swimmers_record, open("record.pickle", "wb"))

end_program = "No"
while end_program == "No":
    options = getInput(
        prompt="Enter 1 for registration. \nEnter 2 to print data. \nEnter -> ",
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
                prompt="Enter 1 to create user. \nEnter 2 to delete user. \nEnter 3 to record swimmers' timings. \nEnter -> ",
                cast=int,
                condition=lambda x: x == 1 or x == 2 or x == 3,
                errorMessage="You can only enter 1 or 2 or 3.",
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
                    if year == "" or month == "" or day == "":
                        print("You cannot leave balnks.")
                        continue
                    elif int(year) > 2021:
                        print("Year has to be less than 2021.")
                        continue
                    elif int(month) > 12:
                        print("Month has to be less than or equal 12.")
                        continue
                    elif int(day) > 31:
                        print("Day has to be less than or equal 31.")
                        continue
                    else:
                        # Calculate age
                        print(year, month, day)
                        calc_age = age(date(int(year), int(month), int(day)))
                        print(calc_age)
                        swimmer_age = str(calc_age)
                        break

                # Status
                swimmer_status = "active"
                # Adding data and checking user's existence
                if swimmer_name in swimmers:
                    if swimmer_name == swimmers[swimmer_name]["name"]:
                        if swimmers[swimmer_name]["status"] == "inactive":
                            print("User already existed and status is updated to active.")
                            swimmers[swimmer_name]["status"] = "active"
                            pickle.dump(swimmers, open("data.pickle", "wb"))
                        else:
                            print("User already exist and it's status is active.")
                else:
                    # Add user data to the dictionary
                    new_data = add_user(swimmer_name, swimmer_gender, swimmer_age, swimmer_status)
                    swimmers[swimmer_name] = new_data
                    pickle.dump(swimmers, open("data.pickle", "wb"))
                    print(f"New user {swimmer_name} registered successfully.")

            elif create_delete == 2:
                # Deleting the searched user
                delete_swimmer = str
                delete_swimmer = name_validate(delete_swimmer)
                if delete_swimmer in swimmers:
                    if swimmers[delete_swimmer]["status"] == "active":
                        swimmers[delete_swimmer]["status"] = "inactive"
                        print(f"{delete_swimmer}'s status has been updated to inactive.")
                        pickle.dump(swimmers, open("data.pickle", "wb"))
                    else:
                        print(f"{delete_swimmer} is already inactive.")
                else:
                    print(f"{delete_swimmer} doesn't exist.")

            elif create_delete == 3:
                # Record swimmers' timmings
                record_swimmer = ""
                record_swimmer = name_validate(record_swimmer)
                record_swimmer_gender = ""
                events = ""
                swimmer_timming = ""
                meet = ""
                record_swimmer_age = ""
                record_swimmer_status = ""

                if record_swimmer in swimmers:
                    # Check if the swimmer exists.
                    if record_swimmer == swimmers[record_swimmer]["name"]:
                        # Choosing event types
                        event_type = getInput(
                            prompt="Enter 1 for Freestyle. \nEnter 2 for Backstroke. \nEnter 3 for Breaststroke. \nEnter 4 for Butterfly. \nEnter 5 for Individual Medley. \nEnter -> ",
                            cast=int,
                            condition=lambda x: x == 1 or x == 2 or x == 3 or x == 4 or x == 5,
                            errorMessage="You can only enter number from 1 to 5.",
                        )
                        if event_type == 1:
                            meters = getInput(
                                prompt="How many meters?(50, 100, 200, 400, 800, 1500): ",
                                cast=int,
                                condition=lambda x: x == 50
                                or x == 100
                                or x == 200
                                or x == 400
                                or x == 800
                                or x == 1500,
                                errorMessage="You can only enter 50, 100, 200, 400, 800, 1500",
                            )
                            if meters == 50:
                                events = f"{meters} Freestyle"
                                print(events)
                            elif meters == 100:
                                events = f"{meters} Freestyle"
                            elif meters == 200:
                                events = f"{meters} Freestyle"
                            elif meters == 400:
                                events = f"{meters} Freestyle"
                            elif meters == 800:
                                events = f"{meters} Freestyle"
                            elif meters == 1500:
                                events = f"{meters} Freestyle"
                        if event_type == 2:
                            meters = getInput(
                                prompt="How many meters?(50, 100, 200): ",
                                cast=int,
                                condition=lambda x: x == 50 or x == 100 or x == 200,
                                errorMessage="You can only enter 50, 100, 200",
                            )
                            if meters == 50:
                                events = f"{meters} Backstroke"
                                print(events)
                            elif meters == 100:
                                events = f"{meters} Backstroke"
                            elif meters == 200:
                                events = f"{meters} Backstroke"
                        if event_type == 3:
                            meters = getInput(
                                prompt="How many meters?(50, 100, 200): ",
                                cast=int,
                                condition=lambda x: x == 50 or x == 100 or x == 200,
                                errorMessage="You can only enter 50, 100, 200",
                            )
                            if meters == 50:
                                events = f"{meters} Breaststroke"
                                print(events)
                            elif meters == 100:
                                events = f"{meters} Breaststroke"
                            elif meters == 200:
                                events = f"{meters} Breaststroke"
                        if event_type == 4:
                            meters = getInput(
                                prompt="How many meters?(100, 200): ",
                                cast=int,
                                condition=lambda x: x == 100 or x == 200,
                                errorMessage="You can only enter 100, 200",
                            )
                            if meters == 100:
                                events = f"{meters} Butterfly"
                            elif meters == 200:
                                events = f"{meters} Butterfly"
                        if event_type == 5:
                            meters = getInput(
                                prompt="How many meters?(100, 200, 400): ",
                                cast=int,
                                condition=lambda x: x == 100 or x == 200 or x == 400,
                                errorMessage="You can only enter 100, 200, 400",
                            )
                            if meters == 100:
                                events = f"{meters} Individual"
                            elif meters == 200:
                                events = f"{meters} Individual"
                            elif meters == 400:
                                events = f"{meters} Individual"
                        while True:
                            swimmer_timming = input("Enter your simmer timming.(e.g., 1.03.56, 0.32.45): ")
                            hour, minute, second = swimmer_timming.split(".")
                            if hour == "" or minute == "" or second == "":
                                print("You cannot leave blanks.")
                                continue
                            elif int(hour) > 12:
                                print("Hour has to be less than 12.")
                                continue
                            elif int(minute) > 60:
                                print("Minute has to be less than or equal 60.")
                                continue
                            elif int(second) > 60:
                                print("Second has to be less than or equal 30.")
                                continue
                            else:
                                break

                        meet = input("Enter the competition that this timing was achieved: ")
                        record_swimmer_age = swimmers[record_swimmer]["age"]
                        post = getInput(
                            prompt="Do you want to post it?(yes or no): ",
                            condition=lambda x: x == "Yes" or x == "No",
                            errorMessage="You can only enter yes or no.",
                        )
                        if post == "Yes":
                            record_swimmer_status = "Posted"
                            print("Posted successfully,")
                        elif post == "No":
                            record_swimmer_status = "Unposted"
                            print("Unposted.")
                        # Add user record to the dictionary
                        new_record_data = [
                            record_swimmer,
                            swimmers[record_swimmer]["gender"],
                            events,
                            swimmer_timming,
                            meet,
                            swimmers[record_swimmer]["age"],
                            record_swimmer_status,
                        ]
                        swimmers_record[record_swimmer + "#" + str(randrange(1, 1000))] = new_record_data
                        pickle.dump(swimmers_record, open("record.pickle", "wb"))
                        print(f"{record_swimmer}'s event registered successfully.")

                else:
                    print("You need to register first.")

            end_register = getInput(
                prompt="Do you want to end the registration?(yes or no): ",
                condition=lambda x: x == "Yes" or x == "No",
                errorMessage="You can only enter yes or no.",
            )

    elif options == 2:
        # Printing data
        end_print = "No"
        while end_print == "No":
            display_options = getInput(
                prompt="Enter 1 to print register data. \nEnter 2 to print event data. \nEnter -> ",
                cast=int,
                condition=lambda x: x == 1 or x == 2,
                errorMessage="You can only enter 1 or 2.",
            )

            if display_options == 1:
                # Display register data
                print("{0:21} {1:21} {2:21} {3:}".format("Name", "Gender", "Age", "Status"))
                loop_dic(swimmers)
            elif display_options == 2:
                # Display events data
                filter_events = getInput(
                    prompt="Enter 1 to filter by name. \nEnter 2 to filter by name and event name. \nEnter 3 to print all data. \nEnter -> ",
                    cast=int,
                    condition=lambda x: x == 1 or x == 2 or x == 3,
                )
                # Search method implementation
                if filter_events == 1:
                    # Search with name
                    search_name = str
                    search_name = name_validate(search_name)
                    print(
                        "{0:21} {1:21} {2:21} {3:21} {4:21} {5:21} {6:}".format(
                            "Name", "Gender", "Event", "Time", "Meet", "Age", "Status"
                        )
                    )
                    for index in swimmers_record:
                        try:
                            if search_name in swimmers_record[index]:
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        except:
                            print("User not found.")
                    # Posted and unposted
                    post = getInput(
                        prompt="Do you want to post the unposted posts? (yes or no): ",
                        condition=lambda x: x == "Yes" or x == "No",
                        errorMessage="You can only enter yes or no.",
                    )

                    if post == "Yes":
                        for index in swimmers_record:
                            if search_name in swimmers_record[index]:
                                swimmers_record[index][6] = "Posted"
                                pickle.dump(swimmers_record, open("record.pickle", "wb"))
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        print("Posted successfully!")
                    else:
                        for index in swimmers_record:
                            if search_name in swimmers_record[index]:
                                swimmers_record[index][6] = "Unposted"
                                pickle.dump(swimmers_record, open("record.pickle", "wb"))
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        print("Unposted successfully!")

                elif filter_events == 2:
                    # Search with name and event
                    search_name = str
                    search_name = name_validate(search_name)
                    search_event = str
                    search_event = input("Enter the event name: ").title()
                    print(
                        "{0:21} {1:21} {2:21} {3:21} {4:21} {5:21} {6:}".format(
                            "Name", "Gender", "Event", "Time", "Meet", "Age", "Status"
                        )
                    )
                    for index in swimmers_record:
                        try:
                            if search_name in swimmers_record[index] and search_event in swimmers_record[index]:
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        except:
                            print("Not found.")

                    # Posted and unposted
                    post = getInput(
                        prompt="Do you want to post the unposted posts? (yes or no): ",
                        condition=lambda x: x == "Yes" or x == "No",
                        errorMessage="You can only enter yes or no.",
                    )

                    if post == "Yes":
                        for index in swimmers_record:
                            if search_name in swimmers_record[index] and search_event in swimmers_record[index]:
                                swimmers_record[index][6] = "Posted"
                                pickle.dump(swimmers_record, open("record.pickle", "wb"))
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        print("Posted successfully!")
                    else:
                        for index in swimmers_record:
                            if search_name in swimmers_record[index] and search_event in swimmers_record[index]:
                                swimmers_record[index][6] = "Unposted"
                                pickle.dump(swimmers_record, open("record.pickle", "wb"))
                                for value in swimmers_record[index]:
                                    print("{0:21}".format(value), end=" ")
                                print("")
                        print("Unposted successfully!")

                elif filter_events == 3:
                    # Display without filter
                    print(
                        "{0:21} {1:21} {2:21} {3:21} {4:21} {5:21} {6:}".format(
                            "Name", "Gender", "Event", "Time", "Meet", "Age", "Status"
                        )
                    )
                    loop_tuple(swimmers_record)

            end_print = getInput(
                prompt="Do you want to end the printing process? (yes or no): ",
                condition=lambda x: x == "Yes" or x == "No",
                errorMessage="You can only enter yes or no.",
            )

    end_program = getInput(
        prompt="Do you want to end the program? (yes or no): ",
        condition=lambda x: x == "Yes" or x == "No",
        errorMessage="You can only enter yes or no.",
    )
