import modules.agregar_contacto
import modules.actualizar_contacto
import modules.eliminar_contacto

def editar_contactos():
  while True:
    try:
      eleccion = int(input('✏️ Editando contactos... \n1. Agregar contactos \n2. Actualizar contacto. \n3. Eliminar contacto.  \n4. Volver. \nOpción: '))
      print()
      
      if eleccion == 1:
        modules.agregar_contacto.agregar_contacto()
      elif eleccion == 2:
        modules.actualizar_contacto.actualizar_contacto()
      elif eleccion == 3:
        modules.eliminar_contacto.eliminar_contacto()
      elif eleccion == 4:
        break
      else:
        print('⚠️ Error: opción invalida.\n')
    except ValueError:
      print('⚠️ Error: debe ingresar un número valido.\n')