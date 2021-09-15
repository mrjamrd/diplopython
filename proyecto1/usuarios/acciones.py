import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Debes completa el formulario")
        nombre = input("Cual es tu nombre?")
        apellidos = input("Cuales son tus apellidos?")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} Te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente!!!")


    def login(self):
        print("Debes ingresar los datos")
        try:

            email = input("Introduce tu E-mail:")
            password = input("Introduce tu password:")

            usuario = modelo.Usuario('','',email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]} Has Iniciado en el sistema el {login[5]}")
                self.proximasAcciones(login)
            else:
                print("Error")
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"login Incorrecto intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
            - Crear Nota (crear)
            - Mostrar Nota (mostrar)
            - Eliminar Nota (eliminar)
            - Salir (salir)
         """)

        accion = input("Que quieres Realizar: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            exit()
        else:
            print("Accion no valida")
            self.proximasAcciones(usuario)
