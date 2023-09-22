from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_calculated.config(text=f"{km}")


# user input miles to convert
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_calculated = Label(text="0")
km_calculated.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=calculate)
cal_button.grid(column=1, row=2)







window.mainloop()

