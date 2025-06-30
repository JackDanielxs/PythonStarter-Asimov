import os

# Obtém o diretório atual de trabalho
cwd = os.getcwd()

# Lista todos os arquivos e pastas no diretório atual
full_list = os.listdir(cwd)

# Filtra apenas os arquivos que não possuem a extensão '.py'
files_list = [f for f in full_list if os.path.isfile(f) and not f.endswith('.py')]

# Cria um conjunto com todas as extensões únicas dos arquivos válidos
extensions = set()
for f in files_list:
    if '.' in f:
        ext = f.split('.')[-1]
        extensions.add(ext)

# Cria uma pasta para cada extensão, se ainda não existir
for ext in extensions:
    folder_path = os.path.join(cwd, ext)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Move os arquivos para suas respectivas pastas
for file in files_list:
    if '.' not in file:
        continue  # pula arquivos sem extensão

    ext = file.split('.')[-1]
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, ext, file)

    # Verifica se o arquivo já foi movido
    if not os.path.exists(to_path):
        os.replace(from_path, to_path)
