# Estado de COVID-19
#
# Integrantes: Francisco Sánchez, Victoria García, Andrea Angulo, Belén Aravena
# Informática Biomédica

from pickle import FALSE

nombre = ""
apellido = ""
salir = False
fonosaludresponde = 6003607777
domicilio = "domicilio"
hosp = "hospitalizado"

# Variables para controlar el ciclo
sen = False
sen2 = False
sen5 = False 
sen9 = False    
sen8 = False 
sen6 = False
sen3 = False
sen7 = False

# Presentación y recolección de nombre del paciente
print ("--- BIENVENIDO(A) AL PROGRAMA DE DIAGNÓSTICO COVID-19 --- \n")
nombre = input("Ingrese su nombre \n")
apellido = input("Ingrese su apellido \n")

# Empecemos
while not salir:
    print ("\nProtocolo de salud COVID-19")
    print ("Elija una opción: ")
    print ("1. Tengo sintomas de COVID-19")
    print ("2. He estado en zona de riesgo o contacto con un contagiado")
    print ("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print (f"\nCorrecto... Sr/a {nombre}, ¿Ha estado en zona de riesgo o en contacto con un contagiado?")
        print ("1. Si")
        print ("2. No")
        opcion2 = int(input("Ingrese una opción: "))
        if opcion2 == 1:
            print ("\nDebe aislarse en su domicilio. ")
            print (f"Llame al {fonosaludresponde}, teléfono Salud Responde del MINSAL")
            print ("Le harán un examen PCR.")
            while not sen:
                print ("\nCual es el resultado del examen?")
                print ("1. Positivo")
                print ("2. Negativo")
                opcion3 = int(input("Ingrese una opción: "))
                if opcion3 == 1:
                    print ("\nCaso positivo.")
                    covidpositivo = True
                    while not sen2:
                        print ("¿Cuál es el grado de sus sintomas?")
                        print ("1. Leves")
                        print ("2. Graves")
                        opcion4 = int(input("Ingrese una opción: "))
                        if opcion4 == 1:
                            print (f"\nSr/a {nombre}")
                            print (f"Usted debe aislarse en su {domicilio}")
                            exit()
                        elif opcion4 == 2:
                            print (f"\nSr/a {nombre}")
                            print (f"Según sus sintomas, debería usted ser {hosp}.")
                            opcion == 0
                            exit ()
                elif opcion3 == 2:
                    print ("\nCaso negativo.")
                    covidpositivo = False
                    print (f"Sr/a {nombre}, se descarta el caso de COVID-19.")
                    opcion = 0
                    exit ()
        if opcion2 == 2:
            print (f"\nSr/a {nombre}, puede acudir a su médico como una consulta habitual")
            exit ()
    elif opcion == 2:
        while not sen5:
                print (f"\nCorrecto... Sr/a {nombre}, ¿Tiene sintomas?")
                print ("1. Sí")
                print ("2. No")
                opcion5 = int(input("Ingrese una opción: "))
                if opcion5 == 1:
                    print ("\nDebe aislarse en su domicilio. ")
                    print (f"Llame al {fonosaludresponde}, teléfono Salud Responde del MINSAL")
                    print ("Le harán un examen PCR.")
                    while not sen9:
                        print ("\nCual es el resultado del examen?")
                        print ("1. Positivo")
                        print ("2. Negativo")
                        opcion6 = int(input("Ingrese una opción: "))
                        if opcion6 == 1:
                            print ("\nCaso positivo.")
                            covidpositivo = True
                            while not sen8:
                                print ("¿Cuál es el grado de sus sintomas?")
                                print ("1. Leves")
                                print ("2. Graves")
                                opcion7 = int(input("Ingrese una opción: "))
                                if opcion7 == 1:
                                    print (f"\nSr/a {nombre}")
                                    print (f"Usted debe aislarse en su {domicilio}")
                                    exit()
                                elif opcion7 == 2:
                                    print (f"\nSr/a {nombre}")
                                    print (f"Según sus sintomas, debería usted ser {hosp}.")
                                    opcion == 0
                                    exit ()
                        elif opcion6 == 2:
                            print ("\nCaso negativo.")
                            covidpositivo = False
                            print (f"Sr/a {nombre}, se descarta el caso de COVID-19.")
                            opcion = 0
                            exit ()
                elif opcion5 == 2:
                    print (f"\nSr/a {nombre}, ¿Ha estado a menos de dos metros de un contagiado durante un tiempo continuado?")
                    print ("1. Si")
                    print ("2. No")
                    opcion7 = int(input("Ingrese una opción: "))
                    if opcion7 == 1:
                        print ("\nDebe aislarse en su domicilio. ")
                        print (f"Sr/a {nombre}, ¿Aparecen síntomas?")
                        print ("1. Si")
                        print ("2. No")
                        opcion8 = int(input("Ingrese una opción: "))
                        if opcion8 == 1:      
                            print (f"Llame al {fonosaludresponde}, teléfono Salud Responde del MINSAL")
                            print ("Le harán un examen PCR.")
                            while not sen6:
                                print ("\nCual es el resultado del examen?")
                                print ("1. Positivo")
                                print ("2. Negativo")
                                opcion9 = int(input("Ingrese una opción: "))
                                if opcion9 == 1:
                                    print ("\nCaso positivo.")
                                    covidpositivo = True
                                    while not sen8:
                                        print ("¿Cuál es el grado de sus sintomas?")
                                        print ("1. Leves")
                                        print ("2. Graves")
                                        opcion10 = int(input("Ingrese una opción: "))
                                        if opcion10 == 1:
                                            print (f"\nSr/a {nombre}")
                                            print (f"Usted debe aislarse en su {domicilio}")
                                            exit()
                                        elif opcion10 == 2:
                                            print (f"\nSr/a {nombre}")
                                            print (f"Según sus sintomas, debería usted ser {hosp}.")
                                            opcion == 0
                                            exit ()
                                elif opcion9 == 2:
                                    print ("\nCaso negativo.")
                                    covidpositivo = False
                                    print (f"Sr/a {nombre}, se descarta el caso de COVID-19.")
                                    opcion = 0
                                    exit ()
                        elif opcion8 == 2:
                            print ("Continúe hasta los 14 días en cuarentena.")
                            exit ()
                    elif opcion7 == 2:
                        print ("\nDebe aislarse en su domicilio. ")
                        print (f"Sr/a {nombre}, ¿Aparecen síntomas?")
                        print ("1. Si")
                        print ("2. No")
                        opcion11 = int(input("Ingrese una opción: "))
                        if opcion11 == 1:
                            print (f"Llame al {fonosaludresponde}, teléfono Salud Responde del MINSAL")
                            while not sen3:
                               print ("\nCual es el resultado del examen?")
                               print ("1. Positivo")
                               print ("2. Negativo")
                               opcion12 = int(input("Ingrese una opción: "))
                               if opcion12 == 1:
                                   print ("\nCaso positivo.")
                                   covidpositivo = True
                                   while not sen7:
                                       print ("¿Cuál es el grado de sus sintomas?")
                                       print ("1. Leves")
                                       print ("2. Graves")
                                       opcion13 = int(input("Ingrese una opción: "))
                                       if opcion13 == 1:
                                            print (f"\nSr/a {nombre}")
                                            print (f"Usted debe aislarse en su {domicilio}")
                                            exit ()
                                       elif opcion13 == 2:
                                            print (f"\nSr/a {nombre}")
                                            print (f"Según sus sintomas, debería usted ser {hosp}.")
                                            opcion == 0
                                            exit ()
                               elif opcion12 == 2:
                                    print ("\nCaso negativo.")
                                    covidpositivo = False
                                    print (f"Sr/a {nombre}, se descarta el caso de COVID-19.")
                                    opcion = 0
                                    exit ()
                        elif opcion11 ==2:
                            print ("Continúe hasta los 14 días en cuarentena.")
                            exit ()