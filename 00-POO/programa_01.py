
seguir = True
carreras = []

while seguir:
    
    print("****************")
    print("Menu")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar Carrera")
    print("5. Salir")
    
    print("****************")
    
    opcion = int (input("Ingrese su opcion:"))
    
    
    
    print("*")
    if opcion==1:
        print("Ingresar carrera")
        nombre = input("Nombre:")
        dicCarrera={}
        dicCarrera["carrera"]= nombre
        carreras.append(dicCarrera)
        print("Carrera agregada exitosamente")
        
    elif opcion==2:
        print("Leer (Mostrar) carrera")
        for carrera in carreras:
            print("-Nombre:"+carrera["carrera"])
            
    elif opcion ==3:
        print("Actualizar carrera")
        nombre = input("Ingrese el nombre de la carrera:")
        
        
    elif opcion==4:
        print("Borrar carrera")
        
        
    elif opcion==5:
        print("Hasta la proxima")
        
        seguir==False
print("")

"""
    entrada = input("Ingresa un número entero: ")
if validar_entero(entrada):
    print("La entrada es un número entero.")
else:
    print("La entrada no es un número entero.")
"""