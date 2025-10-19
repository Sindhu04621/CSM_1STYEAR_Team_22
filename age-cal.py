import tkinter as tk
from datetime import date, datetime

# Create the main window
root = tk.Tk()
root.title("My First Code - Age Calculator")
root.geometry("400x250")

# Label to display messages or result
label = tk.Label(root, text="Hello!", font=("Arial", 10), fg="red")
label.grid(row=3, column=0, pady=5)

# Label and entry for date of birth
label_input = tk.Label(root, text="Enter DOB (YYYY-MM-DD):", font=("Arial", 10))
label_input.grid(row=0, column=0, pady=5)

dob_entry = tk.Entry(root, font=("Arial", 10))
dob_entry.grid(row=0, column=1, pady=5)

# Function to calculate age
def calculate_age():
    dob_str = dob_entry.get()
    try:
        # Convert entered text to date
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        label.config(text="❌ Please enter DOB in YYYY-MM-DD format", fg="red")
        return

    today = date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    label.config(text=f"✅ Your Age is: {age} years", fg="green")

# Button to calculate age
button = tk.Button(root, text="Calculate Age", font=("Arial", 14), command=calculate_age)
button.grid(row=1, column=1, pady=10)

# Run the GUI loop
root.mainloop()
