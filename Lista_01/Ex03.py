# Extraia o domínio de um e-mail informado

print("Insira um e-mail: ")
email = input()
dominio = email.split("@") [-1] # Último elemento
print("Domínio: {}".format(dominio))