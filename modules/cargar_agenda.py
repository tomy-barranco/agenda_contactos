import csv
import pandas as pd

# def cargar_agenda(archivo="agenda.csv"):
#   agenda = []
#   try:
#     with open(archivo, "r", encoding="utf-8") as f:
#       reader = csv.DictReader(f)
#       for row in reader:
#         agenda.append(row)
#       print(agenda)
#   except FileNotFoundError:
#     print("No se encontró el archivo, creando una nueva agenda...")
#   return agenda

def cargar_agenda(archivo="agenda.csv"):
  try:
    agenda = pd.read_csv(archivo, encoding="utf-8")
    print(agenda)
    print("📒 Agenda cargada correctamente")
  except FileNotFoundError:
    print("⚠️ No se encontró el archivo, creando una nueva agenda...")
    open("agenda.csv", "x")
    df = pd.DataFrame(columns=["Nombre", "Telefono", "Correo"])
    df.to_csv("agenda.csv", index=False)


cargar_agenda()