# GUI-based-Cashmemo-App-Using-OOP-Concepts-in-Python

This project implements a Cash Memo system using Python and Tkinter for GUI development. It allows users to input customer details, purchase items, generate a bill, and optionally print it to a PDF.

## Youtube
Here is the youtube video link that explains te code: https://youtu.be/4soRDhU4RBE

## Features

- **Customer Information**: Collects customer details including serial number, name, and address.
- **Product Details**: Enables adding, editing, and deleting items with particulars, rate, and quantity.
- **Generate Cash Memo**: Creates a formatted cash memo with a total amount calculation.
- **Print to PDF**: Converts the cash memo into a PDF document for easy printing.

## Libraries Used

- **Tkinter**: Python's de-facto standard GUI (Graphical User Interface) package.
- **ReportLab**: Used for generating PDFs programmatically.
- **CustomTkinter (ctk)**: A custom library (assumed to enhance Tkinter) for creating more aesthetically pleasing GUI components.

#  Object-Oriented Programming (OOP) Concepts

## Classes Overview

### Date Class

- Manages date information for the cash memo.
- Ensures validity of date entries (day, month, year).
- Provides string representation in a readable format.

### Name Class

- Stores customer's first and last names.
- Implements proper casing of names for consistent formatting.

### Address Class

- Holds details about the customer's address (house number, street, town, city).
- Provides a formatted string representation of the address.

### Object Class

- Represents purchased items with attributes for quantity, particulars, and rate.
- Calculates the total amount for each item based on quantity and rate.

### CashMemo Class

- Aggregates customer information (Date, Name, Address) and purchased items (Object).
- Calculates the total amount of the bill.
- Provides a formatted string representation of the cash memo for display.

### CashMemoApp Class

- Inherits from CashMemo to extend functionalities for GUI interaction.
- Implements tkinter-based GUI for user input and interaction.
- Supports operations such as adding, editing, deleting items, and generating bills.

## Key OOP Concepts Demonstrated

- **Encapsulation**: Private attributes (`__attribute`) and methods ensure controlled access and modification of class data.
  
- **Inheritance**: The `CashMemo` class inherits attributes and methods from other classes, facilitating code reuse and maintaining a hierarchical structure.

- **Polymorphism**: Method overriding (`__repr__` methods) provides specific representations of data based on context.

- **Abstraction**: The `CashMemoApp` class abstracts underlying complexities by providing a user-friendly GUI interface.

- **Association**: The relationship between `CashMemoApp` and `CashMemo` classes allows interactive bill generation and display.

# Dependencies for Cash Memo System

## Python Libraries

- **tkinter**: Python's de-facto standard GUI (Graphical User Interface) package.
  - Used for creating the graphical user interface (GUI) of the Cash Memo application.
  - Documentation: [tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

- **reportlab**: A library for generating PDF documents programmatically.
  - Used to create PDF versions of the generated cash memos.
  - Documentation: [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)

- **customtkinter**: Custom library for enhancing GUI elements (assuming it's a custom module used in the project).
  - Enhances the appearance and functionality of tkinter-based GUI elements.
  - Custom implementation provided in the project.


To install these dependencies, make sure you have Python installed on your system. You can install additional packages using pip, the Python package installer.

Example installation commands:
```bash
pip install reportlab tkinter customtkinter
   ```

## Usage
To run the Cash Memo System:
1. Ensure Python and tkinter are installed.
2. Execute `cashmemo_gui.py` to launch the GUI application.
3. Enter customer details, add purchased items, and generate bills with options to print to terminal or PDF.
4. **Setup**: Ensure Python and necessary libraries (`tkinter`, `reportlab`, `customtkinter`) are installed.
5. **Run the Application**:
   python cashmemo.py
## Future Enhancements

- Improve error handling and input validation in GUI.
- Enhance PDF generation with more styling and customization options.
- Extend functionalities to support database integration for storing and retrieving customer data.

By following Object-Oriented Programming principles, the Cash Memo System achieves modularity, extensibility, and maintainability, making it suitable for further development and customization.

##Screenshots
![sssp1](https://github.com/muqniturrehman/GUI-based-Cashmemo-App-Using-OOP-Concepts-in-Python/assets/171343101/44a05062-a01b-47d6-bd9e-270c28b4a7de)
![sp3](https://github.com/muqniturrehman/GUI-based-Cashmemo-App-Using-OOP-Concepts-in-Python/assets/171343101/5aa1534d-a006-4ff0-b5dc-79d16519a9ca)
![ssp2](https://github.com/muqniturrehman/GUI-based-Cashmemo-App-Using-OOP-Concepts-in-Python/assets/171343101/fcf8ec86-281f-48fe-a50f-65a46c81dfb1)
