
#Descripcion: En este programa se realiza una interación en la que se cuentan las letras del texto introducido
#y se sustituyen con las letras mas aparecidas en el lenguaje. Una vez hecho esto se comprueba si el mensaje tiene sentido.
#Si tiene sentido se termina el programa.
#Sino, se le pregunta al usuario que valor de letra quiere introducir. Una vez introducido un valor para las letras se realizara otra iteracion
#pero con los nuevos valores introducidos por el usuario.


#A la hora  de sustituir un caracter por otro, se debe de introducir en este formato A=D, esto quiere decir que, 
# todos los caracteres que contengan A en el mensaje traducido pasarán a tomar el valor de D,
# esto modificará la clave de tal forma que, el caracter que sustituia A del mensaje cifrado ahora lo sustituye D

#Precondicion: El texto introducido debe de estar en castellano, sin embargo si se deseara introducir otro idioma habria que cambiar los porcentajes de aparicion

def convertidorAnalisisFrecuencia(texto):
    contador = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "Ñ":0,"O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    
    porcentajeDeAparicion = {
        "E": 16.78, "A": 11.96, "O": 8.69, "L": 8.37, "S": 7.88, "N": 7.01, "D": 6.87, "R": 4.94, "U": 4.8, "I": 4.15,
        "T": 3.31, "C": 2.92, "P": 2.776, "M": 2.12, "Y": 1.54, "Q": 1.53, "B": 0.92, "H": 0.89, "G": 0.73, "F": 0.52,
        "V": 0.39, "J": 0.3,"Ñ":0.29, "Z": 0.15, "X": 0.06, "K": 0, "W": 0
    }

    resultado = contador.copy()
    traduccionCorrecta = False

    for letra in texto.upper():
        if letra in contador:
            contador[letra] += 1

    listaLetras = sorted(porcentajeDeAparicion.items(), key=lambda item: item[1], reverse=True)
    listaLetras=[item[0] for item in listaLetras]
    resultadoPropuesto = resultado.copy()
    ordenAparicionLetras = sorted(contador.items(), key=lambda item: item[1], reverse=True)
    ordenAparicionLetras=[item[0] for item in ordenAparicionLetras]
    while not traduccionCorrecta:
        i = 0
        for letra in ordenAparicionLetras:
            resultado[letra] = listaLetras[i]
            i += 1

        traduccion = ""
        for letra in texto.upper():
            if letra in resultado and resultado[letra] != 0:
                traduccion += resultado[letra]
            else:
                traduccion += letra

        print(traduccion)
        print("\nLa clave obtenida a partir del mensaje es esta:\n")
        print(resultado)
        print("\n")
        respuesta = input("¿Es la traducción correcta? \n").lower().strip()
        if respuesta == "si":
            traduccionCorrecta = True
        else:
            print("Letras disponibles a asignar:\n")
            print(listaLetras)
            print("\n")
            print("Letras que ya han sido asignadas:\n")
            print(resultadoPropuesto)
            print("\n")
            print("Cambia la letras del mensaje que creas que no son correctas\n")
            print("Introduce las letras de esta forma: A=E,B=Z,C=T...\n")
            respuesta = input().strip()
            respuesta = respuesta.split(",")
            resultadoAnterior=list(resultado.items())
            for letraResult in resultado.keys():
                if resultadoPropuesto[letraResult] == 0:
                    resultado[letraResult] = 0
            print(resultadoAnterior)
            for asignacion in respuesta:
                if len(asignacion) == 3 and asignacion[1] == '=' and asignacion[2].isalpha() and asignacion[0].isalpha():
                    i=0
                    enc=False
                    while i < len(resultadoAnterior) and not enc:
                        if asignacion[0]== resultadoAnterior[i][1]:
                            enc=True
                        else:
                            i+=1
                    resultadoPropuesto[resultadoAnterior[i][0]] = asignacion[2]
                    resultado[resultadoAnterior[i][0]] = asignacion[2]
                    if asignacion[2] in listaLetras and resultadoAnterior[i][0] in ordenAparicionLetras:
                        ordenAparicionLetras.remove(resultadoAnterior[i][0])
                        listaLetras.remove(asignacion[2])
                        

            

convertidorAnalisisFrecuencia("RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIVCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.")


