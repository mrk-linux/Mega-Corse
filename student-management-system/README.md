# 🎓 Student Management System

This project is a **Student Management System** built with PyQt6 and SQLite. It allows you to manage student records with a graphical user interface.

---

## 🚀 Features

- View all students in a table
- Add new students to the database
- Edit existing student records
- Delete student records
- Search for students by name
- About dialog with app information
- Status bar with edit and delete buttons
- Toolbar for quick actions

---

## 📁 Project Structure

```
Student_Management/
├── main.py               # Main application script
├── database.db           # SQLite database file
└── icons/                # Icon files
    ├── add.png
    └── search.png
```

---

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install PyQt6
```

---

## 🗄️ Database Setup

The application uses SQLite. Create a database with the following table:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    mobile TEXT NOT NULL
);
```

---

## ▶️ Usage

Run the script from the terminal:

```bash
python main.py
```

### Main Features:

1. **Add Student**: Click the "Add Student" button or use File menu
2. **Edit Student**: Click on a row, then click "Edit Record" in status bar
3. **Delete Student**: Click on a row, then click "Delete Record" in status bar
4. **Search Student**: Use Edit menu or toolbar search button
5. **About**: Help menu → About

---

## 🧠 How It Works

1. The application connects to an SQLite database
2. Student data is displayed in a QTableWidget
3. CRUD operations (Create, Read, Update, Delete) are performed through dialogs
4. The status bar shows edit/delete buttons when a row is selected
5. Toolbar provides quick access to main actions

---

## 📌 Notes

- Make sure the `icons` folder exists with `add.png` and `search.png` icons
- The database file `database.db` will be created automatically
- Default courses: Biology, Math, Astronomy, Physics

---

## 🔧 Suggested Improvements

- [ ] Add validation for mobile number format
- [ ] Add email field to student records
- [ ] Export data to CSV or Excel
- [ ] Add print functionality
- [ ] Add dark/light theme toggle
- [ ] Add pagination for large datasets

---

## 👨‍💻 Developer

- Name: alimrk
- GitHub: [https://github.com/mrk-linux](https://github.com/mrk-linux)

---

## 📄 License

This project is released under the **MIT** license.

---

**Made with ❤️ in Iran**