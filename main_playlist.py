import def_playlist as fp   # importar modulo para poder utilizar funciones
from os import system  # libreria y modulo para trabajar comandos de consola
#playlist = [d for d in playlist if d['genero']=='rock' and d['duracion']=4.5] # clase usc list comprehension
def run():  # principal funtion
    file = input('Enter name of the file to read: ')    # captura de dato
    super_list = fp.ReadFile(file)  # enviar parametro a funcion para leer archivo y recibir list

    fp.MenuFuntions(super_list) # enviar list optenido como parametro a la funcion menu

    # message_ppal = '''Elija la funcion de orden superior
    # 1. Funcion MAP
    # 2. Funcion FILTER
    # 3. Funcion REDUCE
    # : '''

    # opc = int(input(message_ppal))

    # if opc == 1:
    #     fp.FuntionMap(super_list)
    # elif opc == 2:
    #     fp.FuntionFilter(super_list)
    # elif opc == 3:
    #     fp.FuntionReduce(super_list)



if __name__ =='__main__':   #entry point
    system('cls')   # limpiar consola de inicio de programa
    print('***--- WELCOME TO THE CSV FILE READER PROGRAM ---*** \r\n')
    run()   # start program
