from time import sleep, time
from csv import reader as csv_reader


"""
LA INFO EN LOS OBJETOS DE TIPO DATA ES EN TUPLAS
MÁS RÁPIDO EN ORGANIZAR Y ALMACENAR INFO
"""

id_increment = 0

ASCENDENTE = "ASCENDENTE"
DESCENDENTE = "DESCENDENTE"
DESORDENADO = "DESORDENADO"

NORMAL = "NORMAL"
FRECUENCIA = "FRECUENCIA"
NO_REPETICIONES = "NO REPETICIONES"



class Data:

    def __init__(self, values):
        
        global id_increment

        id_increment += 1

        self.__id = id_increment #privada

        self.values = values #privada

        self.aFrec = 1 #privada

        self.aDer = None #privada

        self.aIzq = None #privada

    
    def __repr__(self):

        return str(self.values)
    

class Arbol:

    def __init__(self,keys,key_for_index,tipo_arbol = NORMAL):

        self.aRoot = None #privada
        self.keys = keys #privada
        self.id_key_for_index = self.keys.index(key_for_index) #super privada
        self.__tipo_arbol = tipo_arbol #privada

        self.way_for_repr = ASCENDENTE #privada

        self.dictionary_format_for_data = False #privada
   
    def push(self,values):

        if not (self.aRoot):
            self.aRoot = Data(values)

        else:
            
            dato = self.aRoot

            if self.__tipo_arbol == NORMAL:
                while 1:
                    
                    if values[self.id_key_for_index] < dato.values[self.id_key_for_index]:

                        if not dato.aIzq:
                            dato.aIzq = Data(values)
                            break
                        
                        else:
                            dato = dato.aIzq
                    
                    elif values[self.id_key_for_index] >= dato.values[self.id_key_for_index]:
                        if not dato.aDer:
                            dato.aDer = Data(values)
                            break
                        
                        else:
                            dato = dato.aDer

            elif self.__tipo_arbol == NO_REPETICIONES:
                
                while 1:
                    if values[self.id_key_for_index] < dato.values[self.id_key_for_index]:

                        if not dato.aIzq:
                            dato.aIzq = Data(values)
                            break
                        
                        else:
                            dato = dato.aIzq
                    
                    elif values[self.id_key_for_index] > dato.values[self.id_key_for_index]:
                        if not dato.aDer:
                            dato.aDer = Data(values)
                            break
                        
                        else:
                            dato = dato.aDer
                    else:
                        if values != dato.values:
                            if not dato.aDer:
                                dato.aDer = Data(values)
                                break
                            else:
                                dato = dato.aDer
                        else:
                            break
            
            elif self.__tipo_arbol == FRECUENCIA:
                while True:
                    
                    if values[self.id_key_for_index] < dato.values[self.id_key_for_index]:

                        if not dato.aIzq:
                            dato.aIzq = Data(values)
                            break
                        
                        else:
                            dato = dato.aIzq
                    
                    elif values[self.id_key_for_index] > dato.values[self.id_key_for_index]:
                        if not dato.aDer:
                            dato.aDer = Data(values)
                            break
                        else:
                            dato = dato.aDer
                    else:
                        dato.aFrec += 1
                        break

    def getDictionary(self,values):
        dic = list(zip(self.keys,values))
        dic = {key:value for key,value in dic}
        return dic
    
    def __repr__(self):

        lista = []
        dato = self.aRoot

        if self.way_for_repr == ASCENDENTE:
            while lista != [] or dato != None:
                
                if dato != None:
                    lista.append(dato)
                    dato = dato.aIzq
                
                else:

                    dato = lista[-1]
                    lista.pop()
                    if not self.dictionary_format_for_data:
                        print(dato)
                    else:
                        print(self.getDictionary(dato.values))

                    dato = dato.aDer
        
        elif self.way_for_repr == DESCENDENTE:
            while lista != [] or dato != None:
                
                if dato != None:
                    lista.append(dato)
                    dato = dato.aDer
                
                else:

                    dato = lista[-1]
                    lista.pop()
                    if not self.dictionary_format_for_data:
                        print(dato)
                    else:
                        print(self.getDictionary(dato.values))
                    dato = dato.aIzq
        
        elif self.way_for_repr == DESORDENADO:
            
            while lista != [] or dato != None:
                if dato != None:
                    if not self.dictionary_format_for_data:
                        print(dato)
                    else:
                        print(self.getDictionary(dato.values))
                    lista.append(dato)
                    dato = dato.aIzq
                else:
                    dato = lista[-1]
                    lista.pop()
                    dato = dato.aDer

        self.way_for_repr = ASCENDENTE
        self.dictionary_format_for_data = False
                    
        return ""
    



class Lista_con_Arboles:

    def __init__(self, keys = (), tipo_arbol = NORMAL):

        self.keys = keys

        self.lista = []
        self.lista_arboles_indexados = []

        self.__tipo_arbol = tipo_arbol

        for n,key in enumerate(keys):
            self.lista_arboles_indexados.append(Arbol(keys,keys[n],tipo_arbol))


    def push(self,values):

        data = list(zip(self.keys,values))

        self.lista.append({key:value for key,value in data})
        
        for arbol in self.lista_arboles_indexados:
            arbol.push(values)


    def read(self,path):

        self.lista_arboles_indexados.clear()

        with open(path) as file:
            
            reader = csv_reader(file,delimiter= ",")

            header = tuple(next(reader))

            self.keys = header

            for n,key in enumerate(self.keys):
                self.lista_arboles_indexados.append(Arbol(self.keys,self.keys[n],self.__tipo_arbol))

            for row in reader:
                for tree in self.lista_arboles_indexados:
                    tree.push(tuple(row))
                    self.lista.append(tuple(row))


    def __pdelr(self,pData,values):
        pass

    def delr(self,values):

        if self.aRoot and type(values) == tuple:
            pass

    
    def __repr__(self):

        return str(self.lista)

    
    def repr(self,campo,orden = ASCENDENTE,dictionary_format = False):
        indice = self.keys.index(campo)

        if not dictionary_format:
            print(self.keys)
        else:
            self.lista_arboles_indexados[indice].dictionary_format_for_data = True 

        if orden == ASCENDENTE:
            pass

        elif orden == DESCENDENTE:
            self.lista_arboles_indexados[indice].way_for_repr = DESCENDENTE
            
        elif orden == DESORDENADO:
            self.lista_arboles_indexados[indice].way_for_repr = DESORDENADO
            
        print(self.lista_arboles_indexados[indice])

        return ""




#Ahora hay que hacer que pueda imprimir los datos desordenadamente y ordenada de manera descendiente

if __name__ == "__main__":

    lista = Lista_con_Arboles(tipo_arbol=NO_REPETICIONES)

    time1 = time()
    lista.read("./personas.csv")
    lista.read("../Platzi/Data Science e IA/world_population.csv")
    #lista.read("/Users/rodrigoconsuelos/Documents/Python Projects/nombres.csv")
    time2 = time()

    print(time2 - time1)

    #lista.repr(lista.keys[0],dictionary_format=True)
 
    #lista.repr(lista.keys[0])
   


    
    