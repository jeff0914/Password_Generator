import tkinter as tk
import string
import random

def password_generator(min_length, numbers=True, special_charaters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_charaters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_charaters:
            meets_criteria = meets_criteria and has_special

    return pwd

def generate_password():
    min_length = int(entry_min_length.get())
    has_number = var_number.get() == 1
    has_special = var_special.get() == 1
    pwd = password_generator(min_length, has_number, has_special)
    result_entry.delete(0, 'end')
    result_entry.insert(0, pwd)

root = tk.Tk()
root.title("密碼生成器")

label_min_length = tk.Label(root, text="輸入最小長度:")
label_min_length.pack()
entry_min_length = tk.Entry(root)
entry_min_length.pack()

var_number = tk.IntVar()
check_number = tk.Checkbutton(root, text="需要數字?", variable=var_number)
check_number.pack()

var_special = tk.IntVar()
check_special = tk.Checkbutton(root, text="需要特殊字元?", variable=var_special)
check_special.pack()

generate_button = tk.Button(root, text="生成密碼", command=generate_password)
generate_button.pack()

result_entry = tk.Entry(root)
result_entry.pack()

root.mainloop()
