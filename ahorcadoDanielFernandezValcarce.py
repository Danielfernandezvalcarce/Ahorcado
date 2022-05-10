#ESTE PROGRAMA HACE UN AHORCADO
#IMAGENES DEL AHORACADO EN UNA LISTA
imagenes = ['''
        
           
               
               
                
               
                
         =========''','''
        
           
               
               
                
               
                
         =========''','''
        
           
               |
               |
               |
               |
               |
         =========''','''
        
           +---+
               |
               |
               |
               |
               |
         =========''','''
        
           +---+
           |   |
               |
               |
               |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
               |
               |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         =========''', '''
        
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         =========''']
#FUNCION QUE NOS AYUDA A IMPRIMIR EL MUÑECO
def muñeco():
    print(imagenes[contador])
#FUNCION PRINCIPAL
def ahorcado():
    global contador
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    especiales = " .,:;¡!¿?0123456789"
    palabra_secreta = input("Introduce una frase secreta: ")
    lista_alphabet = []
    lista_palabra_secreta = []
    lista_especiales = []
#CONVERTIMOS LOS STRING A LISTAS    
    for i in alphabet:
        lista_alphabet = lista_alphabet+[i]
    for j in palabra_secreta:
        lista_palabra_secreta = lista_palabra_secreta+[j]
    for k in especiales:
        lista_especiales = lista_especiales+[k]
#ESTRUCTURA QUE OCULTA LAS LETRAS DE LA PALABRA QUE HAY QUE ADIVINAR    
    booleano1=True
    resultado=""
    lista_resultado=[]
    while booleano1:
        if len(palabra_secreta)>0:
            print("La palabra que tienes que adivinar es: ")
        for i in lista_palabra_secreta:
            for j in lista_alphabet:
                if i==j:
                    lista_resultado = lista_resultado + ["_ "]
            for k in lista_especiales:
                if i==k:
                    lista_resultado = lista_resultado + [k]
        for l in lista_resultado:
            resultado=resultado+str(l)
        print("la frase que debes de adivinar es: ",resultado)
        booleano1=False
#ESTRUCTURA QUE HACE LA PREGUNTA Y GUARDA EL CONTADOR
    booleano2=True
    lista_letra=[]
    contador=0
    almacenadas=""
    encontradas=""
    while booleano2 and ("_" in resultado):
        letra=input("Introduce una letra: ")
        for i in letra:
            lista_letra=[i]
        if (len (letra))!=1:
            print("Recuerda solo puedes poner un caracter por pregunta!")
        elif letra in almacenadas:
            print("Esa letra ya la has introducido, vuelve a intentalos")
        #ESTRUCTURA PARA ACIERTO
        elif contador<9 and letra not in almacenadas:
            for i in letra:
                almacenadas = almacenadas + i
            print(almacenadas)
            if letra in palabra_secreta:
                print("Felicidades! Esa letra está contenida en la palabra/frase secreta!")
                resultado2 = ""
                for m in letra:
                    encontradas = encontradas + m
                for i in palabra_secreta:
                    for j in almacenadas:
                        if i == j:
                            resultado2 = resultado2 + i
                    for k in especiales:
                        if i == k:
                            resultado2 = resultado2 + k
                    for l in alphabet:
                        if i==l and i not in almacenadas:
                            resultado2 = resultado2 + "_ "
                resultado=resultado2
                muñeco()
                print("Asi esta ahora mismo la palabra/frase que debes de adivinar",resultado)
            #ESTRUCTURA PARA FALLO
            if letra not in palabra_secreta:
                contador=contador+1
                print("Vaya! tu letra no estaba contenida en la frase!")
                print("Llevas",contador,"intentos, recuerda! tienes 10 intentos como máximo")
                muñeco()
                print("Asi esta ahora mismo la palabra/frase que debes de adivinar",resultado)
        #ESTRUCTURA PARA SI HAS PERDIDO
        elif contador == 9:
            contador = 10
            print("Has perdido!!")
            muñeco()
            if (input("Si desea jugar otra vez, escribe \"SI\" si no, presione enter.")) == "SI":
                ahorcado()
            else:
                quit()
    #ESTRUCTURA POR SI HAS GANADO
    if contador < 9:
        print("Genial!, has ganado!!!")
ahorcado()