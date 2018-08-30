from tkinter import *

class calculadora(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Dotum 15')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculadora Simples')

        self.display = StringVar()
        e = Entry(self, relief=SUNKEN, textvariable=self.display)
        e.pack(side=TOP, expand=YES, fill=BOTH)

        for key in ("123", "456", "789"):
            keyF = self.frame(TOP)
            for char in key:
                self.button(keyF, LEFT, char,
                            lambda c=char: self.digit(c))

        keyF = self.frame(TOP)
        self.button(keyF, LEFT, '0', lambda ch='0': self.digit(ch))

        opsF = self.frame(TOP)
        for char in "+-=":
            if char == '=':
                btn = self.button(opsF, LEFT, char, self.calc)
            else:
                btn = self.button(opsF, LEFT, char, 
                                  lambda disp=self, s=char: disp.oper(s))

        clr = self.frame(BOTTOM)
        self.button(clr, LEFT, 'C', lambda disp=self.display: disp.set(''))
    

    def frame(this, side): 
        disp = Frame(this)
        disp.pack(side=side, expand=YES, fill=BOTH)
        return disp


    def button(this, win, side, text, command=None): 
        disp = Button(win, text=text, fg='red', command=command) 
        disp.pack(side=side, expand=YES, fill=BOTH)
        return disp    

    clear = False
    def digit(self, digit):
        if self.clear:
            self.display.set('')
            self.clear = False
        self.display.set(self.display.get() + digit)

    def sign(self):
        clear = False
        cont = self.display.get()
        if len(cont) > 0 and cont[0] == '-':
            self.display.set(cont[1:])
        else:
            self.display.set('-' + cont)


    def oper(self, op):
        self.display.set(self.display.get() + ' ' + op + ' ')
        self.clear = False

    def calc(self):
        try:
            self.display.set(eval(self.display.get()))
            self.clear = True
        except:
            showerror('Operation Error', 'Illegal Operation')
            self.display.set('')
            self.clear = False

    def equals(self):
        try:
            result = eval(self.display.get())
            if result >= 1000:
                result (calc)
        except: 
            results("ERROR")
        display.delete(0, END) 
        display.insert(0, display)

    

if __name__ == '__main__':
    calculadora().mainloop()
