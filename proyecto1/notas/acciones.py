import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nueva Nota")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota =  modelo.Nota(usuario[0],titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guardao la nota: {nota.titulo}")
        else:
            print(f"Error no se puedo guardar la nota {nota.titulo}")

    def mostrar(self, usuario):
        print(f" Vale!! {usuario[1]}!! Aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0],'','')
        notas = nota.listar()
        for nota in notas:
            print("*******************************************************************")
            print(f" Titulo: {nota[2]}")
            print(f" Descripcion: {nota[3]}")

    def borrar(self, usuario):
        print(f"Okey {usuario[1]} Vamos a borrar notas")

        titulo = input("Introduce el titulo de nota borrar: ")

        nota = modelo.Nota(usuario[0],titulo,'')
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota...")
