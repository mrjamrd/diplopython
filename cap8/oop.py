import clases


persona = clases.Persona()

persona.setNombre("Jose Armando")
persona.setApellidos("Matias Medina")
persona.setAltura("5-8")
persona.setEdad("32 Años")

print(f"La personas es: {persona.getNombre()} {persona.getApellidos()} edad: {persona.getEdad()}")
