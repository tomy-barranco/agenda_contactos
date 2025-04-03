import pandas as pd

def buscar_contacto():
  while True:
    try:
      eleccion = int(input('🔎 Buscar contacto... \n1. Buscar por nombre \n2. Buscar por telefono. \n3. Buscar por correo.  \n4. Volver. \nOpción: '))
      print()
      
      if eleccion == 1:
        nombre = input('Ingrese el nombre del contacto: ')
        try:
          df = pd.read_csv("agenda.csv", encoding="utf-8")
          resultado = df[df["Nombre"].str.contains(nombre, case=False)]
          if resultado.empty:
            print(f'⚠️ No se encontró el contacto con nombre {nombre}. \n')
          else:
            print(resultado)
            print()
        except FileNotFoundError:
          print('⚠️ Error: no se encontró el archivo agenda.csv.')
      elif eleccion == 2:
        telefono = input('Ingrese el telefono del contacto: ')
        try:
          df = pd.read_csv("agenda.csv", encoding="utf-8")
          resultado = df[df["Telefono"].str.contains(telefono)]
          if resultado.empty:
            print(f'⚠️ No se encontró el contacto con telefono {telefono}. \n')
          else:
            print(resultado)
            print()
        except FileNotFoundError:
          print('⚠️ Error: no se encontró el archivo agenda.csv.')
      elif eleccion == 3:
        correo = input('Ingrese el correo del contacto: ')
        try:
          df = pd.read_csv("agenda.csv", encoding="utf-8")
          resultado = df[df["Correo"].str.contains(correo)]
          if resultado.empty:
            print(f'⚠️ No se encontró el contacto con correo {correo}. \n')
          else:
            print(resultado)
            print()
        except FileNotFoundError:
          print('⚠️ Error: no se encontró el archivo agenda.csv.')
      elif eleccion == 4:
        break
      else:
        print('⚠️ Error: opción invalida.\n')
    except ValueError:
      print('⚠️ Error: debe ingresar un número valido.\n')