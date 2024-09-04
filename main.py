from processes import *

def mostrar_menu():
    print('0 - Salir del menu de opciones')
    print('1 - Cargar un vector de n apuestas')
    print('2 - Mostrar el contenido del vector ordenado por numero de ticket')
    print('3 - Buscar ticket seleccionado')
    print('4 - Contar cuantas apuestas se realizaron para cierto caballo')
    print('5 - Mostrar los datos del ticket con mayor monto apostado')    
    opcion = int(input('Ingrese opcion'))
    return opcion

def main():
    op = -1
    v = []
    while op != 0:
        op = mostrar_menu()
        if op == 1:
            n = validar_mayor_que(0,'Ingrese cant de apuestas realizadas')
            v = cargar_vector(n)
        if op == 2:
            ordenar_vector_ticket(v)
            for apuesta in v:
                print(apuesta)
        if op == 3:
            ticket_a_buscar = validar_intervalo(0,100,'Ingrese el ticket a buscar')
            ticket_buscado = buscar_elemento(v,ticket_a_buscar)
            if ticket_buscado == -1:
                print('No se encontro el ticket buscado')
        if op == 4:
            caballo = validar_intervalo(0,9,'Ingrese el numero de caballo del que quiere conocer la cant de apuestas: ')
            contador_de_apuestas = contador(v,caballo)
            print('La cant de apuestas para el caballo' + str(caballo) + 'fue de ' + str(contador_de_apuestas))
        if op == 5:
            mayor_apuesta = buscar_mayor_ticket(v)
            print(mayor_apuesta)
if __name__ == '__main__':
    main()