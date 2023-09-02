import pandas as pd

# Especifica la ruta del archivo XLSX
archivo_excel = 'C:/Users/pablo/OneDrive/Github/Progreso/tareas.xlsx'
csv_file = 'C:/Users/pablo/OneDrive/Github/Progreso/progreso.csv'
# Lee el archivo XLSX en un DataFrame de pandas
df_excel = pd.read_excel(archivo_excel)

# Extract the "Resultados" column as a separate Series
resultados_column = df_excel['Resultados']

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file)

# Update the "Tareas" column in the CSV DataFrame with the "Resultados" data
df_csv['Tareas'] = resultados_column

# Write the updated DataFrame back to the CSV file
df_csv.to_csv(csv_file, index=False)


print("Data from 'Resultados' column in Excel has been copied to the 'Tareas' column in the CSV file.")







