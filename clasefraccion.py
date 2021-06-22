class fraccion:
    __numerador = 0
    __denominador = 1
    def __init__(self, num=0, den=1):
        self.__numerador = num
        self.__denominador = den

    def simpli(self):
        signo = 1
        if self.__numerador < 0:
            signo = -1
            self.__numerador = -1 * self.__numerador  # Lo pongo positivo para operar
        if self.__denominador != 0:
            resto_division = self.__numerador % self.__denominador
            if resto_division != 0:
                if self.__numerador < self.__denominador:
                    i = self.__numerador
                    while i > 1:
                        num_resto = self.__numerador % i
                        den_resto = self.__denominador % i
                        if num_resto == 0 and den_resto == 0:
                            self.__numerador = self.__numerador / i
                            self.__denominador = self.__denominador / i
                        i -= 1
                elif self.__numerador > self.__denominador:
                    i = self.__denominador
                    while i > 1:
                        num_resto = self.__numerador % i
                        den_resto = self.__denominador % i
                        if num_resto == 0 and den_resto == 0:
                            self.__numerador = self.__numerador / i
                            self.__denominador = self.__denominador / i
                        i -= 1
            else:
                self.__numerador = self.__numerador / self.__denominador
                self.__denominador = 1

        self.__numerador = signo * self.__numerador

    def numerador(self):
        return self.__numerador
    def denominador(self):
        return self.__denominador
    def getValor(self):
        return self.__numerador / self.__denominador

    def __str__(self):
        if self.__denominador != 1:
            cadena = str(int(self.__numerador)) + '/' + str(int(self.__denominador))
        else:
            cadena = str(int(self.__numerador))
        return cadena

 
    def __truediv__(self, otro):
        if isinstance(otro, fraccion):
            return fraccion(self.__numerador * otro.__denominador, self.__denominador * otro.__numerador)
        elif isinstance(otro, int) or isinstance(otro, float):
            return fraccion(self.__numerador, self.__denominador * otro)

    def __rtruediv__(self, otro):
        if isinstance(otro, fraccion):
            return fraccion(self.__numerador * otro.__denominador, self.__denominador * otro.__numerador)
        elif isinstance(otro, int) or isinstance(otro, float):
            return fraccion(self.__denominador * otro, self.__numerador)
        
    def __sub__(self, otro):
        if isinstance(otro, fraccion):
            numero1 = self.__numerador * otro.__denominador
            numero2 = otro.__numerador * self.__denominador
            deno = self.__denominador * otro.__denominador
            return fraccion(numero1 - numero2, deno)
        elif isinstance(otro, int) or isinstance(otro, float):
            numero = self.__numerador - self.__denominador * otro
            return fraccion(numero, self.__denominador)

    def __rsub__(self, otro):
        if isinstance(otro, fraccion):
            numero1 = self.__numerador * otro.__denominador
            numero2 = otro.__numerador * self.__denominador
            deno = self.__denominador * otro.__denominador
            return fraccion(numero1 - numero2, deno)
        elif isinstance(otro, int) or isinstance(otro, float):
            numero = self.__denominador * otro - self.__numerador
            print(numero)
            return fraccion(numero, self.__denominador)

    def __mul__(self, otro):
        if isinstance(otro, fraccion):
            return fraccion(self.__numerador * otro.__numerador, self.__denominador * otro.__denominador)
        elif isinstance(otro, int) or isinstance(otro, float):
            return fraccion(self.__numerador * otro, self.__denominador)

    def __rmul__(self, otro):
        if isinstance(otro, fraccion):
            return fraccion(self.__numerador * otro.__numerador, self.__denominador * otro.__denominador)
        elif isinstance(otro, int) or isinstance(otro, float):
            return fraccion(self.__numerador * otro, self.__denominador)

    def __add__(self, otro):
        if isinstance(otro, fraccion):
            numero1 = self.__numerador * otro.__denominador
            numero2 = otro.__numerador * self.__denominador
            deno = self.__denominador * otro.__denominador
            return fraccion(numero1 + numero2, deno)
        elif isinstance(otro, int) or isinstance(otro, float):
            numero = self.__denominador * otro + self.__numerador
            return fraccion(numero, self.__denominador)

    def __radd__(self, otro):
        if isinstance(otro, fraccion):
            numero1 = self.__numerador * otro.__denominador
            numero2 = otro.__numerador * self.__denominador
            deno = self.__denominador * otro.__denominador
            return fraccion(numero1 + numero2, deno)
        elif isinstance(otro, int) or isinstance(otro, float):
            numero = self.__denominador * otro + self.__numerador
            return fraccion(numero, self.__denominador)
    