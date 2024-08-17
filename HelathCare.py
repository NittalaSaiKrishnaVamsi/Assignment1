import datetime

patients = {}

def register_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    patients[patient_id] = {'Name': name, 'Age': age, 'Gender': gender, 'History': []}
    print(f"Patient {name} registered successfully!")

def add_diagnosis():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        diagnosis = input("Enter Diagnosis: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        patients[patient_id]['History'].append({'Diagnosis': diagnosis, 'Date': date})
        print(f"Diagnosis added for {patients[patient_id]['Name']}")
    else:
        print("Patient not found!")

def generate_report():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        print(f"--- Report for {patients[patient_id]['Name']} ---")
        for record in patients[patient_id]['History']:
            print(f"Date: {record['Date']}, Diagnosis: {record['Diagnosis']}")
    else:
        print("Patient not found!")

def main():
    while True:
        print("\n1. Register Patient\n2. Add Diagnosis\n3. Generate Report\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            register_patient()
        elif choice == 2:
            add_diagnosis()
        elif choice == 3:
            generate_report()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
