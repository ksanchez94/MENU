#MENU INTERACTIVO: PILAS Y LISTAS
class menu():
    opciones=["","1","2","3"]
    while True:
        print("**** Menú Interactivo ****")
        print("Ingresa frases y mi programa te ayudara a deletrearlos")
        print("1. Revelador de vocales")
        print("2. Contador de letras")
        print("3. Salir")

        opcion=input("Introduce una opcion: ")
        if not(opcion in opciones):
            print("No selecciono ninguna opcion valida")
            input("pulse para continuar")
            continue
        if opcion=="1":
            vocales = 0
            vocal_a = 0
            vocal_e = 0
            vocal_i = 0
            vocal_o = 0
            vocal_u = 0
            frase = input("Escribe una frase:")

            for i in frase:
                if i.lower() == "a":
                    print("Existe la vocal a")
                    vocal_a += 1
                    vocales += 1
                elif i.lower() == "e":
                    print("Existe la vocal e")
                    vocal_e += 1
                    vocales += 1
                elif i.lower() == "i":
                    print("Existe la vocal i")
                    vocal_i += 1
                    vocales += 1
                elif i.lower() == "o":
                    print("Existe la vocal o")
                    vocal_o += 1
                    vocales += 1
                elif i.lower() == "u":
                    print("Existe la vocal u")
                    vocal_u += 1
                    vocales += 1
            print("La frase tiene: ", vocal_a, " vocales a - ", vocal_e, " vocales e - ", vocal_i, " vocales i - ",
                  vocal_o, "vocales 0 - ", vocal_u, " vocales u.")
            print("La frase tiene un total de: ", vocales, " vocales. ")

        if opcion=="2":
            frc = (input("Ingresa una frase: "))
            let = len(frc)
            cont = 0
            contnum = 0
            contpuc = 0
            suma = 0
            for i in range(0, let):
                if (frc[i].isspace()):
                    cont += 1
                elif (frc[i].isdigit()):
                    contnum += 1
                elif (frc[i] in "?¡¿*,.-_'"):
                    contpuc += 1
                suma = cont + contnum + contpuc
            rpta = let - suma
            print("La frase tiene un total de",rpta,"letras")
            opciones.pop(3)
            print("¡Gracias por utilizar este menú interactivo! ")

        if opcion=="3":
            print("SALUDOS")
            break