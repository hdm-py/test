# Contact Management System

A simple Python-based contact management system that interacts with a PostgreSQL database to create, update, retrieve, and delete contact information.

## Features
- **Create Contact**: Add a new contact to the database with name, phone number, email, and address.
- **View Contacts**: Retrieve all contacts stored in the database.
- **Update Contact**: Modify an existing contact's details.
- **Delete Contact**: Remove a contact from the database.

## Requirements
- Python 3.x
- PostgreSQL

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/LeonByte/contact-manager.git
   ```
   
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Set up the PostgreSQL database:
   - Create a PostgreSQL database (e.g., `contacts_db`).
   - Update the connection details in the code (e.g., username, password) to match your PostgreSQL setup.

4. Run the application:
   ```bash
   python index.py
   ```

## Usage

Once the project is running, you can interact with it through the command-line interface. The available options are:
- **1**: Create a new contact.
- **2**: Show all contacts.
- **3**: Update an existing contact.
- **4**: Remove a contact.
- **5**: Quit the application.

## Contributing

Feel free to fork the repository and submit pull requests for bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.