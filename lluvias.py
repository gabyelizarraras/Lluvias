import xlrd  #píp install xlrd
from arrays import Array3D

def main():
    a3= Array3D(34,35,14)
    for anio in range(1985,2019,1):
        ruta='./Precipitacion/'+str(anio)+'Precip.xls' #se le quita la ultima x
       # print(ruta)
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0) #desplega el archivo deseado
       # print(hoja.cell_value(2,1)) imprime el promedio de enero en aguasc de todos los años
        
              
        for r in range(1,35,1): # da los renglones
            for c in range (0,14,1):
                #print(hoja.cell_value(r,c),end='')
               # print(anio, r, c)
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))

            #print("----------------")
    #a3.to_string()
    print("NUMERO 1")
    a= int(input("Año:(1985-2019) "))
    e= int(input("Edo(1-32):"))
    m= int(input("Mes(1-12):"))
    print(f"Promedio {a3.get_item(a-1985,e,m)}")

    print(f"En el estado de {a3.get_item(0,e,0)} Llovió  un promedio de {a3.get_item(a-1985,e,m)} centímetros cúbicos en el mes de {a3.get_item(0,0,m)}")

    print("NUMERO 2")
    aux=0
    for i in range (1985,2019,1):
        a=a3.get_item(i-1985,e,m)
        #print(a)
        aux+=a
    promedio=(aux/33)
    
    print(f"El promedio de todos los años del mes {a3.get_item(0,0,m)} en el estado de {a3.get_item(0,e,0)} es de {promedio}")


    print("NUMERO 3")
    aux=0
    for y in range(1985,2019,1):
        anual= a3.get_item(y-1985,e,13)
        aux+=anual
    proestado=(aux/33)
    print(f"El promedio total de todos los años de todos los meses en el estado de {a3.get_item(0,e,0)} es de {proestado}")

    
    print("NUMERO 4")
    aux=0
    for x in range (1985,2019,1):
        nacional=a3.get_item(x-1985,33,13)
        aux+=nacional
    prototal=(aux/33)
    print(f"El promedio total de todos los años (1985 al 2018) de todos los meses y todos los estados es de {prototal}")
        
        
    
main()
