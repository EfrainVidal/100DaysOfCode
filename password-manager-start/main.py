from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # empty the field and regenerate
    password_entry.delete(0, END)

    # Generate the password randomly and join it
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)  # copies the password to the mouse for the user to paste where needed

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password_string = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password_string,
        }
    }

    # message box for user verification
    if len(website) == 0 or len(password_string) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # # json.dump is used to write json files
                data = json.load(data_file)  # json load is to read json files
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # print(data) # type dictionary
            data.update(new_data)  # update and add new information in json file

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)  # indent to make it easier to read for user
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()

    # message box for user verification
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details found for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=190, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)  # has to be there in order to show on screen

# Create labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()  # in order for cursor to focus on it when starting the app

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "Nsaneseal@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window = mainloop()
