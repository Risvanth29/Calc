from tkinter import *
from tkinter import ttk
import math

win = Tk()
a = IntVar()
win.geometry('300x400')
win.title("Calculator")
win.config(bg='powder blue')
win.resizable(0,0)
win.iconbitmap('LOGO.ico')
e = Entry(win, text = a, width = 20,font = ("",16),borderwidth = 0)
e.place(x=30,y=10,height = 40)

e.delete(0,"end")
def insert0():
	global e
	e.insert('end',1)
def insert1():
	global e
	e.insert('end',2)
	
def insert2():
	global e
	e.insert('end',3)
	
def insert3():
	global e
	e.insert('end',4)
	
def insert4():
	global e
	e.insert('end',5)
	
def insert5():
	global e
	e.insert('end',6)
	
def insert6():
	global e
	e.insert('end',7)
	
def insert7():
	global e
	e.insert('end',8)
	
def insert8():
	global e
	e.insert('end',9)
	
def insert9():
	global e
	e.insert('end',0)
	
def dele():
	global e
	e.delete(0,'end')
	
def delet():
	global e
	global char_
	char_ = a.get()
	char_ = str(char_)
	chars_ = len(char_)
	to_dele = (chars_-1) 
	e.delete(to_dele,'end')
def plus():
	global first_num
	global sign
	sign = '+'
	first_num = a.get()	
	e.delete(0,'end')
def minus():
	global first_num
	global sign
	sign = '-'
	first_num = a.get()	
	e.delete(0,'end')
def mul():
	global first_num
	global sign
	sign = '*'
	first_num = a.get()	
	e.delete(0,'end')
def div():
	global first_num
	global sign
	sign = '/'
	first_num = a.get()	
	e.delete(0,'end')
def eq():
	global first_num
	print(first_num)
	second_num = a.get()
	if sign=='+':
		e.delete(0,'end')
		e.insert(0, (first_num+second_num))
	if sign=='-':
		e.delete(0,'end')
		e.insert(0, (first_num-second_num))
	if sign=='/':
		e.delete(0,'end')
		e.insert(0, (first_num/second_num))
	if sign=='*':
		e.delete(0,'end')
		e.insert(0, (first_num*second_num))
	if sign=='**':
		e.delete(0,'end')
		e.insert(0, (first_num**second_num))

def sqr():
	global sign
	global first_num
	sign = '**'
	first_num = a.get()	
	e.delete(0,'end')

def sqrtfunc():
	global sign
	global first_num
	sign = 'sqrt'
	first_num = a.get()
	e.delete(0,"end")
	if sign=="sqrt":
		e.delete(0,"end")
		e.insert(0, (math.sqrt(first_num)))

def normal():
	b70.config(text = "+",command = plus)
	b102.config(text = '>>>', command = next)
	b80.config(text = "-", command = minus)
	b70.config(text = "+",command=plus)
def fac():
	global first_num
	first_num = a.get()
	first_num = math.factorial(first_num)
	e.insert(0,first_num)
def next():
	b70.config(text = "power", command = sqr)
	b102.config(text = "<<<", command = normal)
	b80.config(text = "!", command = fac)
	b90.config(text = "sqrt",command = sqrtfunc)

b = Button(win, text = 1,width = 6,height = 3,command = insert0,borderwidth = 0)
b.place(x=30,y=70)
b1 = Button(win, text = 2, width = 6, height = 3,command = insert1,borderwidth = 0)
b1.place(x=90,y=70)
b2 = Button(win, text = 3, width = 6, height = 3,command = insert2,borderwidth = 0)
b2.place(x=150,y=70)
b3 = Button(win, text = 4, width = 6, height = 3,command = insert3,borderwidth = 0)
b3.place(x=210,y=70)
b4 = Button(win, text = 5, width = 6, height = 3,command = insert4,borderwidth = 0)
b4.place(x=30,y=140)
b10 = Button(win, text = 6, width = 6, height = 3,command = insert5,borderwidth = 0)
b10.place(x=90,y=140)
b20 = Button(win, text = 7, width = 6, height = 3,command = insert6,borderwidth = 0)
b20.place(x=150,y=140)
b30 = Button(win, text = 8, width = 6, height = 3,command = insert7,borderwidth = 0)
b30.place(x=210,y=140)
b40 = Button(win, text = 9,width = 6,height = 3,command = insert8,borderwidth = 0)
b40.place(x=90,y=210)
b50 = Button(win, text = 0,width = 6,height = 3,command = insert9,borderwidth = 0)
b50.place(x=150,y=210)
b50 = Button(win, text = "CLEAR",width = 6,height = 3,command = dele,borderwidth = 0)
b50.place(x=210,y=210)
b60 = Button(win, text = "AC",width = 6,height = 3,command = delet,borderwidth = 0)
b60.place(x=30,y=210)
b70 = Button(win, text = "+",width = 6,height = 3,command = plus,borderwidth = 0)
b70.place(x=30,y=280)
b80 = Button(win, text = "-",width = 6,height = 3,command = minus,borderwidth = 0)
b80.place(x=90,y=280)
b90 = Button(win, text = "/",width = 6,height = 3,command = div,borderwidth = 0)
b90.place(x=150,y=280)
b100 = Button(win, text = "x",width = 6,height = 3,command = mul,borderwidth = 0)
b100.place(x=210,y=280)
b101 = Button(win, text = '=', width = 6, height = 2, command = eq,borderwidth = 0)
b101.place(x = 90, y = 345)
b102 = Button(win, text = '>>>', width = 6,height = 2, command = next,borderwidth = 0)
b102.place(x = 150, y = 345)
win.mainloop()
