from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    with open("data.txt", "a") as save_file:
        save_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

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

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="100daysOfPy/passwordGen/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
#canvas.grid(column=1, row=1)


window.mainloop()