"""
Una lista con n dicionario dentro
"""
contactos = [
  {
    'nombre':'Jose',
    'email':'jose@gmail.com'
  },
  {
    'nombre' : 'luis',
    'email' : 'luis@luis.com'
  },
  {
    'nombre': 'Jeralmy',
    'email' : 'jeralmy@jeralmy.com'
  }
]
contactos[0]['nombre'] = "Emil"
print(contactos[0]['nombre'])

for contacto in contactos:
    print(f" Nombre de contacto: {contacto['nombre']}")
    print(f" Email.com del contacto: {contacto['email']}")
