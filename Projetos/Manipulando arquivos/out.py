import os

# Obtém o diretório atual de trabalho
cwd = os.getcwd()

# Lista todas as pastas no diretório atual
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

# Para cada pasta encontrada
for folder in folder_list:
    path = os.path.join(cwd, folder)

    # Lista os arquivos dentro da pasta
    files = os.listdir(path)
    
    # Move todos os arquivos da pasta para o diretório atual
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(cwd, file)

        # Se o nome do arquivo já existir no destino, renomeia para evitar conflito
        if os.path.exists(to_path):
            base, ext = os.path.splitext(file)
            i = 1
            while os.path.exists(to_path):
                new_name = f"{base}_{i}{ext}"
                to_path = os.path.join(cwd, new_name)
                i += 1

        os.replace(from_path, to_path)

    # Após mover todos os arquivos, remove a pasta vazia
    os.rmdir(path)
