from tkinter import *
from tkinter import ttk
from functools import partial
from clasefraccion import fraccion

class Calculadora(object):
    __ventana = None
    __operador = None
    __primerOperando = None
    __segundoOperando = None
    __resultado = 0
    __panel = None


    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculadora')
        self.__ventana.resizable(0, 0)
        frame = ttk.Frame(self.__ventana, padding="3 10 3 10")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame['borderwidth'] = 2
        frame['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        self.__resultado = 0
        operatorEntry = ttk.Entry(frame, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(frame, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))

        ttk.Button(frame, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(frame, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(frame, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(frame, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(frame, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(frame, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(frame, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(frame, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(frame, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(frame, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(frame, text='+', command=partial(self.opera, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(frame, text='-', command=partial(self.opera, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(frame, text='*', command=partial(self.opera, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(frame, text='%', command=partial(self.opera, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(frame, text='/', command=partial(self.ponerNUMERO, '/')).grid(column=3, row=7, sticky=W)
        ttk.Button(frame, text='=', command=partial(self.opera, '=')).grid(column=2, row=8, sticky=(W, E),
                                                                                       columnspan=2)
        ttk.Button(frame, text='DEL', command=self.borrar).grid(column=1, row=8, sticky=W)
        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            if numero == '/':
                pos = valor.find('/')
                if pos != -1:
                    self.__panel.set(valor)
                else:
                    self.__panel.set(valor + numero)
            else:
                self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            pos = valor.find('/')
            if pos != -1:
                num = int(valor[0:pos])
                den = int(valor[pos + 1:])
                self.__primerOperando = fraccion(num, den)
            else:
                self.__primerOperando = int(valor)
            self.__panel.set(numero)

    def borrar(self):
        self.__panel.set('')
        self.__operador.set('')

    def resolver(self, operando1, operacion, operando2):
        if operacion != '':
            resultado = 0
            if operacion == '+':
                resultado = operando1 + operando2
            else:
                if operacion == '-':
                    resultado = operando1 - operando2
                else:
                    if operacion == '*':
                        resultado = operando1 * operando2
                    else:
                        if operacion == '%':
                            resultado = operando1 / operando2

            if isinstance(resultado, fraccion):
                resultado.simpli()

            self.__panel.set(str(resultado))

    def opera(self, op):
        if op == '=':
            operacion = self.__operador.get()
            self.__segundoOperando = self.__panel.get()
            pos = self.__segundoOperando.find('/')
            if pos != -1:
                if operacion != '':
                    num = int(self.__segundoOperando[0:pos])
                    den = int(self.__segundoOperando[pos + 1:])
                    self.__segundoOperando = fraccion(num, den)
                    self.__segundoOperando.simpli()
                else:
                    num = int(self.__segundoOperando[0:pos])
                    den = int(self.__segundoOperando[pos + 1:])
                    self.__segundoOperando = fraccion(num, den)
                    self.__segundoOperando.simpli()
                    self.__panel.set(str(self.__segundoOperando))
            else:
                self.__segundoOperando = int(self.__panel.get())
            self.resolver(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = self.__panel.get()
                pos = self.__segundoOperando.find('/')
                if pos != -1:
                    num = int(self.__segundoOperando[0:pos])
                    den = int(self.__segundoOperando[pos + 1:])
                    self.__segundoOperando = fraccion(num, den)
                    self.__segundoOperando.simpli()
                else:
                    self.__segundoOperando = int(self.__panel.get())
                self.__operador.set(op)
                self.__operadorAux = op
                self.resolver(self.__primerOperando, operacion, self.__segundoOperando)

if __name__ == '__main__':
    miapp = Calculadora()