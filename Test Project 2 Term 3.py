import tkinter

root = tkinter.Tk()
root.geometry("400x400")
root.title("BMI calculator")


def BMI():
    user_input = entry.get().upper()
    if user_input == "18":
        result.config(text="flaco")
    elif user_input == "18.5 - 24.9":
        result.config(text="underweight")
    elif user_input == "25 - 29.9":
        result.config(text="normal")
    elif user_input == "30 - 34.9":
        result.config(text="overweigh")
    elif user_input == "35 - 39.9":
        result.config(text="obese")
    elif user_input == ">40":
        result.config(text="extremly obese")
    



label1 = tkinter.Label(root, text="Enter your heigh in meters:")
label1.pack(pady=10)

entry = tkinter.Entry(root)
entry.pack(pady=10)

weight = tkinter.Label(root, text="Enter your weight in kilograms:")
weight.pack()

entry2 = tkinter.Entry(root)
entry2.pack(pady=10)

button1 = tkinter.Button(root, text="Calculate BMI")
button1.pack(pady=10)


result = tkinter.Label(root, text="")
result.pack(pady=10)



root.mainloop()