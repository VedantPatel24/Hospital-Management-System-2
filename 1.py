import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

# File paths
USER_FILE = "users.csv"
DOCTOR_FILE = "doctors.csv"
PATIENT_FILE = "patients.csv"
APPOINTMENT_FILE = "appointments.csv"
ADMIN_FILE = "admin.csv"

# Initialize admin file with a default admin user
def initialize_admin():
    if not os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["admin", "admin123"])  # Predefined admin credentials
            

def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []  # Return an empty list instead of an error
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Write to CSV file
def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# User registration
def register_user():

    if os.path.exists(USER_FILE):
        users = read_csv(USER_FILE)
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if username already exists
        for user in users:
            if user[0] == username:
                print("Username already exists. Try again.")
                return

        users.append([username, password])
        write_csv(USER_FILE, users)
        print("User registered successfully! Please login.")
    else:
        file=open(USER_FILE,'w')
        username = input("Enter username: ")
        password = input("Enter password: ")
        writer = csv.writer(file)
        writer.writerow([username,password])

# User login
def login_user():
    users = read_csv(USER_FILE)
    admin_data = read_csv(ADMIN_FILE)

    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            # Check admin credentials first
            if [username, password] in admin_data:
                print("Admin login successful! Accessing admin menu...")
                admin_menu()
                return
            
            # Then check user credentials
            print(users)
            if os.path.exists(USER_FILE) and [username, password] in users:
                print("Login successful! Accessing user menu...")
                user_menu()
                return

            print("Invalid credentials, try again.")

        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Exiting program...")
            return


        

# Admin menu (doctor management)
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Appointments per Doctor")
        print("6. Patients per Doctor")
        print("7. Appointments Over Time")
        print("8. Gender Distribution of Patients")
        print("9. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_doctors()
        elif choice == "3":
            update_doctor()
        elif choice == "4":
            delete_doctor()
        elif choice == "5":
            plot_appointments_per_doctor()
        elif choice == "6":
            plot_patients_per_doctor()
        elif choice == "7":
            plot_appointments_over_time()
        elif choice == "8":
            plot_gender_distribution()
        elif choice == "9":
            print("Logging out...")
            login_user()
            break
        else:
            print("Invalid choice, try again.")

# User menu (patient & appointment management)
def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Add Appointment")
        print("6. View Appointments")
        print("7. Update Appointment")
        print("8. Delete Appointment")
        print("9. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            add_appointment()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            update_appointment()
        elif choice == "8":
            delete_appointment()
        elif choice == "9":
            print("Logging out...")
            login_user()
            break
        else:
            print("Invalid choice, try again.")

# Doctor operations
def add_doctor():
    while True:
        try:
            doctors = read_csv(DOCTOR_FILE)
            name = input("Enter doctor's name: ")
            specialty = input("Enter specialty: ")
            phone = int(input("Enter phone number: "))
            if len(str(phone))!=10:
                print("Phone number not entered Properly")
                break
            doctor_id = str(len(doctors) + 1)
            doctors.append([doctor_id, name, specialty, phone])
            write_csv(DOCTOR_FILE, doctors)
            print("Doctor added successfully!")
            break
        except Exception as e:
            print(e)   

def view_doctors():
    doctors = read_csv(DOCTOR_FILE)
    for doctor in doctors:
        print(doctor)

def update_doctor():
    doctors = read_csv(DOCTOR_FILE)
    doctor_id = input("Enter doctor ID to update: ")
    if(doctor_id in doctors[0]):
        for doctor in doctors:
            try:
                if doctor[0] == doctor_id:
                    doctor[1] = input("Enter new name: ") or doctor[1]
                    doctor[2] = input("Enter new specialty: ") or doctor[2]
                    doctor[3] = int(input("Enter new phone: ")) or doctor[3]
                    if len(str(doctor[3]))!=10:
                        print("Phone number not entered Properly")
                        break
                    write_csv(DOCTOR_FILE, doctors)
                    print("Doctor updated successfully!")
                    break
            except Exception as e:
                print(e)    
    else:            
        print("Doctor ID not found.")

def delete_doctor():
    doctors = read_csv(DOCTOR_FILE)
    doctor_id = input("Enter doctor ID to delete: ")

    for doctor in doctors:
        if (doctor[0]==doctor_id):
            updated_doctors = [row for row in doctors if row[0] != doctor_id]
            write_csv(DOCTOR_FILE, updated_doctors)
            print("Doctor deleted successfully!")
            break  
        else:
            continue
    else:
        print("Invalid Doctor Id") 



# Appointments per Doctor
def plot_appointments_per_doctor():
    appointments = read_csv(APPOINTMENT_FILE)
    if not appointments:
        print("No appointment data available.")
        return

    doctor_appointments = Counter([appointment[2] for appointment in appointments])

    plt.figure(figsize=(8, 6))
    plt.bar(doctor_appointments.keys(), doctor_appointments.values(), color='skyblue')
    plt.xlabel("Doctor ID")
    plt.ylabel("Number of Appointments")
    plt.title("Appointments per Doctor")
    plt.show()

# Patients per Doctor
def plot_patients_per_doctor():
    patients = read_csv(PATIENT_FILE)
    if not patients:
        print("No patient data available.")
        return

    doctor_patients = Counter([patient[4] for patient in patients])

    plt.figure(figsize=(8, 6))
    plt.bar(doctor_patients.keys(), doctor_patients.values(), color='lightcoral')
    plt.xlabel("Doctor ID")
    plt.ylabel("Number of Patients")
    plt.title("Patients per Doctor")
    plt.xticks(rotation=45)
    plt.show()

# Appointments Over Time
def plot_appointments_over_time():
    appointments = read_csv(APPOINTMENT_FILE)
    if not appointments:
        print("No appointment data available.")
        return

    dates = [appointment[3] for appointment in appointments]
    date_counts = Counter(dates)
    
    sorted_dates = sorted(date_counts.keys())
    counts = [date_counts[date] for date in sorted_dates]

    plt.figure(figsize=(8, 6))
    plt.plot(sorted_dates, counts, marker='o', linestyle='-', color='green')
    plt.xlabel("Date")
    plt.ylabel("Number of Appointments")
    plt.title("Appointments Over Time")
    plt.xticks(rotation=90)
    plt.show()

# Gender Distribution of Patients
def plot_gender_distribution():
    patients = read_csv(PATIENT_FILE)
    if not patients:
        print("No patient data available.")
        return

    genders = [patient[3].upper() for patient in patients]
    gender_counts = Counter(genders)

    plt.figure(figsize=(8, 6))
    plt.pie(gender_counts.values(), labels=gender_counts.keys(), autopct='%1.1f%%', startangle=140, colors=['blue', 'pink'])
    plt.title("Gender Distribution of Patients")
    plt.show()


# Patient operations

def add_patient():
    while True:
        try:
            patients = read_csv(PATIENT_FILE)
            name = input("Enter patient's name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender(M/F): ")
            if gender not in 'MmFf':
                print("Gender not Entered Properly")
                break
            doctor_id = input("Enter assigned doctor ID: ")
            
            if doctor_exists(doctor_id):
                patient_id = str(len(patients) + 1)
                patients.append([patient_id, name, age, gender, doctor_id])
                write_csv(PATIENT_FILE, patients)
                print("Patient added successfully!")
                break
            else:
                print("Invalid Doctor ID.")
                break
        except Exception as e:
            print(e)        

def view_patients():
    patients = read_csv(PATIENT_FILE)
    for patient in patients:
        print(patient)

def update_patient():
    patients = read_csv(PATIENT_FILE)
    patient_id = input("Enter patient ID to update: ")

    if(patient_id in patients[0]):
        for patient in patients:
            print(patient)
            if patient[0] == patient_id:
                patient[1] = input("Enter new name: ") or patient[1]
                patient[2] = input("Enter new age: ") or patient[2]
                patient[3] = input("Enter new gender: ") or patient[3]
                if patient[3] not in 'MmFf':
                    print("Gender not Entered Properly")
                    break
                patient[4] = input("Enter new doctor ID: ") or patient[4]
                if (doctor_exists(patient[4])):
                    write_csv(PATIENT_FILE, patients)
                    print("Patient updated successfully!")
                    return
                else:
                    print("Invalid Doctor ID.")
                    break
    else:
        print("Patient ID not found.")

def delete_patient():
    patients = read_csv(PATIENT_FILE)
    patient_id = input("Enter patient ID to delete: ")


    for patient in patients:
        if (patient[0]==patient_id):
            updated_patients = [row for row in patients if row[0] != patient_id]
            write_csv(PATIENT_FILE, updated_patients)
            print("Patient deleted successfully!")
            break  
        else:
            continue
    else:
        print("Invalid Patient Id") 


# Appointment operations

def add_appointment():
    appointments = read_csv(APPOINTMENT_FILE)
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    
    if doctor_exists(doctor_id) and patient_exists(patient_id):
        while True:
            try:
                # Get user input
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                appointment_time = input("Enter appointment time (HH:MM, 24-hour format): ")
                
                # Combine date and time into a full datetime object
                appointment_datetime = datetime.strptime(appointment_date + " " + appointment_time, "%Y-%m-%d %H:%M")

                # Get the current datetime
                current_datetime = datetime.now()

                # Check if the entered datetime is in the future
                if appointment_datetime > current_datetime:
                    print("Appointment scheduled successfully!")
                    status = "Scheduled"
                    appointment_id = str(len(appointments) + 1)
                    appointments.append([appointment_id, patient_id, doctor_id, appointment_date, appointment_time, status])
                    write_csv(APPOINTMENT_FILE, appointments)
                    print("Appointment added successfully!")
                    break  # Exit loop if valid
                else:
                    print("Error: The appointment date and time must be in the future. Please try again.")

            except ValueError:
                print("Invalid format! Please enter date as YYYY-MM-DD and time as HH:MM (24-hour format).")
    else:
        print("Invalid Doctor ID OR Invalid Patient ID")

def view_appointments():
    appointments = read_csv(APPOINTMENT_FILE)
    for appointment in appointments:
        print(appointment)

def update_appointment():
    appointments = read_csv(APPOINTMENT_FILE)
    appointment_id = input("Enter appointment ID to update: ")

    for appointment in appointments:
        print(appointment[0])
        if(appointment_id != appointment[0]):
            print("Appointment Id Not Found!!!")
        else:    
            try:
                if appointment[0] == appointment_id:
                    appointment[3] = input("Enter new date: ") or appointment[3]
                    appointment[4] = input("Enter new time: ") or appointment[4]
                
                    appointment_datetime = datetime.strptime(appointment[3] + " " + appointment[4], "%Y-%m-%d %H:%M")
                    current_datetime = datetime.now()
                    if appointment_datetime > current_datetime:
                        print("Appointment Re-Scheduled successfully!")
                        break 
                    else:
                        print("Error: The appointment date and time must be in the future. Please try again.")

            except ValueError:
                print("Invalid format! Please enter date as YYYY-MM-DD and time as HH:MM (24-hour format).")

                appointment[5] = "Re-Scheduled"
                write_csv(APPOINTMENT_FILE, appointments)
                print("Appointment updated successfully!")
                break

def delete_appointment():
    appointments = read_csv(APPOINTMENT_FILE)
    appointment_id = input("Enter appointment ID to delete: ")

    for appointment in appointments:
        if (appointment[0]==appointment_id):
            updated_appointments = [row for row in appointments if row[0] != appointment_id]
            write_csv(APPOINTMENT_FILE, updated_appointments)
            print("Appointment deleted successfully!")
            break  
        else:
            continue
    else:
        print("Invalid Appointment Id")    


# Utility function to check doctor existence
def doctor_exists(doctor_id):
    doctors = read_csv(DOCTOR_FILE)
    for doctor in doctors:
        if doctor[0] == doctor_id:
            return True
    return False

# Utility function to check patient existence
def patient_exists(patient_id):
    patients = read_csv(DOCTOR_FILE)
    for patient in patients:
        if patient[0] == patient_id:
            return True
    return False



initialize_admin()
login_user()

