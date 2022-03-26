from tkinter import *

CONVERSION_RATIO = 1.609


def convert_to_km():
    miles = miles_entry.get()
    km_value["text"] = ''
    if miles != '' and miles.isnumeric():
        km_value["text"] = int(miles) * 1.609


window = Tk()

window.title("Miles to Km Converter")
window.config(padx=25, pady=25)
window.minsize(width=250, height=100)

miles_entry = Entry(width=5)
miles_entry.grid(row=1, column=2)
miles_label = Label(text="Miles")
# label.pack(side="left")
miles_label.grid(row=1, column=3)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=2, column=1)

km_value = Label()
km_value.grid(row=2, column=2)

km_unit_label = Label(text="km")
km_unit_label.grid(row=2, column=3)

calc_button = Button(text="Calculate", command=convert_to_km)
calc_button.grid(row=3, column=2)

window.mainloop()
