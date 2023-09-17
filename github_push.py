import os
import git
from github import Github

# Ruta del directorio del repositorio local
repo_dir = os.path.dirname(os.path.abspath(__file__))

# Mensaje del commit
commit_message = 'Tu mensaje de commit aquí'

# Nombre de la rama en la que deseas hacer el commit y el push
branch_name = 'main'

# Token de autenticación de GitHub (necesario para realizar el push)
github_token = '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'

# Nombre de usuario de GitHub
github_username = 'Asintota'

# Nombre del repositorio en GitHub
github_repo_name = '3C'

# Ruta al archivo remoto del repositorio en GitHub
remote_repo_url = f'https://github.com/{github_username}/{github_repo_name}.git'

print(remote_repo_url)

try:
# Cambia al directorio del repositorio local
    os.chdir(repo_dir)

    # Inicializa el repositorio Git
    repo = git.Repo(repo_dir)
    
    # Agrega todos los cambios al área de preparación
    repo.git.add('--all')

    # Realiza el commit
    repo.git.commit('-m', commit_message)

    # Conecta con GitHub usando tu token
    g = Github(github_token)

    # Obtiene el repositorio remoto en GitHub
    repo_github = g.get_repo(f'{github_username}/{github_repo_name}')

    # Obtiene la rama específica en la que deseas hacer el push
    branch = repo_github.get_branch(branch_name)

    # Sube los cambios al repositorio remoto en la rama especificada
    repo.git.push(remote_repo_url, branch_name)

    print(f'Commit y push exitosos en la rama {branch_name} de {github_repo_name}.')

except Exception as e:
    print(f"An error occurred: {e}")