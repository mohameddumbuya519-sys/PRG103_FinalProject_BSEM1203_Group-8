import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# student data storage
students = []

# Predefined admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


# ==================== MAIN APPLICATION WINDOW ====================
class StudentSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")
        self.root.geometry("650x450")
        self.root.configure(bg="#F5F7FA")

        # Header Label
        header = tk.Label(root, text="STUDENT RECORD MANAGEMENT SYSTEM", font=("Helvetica", 16, "bold"), fg="#2C3E50",
                          bg="#F5F7FA")
        header.pack(pady=15)

        # --- Control Buttons Frame ---
        btn_frame = tk.Frame(root, bg="#F5F7FA")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Add Student", width=15, command=self.add_student, bg="#2ECC71", fg="Blue",
                  font=("Helvetica", 10, "bold"), bd=0, cursor="hand2", padx=5, pady=5).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="🔍 Search", width=15, command=self.search_student, bg="#3498DB", fg="Blue",
                  font=("Helvetica", 10, "bold"), bd=0, cursor="hand2", padx=5, pady=5).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🔄 Update", width=15, command=self.update_student, bg="#E67E22", fg="Blue",
                  font=("Helvetica", 10, "bold"), bd=0, cursor="hand2", padx=5, pady=5).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="❌ Delete", width=15, command=self.delete_student, bg="#E74C3C", fg="Blue",
                  font=("Helvetica", 10, "bold"), bd=0, cursor="hand2", padx=5, pady=5).grid(row=0, column=3, padx=5)

        # --- Data Table (Treeview) ---
        table_frame = tk.Frame(root, bg="#F5F7FA")
        table_frame.pack(pady=15, fill="both", expand=True, padx=20)

        columns = ("ID", "Name", "Age", "Course")

        # Style Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="Green", foreground="#333", rowheight=25, fieldbackground="white")
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#ECF0F1", foreground="#2C3E50")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Scrollbar for table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Initial refresh
        self.refresh_table()

    def refresh_table(self):
        """Clears and reloads data into the table view."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for s in students:
            self.tree.insert("", "end", values=(s["ID"], s["Name"], s["Age"], s["Course"]))

    def add_student(self):
        """Opens prompt dialogs to collect new student details."""
        sid = simpledialog.askstring("Input", "Enter Student ID:", parent=self.root)
        if not sid: return  # Cancelled

        if any(s["ID"] == sid for s in students):
            messagebox.showerror("Error", "A student with this ID already exists.")
            return

        name = simpledialog.askstring("Input", "Enter Student Name:", parent=self.root)
        if not name: return

        try:
            age = simpledialog.askinteger("Input", "Enter Age:", parent=self.root, minvalue=1, maxvalue=120)
            if not age: return
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid number.")
            return

        course = simpledialog.askstring("Input", "Enter Course:", parent=self.root)
        if not course: return

        students.append({"ID": sid, "Name": name, "Age": age, "Course": course})
        messagebox.showinfo("Success", "Student added successfully!")
        self.refresh_table()

    def search_student(self):
        sid = simpledialog.askstring("Search", "Enter Student ID to search:", parent=self.root)
        if not sid: return

        for s in students:
            if s["ID"] == sid:
                msg = f"Record Found!\n\nID: {s['ID']}\nName: {s['Name']}\nAge: {s['Age']}\nCourse: {s['Course']}"
                messagebox.showinfo("Search Result", msg)
                return
        messagebox.showwarning("Not Found", "Student not found.")

    def update_student(self):
        sid = simpledialog.askstring("Update", "Enter Student ID to update:", parent=self.root)
        if not sid: return

        for s in students:
            if s["ID"] == sid:
                new_name = simpledialog.askstring("Update", f"Enter new name ({s['Name']}):", parent=self.root)
                if new_name: s["Name"] = new_name

                new_age = simpledialog.askinteger("Update", f"Enter new age ({s['Age']}):", parent=self.root,
                                                  minvalue=1)
                if new_age: s["Age"] = new_age

                new_course = simpledialog.askstring("Update", f"Enter new course ({s['Course']}):", parent=self.root)
                if new_course: s["Course"] = new_course

                messagebox.showinfo("Success", "Record updated successfully.")
                self.refresh_table()
                return
        messagebox.showwarning("Not Found", "Student not found.")

    def delete_student(self):
        sid = simpledialog.askstring("Delete", "Enter Student ID to delete:", parent=self.root)
        if not sid: return

        for s in students:
            if s["ID"] == sid:
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {s['Name']}?")
                if confirm:
                    students.remove(s)
                    messagebox.showinfo("Success", "Record deleted successfully.")
                    self.refresh_table()
                return
        messagebox.showwarning("Not Found", "Student not found.")


# ==================== MODERN LOGIN WINDOW ====================
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure System Login")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        # Color Palette
        self.bg_color = "#2C3E50"  # Dark slate blue
        self.card_color = "#FFFFFF"  # White container
        self.accent_color = "#3498DB"  # Bright corporate blue
        self.text_muted = "#7F8C8D"  # Gray text

        # Window Background
        self.root.configure(bg=self.bg_color)

        # Main login container card
        card_frame = tk.Frame(root, bg=self.card_color, bd=0, relief="flat")
        card_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=340)

        # Header Typography
        tk.Label(card_frame, text="ADMIN LOGIN", font=("Helvetica", 16, "bold"),
                 bg=self.card_color, fg=self.bg_color).pack(pady=(25, 5))

        tk.Label(card_frame, text="Sign in to manage records", font=("Helvetica", 9),
                 bg=self.card_color, fg=self.text_muted).pack(pady=(0, 20))

        # Input Form Layout
        # --- Username ---
        lbl_user = tk.Label(card_frame, text="Username", font=("Helvetica", 10, "bold"),
                            bg=self.card_color, fg=self.bg_color)
        lbl_user.pack(anchor="w", padx=25, pady=(5, 2))

        self.username_entry = tk.Entry(card_frame, font=("Helvetica", 11), bg="#F2F4F4",
                                       bd=0, highlightthickness=1, highlightbackground="#BDC3C7",
                                       highlightcolor=self.accent_color)
        self.username_entry.pack(fill="x", padx=25, ipady=6)
        self.username_entry.focus()

        # --- Password ---
        lbl_pass = tk.Label(card_frame, text="Password", font=("Helvetica", 10, "bold"),
                            bg=self.card_color, fg=self.bg_color)
        lbl_pass.pack(anchor="w", padx=25, pady=(15, 2))

        self.password_entry = tk.Entry(card_frame, font=("Helvetica", 11), show="*", bg="#F2F4F4",
                                       bd=0, highlightthickness=1, highlightbackground="#BDC3C7",
                                       highlightcolor=self.accent_color)
        self.password_entry.pack(fill="x", padx=25, ipady=6)

        # Bind Enter key to instantly submit login info
        self.root.bind('<Return>', lambda event: self.validate_login())

        # --- Modern Flat Button ---
        self.login_btn = tk.Button(card_frame, text="Login Securely", font=("Helvetica", 11, "bold"),
                                   bg=self.accent_color, fg="Blue", bd=0, cursor="hand2",
                                   activebackground="#2980B9", activeforeground="Blue",
                                   command=self.validate_login)
        self.login_btn.pack(fill="x", padx=25, pady=(30, 0), ipady=8)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Close the login window

            # Open the main management window
            main_window = tk.Tk()
            app = StudentSystemApp(main_window)
            main_window.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password.")


# ==================== START EXECUTION ====================
if __name__ == "__main__":
    login_root = tk.Tk()
    login_screen = LoginWindow(login_root)
    login_root.mainloop()
