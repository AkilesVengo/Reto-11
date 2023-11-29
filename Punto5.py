#Este programa permite sumar los elementos de una fila dada de una matriz

def sumaFila(A,fila):
    x:int=0
    for i in range (len(A[0])):
        x+=A[fila][i]
    return x

if __name__=="__main__":
    fils=[]
    A=[]
    nFilasA = int(input("Ingrese la cantidad de filas de la matriz: "))
    nColsA = int(input("Ingrese la cantidad de columnas de la matriz: "))
    for i in range(nFilasA):
        for j in range(nColsA):
            cFilas = int(input("Ingrese el número que se ubica en la columna "+ str(j)+ " y la fila " + str(i)+ ": "))
            fils.append(cFilas)
        A.append(fils)
        fils = []
    print("La matriz ingresada es: ")
    for x in range(len(A)):
        print(A[x])

    fila=int(input("Ingrese el número de la fila, para sumar sus elementos: "))
    
    sumaElementosFila=sumaFila(A,fila)
    print("La suma de los elementos de la fila " +str(fila)+ " es: "+ str(sumaElementosFila))