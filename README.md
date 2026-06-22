📚 Student Record Management System (Tkinter + JSON)

A simple desktop-based Student Record Management System built using Python Tkinter for the GUI and JSON file storage for persistent data management.

🚀 Features
🔐 Admin Login System
➕ Add new students
🔍 Search student records
✏ Update student information
🗑 Delete student records
📊 Dashboard with total student count
💾 Automatic data saving using JSON file
🎨 Modern dark-themed GUI (Tkinter)
🛠 Technologies Used
Python 3
Tkinter (GUI framework)
JSON (Data storage)
OS module (file handling)
📁 Project Structure
Student-Record-System/
│
├── main.py              # Main application file
├── students.json        # Auto-created data storage file
└── README.md            # Project documentation
⚙️ How It Works
The program starts with a Login Screen
Admin enters username and password:
Username: admin
Password: password123
If login is successful, the Dashboard opens
All student data is:
Stored in memory (Python list)
Saved permanently in students.json
▶️ How to Run the Project
1. Install Python

Make sure Python 3 is installed:

python --version
2. Run the program
python main.py
👤 Default Login Credentials
Username: admin
Password: password123
💾 Data Storage (JSON)

Student data is saved in students.json like this:

[
    {
        "ID": "1",
        "Name": "John",
        "Age": 20,
        "Course": "Computer Science"
    }
]
🧩 Core Functionalities
➕ Add Student
Enter ID, Name, Age, Course
Data is saved automatically
🔍 Search Student
Search using Student ID
Displays full record
✏ Update Student
Modify existing student details
🗑 Delete Student
Remove student by ID
🎨 UI Overview
Dark modern dashboard theme
Sidebar navigation menu
Table view for student records
Clean form-based input system
📌 Future Improvements
📊 Add charts and analytics dashboard
🗄 Upgrade to SQLite or MySQL database
🌐 Convert into a web application (Flask/Django)
👥 Add multiple user roles (Admin, Teacher, Student)
📄 Export data to PDF/Excel
👨‍💻 Author

Developed as a learning project using Python Tkinter.

📜 License

This project is for educational purposes only.b
