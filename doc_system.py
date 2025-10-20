

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
# Function: doctor()
# Displays a list of doctor categories and let users choose their preffered doctors.
# ================================================

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


# ================================================
# Function: schedule()
# Let users choose what day and time for their appointment.
# ================================================

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


# ================================================
# Function: view_appointments()
# Asks and displays patient appointment details and checks for missing or invalid information
# ================================================

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
# Function: display()
# The main menu and let user's choose their options.
# ================================================

def display():
    os.system('cls')
    print("==============================================")
    print("   Welcome to the Doctor Appointment System   ")
    print("==============================================")
                
    print("\nMain Menu")
    print("1: View Available Doctors")
    print("2: Schedule an Appointment")
    print("3: View Appointment Records")
    print("4: Exit")
    print("================================================")
    
#main program loop
# It continuously displays until user choose exits.
#=============================================================
played = False
played7 = False

while True:
   display()
   if not played:
        playsound("welcome.wav")
        played = True
   option = input("\nPlease enter your option( 1, 2, 3, or 4):")
   
   if option == "1":
    os.system('cls')
    print("\nYou have selected: -- View Available Doctors -- ")
    doctor()

   elif option == "2":
    os.system('cls')
    print("\nYou have selected: -- Schedule an Appointment -- ")
    schedule()

   elif option == "3":
    os.system('cls')
    print("\nYou have selected: -- View Appointment Records -- ")
    view_appointments()

      
   elif option == "4":
    os.system('cls')
    print("\n-- Exit Program --")
    confirm = input("\nAre you sure you want to exit? (yes/no): ").strip().lower()

    if confirm == "yes":
        os.system('cls')
        print("\n-- Your session has ended. Thank you! --")
        if not played7:
          playsound("exit.wav")
          played7 = True
        break
    elif confirm == "no":
        os.system('cls')
        print("\nRedirecting to the main menu...")
        input("\nPlease Press Enter to continue...")
    else:
        print("\nInvalid input. Please type 'yes' or 'no'.")
        input("\nPress Enter to continue...")


#====================================================================






