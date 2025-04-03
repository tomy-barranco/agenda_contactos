import pandas as pd

def actualizar_contacto():
    try:
        df = pd.read_csv("agenda.csv")  # Cargar el archivo CSV
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo agenda.csv. Asegúrate de que existe.")
        return
    
    print("📋 Contactos actuales:")
    print(df)  # Muestra los contactos antes de actualizar

    # Pedir el dato identificador (nombre, teléfono o correo)
    criterio = input("🔍 Ingrese el nombre, teléfono o correo del contacto a actualizar: ")

    # Buscar el contacto en cualquier columna
    contacto_idx = df[
        (df["Nombre"] == criterio) | (df["Telefono"] == criterio) | (df["Correo"] == criterio)
    ].index

    if contacto_idx.empty:
        print("❌ Contacto no encontrado.")
        return

    print("\n📌 Contacto encontrado:")
    print(df.loc[contacto_idx])

    # Pedir nuevos datos
    nuevo_nombre = input("Ingrese el nuevo nombre (Enter para mantener): ")
    nuevo_telefono = input("Ingrese el nuevo teléfono (Enter para mantener): ")
    nuevo_correo = input("Ingrese el nuevo correo (Enter para mantener): ")

    # Actualizar solo si el usuario ingresó un nuevo valor
    if nuevo_nombre:
        df.loc[contacto_idx, "Nombre"] = nuevo_nombre
    if nuevo_telefono:
        df.loc[contacto_idx, "Telefono"] = nuevo_telefono
    if nuevo_correo:
        df.loc[contacto_idx, "Correo"] = nuevo_correo

    # Guardar cambios
    df.to_csv("agenda.csv", index=False)
    print("✅ Contacto actualizado exitosamente.\n")
