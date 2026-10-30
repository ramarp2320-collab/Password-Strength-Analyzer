"""
Password Strength Analyzer
A beginner-friendly command-line password checker.

Features:
- Checks length, uppercase/lowercase letters, digits, and symbols
- Flags common and repetitive passwords
- Gives practical improvement suggestions
- Generates a strong alternative using Python's secrets module

Note: This is an educational checker, not a replacement for a production
authentication system. It does not store passwords or verify whether a
password has appeared in a data breach.
"""

import secrets
import string
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "qwerty123", "admin", "letmein",
    "welcome", "iloveyou"
}


def analyze_password(password):
    """Return a strength score, label, and improvement suggestions."""
    suggestions = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters (8 is the minimum).")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters such as !, @, #, or %.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common passwords that are easy to guess.")

    if len(password) > 0 and len(set(password)) == 1:
        score = 0
        suggestions.append("Avoid using the same character repeatedly.")

    if len(password) >= 12 and len(set(password)) <= 3:
        score = min(score, 2)
        suggestions.append("Use a wider variety of characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    if not suggestions:
        suggestions.append("Good job! Keep this password private and unique.")

    return strength, score, suggestions


def generate_password(length=16):
    """Generate a password using a cryptographically secure random source."""
    if length < 12:
        raise ValueError("Password length must be at least 12.")

    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each required character category.
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    remaining = [
        secrets.choice(alphabet) for _ in range(length - len(required))
    ]
    characters = required + remaining

    # Securely shuffle the generated characters.
    for index in range(len(characters) - 1, 0, -1):
        swap_index = secrets.randbelow(index + 1)
        characters[index], characters[swap_index] = (
            characters[swap_index],
            characters[index],
        )

    return "".join(characters)


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)
    print("Your password is hidden while you type.\n")

    password = getpass.getpass("Enter a password to analyze: ")

    if not password:
        print("\nNo password entered. Please try again.")
        return

    strength, score, suggestions = analyze_password(password)

    print("\n---------- ANALYSIS REPORT ----------")
    print(f"Strength : {strength}")
    print(f"Score    : {score}/6")
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

    print("\nWould you like a stronger password suggestion?")
    choice = input("Generate one? (y/n): ").strip().lower()

    if choice == "y":
        print("\nGenerated password:")
        print(generate_password())
        print("\nSave it in a trusted password manager.")
    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
