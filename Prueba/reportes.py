import json

def prestamos():
    with open("biblioteca.json", mode="r")as lecturaJson:
        archivoJson = json.load(lecturaJson)

        vecesPrestado = 0

        for prestamo in archivoJson["Prestamo"]:
            for libro in archivoJson["Libro"]:
                if prestamo['LibroID'] == libro['LibroID']:
                    vecesPrestado += 1
                    break
            break

        print("*" * 74)
        print("*", " " * 5, "Libro", " "* 25, "Cantidad de veces prestado", " " * 5, "*")
        print("*" * 74)

        for libro in archivoJson["Libro"]:
            print(f"{libro['Titulo']:<55}{vecesPrestado:<30}")