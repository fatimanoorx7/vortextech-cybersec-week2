COMMON_PASSWORDS = [
    "123456",
    "password",
    "qwerty",
    "12345678",
    "admin",
    "letmein"
]


def check_password_strength(password):
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak", ["This is a very common password. Choose a unique password."]

    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    lowercase_ok = any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    special_ok = any(not c.isalnum() for c in password)

    checks_passed = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        special_ok
    ])

    if not length_ok:
        feedback.append("Use at least 8 characters.")

    if not uppercase_ok:
        feedback.append("Add at least one uppercase letter.")

    if not lowercase_ok:
        feedback.append("Add at least one lowercase letter.")

    if not number_ok:
        feedback.append("Add at least one number.")

    if not special_ok:
        feedback.append("Add at least one special character.")

    if checks_passed <= 2:
        strength = "Weak"
    elif checks_passed <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    if not feedback:
        feedback.append("Good password structure.")

    return strength, feedback


def main():
    password = input("Enter a password to evaluate: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)
    print("Feedback:")

    for message in feedback:
        print("-", message)


if __name__ == "__main__":
    main()