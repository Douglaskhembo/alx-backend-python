# Getting Started with Python Generators

## Project Overview

This project demonstrates how to use Python generators in a practical scenario by **streaming rows from a MySQL database one by one**. It focuses on efficient data handling by avoiding loading all rows into memory at once.

---

## Objective

Create a **generator** that streams rows from an SQL database one at a time using Python's `yield`.

---

## Project Structure

python-generators-0x00/
├── 0-main.py # Main script to test database connection and data seeding
├── seed.py # Contains database setup and utility functions
├── user_data.csv # CSV file used to populate the database
├── README.md # This file


---

## Features

- Connects to a MySQL server
- Creates the database `ALX_prodev` if it doesn't exist
- Creates the `user_data` table with these fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Inserts sample data from `user_data.csv`
- Displays the first 5 rows of the table

---

## Usage

### Steps to Run

1. **Clone the Repository** (if you haven't):

   ```bash
   git clone https://github.com/your-username/alx-backend-python.git
   cd alx-backend-python/python-generators-0x00

2. **Set Up a Virtual Environment**
    python3 -m venv venv
    source venv/bin/activate

3. **Install required packages**
    pip install mysql-connector-python

4. **Make 0-main.py Executable**
    chmod +x 0-main.py

5. **Run the Main Script**
    python 0-main.py