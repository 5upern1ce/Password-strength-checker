
lower_count = 0
upper_count = 0
number_count = 0
counter = 0
def check_password_strength():
    global lower_count
    global upper_count
    global number_count
    global counter
    password = input(f"What password would you like to try? You're on try {counter}/3! \n")
    if len(password) > 12 or len(password) < 6:
        counter += 1
        print("Password is either less than 6 characters or more than 12 characters!")
        if counter < 3:
            check_password_strength()
        else:
            return 1

    else:
        for letter in password:
            if 'a' <= letter <= 'z': 
                lower_count += 1
            elif 'A' <= letter <= 'Z':
                upper_count += 1
            elif '0' <= letter <= '9':
                number_count += 1
        types_of_char = 0
        if lower_count > 0:
            types_of_char += 1
        if upper_count > 0:
            types_of_char += 1
        if number_count > 0:
            types_of_char += 1


        if types_of_char == 1:
            print("This is a weak password")
            counter += 1
            if counter < 3:
                check_password_strength()
            else:
                return 1
        elif types_of_char == 2:
            print("This is a medium password")
            counter += 1
            if counter < 3:
                check_password_strength()
            else:
                return 1
        elif types_of_char == 3:
            print("This is a strong password")
            counter += 1
            if counter < 3:
                check_password_strength()
            else:
                return 1
        else:
            print("Something has gone wrong!")
            counter += 1
            if counter < 3:
                check_password_strength()
            else:
                return 1
def main():
    check_password_strength()


if __name__ == "__main__":
    main()