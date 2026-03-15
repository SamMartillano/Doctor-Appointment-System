

#=========================================================
# Doctor Appointment System
# Submitted by: Martillano, Samantha Allyson T.
# Description: A simple doctor appointment booking system
#
#=========================================================


import os
import random
from fpdf import FPDF
from playsound import playsound
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext 

# === Doctor Information & Categories === #

doctors = {

    "Pediatrician":["Dr. Mendoza", "Dr. Flores"],
    "Ophthalmologist":["Dr. Bautista", "Dr. Carmen"],
    "Cardiologist": ["Dr. Smith", "Dr. Wilson"],
    "General Physician": ["Dr. Robinson", "Dr. Campbell"],
    "Psychiatrist": ["Dr. Lim", "Dr. Fernandez"],
}

# === Schedule ( Days & Available Time Slots) === #

schedule = {
    "Monday": ["10:00 AM", "1:00 PM", "4:00 PM"],
    "Tuesday": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "Wednesday": ["8:00 AM", "2:00 PM", "5:00 PM"],
    "Thursday": ["9:00 AM", "11:30 AM", "1:00 PM"],
    "Friday": ["10:00 AM", "2:00 PM", "4:00 PM"],
}
     
#Global Variables
patient_doctor = ""
day_choice = ""
time_choice = ""
ticket_number = ""
played1 = False 
played2 = False 
played3 = False 
played4 = False 
played5 = False 
played6 = False 
    
# === Stored Book Appointments === #
patients = []

# === File Name === #
file_name = "your_appointment.pdf"

# === Main Menu Options === #

main_options = {
    "1": "View Available Doctors",
    "2": "Schedule an Appointment",
    "3":  "View Appointments",
    "4":  "Exit",
}

# ================================================
# Function: doctor() - DEPRECATED (Use GUI instead)
# ================================================
"""
def doctor():
  global patient_doctor, played1
  print("==============================================")
  print("               DOCTOR SELECTION               ")
  print("==============================================")
  print("1. Pediatrician")
  print("2. Ophthalmologist")
  print("3. Cardiologist")
  print("4. General Physician")
  print("5. Psychiatrist")
  print("==============================================")
  if not played1:
        playsound("doctor.wav")
        played1 = True
  doctor_category = input("Enter the number assigned to your chosen category (1-5): ")
  patient_doctor = ""


#======= Pediatrician ==========

  if doctor_category == "1":
     os.system('cls')
     print("1. Dr. Mendoza")
     print("2. Dr. Flores")
     doctor_choice = input("Choose your doctor (1-2): ")


     if doctor_choice == "1":
       patient_doctor = "Dr. Mendoza"
     elif doctor_choice == "2":
       patient_doctor = "Dr. Flores"
     else:
       print("Invalid Doctor Choice")

#======= Ophthalmologist ==========

  elif doctor_category == "2":
     os.system('cls')
     print("1. Dr. Bautista")
     print("2. Dr. Carmen")
     doctor_choice = input("Choose your doctor (1-2): ")
     

     if doctor_choice == "1":
       patient_doctor = "Dr. Bautista"
     elif doctor_choice == "2":
       patient_doctor = "Dr. Carmen"
     else:
       print("Invalid Doctor Choice")

#======= Cardiologist ==========

  elif doctor_category == "3":
     os.system('cls')
     print("1. Dr. Smith")
     print("2. Dr. Wilson")
     doctor_choice = input("Choose your doctor (1-2): ")
     
     if doctor_choice == "1":
       patient_doctor = "Dr. Smith"
     elif doctor_choice == "2":
       patient_doctor = "Dr. Wilson"
     else:
       print("Invalid Doctor Choice")

#======= General Physician ==========

  elif doctor_category == "4":
     os.system('cls')
     print("1. Dr. Robinson")
     print("2. Dr. Campbell")
     doctor_choice = input("Choose your doctor (1-2): ")
     
     if doctor_choice == "1":
       patient_doctor = "Dr. Robinson"
     elif doctor_choice == "2":
       patient_doctor = "Dr. Campbell"
     else:
       print("Invalid Doctor Choice")

#======= Psychiatrist ==========

  elif doctor_category == "5":
     os.system('cls')
     print("1. Dr. Lim")
     print("2. Dr. Fernandez")
     doctor_choice = input("Choose your doctor (1-2): ")
     
     if doctor_choice == "1":
       patient_doctor = "Dr. Lim"
     elif doctor_choice == "2":
       patient_doctor = "Dr. Fernandez"
     else:
       print("Invalid Doctor Choice")
 
  else:
    print("Invalid Input. Please Enter a Number Between 1-5: ")

  if patient_doctor:
    print(f"\nYou successfully selected: {patient_doctor}")

  input("\nPress Enter to return to the main menu...")
"""


# ================================================
# Function: schedule() - DEPRECATED (Use GUI instead)
# ================================================
"""
def schedule():
    global day_choice, time_choice, played2 
    os.system('cls')
    print("==============================================")
    print("          SCHEDULE AN APPOINTMENT             ")
    print("==============================================")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("==============================================")
    if not played2:
          playsound("schedule.wav")
          played2 = True
    day_input = input("Enter the number assigned to your chosen day (1-5): ")
    time_choice = ""

#====================================================
    if day_input == "1":
       day_choice = "Monday"
       os.system('cls')
       print("\nAvailable Time Slots For Monday:")
       print("1. 10:00 AM")
       print("2. 1:00 PM")
       print("3. 4:00 PM")
    
       time_input = input("Please select your preferred time (1-3): ")

       if time_input =="1":
        time_choice = "10: 00 AM"
       elif time_input == "2":
        time_choice = "1:00 PM"
       elif time_input == "3":
        time_choice = "4:00 PM"
       else:
        print("Invalid Time Selection")
        input("\nPress Enter to return to the main menu...")
        return

       print(f"\nYou have selected: {day_choice}, {time_choice}")
       input("\nPress Enter to return to the main menu...")


#==================================================
   
    elif day_input == "2":
       day_choice = "Tuesday"
       os.system('cls')
       print("\nAvailable Time Slots For Tuesday:")
       print("1. 9:00 AM")
       print("2. 11:00 AM")
       print("3. 2:00 PM")
    
       time_input = input("Please select your preferred time (1-3): ")

       if time_input == "1":
        time_choice = "9:00 AM"
       elif time_input == "2":
        time_choice = "11:00 AM"
       elif time_input == "3":
        time_choice = "2:00 PM"
       else:
        print("Invalid Time Selection")
        input("\nPress Enter to return to the main menu...")
        return

       print(f"\nYou have selected: {day_choice}, {time_choice}")
       input("\nPress Enter to return to the main menu...")
#====================================================

    elif day_input == "3":
       day_choice = "Wednesday"
       os.system('cls')
       print("\nAvailable Time Slots For Wednesday:")
       print("1. 8:00 AM")
       print("2. 2:00 PM")
       print("3. 5:00 PM")
    
       time_input = input("Please select your preferred time (1-3): ")

       if time_input == "1":
        time_choice = "8:00 AM"
       elif time_input == "2":
        time_choice = "2:00 PM"
       elif time_input == "3":
        time_choice = "5:00 PM"
       else:
        print("Invalid Time Selection")
        input("\nPress Enter to return to the main menu...")
        return

       print(f"\nYou have selected: {day_choice}, {time_choice}")
       input("\nPress Enter to return to the main menu...")
   
#=========================================================

    elif day_input == "4":
       day_choice = "Thursday"
       os.system('cls')
       print("\nAvailable Time Slots For Thursday:")
       print("1. 9:00 AM")
       print("2. 11:30 AM")
       print("3. 1:00 PM")
    
       time_input = input("Please select your preferred time (1-3): ")

       if time_input == "1":
        time_choice = "9:00 AM"
       elif time_input == "2":
        time_choice = "11:30 AM"
       elif time_input == "3":
        time_choice = "1:00 PM"
       else:
        print("Invalid Time Selection")
        input("\nPress Enter to return to the main menu...")
        return

       print(f"\nYou have selected: {day_choice}, {time_choice}")
       input("\nPress Enter to return to the main menu...")
       
#==========================================================

    elif day_input == "5":
       day_choice = "Friday"
       os.system('cls')
       print("\nAvailable Time Slots For Friday:")
       print("1. 10:00 AM")
       print("2. 2:00 PM")
       print("3. 4:00 PM")
    
       time_input = input("Please select your preferred time (1-3): ")

       if time_input == "1":
        time_choice = "10:00 AM"
       elif time_input == "2":
        time_choice = "2:00 PM"
       elif time_input == "3":
        time_choice = "4:00 PM"
       else:
        print("Invalid Time Selection")
        input("\nPress Enter to return to the main menu...")
        return

       print(f"\nYou have selected: {day_choice}, {time_choice}")
       input("\nPress Enter to return to the main menu...")
      
#============================================================
    else:
        print("Invalid Day Selection")
        input("\nPress Enter to return to the main menu...")
"""


# ================================================
# Function: view_appointments() - DEPRECATED (Use GUI instead)
# ================================================
"""
def view_appointments():
    global ticket_number, played3, played4, played5, played6 
    os.system('cls')
    print("==============================================")
    print("           VIEW APPOINTMENT RECORDS           ")
    print("==============================================")
    if not played3:
          playsound("view_details.wav")
          played3 = True            
    patient_name = input("\nEnter your name: ")
    patient_contact = input("Enter your contact number: ")
    patient_email = input("Enter your contact email: ")
    patient_address = input("Enter your home address: ")

    os.system('cls')
    print("\n==============================================")
    print("             APPOINTMENT SUMMARY              ")
    print("==============================================")
    print(f"Patient Name      : {patient_name if patient_name else 'Missing'}")
    print(f"Patient Contact   : {patient_contact if patient_contact else 'Missing'}")
    print(f"Contact Email     : {patient_email if patient_email else 'Missing'}")
    print(f"Patient Address   : {patient_address if patient_address else 'Missing'}")
    print(f"Assigned Doctor   : {patient_doctor if patient_doctor else 'Pending Selection'}")
    print(f"Appointment Day   : {day_choice if day_choice else 'Pending Selection'}")
    print(f"Appointment Time  : {time_choice if time_choice else 'Pending Selection'}")
    print("==============================================")

    
  
    if not all([patient_name.strip(), patient_contact.strip(), patient_email.strip(), patient_address.strip()]):
        print("\nOops! Missing personal details detected. Kindly ensure all fields are filled in.")
        if not played5:
          playsound("oops.wav")
          played5 = True   

    elif not patient_doctor or not day_choice or not time_choice:
        print("\nIncomplete Details.")
        print("Please select your doctor, appointment day, and time before proceeding.")
        if not played6:
          playsound("incomplete.wav")
          played6 = True  

    else:
        
        ticket_number = random.randint(100000, 999999)

        print("\nThank you! Your appointment has been successfully recorded")
        print(f"Ticket Number: #{ticket_number}")
        print("==============================================")
        if not played4:
          playsound("summary.wav")
          played4 = True        
        export_choice = input("\nDo you wish to export your appointment details to PDF? (yes/no): ").strip().lower()
        if export_choice == "yes":
          export_to_pdf(patient_name, patient_contact, patient_email, patient_address,
                  patient_doctor, day_choice, time_choice, ticket_number)


    input("\nPress Enter to return to the main menu...")
"""

#===============================================================
# Function: export_to_pdf()
# PDF format when appointment details are exported
#===============================================================


def export_to_pdf(patient_name, patient_contact, patient_email, patient_address,
                  patient_doctor, day_choice, time_choice, ticket_number):



   filename = f"your_appointment_{ticket_number}.pdf"
   pdf = FPDF()
   pdf.add_page()
    
    
   pdf.set_draw_color(255, 200, 220)
   pdf.set_line_width(3)
   pdf.rect(5, 5, 200, 287)
    
    
   pdf.set_draw_color(255, 200, 220)
   pdf.set_line_width(1.5)
   pdf.line(10, 20, 200, 20)
    
   pdf.set_font("Times", 'B', 18)
   pdf.set_text_color(0, 0, 0)
   pdf.cell(0, 10, "Appointment Summary", ln=True, align="C")
   pdf.ln(8)
    
   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Patient Name:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, patient_name, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Contact Number:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, patient_contact, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Email:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, patient_email, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Address:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, patient_address, ln=True)
   pdf.ln(5)
    
    
   pdf.set_draw_color(255, 200, 220)
   pdf.set_line_width(0.8)
   pdf.line(10, pdf.get_y(), 200, pdf.get_y())
   pdf.ln(5)
    
    
   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Assigned Doctor:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, patient_doctor, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Appointment Day:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, day_choice, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Appointment Time:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, time_choice, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Ticket No.", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0,7,f"#{ticket_number}", ln=True)
   pdf.ln(10)


   now = datetime.now()
   date_submitted = now.strftime("%B %d, %Y")
   time_submitted = now.strftime("%I:%M %p")
   
   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Date Submitted:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, date_submitted, ln=True)

   pdf.set_font("Times", 'B', 13)
   pdf.cell(50, 8, "Time Submitted:", ln=False)
   pdf.set_font("Times", '', 13)
   pdf.cell(0, 8, time_submitted, ln=True)
   pdf.ln(10)

    
   pdf.set_draw_color(255, 200, 220)
   pdf.set_line_width(1.2)
   pdf.line(10, pdf.get_y(), 200, pdf.get_y())
   pdf.ln(5)
    
   pdf.set_font("Times", 'I', 12)
   pdf.set_text_color(0, 0, 0)
   pdf.multi_cell(0, 8, "Thank you for scheduling your appointment with us!", align='C')
        
    
   pdf.output(filename)
   print(f"\nPDF has been successfully exported as {filename}'")

   os.startfile(filename)

#============================================================

# ================================================
# GUI Main Application Class
# ================================================

class DoctorAppointmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Appointment System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.played = False
        self.show_main_menu()
    
    def clear_window(self):
        """Clear all widgets from the main window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Display the main menu"""
        self.clear_window()
        
        if not self.played:
            try:
                playsound("welcome.wav")
            except:
                pass
            self.played = True
        
        # Main frame
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(frame, text="Welcome to the Doctor Appointment System", 
                              font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)
        
        # Buttons
        btn_doctors = tk.Button(frame, text="View Available Doctors", width=30, 
                               command=self.show_doctor_menu, bg="#4CAF50", fg="white", 
                               font=("Arial", 10), pady=10)
        btn_doctors.pack(pady=5)
        
        btn_schedule = tk.Button(frame, text="Schedule an Appointment", width=30,
                                command=self.show_schedule_menu, bg="#4CAF50", fg="white",
                                font=("Arial", 10), pady=10)
        btn_schedule.pack(pady=5)
        
        btn_view = tk.Button(frame, text="View Appointment Records", width=30,
                            command=self.show_view_records, bg="#4CAF50", fg="white",
                            font=("Arial", 10), pady=10)
        btn_view.pack(pady=5)
        
        btn_exit = tk.Button(frame, text="Exit", width=30,
                            command=self.exit_app, bg="#f44336", fg="white",
                            font=("Arial", 10), pady=10)
        btn_exit.pack(pady=5)
    
    def show_doctor_menu(self):
        """Show doctor selection menu"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(frame, text="Doctor Selection", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        label = tk.Label(frame, text="Select a doctor category:", bg="#f0f0f0")
        label.pack()
        
        # Create a frame for doctor categories
        doctor_frame = tk.Frame(frame, bg="#f0f0f0")
        doctor_frame.pack(pady=10)
        
        categories = ["Pediatrician", "Ophthalmologist", "Cardiologist", "General Physician", "Psychiatrist"]
        
        for i, category in enumerate(categories):
            btn = tk.Button(doctor_frame, text=category, width=25,
                           command=lambda cat=category: self.show_doctor_selection(cat),
                           bg="#2196F3", fg="white", font=("Arial", 10), pady=5)
            btn.pack(pady=2)
        
        # Back button
        btn_back = tk.Button(frame, text="Back to Main Menu", width=30,
                            command=self.show_main_menu, bg="#FF9800", fg="white", pady=5)
        btn_back.pack(side=tk.BOTTOM, pady=10)
    
    def show_doctor_selection(self, category):
        """Show specific doctors for selected category"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(frame, text=f"Select a {category}", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        global patient_doctor, played1
        
        category_doctors = {
            "Pediatrician": ["Dr. Mendoza", "Dr. Flores"],
            "Ophthalmologist": ["Dr. Bautista", "Dr. Carmen"],
            "Cardiologist": ["Dr. Smith", "Dr. Wilson"],
            "General Physician": ["Dr. Robinson", "Dr. Campbell"],
            "Psychiatrist": ["Dr. Lim", "Dr. Fernandez"],
        }
        
        if not played1:
            try:
                playsound("doctor.wav")
            except:
                pass
            played1 = True
        
        doc_list = category_doctors[category]
        
        for doc in doc_list:
            btn = tk.Button(frame, text=doc, width=25,
                           command=lambda d=doc: self.select_doctor(d),
                           bg="#2196F3", fg="white", font=("Arial", 10), pady=5)
            btn.pack(pady=5)
        
        # Back button
        btn_back = tk.Button(frame, text="Back", width=30,
                            command=self.show_doctor_menu, bg="#FF9800", fg="white", pady=5)
        btn_back.pack(side=tk.BOTTOM, pady=10)
    
    def select_doctor(self, doctor_name):
        """Select a doctor"""
        global patient_doctor
        patient_doctor = doctor_name
        messagebox.showinfo("Success", f"You successfully selected: {patient_doctor}")
        self.show_doctor_menu()
    
    def show_schedule_menu(self):
        """Show schedule selection menu"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(frame, text="Schedule an Appointment", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        label = tk.Label(frame, text="Select a day:", bg="#f0f0f0")
        label.pack()
        
        global played2
        if not played2:
            try:
                playsound("schedule.wav")
            except:
                pass
            played2 = True
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        for day in days:
            btn = tk.Button(frame, text=day, width=25,
                           command=lambda d=day: self.show_time_selection(d),
                           bg="#2196F3", fg="white", font=("Arial", 10), pady=5)
            btn.pack(pady=2)
        
        # Back button
        btn_back = tk.Button(frame, text="Back to Main Menu", width=30,
                            command=self.show_main_menu, bg="#FF9800", fg="white", pady=5)
        btn_back.pack(side=tk.BOTTOM, pady=10)
    
    def show_time_selection(self, day):
        """Show time slots for selected day"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(frame, text=f"Available Time Slots for {day}", 
                              font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        global day_choice, time_choice
        day_choice = day
        
        times = schedule[day]
        
        for time_slot in times:
            btn = tk.Button(frame, text=time_slot, width=25,
                           command=lambda t=time_slot: self.select_time(day, t),
                           bg="#2196F3", fg="white", font=("Arial", 10), pady=5)
            btn.pack(pady=5)
        
        # Back button
        btn_back = tk.Button(frame, text="Back", width=30,
                            command=self.show_schedule_menu, bg="#FF9800", fg="white", pady=5)
        btn_back.pack(side=tk.BOTTOM, pady=10)
    
    def select_time(self, day, time_slot):
        """Select a time slot"""
        global day_choice, time_choice
        day_choice = day
        time_choice = time_slot
        messagebox.showinfo("Success", f"You have selected: {day_choice}, {time_choice}")
        self.show_schedule_menu()
    
    def show_view_records(self):
        """Show view appointment records window"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(frame, text="View Appointment Records", 
                              font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        global played3
        if not played3:
            try:
                playsound("view_details.wav")
            except:
                pass
            played3 = True
        
        # Labels and entry fields
        tk.Label(frame, text="Enter your name:", bg="#f0f0f0").pack(anchor=tk.W, pady=(5, 0))
        entry_name = tk.Entry(frame, width=40)
        entry_name.pack(pady=5)
        
        tk.Label(frame, text="Enter your contact number:", bg="#f0f0f0").pack(anchor=tk.W, pady=(5, 0))
        entry_contact = tk.Entry(frame, width=40)
        entry_contact.pack(pady=5)
        
        tk.Label(frame, text="Enter your contact email:", bg="#f0f0f0").pack(anchor=tk.W, pady=(5, 0))
        entry_email = tk.Entry(frame, width=40)
        entry_email.pack(pady=5)
        
        tk.Label(frame, text="Enter your home address:", bg="#f0f0f0").pack(anchor=tk.W, pady=(5, 0))
        entry_address = tk.Entry(frame, width=40)
        entry_address.pack(pady=5)
        
        def submit_appointment():
            patient_name = entry_name.get()
            patient_contact = entry_contact.get()
            patient_email = entry_email.get()
            patient_address = entry_address.get()
            
            self.process_appointment(patient_name, patient_contact, patient_email, patient_address)
        
        # Submit button
        btn_submit = tk.Button(frame, text="Submit", width=30, command=submit_appointment,
                             bg="#4CAF50", fg="white", font=("Arial", 10), pady=5)
        btn_submit.pack(pady=10)
        
        # Back button
        btn_back = tk.Button(frame, text="Back to Main Menu", width=30,
                            command=self.show_main_menu, bg="#FF9800", fg="white", pady=5)
        btn_back.pack(side=tk.BOTTOM, pady=10)
    
    def process_appointment(self, patient_name, patient_contact, patient_email, patient_address):
        """Process the appointment submission"""
        global ticket_number, played5, played6, played4
        
        # Check if all personal details are filled
        if not all([patient_name.strip(), patient_contact.strip(), patient_email.strip(), patient_address.strip()]):
            messagebox.showerror("Missing Details", "Oops! Missing personal details detected.\nKindly ensure all fields are filled in.")
            if not played5:
                try:
                    playsound("oops.wav")
                except:
                    pass
                played5 = True
            return
        
        # Check if doctor, day, and time are selected
        if not patient_doctor or not day_choice or not time_choice:
            messagebox.showerror("Incomplete Details", "Incomplete Details.\nPlease select your doctor, appointment day, and time before proceeding.")
            if not played6:
                try:
                    playsound("incomplete.wav")
                except:
                    pass
                played6 = True
            return
        
        # Generate ticket number
        ticket_number = random.randint(100000, 999999)
        
        # Show summary
        summary = f"""Thank you! Your appointment has been successfully recorded.

APPOINTMENT SUMMARY
==========================================
Patient Name      : {patient_name}
Patient Contact   : {patient_contact}
Contact Email     : {patient_email}
Patient Address   : {patient_address}
Assigned Doctor   : {patient_doctor}
Appointment Day   : {day_choice}
Appointment Time  : {time_choice}
Ticket Number     : #{ticket_number}
=========================================="""
        
        if not played4:
            try:
                playsound("summary.wav")
            except:
                pass
            played4 = True
        
        messagebox.showinfo("Appointment Summary", summary)
        
        # Ask to export to PDF
        export_choice = messagebox.askyesno("Export to PDF", "Do you wish to export your appointment details to PDF?")
        
        if export_choice:
            export_to_pdf(patient_name, patient_contact, patient_email, patient_address,
                         patient_doctor, day_choice, time_choice, ticket_number)
        
        self.show_main_menu()
    
    def exit_app(self):
        """Exit the application"""
        confirm = messagebox.askyesno("Exit Program", "Are you sure you want to exit?")
        
        if confirm:
            global played7
            if not played7:
                try:
                    playsound("exit.wav")
                except:
                    pass
                played7 = True
            self.root.quit()

# ================================================
# Main Program
# ================================================
played = False
played7 = False

if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorAppointmentApp(root)
    root.mainloop()


#====================================================================






