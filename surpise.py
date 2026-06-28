import tkinter as tk
from tkinter import messagebox
import random

correct_name = "Vyshnavi"
correct_birthday = "21-12-2006"

def hearts(window):
    colors = ["red", "pink", "deeppink", "hotpink"]

    def create():
        x = random.randint(20, 560)
        heart = tk.Label(
            window,
            text="❤️",
            font=("Arial", random.randint(18, 30)),
            bg="#ffe4e1",
            fg=random.choice(colors)
        )
        heart.place(x=x, y=380)

        def move(y=380):
            if y > -30:
                heart.place(y=y)
                window.after(40, lambda: move(y - 5))
            else:
                heart.destroy()

        move()
        window.after(300, create)

    create()

def check_details():
    name = name_entry.get().strip()
    birthday = birthday_entry.get().strip()

    if name.lower() == correct_name.lower() and birthday == correct_birthday:
        surprise = tk.Toplevel(root)
        surprise.title("❤️ Surprise ❤️")
        surprise.geometry("600x400")
        surprise.configure(bg="#ffe4e1")

        tk.Label(
            surprise,
            text="❤️ I LOVE YOU VYSHNAVI ❤️",
            font=("Arial", 24, "bold"),
            fg="red",
            bg="#ffe4e1"
        ).pack(pady=20)

        tk.Label(
            surprise,
            text="You are special.\nWishing you lots of happiness!\n🌹❤️🌹",
            font=("Arial", 16),
            bg="#ffe4e1"
        ).pack()

        hearts(surprise)

    else:
        messagebox.showerror("Oops!", "Wrong name or birthday!")

root = tk.Tk()
root.title("Birthday Surprise")
root.geometry("400x250")
root.configure(bg="#ffe4e1")

tk.Label(
    root,
    text="🎁 Secret Surprise 🎁",
    font=("Arial", 18, "bold"),
    bg="#ffe4e1"
).pack(pady=15)

tk.Label(root, text="Enter Your Name", bg="#ffe4e1").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter Birthday (DDMMYYYY)", bg="#ffe4e1").pack()
birthday_entry = tk.Entry(root)
birthday_entry.pack()

tk.Button(
    root,
    text="Open Surprise ❤️",
    command=check_details
).pack(pady=20)

root.mainloop()


