# Password-manager-LockHaven

## Overview
SecurePass is a secure, locally-stored password manager that helps you generate, store, and manage your passwords with strong encryption. Built with Python, it uses AES-256 encryption to protect your sensitive data.

## Features

* 🔒 **Secure Password Storage**: All passwords are encrypted before storage
* 🎲 **Password Generator**: Create strong, random passwords with customizable options
* 🔍 **Password Retrieval**: Securely access stored passwords with your master password
* 📂 **Categories & Tags**: Organize passwords by service type or category
* 📋 **Copy to Clipboard**: Quickly copy passwords without displaying them
* 🔄 **Update & Delete**: Modify or remove stored credentials as needed

## Installation

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/securepass.git
cd securepass
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python securepass.py
```

### Dependencies

* `cryptography` - For AES encryption implementation
* `pyperclip` - For clipboard functionality
* `colorama` - For colored console output

## Usage

### First Run Setup
* Create a strong master password (minimum 8 characters)
* Remember this password - it cannot be recovered if lost

### Main Menu
```
1. Add new password
2. View passwords
3. Generate random password
4. Update password
5. Delete password
Q. Quit
```

### Adding a Password
* Enter service/website name
* Enter username/email
* Enter password (or leave blank to generate)
* Optional: Add category and notes

### Viewing Passwords
* Lists all stored services
* Select a service to copy password to clipboard

## Security Implementation

* 🔐 **Encryption**: AES-256 encryption using Fernet
* 🔑 **Key Derivation**: PBKDF2HMAC with SHA256
* 🧂 **Unique Salt**: Random salt for each user
* 🧹 **Memory Safety**: Keys wiped from memory after use

## File Structure

```
/securepass
│
├── securepass.py          # Main application
├── crypto.py             # Encryption functions
├── database.py           # Database operations
├── generator.py          # Password generation
├── requirements.txt      # Dependencies
└── securepass.db         # Database file (created after first run)
```

## Future Enhancements

* Cloud synchronization with end-to-end encryption
* Browser extension for auto-fill
* Two-factor authentication
* Password sharing with trusted contacts
* Password strength analysis
* Dark web monitoring integration

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is a personal project for educational purposes. The developers are not responsible for any data loss or security breaches. Always maintain backups of your important credentials.
