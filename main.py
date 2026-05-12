
from tkinter import messagebox
from tkinter import *
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def login():
    website = text_web_entry.get()
    email = text_email_entry.get()
    password = text_password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        select_ok = messagebox.askokcancel(title="Website", message=f"Please check you data: \n Website: {website} \n "
                                                    f"Email: {email} \n Password: {password}")
        if select_ok:
            with open('password.txt', "a") as data:
                data.write(f"{website} | {email} | {password}\n")

                text_web_entry.delete(0, END)
                text_password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

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
text_web_entry.grid(row=1, column=1, columnspan=2)
text_web_entry.focus()

text_email_entry = Entry(window, width=35)
text_email_entry.grid(row=2, column=1, columnspan=2)
text_email_entry.insert(0, "test@gmail.com")

text_password_entry = Entry(window, width=21)
text_password_entry.grid(row=3, column=1)

# Buttons
button_generate = Button(window, text = "Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(window, width=36, text="Add", command= login,activebackground="blue")
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()