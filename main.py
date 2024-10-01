import tkinter

window = tkinter.Tk()
window.title("My first GUI program with tkinter")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I'm a label", font=("Arial", 14, "bold"))
my_label.pack()

window.mainloop()