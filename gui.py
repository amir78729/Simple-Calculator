from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")

button_1 = Button(window, text="1", height = 1, width = 2)
button_1.grid(column=0, row=0)

button_2 = Button(window, text="2", height = 1, width = 2)
button_2.grid(column=1, row=0)

button_3 = Button(window, text="3", height = 1, width = 2)
button_3.grid(column=2, row=0)

button_4 = Button(window, text="4", height = 1, width = 2)
button_4.grid(column=0, row=1)

button_5 = Button(window, text="5", height = 1, width = 2)
button_5.grid(column=1, row=1)

button_6 = Button(window, text="6", height = 1, width = 2)
button_6.grid(column=2, row=1)

button_7 = Button(window, text="7", height = 1, width = 2)
button_7.grid(column=0, row=2)

button_8 = Button(window, text="8", height = 1, width = 2)
button_8.grid(column=1, row=2)

button_9 = Button(window, text="9", height = 1, width = 2)
button_9.grid(column=2, row=2)

button_0 = Button(window, text="0", height = 1, width = 2)
button_0.grid(column=0, row=3)

button_decimal_point = Button(window, text=".", height = 1, width = 2)
button_decimal_point.grid(column=1, row=3)

button_negative = Button(window, text="-/+", height = 1, width = 2)
button_negative.grid(column=2, row=3)

button_equals = Button(window, text="=", height = 1, width = 2 , bg="red", fg="white")
button_equals.grid(column=3, row=3)

button_sum = Button(window, text="+", height = 1, width = 2)
button_sum.grid(column=3, row=2)

button_minus = Button(window, text="-", height = 1, width = 2)
button_minus.grid(column=3, row=1)

window.mainloop()
