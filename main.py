from tkinter import *


def button_clicked():
    miles = float(mile_entry.get())
    km = round(miles * 1.609)
    km_value["text"] = f"{km}"


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

mile_entry = Entry(width=7)
mile_entry.grid(row=0, column=1)
miles = Label(text="Miles")
miles.grid(row=0, column=2)

km_value = Label(text="0")
km_value.grid(row=1, column=1)
km = Label(text="Km")
km.grid(row=1, column=2)

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(row=2, column=1)


window.mainloop()
