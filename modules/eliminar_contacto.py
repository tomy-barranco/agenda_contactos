import pandas as pd

def eliminar_contacto():
    try:
        df = pd.read_csv("agenda.csv")  # Cargar el archivo CSV
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo agenda.csv. Asegúrate de que existe.")
        return
    
    print("📋 Contactos actuales:")
    print(df)  # Mostrar contactos antes de eliminar

    # Pedir criterio para buscar (nombre, teléfono o correo)
    criterio = input("🔍 Ingrese el nombre, teléfono o correo del contacto a eliminar: ")

    # Buscar el contacto en cualquier columna
    contacto_idx = df[
        (df["Nombre"] == criterio) | (df["Telefono"] == criterio) | (df["Correo"] == criterio)
    ].index

    if contacto_idx.empty:
        print("❌ Contacto no encontrado.")
        return

    print("\n📌 Contacto encontrado:")
    print(df.loc[contacto_idx])

    # Confirmación antes de eliminar
    confirmacion = input("⚠️ ¿Está seguro de que quiere eliminar este contacto? (s/n): ").lower()
    if confirmacion != "s":
        print("❌ Cancelado.")
        return

    # Eliminar contacto
    df.drop(index=contacto_idx, inplace=True)

    # Guardar cambios
    df.to_csv("agenda.csv", index=False)
    print("✅ Contacto eliminado exitosamente.\n")