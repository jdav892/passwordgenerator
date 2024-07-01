from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else: 
        try:
            with open("data.json", "r") as save_file:
                data = json.load(save_file)
                
        except FileNotFoundError:
            with open("data.json", "w") as save_file:
                json.dump(new_data, save_file, indent=4)
        else:
            data.update(new_data) 
                
            with open("data.json", "w"): 
                json.dump(data, save_file, indent=4)
        finally:
            
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("data.json", "r") as save_file:
        data = json.load(save_file)
        for website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=13, height=1, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "Test@gmail.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", width=36, height=1, command=save)
add_button.grid(column=1, row=4, columnspan=2)

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="100daysOfPy/passwordGen/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)



window.mainloop()