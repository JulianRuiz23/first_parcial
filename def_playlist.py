from functools import reduce    # lib para usar la funcion reduce

def SuperList(list):    # funcion para crear lista contenedora de dict´s
    list_group = [] # empy list
    for line in list:   #for loop, leer x objeto(dict) del list
       values_line = line.split(';')    # separar datos de linea 
        # crear dict con las llaves y asignar valores apartir de indice de objetos separados
       dict = {'ARTISTA': values_line[0],
               'ALBUM': values_line[1],
               'GENERO': values_line[2],
               'CANCION': values_line[3],
               'DURACCION': values_line[4]}
       list_group.append(dict)  #add new dict to superlist
    return  list_group  #retornar objeto superlist


def ReadFile(name): # funcion para leer archivo(parametro recibido)
    print('Program running')    # program test
    list_playlist = []  # empy list
    with open(name+'.csv','r', encoding="utf-8") as file_csv:   #con open(archivo,modo lectura, codificacion ascii) alias
        for line in file_csv:   #for loop, leer x linea del archivo
            text = line.strip() #eliminar char especial
            list_playlist.append(text)  # add new line to list

    print(list_playlist)    # program test
    print('********************')   # program test
    list_group = SuperList(list_playlist)   # funcion para crear superlist of dict´s
    print('***',list_group,'***')   #program test
    return list_group   # retorno superlist optenido de la funcion

#HIGHER-ORDER FUNTION

def FuntionMap(arreglo):    # "mapear" nueva lista, nombre de artistas en mayusculas
    list_art_mayus = list(map(lambda x: x['ARTISTA'].upper(),arreglo))  # v = ff(f anonima objeto iterable: objeto['key'].metodo, list )
    print('***',list_art_mayus,'***')   # imprimir mensaje normal


def FuntionFilter(arreglo): # filtrar dict´s que cumplan condicion
    list_gen_rock = list(filter(lambda x: x['GENERO']=='Rock',arreglo)) # v = ff(f anonima objeto iterable: objeto['key'] condicion, list )
    print('***',list_gen_rock,'***')    # imprimir mensaje normal


def FuntionReduce(arreglo): # duracion total de todas las canciones del superlist
    list_duraccion = list(map(lambda x: float(x['DURACCION']), arreglo))    # "mapear" nueva lista y casting directo de str a float
    print('***',list_duraccion,'***')   # test program
    list_total_duraccion = round(float(reduce(lambda z, y: z+y, list_duraccion)),1) # v = ff(f anonima objetos iterables: operacion, list )  castin a float y manejar 1 valor decimal
    print(f'*** MINUTOS TOTAL DE CANCIOPNES: {list_total_duraccion} ***')   # imprimir mensaje con format


def MenuFuntions(super_list):   # funtion menu (list to work)
    message_ppal = '''Elija la funcion de orden superior
    1. Funcion MAP
    2. Funcion FILTER
    3. Funcion REDUCE
    : '''

    opc = int(input(message_ppal))  # captura de opcion tipo (int) desplegando una variable tipo str
    # switch
    if opc == 1:    #option
        FuntionMap(super_list)
    elif opc == 2:  #option
        FuntionFilter(super_list)
    elif opc == 3:  #option
        FuntionReduce(super_list)