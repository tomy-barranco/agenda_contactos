import modules.cargar_agenda
import modules.buscar_contacto
import modules.editar_contactos

print('👥 Bienvenido a la agenda de contactos.')

while True:
  try:
    eleccion = int(input('🌐 Menú: \n1. Ver contactos. \n2. Buscar contacto. \n3. Editar contactos.  \n4. Salir. \nOpción: '))
    print()
    
    if eleccion == 1:
      modules.cargar_agenda.cargar_agenda()
    elif eleccion == 2:
      modules.buscar_contacto.buscar_contacto()
    elif eleccion == 3:
      modules.editar_contactos.editar_contactos()
    elif eleccion == 4:
      print('👋 Saliendo del programa...')
      break
    else:
      print('⚠️ Error: opción invalida.\n')
  except ValueError:
    print('⚠️ Error: debe ingresar un número valido.\n')