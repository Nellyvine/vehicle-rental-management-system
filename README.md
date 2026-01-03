# Vehicle Rental Management System

## Overview

The Vehicle Rental Management System is a Python-based console application designed to automate vehicle rental operations for small rental companies. The system replaces manual paper-based processes with a computerized solution that improves accuracy, efficiency, and record management.

## Main Features

- User authentication (signup and login)
- Vehicle inventory management (add, update, remove, search)
- Customer registration and management
- Rental transaction processing with automatic availability tracking
- Vehicle return processing with automatic cost calculation
- Payment processing and validation
- Report generation (available vehicles, active rentals, revenue)

## Project Structure

```
vehicle-rental-system/
├── main.py                 # Program entry point
├── main_system.py          # Main controller and menu system
├── vehicle.py              # Vehicle class
├── customer.py             # Customer class
├── rental.py               # Rental class
├── payment.py              # Payment class
├── file_manager.py         # File handling operations
└── Data files (created at runtime):
    ├── vehicles.txt
    ├── customers.txt
    ├── rentals.txt
    ├── payments.txt
    └── users.txt
```

## Data Storage

All data is stored in pipe-delimited text files with column headers for easy readability. Each file is automatically created on first run and includes descriptive headers to document the data structure.

## Exception Handling

The system implements comprehensive exception handling for file operations (FileNotFoundError, IOError), invalid inputs (ValueError), business logic errors (vehicle unavailability, duplicate records), and system interruptions (KeyboardInterrupt).

## How to Run the Program

1. Ensure Python 3.x is installed
2. Run `python main.py` in the terminal
3. Choose option 2 to signup (first-time users) or option 1 to login
4. Navigate through the menu-driven interface

**Default test credentials:** username: `admin`, password: `admin123`

## Academic Note

This project was developed as part of the Programming 1 course requirements, demonstrating object-oriented programming, file handling, exception management, and user input validation.

## Contact Information

**Team Members:**
- Baraza Brian
- Tako Nellyvine Mizero

**Facilitator:** Yoovin Porun
**Institution:** African Leadership College of Higher Education (ALCHE)
**Course:** Programming 1