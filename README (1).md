# Password Strength Analyzer 🔐

A beginner-friendly Python command-line project that evaluates password strength and generates stronger password suggestions.

## Features

- Checks password length.
- Checks lowercase and uppercase letters.
- Checks numbers and special characters.
- Flags a small list of commonly used passwords.
- Detects passwords made from one repeated character.
- Gives suggestions to improve weak passwords.
- Generates a random 16-character password using Python's `secrets` module.
- Hides the password while the user types it.

## Technologies Used

- Python 3
- `string` — character groups
- `secrets` — cryptographically secure random password generation
- `getpass` — hides password input in the terminal

All modules used are included with Python. No external packages are required.

## Requirements

- Python 3.8 or later
- VS Code, PyCharm, or any terminal

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run:

   ```bash
   python password_analyzer.py
   ```

   On some Windows systems, use:

   ```bash
   py password_analyzer.py
   ```

4. Enter a test password when prompted.
5. Review the strength rating and suggestions.
6. Choose `y` if you want the program to generate a stronger password.

## Example

```text
=============================================
       PASSWORD STRENGTH ANALYZER
=============================================
Your password is hidden while you type.

Enter a password to analyze:

---------- ANALYSIS REPORT ----------
Strength : Strong
Score    : 6/6

Suggestions:
- Good job! Keep this password private and unique.

Would you like a stronger password suggestion?
Generate one? (y/n):
```

The exact result depends on the password entered. The generated password is random, so its value will differ each time.

## Project Structure

```text
password-strength-analyzer/
├── password_analyzer.py
└── README.md
```

## Security Notes and Limitations

- This is an educational project and uses a small built-in list of common passwords. It does not check every leaked or compromised password.
- The program does not save passwords or store password history.
- It does not connect to a database or check whether a password was previously used.
- Do not enter your real account password into an unfamiliar or demonstration program.
- For real applications, use a trusted password manager and follow established password-storage practices. Never store user passwords as plain text.

## Future Improvements

- Add a graphical user interface (GUI).
- Add a larger common-password list.
- Add an optional password-history database using secure password-hashing practices.
- Add an online breach-check feature using a privacy-preserving method.

## Learning Outcomes

This project introduces Python conditionals, loops, functions, strings, character checking, secure random generation, and basic password-security concepts.

## Author

Add your name here.
