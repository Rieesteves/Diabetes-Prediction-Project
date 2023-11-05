import pandas as pd
from sklearn.naive_bayes import GaussianNB
import tkinter as tk
from tkinter import messagebox

# Load your diabetes dataset
df = pd.read_csv('diabetes.csv')

# Split the dataset into features (X) and target (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Initialize and train the Naive Bayes classifier
clf = GaussianNB()
clf.fit(X, y)

# Calculate the range of feature values
feature_ranges = {col: {'min': X[col].min(), 'max': X[col].max()} for col in X.columns}

# Function to make predictions
def predict_diabetes():
    user_data = [
        pregnancies_var.get(),
        glucose_var.get(),
        blood_pressure_var.get(),
        skin_thickness_var.get(),
        insulin_var.get(),
        bmi_var.get(),
        diabetes_pedigree_var.get(),
        age_var.get()
    ]

    prediction = clf.predict([user_data])

    if prediction[0] == 1:
        result = "Diabetic"
    else:
        result = "Non-Diabetic"

    messagebox.showinfo("Diabetes Prediction", f"The patient is predicted to be {result}")

# Function to clear input fields
def reset_inputs():
    pregnancies_var.set(0)
    glucose_var.set(0)
    blood_pressure_var.set(0)
    skin_thickness_var.set(0)
    insulin_var.set(0)
    bmi_var.set(0.0)
    diabetes_pedigree_var.set(0.0)
    age_var.set(0)

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")

# Create input fields
input_fields = [
    ("Number of Pregnancies:", 0, 17, "pregnancies_var"),
    ("Glucose level:", 0, 199, "glucose_var"),
    ("Blood Pressure:", 0, 122, "blood_pressure_var"),
    ("Skin Thickness:", 0, 99, "skin_thickness_var"),
    ("Insulin level:", 0, 846, "insulin_var"),
    ("BMI:", 0.0, 67.1, "bmi_var"),
    ("Diabetes Pedigree Function:", 0.078, 2.42, "diabetes_pedigree_var"),
    ("Age:", 21, 81, "age_var")
]

for label, min_val, max_val, var_name in input_fields:
    label_widget = tk.Label(root, text=label)
    label_widget.pack()
    entry_var = tk.IntVar() if var_name == "pregnancies_var" or var_name == "glucose_var" or var_name == "blood_pressure_var" or var_name == "skin_thickness_var" or var_name == "insulin_var" or var_name == "age_var" else tk.DoubleVar()
    entry_widget = tk.Entry(root, textvariable=entry_var)
    entry_widget.pack()
    if var_name == "pregnancies_var":
        pregnancies_var = entry_var
    elif var_name == "glucose_var":
        glucose_var = entry_var
    elif var_name == "blood_pressure_var":
        blood_pressure_var = entry_var
    elif var_name == "skin_thickness_var":
        skin_thickness_var = entry_var
    elif var_name == "insulin_var":
        insulin_var = entry_var
    elif var_name == "bmi_var":
        bmi_var = entry_var
    elif var_name == "diabetes_pedigree_var":
        diabetes_pedigree_var = entry_var
    else:
        age_var = entry_var
    entry_var.set(min_val)

# Create prediction button
predict_button = tk.Button(root, text="Predict", command=predict_diabetes)
predict_button.pack()

# Create reset button
reset_button = tk.Button(root, text="Reset Inputs", command=reset_inputs)
reset_button.pack()

# Run the main loop
root.mainloop()
