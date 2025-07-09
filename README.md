# 🏥 Hospital Management System (Python Console App + WhatsApp Notification)

This is a fully console-based Hospital Management System written in Python. It uses CSV files for storing data and features separate login systems for Admin and User roles. The system also integrates Twilio API to send WhatsApp notifications to users when an appointment is successfully booked.

---

## ⚙️ Tech Stack

- **Language**: Python 3.x
- **Interface**: Console-based
- **Storage**: CSV files
- **Notification API**: Twilio (for WhatsApp messages)

---

## 🔐 Features

### 👨‍⚕️ Admin Menu

1. Add Doctor  
2. View Doctors  
3. Update Doctor  
4. Delete Doctor  
5. View Appointments per Doctor  
6. View Patients per Doctor  
7. Appointments Over Time (Analytics)  
8. Gender Distribution of Patients (Analytics)  
9. Logout  

### 👤 User Menu

1. Add Patient  
2. View Patients  
3. Update Patient  
4. Delete Patient  
5. Add Appointment  
6. View Appointments  
7. Update Appointment  
8. Delete Appointment  
9. Logout  

✅ **Bonus**:  
✔ WhatsApp Notification via Twilio when a user books an appointment.

---

## 📲 WhatsApp Integration (via Twilio)

- Twilio's API is used to send WhatsApp messages when appointments are booked.
- Users receive real-time booking confirmations with details such as doctor name, time, and patient name.

### 🔧 Twilio Setup

1. Create a Twilio account and get a trial WhatsApp-enabled number.
2. Install Twilio Python SDK:
   ```bash
   pip install twilio
