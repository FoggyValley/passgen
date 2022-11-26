#!/usr/bin/env python

import random
import os
import datetime


def initialize_params():
    
    while True:
        password_lenght = input('What password lenght do you preffer?(default: 16 characters)? ')
        
        if password_lenght == '':
            password_lenght = 16
            break
        elif not password_lenght.isdigit():
            print('Please, type a digit')
            continue
        else:
            password_lenght = int(password_lenght)
            break
            
    while True:
        uppercase_letters = input('Use uppercase letters ([y]/n)? ')
        if uppercase_letters != 'y' and uppercase_letters != 'n' and uppercase_letters != '':
            print('''Please, type 'y' or 'n' ''')
            continue
        elif uppercase_letters == 'y' or uppercase_letters == '':
            uppercase_letters = True
            break
        else:
            uppercase_letters = False
            break
            
    while True:
        symbols = input('''Use other symbols (e.g. '!@#$%&*?') ([y]/n)? ''')
        
        if symbols != 'y' and symbols != 'n' and symbols != '':
            print('''Please, type 'y' or 'n' ''')
            continue
        elif symbols == 'y' or symbols == '':
            symbols = True
            break
        else:
            symbols = False
            break
            
    name = input('Would you like to name this password record (y/[n])? ')
    
    if name == 'y':
        name = input('Type a name: ')
    else:
        name = 'None'
        
    return password_lenght, uppercase_letters, symbols, name


def password_generator(password_lenght, uppercase_letters=True, symbols=True):
    password = str()
    iteration = 0
    
    while iteration < password_lenght:
        element = random.choices(['lowercase', 'uppercase', 'integer', 'symbol'], weights=[50, 30, 20, 10])
        
        if element[0] == 'lowercase':
            password += random.choice('abcdefghijklmnopqrstuwdxyz')
            iteration+=1
            
        elif element[0] == 'uppercase' and uppercase_letters == True:
            password += random.choice('abcdefghijklmnopqrstuwdxyz'.upper())
            iteration+=1
            
        elif element[0] == 'integer':
            password += str(random.SystemRandom().randint(0,9))
            iteration+=1
            
        elif element[0] == 'symbol' and symbols == True:
            password += random.choice('!@#$%&*?')
            iteration+=1
            
    return password


if __name__ == '__main__':
    password_lenght, uppercase_letters, symbols, name = initialize_params()
    while True:
        password = password_generator(password_lenght, uppercase_letters, symbols)
        print(f'Your new password: {password}')
        repeat = input('Generate other one with same parameters(y/[n])? ')
        
        if repeat !='y':
            current_time = datetime.datetime.now().strftime('%c')
            
            if os.path.exists(f'{os.getcwd()}/passwords.txt'):
                with open(f'{os.getcwd()}/passwords.txt','a') as f:
                    f.write(f'{current_time}\t{password}\t{name}\n')
            else:
                with open(f'{os.getcwd()}/passwords.txt','a') as f:
                    f.write(f'Creation_Time\tPassword\tPassword_Name\n')
                    f.write(f'{current_time}\t{password}\t{name}\n')
                    
            print('You could find a file with your passwords in the working directory')
        
            break
