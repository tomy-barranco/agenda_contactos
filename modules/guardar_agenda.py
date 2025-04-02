import csv

def guardar_agenda_csv(agenda, archivo="agenda.csv"):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "telefono", "correo"])
        writer.writeheader()  # Escribe la primera fila con los nombres de las columnas
        writer.writerows(agenda)