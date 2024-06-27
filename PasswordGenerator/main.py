import tkinter
import string
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password = []
    password += [random.choice(letters) for _ in range(random.randint(8,10))]
    password += [random.choice(numbers) for _ in range(random.randint(2,4))]
    password += [random.choice(symbols) for _ in range(random.randint(2,4))]

    random.shuffle(password)
    final_pass = "".join(password)

    pass_entry.insert(0, final_pass)
    pyperclip.copy(final_pass)











# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        is_empty = messagebox.showwarning(title = "Oops", message = "Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title = website, message= f"These are the details entered: \nEmail: {email_user} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            OUTPUT_FILE = open("output.txt", "a")
            OUTPUT_FILE.write(f"{website.title()} | {email_user} | {password}\n")
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------- Clear All Passwords  ------------------------------- #
def clear_passwords():
    with open("output.txt", "w") as file:
        pass





# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width = 200, height = 200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)

website_label = tkinter.Label(text = " Website:")
website_label.grid(column = 0, row = 1)

website_entry = tkinter.Entry(width = 35)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_user_label = tkinter.Label(text = "Email/Username:")
email_user_label.grid(column = 0, row = 2)

email_user_entry = tkinter.Entry(width = 35)
email_user_entry.grid(column = 1, row = 2, columnspan = 2)
email_user_entry.insert(0, "examplemail@gmail.com")

pass_label = tkinter.Label(text = "Password:")
pass_label.grid(column = 0, row = 3, columnspan = 1)

pass_entry = tkinter.Entry(width = 17)
pass_entry.grid(column = 1, row = 3)

generate_pass_button = tkinter.Button(text = "Generate Password", width = 14, command = pass_generator)
generate_pass_button.grid(column = 2, row = 3)

add_button = tkinter.Button(text = "Add", width= 36, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2)

clear_all_passwords_button = tkinter.Button(text = "Clear All", width = 36, command = clear_passwords)
clear_all_passwords_button.grid(column = 1, row = 5, columnspan = 2)

window.mainloop()
