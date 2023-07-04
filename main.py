from tkinter import *

window = Tk()
window.title("BMI Counter")
window.minsize(width=300, height=300)
window.config(bg="white")

label = Label(text="Enter Your weight (kg)")
label.config(bg="white")
label.config(fg="black")
label.place(x=20, y=0)
label.pack()

entry = Entry(width=20)
entry.place(x=30, y=30)
entry.pack()

label2 = Label(text="Enter Your Height (cm)")
label2.config(bg="white")
label2.config(fg="black")
label2.place(x=20, y=60)
label2.pack()

entry2 = Entry(width=20)
entry2.place(x=30, y=90)
entry2.pack()

result_label = Label(text="", bg="white", fg="black")
result_label.place(x=20, y=150)

def calculate_bmi():
    weight = entry.get()
    height = entry2.get()

    if not weight or not height:
        result_label.config(text="Error: Please enter weight and height")
        return

    try:
        weight = float(weight)
        height = float(height) / 100  # cm to meter conversion

        if weight <= 0 or height <= 0:
            result_label.config(text="Error: Invalid weight or height")
            return

        bmi = weight / (height ** 2)

        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text="BMI: {:.2f} - Category: {}".format(bmi, category))
    except ValueError:
        result_label.config(text="Error: Invalid input")

calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.place(x=30, y=120)
calculate_button.pack()

window.mainloop()
