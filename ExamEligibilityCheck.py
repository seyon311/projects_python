MedicalCause = input("Do you have a medical cause for not taking the exam? (Y/N): ")

if MedicalCause == "Y":
    print("You are eligible to attend the exam.")
elif MedicalCause == "N":
    Attendance = int(input("What is your attendance percentage? (Enter a number between 0 and 100): "))

    if Attendance >= 75:
        print("You are eligible to attend the exam.")
    elif Attendance < 75:
        print("You are not eligible to attend the exam.")
    
    else:    
        print("Invalid input. Please enter a number between 0 and 100.")

else: 
    print("Invalid input. Please enter 'Y' or 'N'.")    