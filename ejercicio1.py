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
#frutas()



def agenda():
    agenda = {}
    while True:
        print("1.Añadir")
        print("2.Buscar")
        print("3.Borrar")
        print("4.Listar")
        print("5.Salir")
        elegido = input("Dime una opción: ")
        if elegido == "1":
            contacto = input("Dime el nombre del contacto que quiere añadir: ")
            if contacto in agenda:
                print("Ese contacto ya está en la agenda", agenda[contacto])
                modificar = input("¿Quieres modificarlo? ")
                if modificar == "si":
                    numero = input("Dígame el número de telefono: ")
                    agenda[contacto]=numero
            else:
                n = input("Dígame el número que quiere añadir: ")
                agenda[contacto]=n

        elif elegido == "2":
            c = input("Dígame el contacto que desea buscar: ")
            for i in agenda:
                if i.startswith(c):
                    print("El número de teléfono de %s es %s" % (i, agenda[i]))
        
        elif elegido == "3":
            c = input("Dígame el contacto que desea borrar: ")
            if c in agenda:
                del agenda[c]
            else:
                print("Ese contacto no existe")

        elif elegido == "4":
            for i in agenda:
                print(i, agenda[i])
        
        elif elegido == "5":
            break

#agenda()


def separar():
    cadena = input("Dime una frase: ")
    resultado = ""
    for i in cadena:
        if i.isupper():
            resultado += " " + i
        else:
            resultado += i
    return resultado
print(separar())