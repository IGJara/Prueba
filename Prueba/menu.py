import categorias
import reportes

while True:
    print("*" * 28)
    print("*", " " * 5, " Mundo Libro", " " * 5, "*" )
    print("*" * 28)

    print("[1] - Mantenedores de Categorias")
    print("[2] - Reportes")
    print(f"[3] - salir \n")

    opcion = int(input("Ingrese La opcion a ver: "))

    if opcion == 1:
        while True:
            print("*" * 37)
            print("*", " " * 5, "Mantenedor Categorias", " " * 5, "*" )
            print("*" * 37)

            print("[1] - Agregar Categoria ")
            print("[2] - Editar Categoria ")
            print("[3] - Eliminar Categoria ")
            print("[4] - Mostrar Categorias ")
            print(f"[5] - Volver \n")

            option = int(input("Ingrese un numero de las opciones: "))

            if option == 1:
                nombre = input("Ingrese el nombre de la nueva categoria: ")
                categorias.agregarCategoria(nombre)
            
            elif option == 2:
                id = int(input("Ingrese el ID de la categoria que desea editar: "))
                nombre = input("Ingrese el nuevo nombre de la categoria: ")
                categorias.editarCategoria(id, nombre)
            
            elif option == 3:
                id = int(input("Ingrese el ID de la categoria que desea eliminar: "))
                categorias.eliminarCategoria(id)

            elif option == 4:
                categorias.mostrarCategoria()
            
            elif option == 5:
                break
            
            else:
                print(f"\n Opcion no valida, pruebe con una de las que se muestran \n")
    
    elif opcion == 2:
        reportes.prestamos()
    
    elif opcion == 3:
        break

    else:
        print(f"\n Opcion no valida, pruebe con las que se muestran \n")