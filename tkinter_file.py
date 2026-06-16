import tkinter
import tkinter as tk
from tkinter.font import Font
#Tk is class...window is the object and to see the window, mainloop is the method

from tkinter import ttk
# ttk is themed tk - we can replace tk with ttk below with label, button .....

window = tk.Tk()
window.title("My App")
window.minsize(width=400,height=300)
# window.geometry("500x500")
#label = tk.Label(text="Hello World", font=("Arial", 20, "bold"))
# label.pack()

custom_font = Font(family="Times New Roman", size=15, weight="bold", slant='italic')
label = ttk.Label(text="My new app", font=custom_font, padding=10, background="gray")
label.pack()
#label.config(font=("Arial", 20, "underline"))
# label.config(text = "Changing Text")
#label.place(x=10, y=50) #For positioning
label['text'] = "Hello World"


# Taking user input using Entry class
# user_input = tk.Entry(width=40, show="*") #For masked input like passwords
user_input = tk.Entry(width=40)
user_input.pack(pady=10)

def fun_button():
    input_text = user_input.get()
    label.config(text=input_text)

# counter = 0
# def fun_button():
#     global counter
#     counter += 1
#     label.config(text=f"Button got clicked {counter} times")

#Buttons
#button = tk.Button(text="Click me", command=lambda: print("You clicked button"))
button = tk.Button(text="Click me", command=fun_button)
button.pack()

quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack(pady=10)
# quit_button.place(x=0,y=0)

# Frames
# my_frame = ttk.Frame()
# my_frame.pack(side="down", fill="both", expand=True)

#Separator
sep = ttk.Separator(orient="horizontal")
sep.pack(fill="x")

#Textbox
text = tk.Text(height=5,width=30)
text.pack(pady=10)
text.focus()
text.insert("1.0","Enter your comments")

def text_function():
    text_data = text.get("1.0", "end")
    print(text_data)

txt_button = ttk.Button(text="Get Text", command=text_function)
txt_button.pack()

# text['state'] = 'disabled'
#
# def enable_text():
#     text['state'] = 'normal'
# enable_button = ttk.Button(text="Enable textbox", command=enable_text)
# enable_button.pack()

#Checkbutton
check_option = tk.IntVar()

def check_option_function():
    print(check_option.get())

check_button = ttk.Checkbutton(text="Agree with terms and conditions", variable=check_option,
                               command=check_option_function)
check_button.pack()


#Radiobutton
radio_value = tk.StringVar()

def radio_function():
    print(radio_value.get())
option_1 = ttk.Radiobutton(text="Yes", variable=radio_value, value="yes",command=radio_function)
option_2 = ttk.Radiobutton(text="No", variable=radio_value, value="no",command=radio_function)
option_1.pack()
option_2.pack()

#Combobox(dropdown)
selected_country = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_country, state="readonly",values=("India","Australia","England"))
countries.pack()

def select_country_function(event):
    label.config(text=f"Selected country is {selected_country.get()}")
    print(selected_country.get())

countries.bind("<<ComboboxSelected>>", select_country_function)

#Listbox

food_items=("Pizza","Burger","Diet Coke","Apple","Mango")
selected_food = tk.StringVar(value = food_items)
food_list = tk.Listbox(listvariable=selected_food, height=5, selectmode="extended")
food_list.pack(pady=10)

def select_food_function(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))
    print()

food_list.bind("<<ListboxSelect>>", select_food_function)

#Spinbox

counter = tk.IntVar(value=10)

def get_spin_box_value():
    print(f"Current spin box value: {spin_box.get()}")

spin_box = ttk.Spinbox(from_=0, to=20, textvariable=counter, wrap=True,command=get_spin_box_value)
#spin_box = ttk.Spinbox(values=tuple(range(5,100,5)), textvariable=counter, wrap=True,command=get_spin_box_value)
spin_box.pack()

print(f"Initial spin box value: {spin_box.get()}")

window.mainloop()

