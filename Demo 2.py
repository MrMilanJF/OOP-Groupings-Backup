from tkinter import *

win = Tk()
win.geometry("490x300+10+10")
win.title("Grid Manager")

text1 = Entry(bd=2)
text1.grid(row=0, column=0)
text1.insert(0, "row 0, cloumn 1")

text2 = Entry(bd=2)
text2.grid(row=0, column=1)
text2.insert(0, "row 0,column 2")

text3 = Entry(bd=2)
text3.grid(row=0, column=2,)
text3.insert(0, "row 0,column 3")

text4 = Entry(bd=2)
text4.grid(row=1, column=0,)
text4.insert(0, "row 0,column 4")

text5 = Entry(bd=2)
text5.grid(row=1, column=1,)
text5.insert(1, "row 0,column 5")

text6 = Entry(bd=2)
text6.grid(row=1, column=2,)
text6.insert(1, "row 0,column 6")

text7 = Entry(bd=2)
text7.grid(row=2, column=0,)
text7.insert(0, "row 0,column 7")

text8 = Entry(bd=2)
text8.grid(row=2, column=1,)
text8.insert(0, "row 0,column 8")

text9 = Entry(bd=2)
text9.grid(row=2, column=2,)
text9.insert(0, "row 0,column 9")





win.mainloop()