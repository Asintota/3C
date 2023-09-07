import pandas as pd

# Especifica la ruta del archivo XLSX
actitud_excel = 'C:/Users/pablo/OneDrive/Github/Progreso/actitud.xlsx'
csv_file = 'C:/Users/pablo/OneDrive/Github/Progreso/csv/datos.csv'
csv_astronauta = 'C:/Users/pablo/OneDrive/Github/Progreso/csv/Astronauta.csv'
csv_senador = 'C:/Users/pablo/OneDrive/Github/Progreso/csv/Senador.csv'
csv_ninja = 'C:/Users/pablo/OneDrive/Github/Progreso/csv/Ninja.csv'
csv_mago = 'C:/Users/pablo/OneDrive/Github/Progreso/csv/Mago.csv'

# Lee el archivo XLSX en un DataFrame de pandas

Astronauta = pd.read_excel(actitud_excel, sheet_name = "Astronauta")
Senador = pd.read_excel(actitud_excel, sheet_name = "Senador")
Mago = pd.read_excel(actitud_excel, sheet_name = "Mago")
Ninja = pd.read_excel(actitud_excel, sheet_name = "Ninja")

Astronauta.to_csv(csv_astronauta, index=False)
print(f"Excel file has been converted to CSV file 'Astronauta.csv'.")
Senador.to_csv(csv_senador, index=False)
print(f"Excel file has been converted to CSV file 'Senador.csv'.")
Mago.to_csv(csv_mago, index=False)
print(f"Excel file has been converted to CSV file 'Mago.csv'.")
Ninja.to_csv(csv_ninja, index=False)
print(f"Excel file has been converted to CSV file 'Ninja.csv'.")



# Extract the "Resultados" column as a separate Series
Astronauta_resultados = Astronauta['Resultados']
Senador_resultados = Senador['Resultados']
Mago_resultados = Mago['Resultados']
Ninja_resultados = Ninja['Resultados']


#

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file)

# Update the "Tareas" column in the CSV DataFrame with the "Resultados" data
df_csv['Astronauta'] = Astronauta_resultados
df_csv['Senador'] = Senador_resultados
df_csv['Mago'] = Mago_resultados
df_csv['Ninja'] = Ninja_resultados

# Write the updated DataFrame back to the CSV file
df_csv.to_csv(csv_file, index=False)
print(f"Excel file has been converted to CSV file 'datos.csv'.")

print("Work done")







