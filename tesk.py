import tkinter as tk
class Program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pro")
        self.window.config(bg="black",cursor="mouse")
        self.window.geometry("450x450")
    def vars(self):
        self.val = ""
        self.number = 0
        self.gr = 1
        self.buttons = []
        self.inputt = tk.StringVar()
    def operators1(self):
        self.val+="*"
        self.inputt.set(self.val)
    def operators2(self):
        self.val+="+"
        self.inputt.set(self.val)
    def operators3(self):
        self.val+="-"
        self.inputt.set(self.val)
    def operators4(self):
        self.val+="/"
        self.inputt.set(self.val)
    def operators5(self):
        self.val+="%"
        self.inputt.set(self.val)
    def operators6(self):
        self.val = ""
        self.inputt.set(self.val)
    def equal(self):
        total = str(eval(self.val))
        self.inputt.set(total)
        self.val = total
    def b1(self):
        self.val+="1"
        self.inputt.set(self.val)
    def b2(self):
        self.val+="2"
        self.inputt.set(self.val)
    def b3(self):
        self.val+="3"
        self.inputt.set(self.val)
    def b4(self):
        self.val+="4"
        self.inputt.set(self.val)
    def b5(self):
        self.val+="5"
        self.inputt.set(self.val)
    def b6(self):
        self.val+="6"
        self.inputt.set(self.val)
    def b7(self):
        self.val+="7"
        self.inputt.set(self.val)
    def b8(self):
        self.val+="8"
        self.inputt.set(self.val)
    def b9(self):
        self.val+="9"
        self.inputt.set(self.val)
    def body(self):
        tk.Entry(self.window,textvariable=self.inputt,bg="white",fg="black",bd=0,font=("Tahoma",18)).grid(row=1,column=1)
        for i in range(2,10+1):
                self.number +=1
                self.buttons.append(tk.Button(self.window,text="{}".format(self.number),bg="black",fg="white",font=("Tahoma",18),bd=0))
        tk.Button(self.window,text="=",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.equal)).grid(row=2,column=4)
        tk.Button(self.window,text="*",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators1)).grid(row=3,column=4)
        tk.Button(self.window,text="+",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators2)).grid(row=4,column=4)
        tk.Button(self.window,text="-",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators3)).grid(row=2,column=5)
        tk.Button(self.window,text="/",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators4)).grid(row=3,column=5)
        tk.Button(self.window,text="%",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators5)).grid(row=4,column=5)
        tk.Button(self.window,text="clear",bg="black",fg="white",bd=0,font=("Tahoma",18),command=(self.operators6)).grid(row=2,column=6)       
        for i in self.buttons[0:3]:
            self.gr+=1
            i.grid(row=self.gr,column=0)
        self.gr = 1
        for i in self.buttons[3:6]: 
            self.gr+=1
            i.grid(row=self.gr,column=1)
        self.gr = 1
        for i in self.buttons[6:9]:
            self.gr+=1
            i.grid(row=self.gr,column=2)  
        self.buttons[0].config(command=(self.b1))
        self.buttons[1].config(command=(self.b2))
        self.buttons[2].config(command=(self.b3))
        self.buttons[3].config(command=(self.b4))
        self.buttons[4].config(command=(self.b5))
        self.buttons[5].config(command=(self.b6))
        self.buttons[6].config(command=(self.b7))
        self.buttons[7].config(command=(self.b8))
        self.buttons[8].config(command=(self.b9))
    def main(self):
        self.vars()
        self.body()
        self.window.mainloop()