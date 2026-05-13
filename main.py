
from tkinter import messagebox
from tkinter import *
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR -------------------------------
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10)) ]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    digits_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + digits_list

    shuffle(password_list)

    password = "".join(password_list)
    text_password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD -------------------------------
def login():
    website = text_web_entry.get()
    email = text_email_entry.get()
    password = text_password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            with open('password.json', "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('password.json',"w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('password.json', "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            text_web_entry.delete(0, END)
            text_password_entry.delete(0, END)

# ----------------------------- FIND PASSWORD -------------------------
def find_password():
    website = text_web_entry.get()
    try:
        with open('password.json') as data_file:
            search = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "Data not fount in the file")
    else:
        if website in search:
            email =search[website]["email"]
            password = search[website]["password"]
            messagebox.showinfo("Website", f"{website}\n Email: {email} \n Password: {password} ")
        else:
            messagebox.showinfo("Error", f"Website: {website} not found")

# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(window, text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entry
text_web_entry = Entry(window, width=35)
text_web_entry.grid(row=1, column=1)
text_web_entry.focus()

text_email_entry = Entry(window, width=35)
text_email_entry.grid(row=2, column=1)
text_email_entry.insert(0, "test@gmail.com")

text_password_entry = Entry(window, width=35)
text_password_entry.grid(row=3, column=1)

# Buttons
button_generate = Button(window, text = "Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(window, width=36, text="Add", command= login)
button_add.grid(row=4, column=1)

button_search = Button(window, text= " Search", width= 13, command=find_password)
button_search.grid(row=1, column=2)


window.mainloop()