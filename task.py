import os
import pandas as pd
from git import Repo
import time

############################
# Excel to csv
############################


# Especifica la ruta del archivo XLSX
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = "actitud.xlsx"
file_path = os.path.join(script_directory, filename)
actitud_excel = file_path
csv_file = os.path.join(script_directory,'csv/datos.csv')
csv_astronauta = os.path.join(script_directory,'csv/Astronauta.csv')
csv_senador = os.path.join(script_directory,'csv/Senador.csv')
csv_ninja = os.path.join(script_directory,'csv/Ninja.csv')
csv_mago = os.path.join(script_directory,'csv/Mago.csv')

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

# Extract the "Alumnos" column
Alumnos = Astronauta['Alumnos']
#

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file)

# Update the "Tareas" column in the CSV DataFrame with the "Resultados" data
df_csv['Astronauta'] = Astronauta_resultados
df_csv['Senador'] = Senador_resultados
df_csv['Mago'] = Mago_resultados
df_csv['Ninja'] = Ninja_resultados
df_csv['Alumnos'] = Alumnos
# Write the updated DataFrame back to the CSV file
df_csv.to_csv(csv_file, index=False)

print(f"Excel file has been converted to CSV file 'datos.csv'.")

print("Work done")





############################
# github push
############################



PATH_OF_GIT_REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)),'.git')  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print('Push and commit done')
    except:
        print('Some error occured while pushing the code')    

git_push()

time.sleep(5)