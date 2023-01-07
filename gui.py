import tkinter as tk
from tkinter import Tk


def entry():
    password_name_greetings = tk.Label(master=frame_right, text='Password Name: ')
    password_name_greetings.pack()

    possible_password_name = tk.Entry(master=frame_right)
    possible_password_name.get()
    possible_password_name.pack()

    #password_length_greetings = tk.Label(master=frame_right, text='Password length: ')
    #password_length_greetings.pack()

    #possible_password_length = tk.Entry(master=frame_right)
    #possible_password_length.insert(0, '16')
    #possible_password_length.get()
    #possible_password_length.pack()


def checkbuttons():
    uppercase_letters = tk.Checkbutton(master=frame_left, text='Uppercase letters')
    uppercase_letters.pack(fill=tk.Y, anchor='w')

    symbols = tk.Checkbutton(master=frame_left, text='Symbols')
    symbols.pack(fill=tk.Y, anchor='w')

    password_length_exact = tk.Checkbutton(master=frame_left, text='Password length 32')
    password_length_exact.pack(fill=tk.Y, anchor='w')


root = Tk()
root.minsize(400, 130)
root.maxsize(400, 130)


name = tk.Label(text='Password Generator')
name.pack()
password = tk.Entry()
password.pack()


frame_left = tk.Frame(master=root, width=300, height=100)
frame_left.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame_right = tk.Frame(master=root, width=300, height=100)
frame_right.pack(fill=tk.Y, side=tk.LEFT, expand=True)

entry()
checkbuttons()


button = tk.Button(master=frame_right, text='Generate Password')
button.pack(fill=tk.Y)

root.mainloop()
