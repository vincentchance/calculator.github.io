from tkinter import*
import math as m

root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.geometry("288x450")
root.iconbitmap("calculator12.ico")

text = Entry(root, font=("calibri",25),justify=RIGHT)
text.pack(fill=X, padx=5,pady=5,ipadx=5,ipady=5)
text.insert(END,0)


def addToText(n):
    text.insert(END,n)
def clear():
    text.delete(0,END)
def backspc():
    current= text.get()
    length=len(current)-1
    text.delete(length,END)
def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)
def negate():
    e= str(-(int(text.get())))
    text.delete(0,END)
    text.insert(0,e)
def roots():
    f= str(m.sqrt(int(text.get())))
    text.delete(0,END)
    text.insert(0,f)

frame = Frame(root)
frame.pack(side = TOP, anchor = NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()
#1 to 3
btn1 = Button(frame1, text= "1", width =7,height=3, font=("calibri",13),bg="snow", command=lambda:addToText("1"))
btn1.pack(side=LEFT)
btn2 = Button(frame1, text ="2", width = 7, height =3,font=("calibri",13),bg="snow",command=lambda:addToText("2"))
btn2.pack(side=LEFT)
btn3 = Button(frame1, text ="3", width=7, height=3, font=("calibri",13),bg="snow", command=lambda:addToText("3"))
btn3.pack(side=LEFT)
btnclear=Button(frame1, text="CE", width=7, height=3, font=("calibri",13),bg="SkyBlue1", command=lambda:clear())
btnclear.pack(side=LEFT)

frame2 =Frame(frame)
frame2.pack()
#4 to 6
btn4=Button(frame2, text="4", width=7,height=3, font=("calibri",13), bg= "snow",command=lambda:addToText("4"))
btn4.pack(side=LEFT)
btn5=Button(frame2, text="5", width=7, height=3, font=("calibri",13),bg= "snow",command=lambda:addToText("5"))
btn5.pack(side=LEFT)
btn6=Button(frame2,text="6",width=7, height=3, font=("calibri",13),bg= "snow",command=lambda:addToText("6"))
btn6.pack(side=LEFT)
btn9=Button(frame2,text="C",width=7,height=3, font=("calibri",13),bg="snow3",command=lambda:backspc())
btn9.pack(side=LEFT)

frame3=Frame(frame)
frame3.pack()
#7 to 9
btn7=Button(frame3,text="7",width=7,height=3, font=("calibri",13),bg= "snow",command=lambda:addToText("7"))
btn7.pack(side=LEFT)
btn8=Button(frame3,text="8",width=7,height=3, font=("calibri",13),bg="snow",command=lambda:addToText("8"))
btn8.pack(side=LEFT)
btn9=Button(frame3,text="9",width=7,height=3, font=("calibri",13),bg="snow",command=lambda:addToText("9"))
btn9.pack(side=LEFT)
btn9=Button(frame3,text="+",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:addToText("+"))
btn9.pack(side=LEFT)

frame4= Frame(frame)
frame4.pack()

btnegate=Button(frame4,text=".", width=7,height=3, font=("calibri",13),bg="snow",command=lambda:addToText("."))
btnegate.pack(side=LEFT)
btpoint=Button(frame4,text="0",width=7,height=3,font=("calibri",13),bg="snow",command=lambda:addToText("0"))
btpoint.pack(side=LEFT)
btneq=Button(frame4,text="=",width=7,height=3,font=("calibri",13), bg="snow",command=lambda:calculate())
btneq.pack(side=LEFT)
btnDivide=Button(frame4,text="-",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:addToText("-"))
btnDivide.pack(side=LEFT)

frame5= Frame(frame)
frame5.pack()

btnRoot=Button(frame5,text="√",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:roots())
btnRoot.pack(side=LEFT)
btnExp=Button(frame5,text="+/-",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:negate())
btnExp.pack(side=LEFT)
btnPlus=Button(frame5,text="÷",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:addToText("/"))
btnPlus.pack(side=LEFT)
btnMinus=Button(frame5,text="x",width=7,height=3,font=("calibri",13),bg="snow3",command=lambda:addToText("*"))
btnMinus.pack(side=LEFT)

root.mainloop()
