import random

def adivina_el_numero_con_vidas():
    numero_objetivo= randon.randint(1,10)
    vidas = 3
    print("piensa un numero del 1 al 10 e intenta adivinarlo")
    while vidas > 0:
        intento= input("ingresa tu adivinanza: ")
        try:
            intento = int(intento)
            if intento < 1 or intento > 10:
                print("Ingresa un numero entre el 1 al 10")
                continue
                except ValueError:
                    print("ingresa un numero valido entre el 1 al 10")
                    continue
             if intento == numero_objetivo: 
                 print("Adivinaste el numero {numero_objetivo}.")
                 break
            elif intento < numero_objetivo:
                print("el numero es mayor. Te quedan {} vidas.".format(vidas -1)) 
            else:
                print("el numero es menor. Te quedan {} vidas.".format(vidas -1)) 
            vidas-= 1
            if vidas == 0:
                print("te quedaste sin vidas el numero objetivo era {numero_objetivo}.")
                
adivina_el_numero_con_vidas()

            