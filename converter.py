from tkinter import *

def mile_to_km():
    miles=miles_entry.get()
    km_value2=int(miles) * 1.609
    km_value.config(text=km_value2)

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
km=0
miles_entry=Entry(width=7)
miles_entry.grid(column=1,row=0)
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal_label=Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)
km_value=Label(text="0")
km_value.grid(column=1,row=1)
Km=Label(text="Km")
Km.grid(column=2,row=1)
button=Button(text="Calculate",command=mile_to_km)
button.grid(column=1,row=2)

window.mainloop()