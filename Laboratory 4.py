from tkinter import *
win = Tk()

win.geometry("330x390")
win.title("Calculator")
win.configure(bg = "light blue")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

#row0
txt1 = Entry(win, bd = 10, bg = "#82EEFD", font = ("calibri", 18), width = 27, textvariable = equation)
txt1.grid(row = 0, column = 0, columnspan =10)

#row1
clrbtn = Button(win, text = "C", width = 28, font = ("calibri", 18), command = clear)
clrbtn.grid(row = 1, column = 0, columnspan = 10)

#row2
btn7 = Button(win, text = "7", width = 6, font = ("calibri", 18), command=lambda: press(7))
btn7.grid(row = 2, column = 0, columnspan = 2)

btn8 = Button(win, text = "8", width = 6, font = ("calibri", 18), command=lambda: press(8))
btn8.grid(row = 2, column = 3, columnspan = 2)

btn9 = Button(win, text = "9", width = 6, font = ("calibri", 18), command=lambda: press(9))
btn9.grid(row =2, column = 6, columnspan = 2)

divbtn = Button(win, text = "/", width = 8, font = ("calibri", 18), command=lambda: press("/"))
divbtn.grid(row = 2, column = 8, columnspan = 2,sticky="E")

#row3
btn4 = Button(win, text = "4", width = 6, font = ("calibri", 18), command=lambda: press(4))
btn4.grid(row = 3, column = 0, columnspan = 2)

btn5 = Button(win, text = "5", width = 6, font = ("calibri", 18), command=lambda: press(5))
btn5.grid(row = 3, column = 3, columnspan = 2)

btn6 = Button(win, text = "6", width = 6, font = ("calibri", 18), command=lambda: press(6))
btn6.grid(row = 3, column = 6, columnspan = 2)

mulbtn = Button(win, text = "*", width = 8, font = ("calibri", 18), command=lambda: press("*"))
mulbtn.grid(row = 3, column = 8, columnspan = 2,sticky="E")

#row4
btn1 = Button(win, text = "1", width = 6, font = ("calibri", 18), command=lambda: press(1))
btn1.grid(row = 4, column = 0, columnspan = 2)

btn2 = Button(win, text = "2", width = 6, font = ("calibri", 18), command=lambda: press(2))
btn2.grid(row = 4, column = 3, columnspan = 2)

btn3 = Button(win, text = "3", width = 6, font = ("calibri", 18), command=lambda: press(3))
btn3.grid(row = 4, column = 6, columnspan = 2)
subbtn = Button(win, text = "-", width = 8, font = ("calibri", 18), command=lambda: press("-"))
subbtn.grid(row = 4, column = 8, columnspan = 2,sticky="E")

#row 5
btn0 = Button(win, text = "0", width = 9, font = ("calibri", 18), command=lambda: press(0))
btn0.grid(row = 5, column = 0, columnspan = 4)

dotbtn = Button(win, text = ".", width = 9, font = ("calibri", 18), command=lambda: press("."))
dotbtn.grid(row = 5, column = 4, columnspan = 4)

addbtn = Button(win, text = "+", width = 9, font = ("calibri", 18), command=lambda: press("+"))
addbtn.grid(row = 5, column = 8, columnspan = 4)

#row 6
equalbtn = Button(win, text = "=", width = 29, font = ("calibri", 18), command = equalpress)
equalbtn.grid(row = 6, column = 0, columnspan = 12)

win.mainloop()
