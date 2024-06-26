import json

def agregarCategoria(parNombre:str ):
    with open("biblioteca.json", mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

        categoriaNueva = {
            "CategoriaID": len(archivoJson["Categoria"])+1,
            "Nombre": parNombre
        }

        archivoJson["Categoria"].append(categoriaNueva)
        
    print(f"\n La categoria {parNombre} fue agregada \n")

    with open("biblioteca.json", mode="w") as escrituraJson:
        json.dump(archivoJson, escrituraJson, indent=1)

#----------------------------------------------------------------------

def editarCategoria(parId:int, parNombre:str):
    with open("biblioteca.json", mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)
        
        for categoria in archivoJson["Categoria"]:
            if categoria['CategoriaID'] == parId:
                categoria['Nombre'] = parNombre
                break
        
        with open("biblioteca.json", mode="w") as escrituraJson:
            json.dump(archivoJson, escrituraJson, indent=4)
            print(f"\n La categoria fue editada \n")

#----------------------------------------------------------------------------

def eliminarCategoria(parId:int):
    with open("biblioteca.json", mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

        Categorias = archivoJson.get("Categoria", [])

        categoriaEliminada = False

        for categoria in Categorias:
            if categoria['CategoriaID'] == parId:
                Categorias.remove(categoria)
                categoriaEliminada = True
                break
        
        if categoriaEliminada:
            with open("biblioteca.json", mode="w") as escrituraJson:
                json.dump(archivoJson, escrituraJson, indent=4)
            print(f"\n La categoria ha sido eliminada \n")
        else:
            print(f"\n La categoria no se a encontrado \n")

#---------------------------------------------------------------------

def mostrarCategoria():
    with open("biblioteca.json", mode="r") as lecturaJson:
        archivoJson = json.load(lecturaJson)

        print(f"{'ID':<10}{'CATEGORIA':<20}")
        print("-" * 30)

        for categoria in archivoJson["Categoria"]:
            print(f"{categoria['CategoriaID']:<10}{categoria['Nombre']:<20}")
    














