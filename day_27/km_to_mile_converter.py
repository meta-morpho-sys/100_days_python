from tkinter import *

def convert_miles(miles):
    km = miles * 1.609
    return km

def button_clicked():
    number = float(unit_to_convert.get())
    km = convert_miles(number)
    result_label.config(text=km)


window = Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=200)
window.config(padx=100, pady=100, bg='blue')


result_unit_label = Label(text='km')
result_unit_label.grid(column=2, row=1)
result_unit_label.config(padx=10, pady=10, borderwidth=1.1)

button = Button(text='Calculate', command=button_clicked, width=4)
button.grid(column=1,row=2)
button.config(padx=10,pady=10)

unit_to_convert = Entry(width=7)
unit_to_convert.insert(END, string="0")
unit_to_convert.focus()
unit_to_convert.grid(column=0, row=0)

unit_label = Label(text='miles')
unit_label.grid(column=1,row=0)
unit_label.config(padx=10,pady=10)

eq_label = Label(text='equals to')
eq_label.grid(column=0,row=1)
eq_label.config(padx=10,pady=10)


result_label = Label(text='0')
result_label.grid(column=1,row=1)
result_label.config(padx=10,pady=10, background='red')

#
# result_unit_label = Label(text='km')
# result_unit_label.grid(column=2, row=1)
# result_unit_label.config(padx=10, pady=10)


window.mainloop()
