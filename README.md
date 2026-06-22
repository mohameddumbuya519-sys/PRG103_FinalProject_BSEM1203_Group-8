Student Record Management System (Tkinter + JSON + Matplotlib)
Overview

This project is a desktop-based Student Record Management System built using Python. It provides a simple graphical user interface (GUI) for managing student records, including adding, updating, deleting, searching, and visualizing data using charts.

The system uses:

Tkinter for the GUI
JSON for data storage
Matplotlib for data visualization

Features
Login System
Secure admin login before accessing the dashboard
Default credentials:
Username
Password

Record Management
 Add new student records
 Update existing records
 Delete records
 Search records by ID, Name, Gender, or Status
 View all records in a table (Treeview)

 Data Visualization
 Bar Chart → Status distribution (Active, Pending, Inactive)
 Pie Chart → Gender distribution
 Line Graph → Student status trend visualization
 
 Technologies Used
 Tool	Purpose
 Python	Core programming language
 Tkinter	GUI development
 JSON	Data storage
 Matplotlib	Charts and graphs

 Project Structure
student-record-system
├── main.py              # Main application file
├── records.json         # Data storage file (auto-created)
└── README.md            # Project documentation

How to Run the Project
1. Install Requirements

Make sure Python is installed. Then install matplotlib:

pip install matplotlib
2. Run the Program
python main.py
 Data Storage

All student records are stored in a JSON file:


  {
    "ID": "1001",
    "Name": "John Kamara",
    "Gender": "Male",
    "Status": "Active"
 

 How It Works
The program starts with a login window
After successful login, the dashboard opens
Records are loaded from records.json
Any changes (add/update/delete) are automatically saved
Charts are generated dynamically using Matplotlib
 Sample Functional Flow

Login → Dashboard → Load Records → Manage Data → Save to JSON → Visualize Charts

Notes
Ensure records.json is in the same folder as main.py
If file does not exist, default sample data will be used automatically
GUI is built using Tkinter, so it works on Windows, Mac, and Linux
 Author
Developed using Python
Purpose: Educational project for structured programming and GUI development
License

This project is for educational use only.
