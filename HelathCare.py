import datetime
import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = np.array([
    [1, 0, 1, 0],  
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
])

y = np.array([0, 1, 0, 1]) 

clf = DecisionTreeClassifier()
clf.fit(X, y)

patients = {}

def register_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    patients[patient_id] = {'Name': name, 'Age': age, 'Gender': gender, 'History': []}
    print(f"Patient {name} registered successfully!")

def predict_disease(symptoms):
    symptoms_array = np.array([symptoms])
    prediction = clf.predict(symptoms_array)
    return prediction[0]

def add_diagnosis():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        symptoms = input("Enter Symptoms as binary (comma-separated, e.g., 1,0,1,0): ")
        symptoms = [int(s) for s in symptoms.split(',')]

        predicted_diagnosis = predict_disease(symptoms)
        diagnosis = 'Flu' if predicted_diagnosis == 1 else 'Cold'

        for record in patients[patient_id]['History']:
            if record['Diagnosis'] == diagnosis:
                print(f"Diagnosis '{diagnosis}' already exists for {patients[patient_id]['Name']}. No new entry added.")
                return

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

def check_password():
    password = "Vamsi" 
    attempt = input("Enter the password to access the system: ")
    if attempt == password:
        print("Access granted. Welcome!")
        return True
    else:
        print("Incorrect password. Access denied.")
        return False

def main():
    if check_password():
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
    else:
        print("Exiting the system.")

if __name__ == "__main__":
    main()
