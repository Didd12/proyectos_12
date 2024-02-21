carreras=[]
clases=[]
seguir = True
seguir_clases = True

 
while seguir:
    print(carreras)
    print("--------------MENU PRINCIPAL--------------")
    print("1.Crear Carrera")
    print("2.Leer carrera")
    print("3.Actualizar carrera")
    print("4.Borrar carrera")
    print("5.Salir")
    print("6.Agregar clases")
    print("--------------------------------")
    option = input("Ingrese su opcion: ")
    
    if option.isnumeric():
        opcion = int(option)
        if opcion == 1:
            print("Ingresar carrera")
            nombre = input("Nombre: ")
            dicCarrea={}
            dicCarrea["carrera"] = nombre
            carreras.append(dicCarrea)
        
        if opcion == 2:
            print("Leyendo las carreras")
            for carrera in carreras:
                print(" Nombre : " + carrera["carrera"])
            
        if opcion == 3:
            car_remplazar=input("carrera a sustituir: ")
            new_carrera=input("Ingrese nueva carrea: ")
            dicCarrea={}
            dicCarrea["carrera"] = new_carrera
            indice = 0
            for carrera in carreras:
                if carrera["carrera"] == car_remplazar:
                    carreras[indice] = dicCarrea
                    break
                else :
                    indice = indice + 1
        
        if opcion == 4:
            print("Borrar Carrera")
            carrera_borrar = input("Ingrese el nombre de la carrera que desea borrar:")
            indice = 0
            for carrera in carreras:
                if carrera["carrera"] == carrera_borrar:
                    carreras.remove(carrera)
                    break
                else :
                    indice = indice + 1
        if opcion == 5:
            print("Hasta la Proxima")
            seguir = False
        elif opcion == 6:
            while seguir_clases:
              print("--------------MENU--------------")
              print("1.Crear clase")
              print("2.Leer carrera")
              print("3.Actualizar carrera")
              print("4.Borrar carrera")
              print("5.Salir")
              print("6.Salir")
              print("--------------------------------")
              option_class = input("Ingrese su opcion")
              
              if option_class.isnumeric():
                  opcion_class = int(option_class)
                  
                  if opcion_class == 1:
                       print("Ingresar clase")
                       nombre = input("Nombre Clase: ")
                       dicClases={}
                       dicClases["clases"] = nombre
                       clases.append(dicClases)
                       
                  elif opcion_class ==6:
                      print("Sale bye")
                      seguir_clases = False
              else:
                  print("Entrada incorrecta, favor ingresar un numero del menu(1-5)")
                  
                  
              
                
                  
             
    else :
        print("Entrada incorrecta, favor ingresar un numero del menu(1-5)")
    print("--------------------------------")

"""
    entrada = input("Ingresa un número entero: ")
if validar_entero(entrada):
    print("La entrada es un número entero.")
else:
    print("La entrada no es un número entero.")
    
if opcion.isnumeric()

else:
"""