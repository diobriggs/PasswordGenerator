import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password = []
    password += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password)
    final_pass = "".join(password)

    pass_entry.insert(0, final_pass)
    pyperclip.copy(final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")

    else:
        try:
            with open("output.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open("output.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("output.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------- Clear All Passwords  ------------------------------- #
def clear_passwords():
    with open("output.json", "w"):
        pass

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    try:
        with open("output.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showwarning(title="Error", message="Sorry you must add a password before continuing.")
    else:
        website = website_entry.get()
        if website in data:
            search_pass = data[website]["password"]
            search_email = data[website]["email"]
            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email: {search_email} \nPassword: {search_pass}")
        else:
            messagebox.showwarning(title="Error", message= f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text=" Website:")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_user_label = tkinter.Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

email_user_entry = tkinter.Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "examplemail@gmail.com")

pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3, columnspan=1)

pass_entry = tkinter.Entry(width=17)
pass_entry.grid(column=1, row=3)

generate_pass_button = tkinter.Button(text="Generate Password", width=14, command=pass_generator)
generate_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

clear_all_passwords_button = tkinter.Button(text="Clear All", width=36, command=clear_passwords)
clear_all_passwords_button.grid(column=1, row=5, columnspan=2)

search_button = tkinter.Button(text = "Search", width=13, command = search)
search_button.grid(column = 2, row = 1)

window.mainloop()
