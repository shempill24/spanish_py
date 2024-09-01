from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def button_click(number):
    	e.insert(0, number)


button_1 = Button(root, padx=40, pady=20, command= lambda: button_click(1),  text="1")
button_2 = Button(root, padx=40, pady=20, command=lambda: button_click(2), text="2")
button_3= Button(root,  padx=40, pady=20, command=lambda: button_click(3), text="3")
button_4 = Button(root,  padx=40, pady=20, command=lambda: button_click(4), text="4")
button_5 = Button(root,  padx=40, pady=20, command=lambda: button_click(5), text="5")
button_6 = Button(root,  padx=40, pady=20, command=lambda: button_click(6), text="6")
button_7 = Button(root, padx=40, pady=20, command=lambda: button_click(7), text="7")
button_8 = Button(root,  padx=40, pady=20, command=lambda: button_click(8), text="8")
button_9 = Button(root, padx=40, pady=20, command=lambda: button_click(9), text="9")
button_0 = Button(root, padx=40, pady=20, command=lambda: button_click(0), text="0")

button_add = Button(root, padx=39, pady=20, command=button_click, text="+")
button_equal = Button(root, padx=91, pady=20, command=button_click, text="=")
button_clear = Button(root, padx=79, pady=20, command=button_click, text="Clear")




#button_placement

button_1.grid(row=3, column = 0)
button_2.grid(row=3, column = 1)
button_3.grid(row=3, column = 2)

button_4.grid(row=2, column = 0)
button_5.grid(row=2, column = 1)
button_6.grid(row=2, column = 2)

button_7.grid(row=1, column = 0)
button_8.grid(row=1, column = 1)
button_9.grid(row=1, column = 2)

button_0.grid(row=4, column = 0)
button_clear.grid(row=4, column = 1, columnspan=2)

button_add.grid(row=5, column = 0)
button_equal.grid(row=5, column = 1, columnspan=2)




root.mainloop() 