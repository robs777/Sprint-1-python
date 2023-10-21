agenda = {

}


def add_info_usuarios(agenda,nome,tel,email,dalt):
    novo_usuario = {}
    novo_usuario["telefone"]=tel
    novo_usuario["email"]=email
    novo_usuario["daltonismo"]=dalt
    

    agenda[nome]=novo_usuario
    print(f"Usuário {nome} adicionado")


def lista_usuarios(agenda):
    print(f"agenda possui {len(agenda)} contatos.")
    for nome, contato in agenda.items():
        print(nome)
        for tipo, valor in contato.items():
            print(f"{tipo}-{valor}")


def editar_infos(agenda,nome,tel,email,dalt):
    novo_usuario = {}
    novo_usuario["telefone"] = tel
    novo_usuario["email"]= email
    novo_usuario["daltonismo"]=dalt

    agenda[nome]=novo_usuario
    print(f"Usuário {nome} editado")

def excluir_usuario(agenda,nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Usuário {nome} excluido.")
    else:
        print(f"Usuário {nome} não existe.")

def buscar_usuario(agenda,nome):
    if nome in agenda:
        print(agenda[nome])
    else:
        print("Usuário não encontrado.")

def quant_dalt(agenda, user_dalt):
    
                
            
    


def menu():
    while True:
        print("\nCadastro SalesForce\n")
        print("1 - Adicionar usuário")
        print("2 - Ver usuários")
        print("3 - Editar informações do usuário")
        print("4 - Excluir informações do usuário")
        print("5 - Buscar usuário")
        print("6 - Quantidade de cada tipo de daltonismo:")
        print("7 - Sair\n")
        op_us = input("Escolha uma opção:")

        if op_us == "1":
            user_name = input("Nome do usuário:")
            if user_name not in agenda:
                user_tel = input("Tel do usuário:")
                user_email = input ("Email do usuário:")
                user_dalt = input("Tipo de Daltonismo do usuário:")
            
                    
                
                add_info_usuarios(agenda,user_name,user_tel,user_email,user_dalt)
            else: 
                print(f"Usuário {user_name} já existe")
            
        
        elif op_us == "2":
            lista_usuarios(agenda)
        
        elif op_us == "3":
            user_name = input("Nome do usuário:")
            if user_name in agenda:
                user_tel=input("Tel do usuário:")
                user_email = input ("Email do usuário:")
                user_dalt = input ("Tipo de Daltonismo do usuário:")
                editar_infos(agenda,user_name,user_tel,user_email,user_dalt)
            else:
                print(f"Usuário {user_name} não existe")

        elif op_us == "4":
            user_name = input("Escolha o usuário para excluir:")
            excluir_usuario(agenda,user_name)

        elif op_us == "5":
            user_name = input("Encontrar usuário:")
            buscar_usuario(agenda,user_name)

        elif op_us == "6":
            user_dalt = input("Qual tipo de daltonismo você quer saber a quantidade? ")
            quant_dalt(agenda,user_dalt)
            

        elif op_us == "7":
            print("Fechando o programa")
            break
        else: 
            print(f"Opção {op_us} invalida. Escolha as opções mostradas")

if __name__ == "__main__":
    menu()
