# 🏥 Clinic Management System

A simple **Clinic Management System** built using **Python** and **MySQL** that allows users to manage patient appointments through a command-line interface (CLI).

This project demonstrates the implementation of **CRUD (Create, Read, Update, Delete)** operations using Python and MySQL Connector.

---

## 📌 Features

* Add new patient appointments
* View all appointments
* Search appointment by Patient ID
* Update existing appointments
* Delete appointments
* Automatic Patient ID generation
* MySQL database integration
* Simple and user-friendly command-line interface

---

# 📂 Project Structure

```
Clinic-Management-System/
│
├── clinic.py          # Main application
├── README.md          # Project documentation
└── LICENSE            # MIT License
```

---

# 🛠 Technologies Used

* Python 3.x
* MySQL
* mysql-connector-python
* Command Line Interface (CLI)

---

# ⚙ Requirements

Install Python dependencies:

```bash
pip install mysql-connector-python
```

Install MySQL Server and create a database.

---

# 🗄 Database Setup

Create the database:

```sql
CREATE DATABASE appointment_booking_system;

USE appointment_booking_system;
```

Create the appointments table:

```sql
CREATE TABLE appointments(
    Patient_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Age INT,
    Contact VARCHAR(15),
    Reason_of_visit VARCHAR(255),
    Appointment_Time VARCHAR(20)
);
```

---

# ▶ Running the Project

Clone the repository:

```bash
git clone https://github.com/vaibhavbarod901/Clinic-Management-System.git
```

Go to the project folder:

```bash
cd Clinic-Management-System
```

Run the program:

```bash
python clinic.py
```

---

# 📋 Menu

```
Welcome to the Clinic

1. Add Appointment
2. Show Appointment
3. Check Appointment
4. Update Appointment
5. Delete Appointment
6. Exit
```

---

# 📷 Example Output

```
Appointment added successfully!

Patient ID : 1
Name       : Vaibhav
Age        : 19
Contact    : 9876543210
Reason     : Fever
Time       : 10:30 AM
```

---

# 🔄 CRUD Operations

### Create

* Add new appointment

### Read

* Display all appointments
* Search appointment by Patient ID

### Update

* Modify patient information

### Delete

* Remove patient appointment

---

# 🚀 Future Improvements

* Graphical User Interface (Tkinter)
* Login Authentication
* Doctor Management
* Appointment Scheduling Calendar
* SMS/Email Notifications
* Billing System
* Prescription Management
* Patient History
* Report Generation
* Flask or Django Web Version
* REST API Integration

---

# 📚 Learning Objectives

This project demonstrates:

* Python Programming
* Functions
* MySQL Database Connectivity
* SQL Queries
* CRUD Operations
* User Input Validation
* Database Transactions
* Command Line Applications

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📝 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

# © Copyright

**Copyright © 2026 Vaibhav Barod**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the conditions of the MIT License.

---

# ⚠ Disclaimer

This project is developed for **educational and learning purposes only**.

It is **not intended for use in real hospitals or healthcare environments** without implementing proper security, authentication, encryption, data validation, and compliance with applicable healthcare regulations.

---

# 👨‍💻 Author

**Vaibhav Barod**

* GitHub: https://github.com/vaibhavbarod901

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
