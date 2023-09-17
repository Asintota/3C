import os
import shutil
import openpyxl

# Specify the path to your Excel file
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = "actitud.xlsx"
file_path = os.path.join(script_directory, filename)
print(file_path)
# Load the workbook
workbook = openpyxl.load_workbook(file_path)

# Select the desired worksheet (for example, the first sheet)
worksheet = workbook.active

# Count the number of rows in the worksheet
num_rows = worksheet.max_row

# Print the number of rows
print(f'Total number of rows: {num_rows}')

# Close the workbook (optional, but recommended)
workbook.close()



source_folder = os.path.join(script_directory, "1")
destination_base = script_directory
num_copies = num_rows-1  # Change this to the number of copies you want to make

for i in range(2, num_copies + 1):
    # Create a new folder name based on the iteration index
    new_folder_name = f'{i}'
    
    # Create the full path for the destination folder
    destination_folder = os.path.join(destination_base, new_folder_name)
    
    # Copy the source folder to the destination
    shutil.copytree(source_folder, destination_folder)
    
    # Rename a file within the copied folder (e.g., rename 'file.txt' to 'new_file.txt')
    file_to_rename = os.path.join(destination_folder, '1.html')
    new_file_name = f'{i}.html'
    os.rename(file_to_rename, os.path.join(destination_folder, new_file_name))
    
    print(f'Copy {i} completed.')


# Ruta de la carpeta que contiene las carpetas de archivos HTML a editar



ruta_carpeta_principal = os.path.dirname(os.path.abspath(__file__))

# Iterar sobre las carpetas en la ruta principal
for nombre_carpeta in os.listdir(ruta_carpeta_principal):
    if nombre_carpeta.isdigit(): # Solo procesar carpetas con nombres numéricos
        ruta_carpeta = os.path.join(ruta_carpeta_principal, nombre_carpeta)
        # Buscar archivos HTML en la carpeta
        for nombre_archivo in os.listdir(ruta_carpeta):
            if nombre_archivo.endswith(".html"):
                nombre_archivo_sin_extension = os.path.splitext(nombre_archivo)[0]
                ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
                # Editar número en las líneas del archivo HTML
                with open(ruta_archivo, "r") as archivo:
                    lineas = archivo.readlines()
                # Cambiar el número en las líneas que deseas
                linea_a_editar1 = 14

                estudiante = nombre_archivo_sin_extension
                
                lineas[linea_a_editar1-1] = lineas[linea_a_editar1-1].replace("1", estudiante)
                
                with open(ruta_archivo, "w") as archivo:
                    archivo.writelines(lineas)
