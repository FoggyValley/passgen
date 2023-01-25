import tkinter as tk
from tkinter import Tk
from tkinter import Message
import datetime
import os
import random


class Window(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        # Frames
        self.frame_left = tk.Frame(master=root, width=300, height=100)
        self.frame_left.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        self.frame_right = tk.Frame(master=root, width=300, height=100)
        self.frame_right.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        # Entries
        self.password_name_greetings = tk.Label(master=self.frame_right, text='Password Name: ')
        self.password_name_greetings.pack()

        self.possible_password_name = tk.Entry(master=self.frame_right)
        self.possible_password_name.insert(0, 'None')
        self.possible_password_name.pack()

        # Checkbox
        self.uppercase = tk.BooleanVar()
        self.uppercase_letters = tk.Checkbutton(master=self.frame_left,
                                                text='Uppercase letters',
                                                variable=self.uppercase)
        self.uppercase_letters.pack(fill=tk.Y, anchor='w')

        self.symbol = tk.BooleanVar()
        self.symbols = tk.Checkbutton(master=self.frame_left,
                                      text='Symbols',
                                      variable=self.symbol)
        self.symbols.pack(fill=tk.Y, anchor='w')

        self.password_length_exact = tk.Label(master=self.frame_left,
                                              text='Password length: ')
        self.password_length_exact.pack(fill=tk.Y, anchor='w')

        self.possible_password_length = tk.Entry(master=self.frame_left)
        self.possible_password_length.insert(0, '16')

        self.possible_password_length.pack()

        # Button
        self.button = tk.Button(master=self.frame_right, text='Generate Password')
        self.button.bind('<ButtonRelease>', self.password_generator)
        self.button.pack(fill=tk.Y)

    def password_generator(self, event):
        __password = str()
        iteration = 0

        while iteration < int(self.possible_password_length.get()):
            element = random.choices(['lowercase', 'uppercase', 'integer', 'symbol'], weights=[50, 30, 20, 10])

            if element[0] == 'lowercase':
                __password += random.choice('abcdefghijklmnopqrstuwdxyz')
                iteration += 1

            elif element[0] == 'uppercase' and self.uppercase.get() is True:
                __password += random.choice('abcdefghijklmnopqrstuwdxyz'.upper())
                iteration += 1

            elif element[0] == 'integer':
                __password += str(random.SystemRandom().randint(0, 9))
                iteration += 1

            elif element[0] == 'symbol' and self.symbol.get() is True:
                __password += random.choice('!@#$%&*?()[]')
                iteration += 1

        self.call_message(__password)

        return __password

    def save_password(self, password):
        current_time = datetime.datetime.now().strftime('%c')

        if os.path.exists(f'{os.getcwd()}/passwords.txt'):
            with open(f'{os.getcwd()}/passwords.txt', 'a') as f:
                f.write(f'{current_time}\t{password}\t{self.possible_password_name.get()}\n')
        else:
            with open(f'{os.getcwd()}/passwords.txt', 'a') as f:
                f.write(f'Creation_Time\tPassword\tPassword_Name\n')
                f.write(f'{current_time}\t{password}\t{self.possible_password_name.get()}\n')

    def call_message(self, password):
        message = Tk()
        message.geometry('200x80')
        message.title('Message')
        w = tk.Label(message, text=f'Your new password is:\n{password}')
        w.pack()

        button = tk.Button(master=message, text='Save Password')
        button.bind('<ButtonRelease>', self.save_password(password))
        button.pack(fill=tk.Y)

        message.mainloop()


root = Tk()

root.title('Password Generator')
root.minsize(400, 130)
root.maxsize(400, 130)

Window(root).pack()

root.mainloop()
