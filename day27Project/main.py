from tkinter import *

# Create a window
window = Tk()

# window properties
window.title("My First GUI Program")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20) # space around the program from edge of screen


def button_clicked():
    # get the string from the input field
    new_text = my_input.get()
    my_label.config(text=new_text)
    print("I got clicked")


# label
my_label = Label(text="I am a label", font=("Ariel", 24, "normal"))
# my_label.pack()  # needed to show up on screen but difficult to specify
# my_label.place(x=100, y=200) # needed to show up on screen but very specific
my_label.grid(column=0, row=0) # needed to show up on screen but very specific
my_label.config(padx=20, pady=20) # add space around the label

# ways to change the text
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

# add the name of the function not call it
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry  - input field
my_input = Entry(width=15)
# my_input.pack()
my_input.grid(column=3, row=2)


#  keep the window open
window.mainloop()
