class hoja(object):
    def __init__(self,peso):#constructor con su atributo peso
        self.peso=peso
        self.der=None#puntero derecho
        self.izq=None#puntero izquierdo
'''fin de la clase hoja'''
'''inicio de la clase arbol'''
class arbol(object):
    def __init__(self):
        self.raiz=None

    def insertar(self,raiz,peso):
        if raiz==None:
            self.raiz=hoja(peso)
        else:
            aux=raiz.peso
            if aux<peso:
                if raiz.der==None:
                    raiz.der=hoja(peso)
                else:
                    self.insertar(raiz.der,peso)
            else:
                if raiz.izq==None:
                    raiz.izq=hoja(peso)
                else:
                    self.insertar(raiz.izq,peso)


    def posOrden(self,raiz):
        if raiz==None:
            return None
        else:
            self.posOrden(raiz.izq)
            self.posOrden(raiz.der)
            print(raiz.peso,"<>")


    def preOrden(self,raiz):
        if raiz==None:
            return None
        else:
            print(raiz.peso,"<>")
            self.preOrden(raiz.izq)
            self.preOrden(raiz.der)


    def inOrden(self,raiz):
        if raiz==None:
            return None
        else:
            self.inOrden(raiz.izq)
            print(raiz.peso,"<>")
            self.inOrden(raiz.der)


    def bfs(self,raiz,peso):
        if raiz==None:
            return None
        else:
            aux=raiz.peso
            if aux<peso:
                return self.bfs(raiz.izq,peso)
            else:
                return self.bfs(raiz.der,peso)

    def eliminar(self,raiz,peso):#metodo de eliminar nodos del arbol
        if raiz==None:
            return 
        else:
            aux=raiz.peso
            if aux==peso:
                if raiz.izq is None and raiz.der is None: #es lo mismo que igualar a none o usar getvacio
                    return None  # retorna a none xq cuando llegue a esta condicion ya no habran mas parientes derechos o izquierdos es cuando tiene izq y der None
                elif not raiz.der: # es lo mismo que decir raiz der=None ya que la patita derecha estara vacia 
                    izq=raiz.izq #x lo que se subira el izquierdo y quedara en lugar de root
                    del raiz
                    return izq # se debe retornar su valor
                elif not raiz.izq: # mismo que lo anterior
                    der=raiz.der
                    del raiz
                    return der
                else:    # caso en que tenga dos parientes izq y derecho
                    raiz.peso=self.minim(raiz.der)
                    temp=self.min(raiz.der)  # funcion min se tuvo q arreglar
                    raiz.der=self.eliminar(raiz.der,temp)
            elif aux<peso:
                raiz.der=self.eliminar(raiz.der,peso)
            else:
                raiz.izq=self.eliminar(raiz.izq,peso)
        return raiz # se debe realizar un return raiz 

    def minim(self,raiz):
        aux=raiz.der
        while aux.izq is not None:
            aux=aux.izq
        return aux.peso #error en aux.izq no vale porq es none a cada rato
'''fin de la clase arbol'''

def main():
    x=arbol()
    x.insertar(x.raiz,5)
    x.insertar(x.raiz,4)
    x.insertar(x.raiz,3)
    x.insertar(x.raiz,8)
    x.insertar(x.raiz,6)
    x.insertar(x.raiz,1)
    x.insertar(x.raiz,7)
    

    print("-"*20)
    print("intOrden")
    x.inOrden(x.raiz)
    print('min',x.minim(x.raiz))

    x.eliminar(x.raiz,7)

    print("-"*20)
    print("intOrden")
    x.inOrden(x.raiz)

if __name__=='__main__':
    main()
    
            




            
            


            
