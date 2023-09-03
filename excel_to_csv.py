import pandas as pd

# Especifica la ruta del archivo XLSX
actitud_excel = 'C:/Users/pablo/OneDrive/Github/Progreso/actitud.xlsx'
csv_file = 'C:/Users/pablo/OneDrive/Github/Progreso/datos.csv'
# Lee el archivo XLSX en un DataFrame de pandas

Astronauta = pd.read_excel(actitud_excel, sheet_name = "Astronauta")
Senador = pd.read_excel(actitud_excel, sheet_name = "Senador")
Mago = pd.read_excel(actitud_excel, sheet_name = "Mago")
Guerrero = pd.read_excel(actitud_excel, sheet_name = "Guerrero")




# Extract the "Resultados" column as a separate Series
Astronauta_resultados = Astronauta['Resultados']
Senador_resultados = Senador['Resultados']
Mago_resultados = Mago['Resultados']
Guerrero_resultados = Guerrero['Resultados']

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file)

# Update the "Tareas" column in the CSV DataFrame with the "Resultados" data
df_csv['Astronauta'] = Astronauta_resultados
df_csv['Senador'] = Senador_resultados
df_csv['Mago'] = Mago_resultados
df_csv['Guerrero'] = Guerrero_resultados

# Write the updated DataFrame back to the CSV file
df_csv.to_csv(csv_file, index=False)


print("Work done")







