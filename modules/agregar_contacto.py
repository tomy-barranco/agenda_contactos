import pandas as pd

def agregar_contacto():
    try:
        df = pd.read_csv("agenda.csv")  
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nombre", "Telefono", "Correo"])  

    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")

    nuevo_contacto = pd.DataFrame([{"Nombre": nombre, "Telefono": telefono, "Correo": correo}]) 
    df = pd.concat([df, nuevo_contacto], ignore_index=True)  
    df.to_csv("agenda.csv", index=False)  

    print("✅ Contacto agregado exitosamente.\n")

# ⛔ Asegura que la función solo se ejecute si este archivo se ejecuta directamente
if __name__ == "__main__":
    agregar_contacto()
