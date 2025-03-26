def check_password_strength(counter: int) -> bool:
    hasLower = False
    hasUpper = False
    hasNumber = False

    types_of_char = 0

    password = input(
        f"What password would you like to try? You're on try {counter}/3! \n"
    )
    if len(password) > 12 or len(password) < 6:
        print("Password is either less than 6 characters or more than 12 characters!")

        counter += 1
        return check_password_strength(counter) if counter < 3 else False
    else:
        for letter in password:
            hasLower = "a" <= letter <= "z" or hasLower
            hasUpper = "A" <= letter <= "Z" or hasUpper
            hasNumber = "0" <= letter <= "9" or hasNumber

        types_of_char = hasLower + hasUpper + hasNumber

    try:
        strength = ["weak", "medium", "strong"][types_of_char - 1]

        print(f"This is a {strength} password")

        if types_of_char == 3:
            return True
    except Exception as e:
        print("Something has gone wrong")
    finally:
        counter += 1
        return check_password_strength(counter) if counter < 3 else False


def main():
    ret = check_password_strength(0)

    if ret:
        print("You have successfully created a strong password.")
    else:
        print("You have failed to create a strong password")


if __name__ == "__main__":
    main()
