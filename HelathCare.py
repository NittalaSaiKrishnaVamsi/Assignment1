import datetime
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Sample training data for the Decision Tree
X = np.array([
    [1, 0, 1, 0],  
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
])

y = np.array([0, 1, 0, 1])  # Labels: 0 for Cold, 1 for Flu

# Train the Decision Tree model
clf = DecisionTreeClassifier()
clf.fit(X, y)

patients = {}

# Function to register a new patient
def register_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    patients[patient_id] = {'Name': name, 'Age': age, 'Gender': gender, 'History': []}
    print(f"Patient {name} registered successfully!")

# Function to predict disease based on symptoms
def predict_disease(symptoms):
    symptoms_array = np.array([symptoms])
    prediction = clf.predict(symptoms_array)
    return prediction[0]

# Function to add a diagnosis for a patient
def add_diagnosis():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        symptoms = input("Enter Symptoms as binary (comma-separated, e.g., 1,0,1,0): ")
        symptoms = [int(s) for s in symptoms.split(',')]

        predicted_diagnosis = predict_disease(symptoms)
        diagnosis = 'Flu' if predicted_diagnosis == 1 else 'Cold'
        
        # Check if the diagnosis already exists in the patient's history
        for record in patients[patient_id]['History']:
            if record['Diagnosis'] == diagnosis:
                print(f"Diagnosis '{diagnosis}' already exists for {patients[patient_id]['Name']}. No new entry added.")
                return

        # Add the diagnosis if it's not a duplicate
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        patients[patient_id]['History'].append({'Diagnosis': diagnosis, 'Date': date})
        print(f"Diagnosis added for {patients[patient_id]['Name']}")
    else:
        print("Patient not found!")

# Function to generate a report for a patient
def generate_report():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        print(f"--- Report for {patients[patient_id]['Name']} ---")
        for record in patients[patient_id]['History']:
            print(f"Date: {record['Date']}, Diagnosis: {record['Diagnosis']}")
    else:
        print("Patient not found!")

# Function to check the password
def check_password():
    password = "Vamsi"  # Replace with your desired password
    attempt = input("Enter the password to access the system: ")
    if attempt == password:
        print("Access granted. Welcome!")
        return True
    else:
        print("Incorrect password. Access denied.")
        return False

# Main function with password protection
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
