from datetime import datetime
import mysql.connector as myconn

mydb = myconn.connect(
    host="localhost",   
    user="root",
    password="Barod@7766",
    database="appointment_booking_system"
)

db_cursor = mydb.cursor()


def menu():
    while True:
        print("\nWelcome to the clinic")
        print("1. Add appointment")
        print("2. Show appointment") 
        print("3. Check appointment")
        print("4. Update appointment")                  
        print("5. Delete appointment")
        print("6. Exit")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            add_appointment() 
        elif choice == "2":
            show_appointment() 
        elif choice == "3":
            check_appointment() 
        elif choice == "4":
            update_appointment()   
        elif choice == "5":
            delete_appointment()                                                    
        elif choice == "6":
            print("Thank you for using the clinic system.")
            break
        else:
            print("Invalid choice")

        more = input("\nDo you want to continue? (y/n): ")       
        if more.lower() != "y":
            print("Goodbye!")
            break


def add_appointment():

    Name = input("Enter Name: ")
    Age = int(input("Enter Age: "))
    Contact = input("Enter Contact Number: ")
    Reason_of_visit = input("Enter Reason of visit: ")
    time = input("Enter Appointment Time: ")

    print("Select Time Format")
    print("1. AM")
    print("2. PM")

    option = input("Enter choice: ")

    if option == "1":
        appointment_time = time + " AM"
    elif option == "2":
        appointment_time = time + " PM"
    else:
        print("Invalid option")
        return

    query = """
    INSERT INTO appointments
    (Name, Age, Contact, Reason_of_visit, Appointment_Time)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (Name, Age, Contact, Reason_of_visit, appointment_time)

    db_cursor.execute(query, values)
    mydb.commit()

    patient_id = db_cursor.lastrowid

    print("\nAppointment added successfully!")
    print(f"Patient ID: {patient_id}")
    print(f"Name: {Name}")
    print(f"Age: {Age}")
    print(f"Contact: {Contact}")
    print(f"Reason: {Reason_of_visit}")
    print(f"Time: {appointment_time}")


def show_appointment():
    query = "SELECT * FROM appointments"
    db_cursor.execute(query)
    records = db_cursor.fetchall()

    print("\nAll Appointments:\n")

    for row in records:
        print(f"Patient ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Age: {row[2]}")
        print(f"Contact: {row[3]}")
        print(f"Reason: {row[4]}")
        print(f"Time: {row[5]}")
        print("-" * 20)


def check_appointment():
    ID = int(input("Enter Patient ID to search: "))

    query = "SELECT * FROM appointments WHERE Patient_ID=%s"
    db_cursor.execute(query, (ID,))
    details = db_cursor.fetchone()

    if details:
        print("\nAppointment Details:")
        print(f"Patient ID: {details[0]}")
        print(f"Name: {details[1]}")
        print(f"Age: {details[2]}")
        print(f"Contact: {details[3]}")
        print(f"Reason: {details[4]}")
        print(f"Time: {details[5]}")
    else:
        print("No appointment found.")


def update_appointment():

    ID = int(input("Enter Patient ID to update: "))

    Name = input("Enter new Name: ")
    Age = int(input("Enter new Age: "))
    Contact = input("Enter new Contact Number: ")
    Reason = input("Enter new Reason of visit: ")
    time = input("Enter Appointment Time: ")

    print("Select Time Format")
    print("1. AM")
    print("2. PM")

    option = input("Enter choice: ")

    if option == "1":
        appointment_time = time + " AM"
    elif option == "2":
        appointment_time = time + " PM"
    else:
        print("Invalid option")
        return

    query = """
    UPDATE appointments
    SET Name=%s, Age=%s, Contact=%s, Reason_of_visit=%s, Appointment_Time=%s
    WHERE Patient_ID=%s
    """

    values = (Name, Age, Contact, Reason, appointment_time, ID)

    db_cursor.execute(query, values)
    mydb.commit()

    print("Appointment updated successfully!")


def delete_appointment():

    ID = int(input("Enter Patient ID to delete: "))

    query = "DELETE FROM appointments WHERE Patient_ID=%s"

    db_cursor.execute(query, (ID,))
    mydb.commit()

    print("Appointment deleted successfully!")


menu()

db_cursor.close()
mydb.close()

print("Thank you for using the clinic. Goodbye!")