import tkinter as tk
import random as rnd
import pyperclip as pc

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation

window = tk.Tk()
group0 = tk.Label(window)
group0.pack(side=tk.TOP,
            fill=tk.X)
           #  ,
           # fill=tk.X,
           # padx=5,
           # pady=5)

window.geometry("500x500")
window.config(bg='white')
photo = tk.PhotoImage(file="locker.png")
photo_label = tk.Label(window, image=photo)
photo_label.place(relx=0.5, rely=0.5, anchor='center')

fields = {"Website", "Email/Username", "Password"}
File_object = open(r"PasswordData.txt", "a+")
File_object.write(f"cat")


def make_form(group1, fields):
    group = tk.Frame(group1)
    group.pack(side=tk.BOTTOM,
               fill=tk.X,
               padx=5,
               pady=5)
    entries = {}
    for field in fields:
        if not field == "Password":
            row = tk.Frame(group)
            ent = tk.Entry(row)
            lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
            ent.insert(0, f"")
            row.pack(side=tk.TOP,
                     fill=tk.X,
                     padx=5,
                     pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                     expand=tk.YES,
                     padx=5,
                     fill=tk.X)
            entries[field] = ent
        else:
            row = tk.Frame(group)
            ent = tk.Entry(row)
            ent.place(relwidth=0.5)
            lab = tk.Label(row, width=11, text=field + ": ", anchor='w')
            ent.insert(0, "")
            row.pack(side=tk.TOP,
                     fill=tk.X,
                     padx=5,
                     pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.LEFT,
                     expand=tk.YES,
                     fill=tk.X)
            button = tk.Button(row, text="generate password", command=(lambda: generate_password(form)))
            button.pack(side=tk.RIGHT,
                        expand=tk.YES,
                        fill=tk.X)
            entries[field] = ent
    row = tk.Frame(group)
    button = tk.Button(row, text="Save data", command=(lambda: save_data(entries)))
    row.pack(side=tk.TOP,
             fill=tk.X,
             padx=5,
             pady=5)
    button.pack(side=tk.RIGHT,
                expand=tk.YES,
                fill=tk.X)
    return entries


def generate_password(entries):
    rand_password = ""
    for _ in range(15):
        rand_password += rnd.choice(printable)
        print(rand_password)
    entries['Password'].insert(0, rand_password)
    pc.copy(rand_password)


def save_data(entries):
    data = File_object.read()
    if entries["Email/Username"].get() == "" or entries["Website"].get() == "" or entries["Password"].get() == "":
        open_popup()
    else:
        username_email = entries["Email/Username"].get()
        print(username_email)
        website = entries["Website"].get()
        print(website)
        password = entries["Password"].get()
        print(password)
        data += f"{website} | {username_email} | {password}\n"
        File_object.write(data)
        entries['Password'].delete(0, 15)


def open_popup():
    top = tk.Toplevel(window)
    top.geometry("250x130")
    top.title("!!!")
    tk.Label(top, text= "Please fill in all the fields!").place(x=125, y=65, anchor ="center")


form = make_form(window, fields)
File_object.write(f"dog")

window.mainloop()
File_object.close()