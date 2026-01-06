import re

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "admin", "letmein", "welcome", "abc123"
]

def check_password_strength(password):
    score = 0
    feedback = []
    
    if password.lower() in COMMON_PASSWORDS:
        return "VERY WEAK", ["This password is too common and easy to guess."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


def main():
    print("Password Strength Checker\n")

    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password is strong and secure.")


if __name__ == "__main__":
    main()
