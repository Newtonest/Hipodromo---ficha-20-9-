import random
class Apuesta:
    def __init__(self,ticket,caballo,monto):
        self.ticket = ticket
        self.caballo = caballo
        self.monto = monto
    
    def __str__(self):
        return str(self.ticket) + " " + str(self.caballo) + " " + str(self.monto)


def contador(v,propiedad):
    contador = 0
    for i in v:
        if i.caballo == propiedad:
            contador += 1
    return contador

def buscar_mayor_ticket(v):
    mayor_ticket = 0
    mayor_apuesta = apuesta
    for apuesta in v:
        if apuesta.ticket > mayor_ticket:
            mayor_ticket = apuesta.ticket
            mayor_apuesta = apuesta
    return mayor_apuesta
def buscar_elemento(v,elemento):
    for element in v:
        if element.ticket == elemento:
            element.monto *= 10
            return element
    return -1

def validar_intervalo(x1,x2,texto):
    num = int(input(texto))
    while x1 > num > x2:
        print('numero invalido')
        num = int(input(texto))
    return num

def validar_mayor_que(inf,mensaje):
    num = int(input(mensaje))
    if num <= inf:
        num = int(input('ERROR' + mensaje))
    return num

def cargar_vector(n):
    v = []
    for i in range(n):
        ticket = random.randint(0,100)
        caballo = random.randint(0,9)
        monto = random.randint(0,9999)
        v.append(Apuesta(ticket,caballo,monto)) 
    return v

def ordenar_vector_ticket(v):
    for i in range(len(v)- 1):
        for j in range(i+1 ,len(v)):
            if v[j].ticket > v[i].ticket:
                v[i],v[j] = v[j], v[i]