# Calculator Application (Python Tkinter + SQLite)

## Project Overview

This is a desktop calculator application developed using Python. The application provides a graphical user interface using Tkinter and stores calculation history using SQLite. The project follows a modular structure consisting of UI, logic, and database layers.

The main purpose of this project is to demonstrate basic software development concepts including GUI design, event handling, database integration, and separation of concerns.

---

## Features

- Multi-screen interface (Home, Calculator, History)
- Basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Modulus
  - Power
- Persistent history storage using SQLite
- Input validation and error handling
- Navigation between different screens

---

## Project Structure

CalculatorProject/

├── main.py  
├── ui/  
│   └── calculator_ui.py  
├── logic/  
│   └── calculator_logic.py  
├── database/  
│   └── db.py  
├── history.db  
└── README.md  

---

## System Architecture

UI Layer (Tkinter)
        ↓
Logic Layer (Arithmetic Operations)
        ↓
Database Layer (SQLite Storage)

---

## Team Members and Contributions

- Minahil: User interface design and multi-screen navigation
- Eman: Implementation of calculator logic and operations
- Hamna: Database handling and history management

---

## How to Run the Project

1. Clone the repository:
   git clone https://github.com/your-username/CalculatorProject.git

2. Navigate to the project directory:
   cd CalculatorProject

3. Run the application:
   python main.py

---

## Database Structure

Table: history

- id: Integer, primary key, auto increment
- expression: Text, stores the arithmetic expression
- result: Text, stores the calculated result

---

## Learning Outcomes

- Understanding of Python GUI development using Tkinter
- Implementation of modular programming
- Basic database operations using SQLite
- Team collaboration using Git and GitHub
- Handling merge conflicts in collaborative development

---

## Future Improvements

- Scientific calculator functionality
- Improved UI design
- Dark mode interface
- Export history feature
- Better input validation and exception handling

---
