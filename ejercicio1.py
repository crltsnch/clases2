from re import A


def cuadrados():
    numero=int(input("Introduce un numero: "))
    dic={}
    for i in range(1, numero+1):
        dic[i]= i**2

    return dic

#print(cuadrados())




def veces():
    dic={}
    cadena=input("Introduce una cadena de caracteres: ")
    for i in cadena:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic
#print(veces())



def frutas():
    dic={"manzana":1, "naranja":2, "platano": 2, "pera":3}
    while True:
        nombre=input("Que fruta quiere?: ")
        if nombre.lower() not in dic:
            print("No existe")
        else:
            cantidad=int(input("Cuanto quieres? "))
            precio=dic[nombre]*cantidad
            print(precio)
        
        otrafruta=input("Quieres algo más?")
        while otrafruta!="si" and otrafruta!="no":
            otrafruta=input("Quieres algo más? ")
        if otrafruta == "no":
            break        
frutas()



def agenda():
    