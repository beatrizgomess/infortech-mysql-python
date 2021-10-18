
import time
import mysql.connector
import pandas as pd
from datetime import date

   

print("=" * 140)
print(f'{"INFORTECH":^130}') 
print("=" * 140)

print("Conectando Banco...")
time.sleep(2)
print("Reorganizando dados...")
time.sleep(2)
print("PRONTO PARA USO!!\n")
escolha = 0

while escolha != 4:
    print("\n\033[32m QUAL SEU PERFIL? \033[m\n")
    print('''[ 1 ] - ADMINISTRADOR
[ 2 ] - FUNCIONARIO
[ 3 ] - CLIENTE
[ 4 ] - SAIR ''')
    escolha = int(input("OPÇÃO: "))
    print("Exibindo dados...")
    time.sleep(2) 





#? SELECIONOU ADMINISTRADOR

    if escolha == 1:
        
        PerfilAdm(int)
        perfiladministrador = int(input("OPÇÃO: "))
        
        #? ESCOLHEU CLIENTES
        escolheuClientes = 0
        while True:
            if perfiladministrador == 1:
                print("\t\nBuscando dados referentes a clientes")
                time.sleep(2)
                #while escolha != 5:
                subMenu(int)
                escolhaAdm = int(input("OPÇÃO: "))
                time.sleep(2)
                print("=" * 130)
                        
                        
                        
                        
                
                if escolhaAdm == 1:
                    print("EXIBIR DADOS")
                    time.sleep(2)
                    exibirTabelas("CLIENTES")
                    sucesso()
                            
                            
                        
                            
                            

                if escolhaAdm == 2:
                    nome_tabela = "CLIENTES"
                    nome_ColunaID = "CPF"
                    #coluna_identificador = "CPF"
                    atualizar("CLIENTES")
                    sucesso()
                                
                                        

                if escolhaAdm == 3:
                    cadastrarCliente("CLIENTES")
                    sucesso()
                        
                        
                        
                        
                        
                if escolhaAdm == 4:
                    print("DELETAR CLIENTE")
                    nome_tabela = "CLIENTES"
                    coluna_identificador = "CPF"
                    #coluna_identificador = "CPF"
                    deletar("CLIENTES")
                    sucesso()
                            
                            
                            
                            
                
                if escolhaAdm == 5:
                    print("\n\tVoltando ao Menu anterior... ")
                    time.sleep(2)
                    PerfilAdm(int)
                    perfiladministrador = int(input("OPÇÃO:  "))
                        
                    
                        
            
    #? ##############################################################################################################

    #! ESCOLHEU PRODUTOS

            escolheuProdutos = 0
            if perfiladministrador == 2:
                   print("=" * 50)
                   print("\tBuscando dados referentes a produtos")
                   time.sleep(2)
                   subMenu(int)
                   escolhaAdm = int(input("OPÇÃO: "))
                   print("=" * 130) 
                                      
                   if escolhaAdm == 1:
                        time.sleep(2)
                        exibirTabelas("PRODUTOS")
                        print("\n")
                        visualizar_Produto = input("\033[33mDeseja visualizar um produto especifico? [S/N]\033[m ").upper().strip()[0] 
                        while visualizar_Produto in "S":
                            print("VISUALIZAR PRODUTOS ESPECIFICOS")
                            nome_tabela = "PRODUTOS"
                            coluna_identificador = "ID_PRODUTO"
                            identificador = input("Informe o ID do PRODUTO: ")
                            
                            time.sleep(2)
                            visualizarEspecificos("PRODUTOS")
                            visualizar_Produto = input("\033[33mDeseja visualizar um produto especifico? [S/N]\033[m ").upper().strip()[0]
                          
                        else:
                            if visualizar_Produto in "N":
                                    time.sleep(2)
                                    True
                        
                        
                        
                    #! ATUALIZAR PRODUTO    
            elif escolhaAdm == 2:
                        print("\n") 
                        print("ATUALIZAR PRODUTO")
                        nome_tabela = "PRODUTOS"
                        nome_ColunaID = "ID_PRODUTO"
                        atualizar('PRODUTOS')
                        sucesso()
                        
                        
                             
                                
                                
                                
                                
                    #! CADASTRAR PRODUTO
            if escolhaAdm == 3:
                        print("=" * 130)
                        print("\n")
                        print("CADASTRAR UM PRODUTO")
                        
                        cadastrar_produto = input("Deseja cadastrar outro produto? [S/N]").upper().strip()[0]
                        if cadastrar_produto in "S":
                            nome_produto = input("NOME DO PRODUTO: ").upper().strip()
                            descricao = input("DETALHES DO PRODUTO: ").title().strip()
                            qant = input("QUANTIDADE: ")
                            valor = input("PREÇO: ")  
                            
                            cadastrarProdutos('PRODUTOS')
                            
                      
                            
                            
                            
                              
                        
                        
                            
                            
                    #! DELETAR PRODUTO        
                    
            if escolhaAdm == 4:
                        print("=" * 130)
                        print("\n")
                        print("DELETAR PRODUTOS")
                        nome_tabela = "PRODUTOS"
                        coluna_identificador = "ID_PRODUTO"
                        
                        deletar('PRODUTOS')
                        
                        
                        
                        
            if escolhaAdm == 5:
                        print("\nVoltando ao Menu anterior... ")
                        time.sleep(2)
                        PerfilAdm(int)
                        perfiladministrador = int(input("OPÇÃO:  "))
                       
                        
         
         
         
                               
    #!###################################################################################################################

    #* ESCOLHEU FUNCIONÁRIO 

            escolheuFuncionarios = 0
            while True:
                if perfiladministrador == 3:
                    print("\nBuscando dados referentes a Funcionarios")
                    time.sleep(2)
                    #while escolheuFuncionarios != 5:
                    subMenu(int)
                    escolhaAdm = int(input("OPÇÃO: "))
                    print("=" * 130)
                    
                    
                    
                    
                    
                    
                    #* VISUALIZAR FUNCIONARIOS (SELECT)
                    
                if escolhaAdm == 1:
                        print("\n")
                        print("EXBIR DADOS")
                        exibirTabelas("FUNCIONARIOS")
                        sucesso()
                        
                        
                        
                        
                        
                        
                        
                    #* ATUALIZAR DADOS (UPDATE)
                        
                elif escolhaAdm == 2:
                        print("=" * 130)
                        print("\n")
                        print("ATUALIZAR FUNCIONARIOS")
                        nome_tabela = 'FUNCIONARIOS'
                        nome_ColunaID = "CPF"
                    
                        atualizar('FUNCIONARIOS')
                        sucesso()
                        
                        
                        
                        
                        
                        
                        
                        
                        #* CADASTRAR FUNCIONARIO (INSERT INTO)
                        
                elif escolhaAdm == 3:
                        print("=" * 130)
                        print("\n")
                        print("CADASTRAR FUNCIONARIOS")
                        while True:
                            cpf = str(input("CPF: "))
                            while len(cpf) != 14: 
                                print("\033[41m CPF INVÁLIDO!!\033[m")
                                print("\033[41m O CPF PRECISA TER 11 DÍGITOS!!\033[m")
                                cpf = (input("CPF: "))
                                
                            
                            else:
                                nome_funcionario = input("NOME FUNCIONARIO: ").strip().title()
                                data_nascF = input("DATA DE NASCIMENTO: ")
                                cargo = input("CARGO: ").strip().title()
                                rua = input("RUA: ").strip().title()
                                bairro = input("BAIRRO: ").strip().title()
                                cidade = input("CIDADE: ").strip().title()
                                cep = input("CEP: ")
                                complemento = input("COMPLEMENTO: ").strip().title()
                                estado = input("ESTADO: EX[PE] ").strip().upper()
                                inserir_funcionario = f"INSERT INTO FUNCIONARIOS (CPF, NOME, DATA_NASC, CARGO, LOGRADOURO, BAIRRO, CIDADE, CEP, ESTADO)\
                                    VALUES ('{cpf}', '{nome_funcionario}', '{data_nascF}', '{cargo}', '{rua}', '{bairro}', '{cidade}', '{cep}', '{estado}')"
                                mycursor.execute(inserir_funcionario)
                                mydb.commit()
                                sucesso()
                                time.sleep(2)
                                print("\033[36mFUNCIONARIO ADICIONADO COM SUCESSO!!!\033[m")
                                cadastrar_funcionario = str(input("\033[31mDeseja cadastrar um funcionário? [S/N]\033[m")).upper().strip()
                        


                        
                        else:
                            time.sleep(2)
                            subMenu(int)
                            escolhaAdm = input("OPÇÃO:  ")
                        
                        
                        
                        
                        #* DELETAR FUNCIONARIO (DELETE)
                        
                if escolhaAdm == 4:   
                            print("=" * 130)
                            print("\n")
                            print("DELETAR FUNCIONARIOS")
                            nome_tabela = 'FUNCIONARIOS'
                            coluna_identificador = "CPF"
                            
                            deletar("FUNCIONARIOS")
                                
                    
                    
                    
                    
                    
                if escolhaAdm == 5:
                        print("\n\t\n\nVoltando ao Menu anterior... ")
                        time.sleep(2)
                        PerfilAdm(int)
                        perfiladministrador = int(input("OPÇÃO:  "))
                                
                        
    #*#########################################################################################################################   
        

        #? ESCOLHEU FORNECEDOR
        while True:
            if perfiladministrador == 4: 
                print("\n\tBuscando referências de Fornecedores...")
                time.sleep(2)
                subMenu(int)
                escolhaAdm = int(input("\033[36mOPÇÃO \033[m "))
                print("=" * 50)
            
            
            
            
            
            
            
            
            #? VISUALIZAR FORNECEDORES (SELECT)
            
            if escolhaAdm == 1:
                print("\n")
                print("VISUALIZAR FORNECEDORES")
                exibirTabelas("FORNECEDORES")
                sucesso()
                
                
                
                
                
                
                
                
                
                
            #? ATUALIZAR FORNECEDOR (UPDATE)    
                
            if escolhaAdm == 2:
                print("\n")
                print("ATUALIZAR DADOS")
                exibirTabelas("FORNECEDORES\n")
                nome_tabela = "FORNECEDORES"
                nome_ColunaID = "CNPJ"
                atualizar('FORNECEDORES')
                
            
            
           
                    
                    
            #? CADASTRAR FORNECEDOR (INSERT INTO)        
                    
            if escolhaAdm == 3:
                print("\n")
                print("CADASTRAR FORNECEDORES")
                cadastrarFornecedor("FORNECEDORES")
               
                   
                   
                   
                   
                            
                            
            #? DELETAR FORNECEDOR (DELETE) 
            
            if escolhaAdm == 4:
                print("\n")
                print("DELETAR FORNECEDOR")
                nome_tabela = "FORNECEDORES"
                coluna_identificador = "CNPJ"
                deletar("FORNECEDORES")
            
            
            
            
            
            
            
            
                     
            if escolhaAdm == 5:
                print("\n\tVoltando ao Menu anterior... ")
                time.sleep(2)
                PerfilAdm(int)
                perfiladministrador = int(input("\033[36mOPÇÃO:\033[m "))        
                    
                    
        
        
                
                  
                  
 #*############################################################################################################################                   
    
    #! PERFIL CLIENTE       
                    
    if escolha == 3:
        print("\n")
        print("\033[33mPERFIL CLIENTE\033[m")
        time.sleep(2)
        perfilCliente = int(input('''\nO que você deseja fazer?\n
[1] - Visualizar Cadastro
[2] - Visualizar Pedidos
[3] - Cancelar Pedidos
[4] - Status dos meus pedidos")
[5] - VOLTAR AO MENU DE OPÇÕES 
OPÇÃO: '''))
        
            
        cpf_cliente = "089.456.234-18"
        if perfilCliente == 1:
            print("\nVISUALIZAR CADASTRO")
            exibir_dados = f"SELECT * FROM CLIENTES WHERE CPF = '{cpf_cliente}'"
            pandas("CLIENTES")
     
            
            
            
            
        elif perfilCliente == 2:
            print("\nVISUALIZAR PEDIDOS")
            exibir_dados = f'''SELECT * FROM PEDIDOS WHERE CPF_CLIENTE = '{cpf_cliente}'
            '''
            pandas("PEDIDOS")
            
            
        if perfilCliente == 3:
            print("\nCANCELAR PEDIDOS")
            
            exibir_dados = f'''SELECT * FROM PEDIDOS WHERE CPF_CLIENTE = '{cpf_cliente}'
            '''
            pandas("PEDIDOS")
            
            cancelar_pedido = input("\033[31m\n Você deseja cancelar o pedido? [S/N]\033[m ").upper().strip()[0]
            if cancelar_pedido in "S":
                id_pedido = input("Informe o ID do pedido: ")
                novo_atributo = ("Cancelado")
                
                exibir_dados = f'''SELECT * FROM PEDIDOS WHERE ID = '{id_pedido}' '''                   
                pandas("PEDIDOS")
                
                
                confirmar_cancelamento = input("\033[4;31mVocê confirma o cancelamento do pedido? [S/N]\033[m ").upper().strip()[0]
                if confirmar_cancelamento in "S":
                    atualizar_statuspedidos = (f"UPDATE STATUS_PEDIDO SET STATUS_PEDIDO = '{novo_atributo}' WHERE (ID_PEDIDOS = {id_pedido} and CPF_CLIENTE = '{cpf_cliente}')")
                    mycursor.execute(atualizar_statuspedidos)
                    
                    exibir_dados = f'''SELECT * FROM STATUS_PEDIDO WHERE ID_PEDIDOS = '{id_pedido}'
                    '''
                    pandas("STATUS_PEDIDO")
                    
                else:
                    print("\033[4;32mO pedido continua em andamento\033[m")
                    True
                
                
                
                        
            else:
                print("\033[4;32m Pedido OK\033[m")
                True
            
            
            
        if perfilCliente == 4:
            print("\n")
            print("VISUALIZAR STATUS DOS MEUS PEDIDOS")
            exibir_dados = f'''SELECT * FROM STATUS_PEDIDO WHERE CPF_CLIENTE = '{cpf_cliente}'
            '''
            pandas("STATUS_PEDIDOS")
            
            
            
                 
        if perfilCliente == 5:
            print("\n\tVoltando ao Menu anterior... ")
            time.sleep(2)
            PerfilAdm(int)
            perfiladministrador = int(input("OPÇÃO:  "))        
                    
            
        
            
    
            
            
#?###################################################################################################################
            
            
            
            
            
    if escolha == 2:
        print("\n")
        print("PERFIL FUNCIONÁRIO")
        time.sleep(2)
        perfilfuncionario = int(input('''O que você deseja fazer? 
[1] - Registrar Pedidos                 ||    [5] - Cadastrar/Visualizar Produtos
[2] - Visualizar Pedidos                ||    [6] - Cadastrar/Visualizar Status Pedidos
[3] - Cadastrar/Visualizar Clientes     ||    [7] - Voltar ao Menu Principal 
[4] - Cadastrar/Visualizar Fornecedores ||    
                  
OPÇÃO: '''))
        
        c = total = quantidade = 0
        
        
        
        if perfilfuncionario == 1:
            print("\n")
            print("REGISTRAR PEDIDOS")  
            cadastrar_pedido = str(input("\033[32mDeseja cadastrar um pedido?[S/N]\033[m ")).upper().strip()
            if cadastrar_pedido in "N":
                    print("Voltando..")
                    time.sleep(2)
                    True
                    
            else:
                if cadastrar_pedido not in "SN":
                    print("\033[30;41mDigite uma opção válida!! [S - SIM || N - NÃO\033[m")
                    cadastrar_pedido = str(input("\033[32mDeseja cadastrar um pedido?[S/N]\033[m ")).upper().strip()[0]
                
                else:
                
                    id_funcionario = str(input("ID DO FUNCIONÁRIO:  "))
                    cpf_cliente = (input("CPF DO CLIENTE: ")).strip().title()
                    adicionar_produtos = input("Deseja adicionar um produto? [S/N] ").upper().strip()[0]
                        
                    while adicionar_produtos in "S":
                        id_produto = (input("\033[36mID PRODUTOS: \033[m")).strip()
                        data = date.today()
                        print("-" * 90)
                        quantidade = quantidade + 1  
                        exibir_dados = f"select produtos.ID_PRODUTO, produtos.nome, valor, sum(produtos.valor) as total from produtos where produtos.ID_PRODUTO in ('{id_produto}')"
                            
                            
                        pandas("PRODUTOS")
                        n = float(input("Informe o valor do produto: "))
                        print("=" * 90)
                        total = total + n
                        adicionar_produtos = input("Deseja adicionar um produto? [S/N] ").upper().strip()
                            
                    else:
                            
                        print(f"\nO Pedido possui {quantidade} produtos")
                        print("\nTOTAL DO PEDIDO: {:.2f}".format(total))
                        confirmar_pedido = " "
                        novo_atributo = "Aguardando Pagamento"
                            
                        while confirmar_pedido not in "SN":
                            confirmar_pedido = input("Deseja registrar esse pedido? [S/N]  ").strip().upper()[0]
                            if confirmar_pedido == "S":
                                registrar_pedido = f"INSERT INTO PEDIDOS (ID_FUNCIONARIO, CPF_CLIENTE, ID_PRODUTO, DATA_PEDIDO, QUANTIDADE, VALOR)\
                                                        VALUES ('{id_funcionario}', '{cpf_cliente}', '{id_produto}','{data}','{quantidade}', '{total}')"
                                
                                    
                                mycursor.execute(registrar_pedido)
                                mydb.commit()
                                print("\n")
                                time.sleep(2)
                                sucesso()
                                    
                                registrar_status = input("Deseja registrar o status do pedido? [S/N] ").upper().strip()[0]
                                if registrar_status in "S":
                                    inserir_status = f"INSERT INTO STATUS_PEDIDO (CPF_CLIENTE, STATUS_PEDIDO)\
                                        VALUES ('{cpf_cliente}', 'Aguardando Pagamento')"
                                    mycursor.execute(inserir_status)
                                    mydb.commit()
                                    time.sleep(2)
                                    sucesso()                                
                                #else:
                                    #print("Opção Inválida")
                                else:    
                                    if confirmar_pedido == "N":
                                        print("\033[31mVocê selecionou NÃO registrar o pedido\033[m")
                                    else:
                                        if registrar_pedido not in "S" or "N":
                                            print("\033[31mOpção Inválida!!\033[m")
                
                
                                
            
        if perfilfuncionario == 2:
            print("\n")
            print("VISUALIZAR PEDIDOS")
            selecione_cliente = input("Informe o CPF do cliente: ")
            time.sleep(2)
            
            print(f"\nExibindo os pedidos do CPF {selecione_cliente}")
            
            
            exibir_dados = f'''select * from pedidos where cpf_cliente = '{selecione_cliente}' '''           
            pandas("PEDIDOS")
            time.sleep(2)
            sucesso()



        if perfilfuncionario == 3:
            while True:
                print('''[1] - Visualizar um cliente especifico\n[2] - Cadastrar um cliente\n[3] - Atualizar Clientes''')
                secaoCliente = int(input())
                
                
                if secaoCliente == 1:
                    print("\n")
                    print("VISUALIZAR CLIENTES")
                    exibirTabelas("CLIENTES")
                    cpf_cliente = input("Informe o CPF do cliente: ")
                    exibir_dados = f"SELECT * FROM CLIENTES WHERE CPF = '{cpf_cliente}'"
                    
                    
                    pandas("CLIENTES")
                    sucesso()
                    
                    
                    
                if secaoCliente == 2:
                    print("\n")
                    print("CADASTRAR CLIENTE")
                    cadastrarCliente("CLIENTES")
                    
                
            
                if secaoCliente == 3:
                    print("\n")
                    print("ATUALIZAR CLIENTE")
                    nome_tabela ="CLIENTES"
                    atualizar("CLIENTES")
                    
                    
                    
                    
                    
                    
                
                
         
                            
        if perfilfuncionario == 4:
            time.sleep(2)
            print('''[1] - Visualizar Fornecedores\n[2] - Cadastrar Fornecedores\n[3] - Atualizar Fornecedores\n[0] - Voltar''')
            secaoFornecedor = int(input("> "))
            time.sleep(2)
            if secaoFornecedor == 0:
                print("Voltando...")
                True
            
            
            
            
            if secaoFornecedor == 1:
                print("\n")
                print("VISUALIZAR FORNECEDORES")
                exibirTabelas("FORNECEDORES")
                selecione_fornecedor = input("Informe o CNPJ: ")
                exibir_dados = f"SELECT * FROM FORNECEDORES WHERE CNPJ = '{selecione_fornecedor}'"
            
                pandas("FORNECEDORES")
            
            
            

            
            if secaoFornecedor == 2:
                print("\n")
                print("CADASTRAR FORNECEDORES")
                cadastrarFornecedor("FORNECEDORES")
                
                
                                
                            
            if secaoFornecedor == 3:
                print("\n")
                print("ATUALIZAR DADOS")
                nome_tabela = "FORNECEDORES"
                atualizar("FORNECEDORES")                
                            




                            
                                
        elif perfilfuncionario == 5:            
            print('''[1] - Visualizar Produtos\n[2] - Cadastrar Produtos\n[3] - Atualizar Produtos4\n[4] - Verificar detalhes dos produtos ''')
            secaoProdutos = str(input("> "))
            time.sleep(2)
            while secaoProdutos not in "12340":
                secaoProdutos = str(input("\033[31m> Selecione uma opção acima ou 0 para sair\033[m "))

            else:
                
                if secaoProdutos == "1":
                    print("\n")
                    print("VISUALIZAR PRODUTOS")
                    time.sleep(2)
                    exibirTabelas("PRODUTOS")
                    visualizar_produto = "S"
                    while visualizar_produto in "S":
                            visualizar_produto = input("\033[32mDeseja visualizar um produto especifico? [S/N]\033[m").upper().strip() 
                            if visualizar_produto in "N":
                                True
                            else:
                                
                                print("\n")
                                print("VISUALIZAR PRODUTOS ESPECIFICOS")
                                nome_tabela = "PRODUTOS"
                                coluna_identificador = "ID_PRODUTO"
                                identificador = input("Informe o ID do PRODUTO: ")
                                                
                                time.sleep(2)
                                visualizarEspecificos("PRODUTOS")
                            
                    
                   
                            
                        
                        
                        
                        
                if secaoProdutos == "2":
                    print("=" * 130)
                    print("\n")
                    print("\033[4;32m2CADASTRAR UM PRODUTO\033[m")
                    cadastrar_produto = "S"
                    while cadastrar_produto in "S":
                        cadastrar_produto = input("\033[32mDeseja cadastrar um produto? [S/N]\033[m ").upper().strip()[0]
                        if cadastrar_produto in "N":
                            True
                        else:
                            nome_produto = input("NOME DO PRODUTO: ").upper().strip()
                            descricao = input("DETALHES DO PRODUTO: ").title().strip()
                            qant = input("QUANTIDADE: ")
                            valor = input("PREÇO: ")  
                                        
                            cadastrarProdutos('PRODUTOS')
                                
                            
                                
                
                
                            
                
                if secaoProdutos == "3":
                    print("\n")
                    nome_tabela = "PRODUTOS"
                    print("ATUALIZAR DADOS")
                    atualizar("PRODUTOS")
                    #pandas("PRODUTOS")
                
                
                
                
                
                
                        
                if secaoProdutos == "4":
                    print("\n")
                    print("VERIFICAR PRODUTOS")
                    id_produto = input("Informe o ID do produto para realizar a busca:  ")
                    verificarPorID("PRODUTOS")
                            
                            
                    
                

                if secaoProdutos == 0:
                    print("\n")
                    priint("Voltando ao Menu Principal")
                    PerfilAdm(int)
                    escolha = int(input("OPÇÃO  "))        
                
                
                
                
                

                        
        elif perfilfuncionario == 6:
                print('''[1] - Visualizar Status Pedido
[2] - Cadastrar Status Pedidos
[3] - Atualizar Status Pedidos ''')
                secaoStatus_pedidos = int(input("OPÇÃO:  "))
                
                if secaoStatus_pedidos == 1:
                    print("\n")
                    print("VISUALIZAR STATUS DOS PEDIDOS")
                    visualizar_pedido = "S"
                    while visualizar_pedido in "S":
                        visualizar_pedido = input("\033[32mDeseja realizar uma  visualização? [S/N]\033[m ").upper().strip()
                        if visualizar_pedido in "N":
                            True
                            
                        else:
                            cpf_cliente = input("Informe o CPF do cliente: ")
                            exibir_dados = f"SELECT * FROM STATUS_PEDIDO WHERE CPF_CLIENTE = '{cpf_cliente}'"
                            pandas("STATUS_PEDIDO")    
                        
                    
                    
                    
                
                
                if secaoStatus_pedidos == 2:
                    print("\n")
                    print("CADASTRAR STATUS PEDIDO")
                    cpf_cliente = input("Informe o CPF do cliente: ")
                    id_pedido = input("Informe o ID do pedido: ")
                    novo_atributo = "Aguardando Pagamento"
                     
                    inserir_status = f"INSERT INTO STATUS_PEDIDO (ID_PEDIDO, CPF_CLIENTE, STATUS_PEDIDO)\
                                       VALUES ('{id_pedido}','{cpf_cliente}, '{novo_atributo}')"
                    mycursor.execute(inserir_status)
                    mydb.commit()
                    sucesso()
                    
                    visualizar_pedido = "S"   
                    while visualizar_pedido in "S":    
                        visualizar_pedido = input("\033[36mDeseja Visualizar este pedido? [S/N]\033[m ").strip().upper()[0] 
                        if visualizar_pedido in "N":
                            True
                        else:
                                       
                            exibir_dados = f"SELECT * FROM STATUS_PEDIDO WHERE CPF_CLIENTE = '{cpf_cliente}'"
                            pandas("STATUS_PEDIDO")
                        
                
                
                
                
                    
            
                if secaoStatus_pedidos == 3: 
                    print("\n")
                    print("ATUALIZAR O STATUS DOS PEDIDOS")
                    
                    atualizar = " "
                    while atualizar not in "NS":
                        atualizar = input("\033[32mDeseja realizar outra atualização? [S/N] \033[m").upper().strip()[0]
                        if atualizar in "N":
                            True
                            
                        else:
                            print("[1] - Buscar Cliente pelo nome ")
                            print("[2] - Informar o CPF ")
                            opStatus_pedidos = int(input("OPÇÃO: "))
                            if opStatus_pedidos == 1:
                                buscar_dados = input("Buscar Cliente: ").title().strip()
                                exibir_dados = f"SELECT * FROM CLIENTES WHERE NOME LIKE '%{buscar_dados}%'"
                                pandas("CLIENTES")
                                cpf_cliente = " " 
                                while len(cpf_cliente) != 14:
                                        cpf_cliente = input("\nInforme o CPF do Cliente: ")
                                        
                                else:
                                    exibir_dados = f"SELECT * FROM STATUS_PEDIDO WHERE CPF_CLIENTE = '{cpf_cliente}'"
                                    pandas("STATUS_PEDIDO")
                                
                                    id_pedido = input("Informe o ID do PEDIDO: ")
                                
                            
                                
                            
                        
                                coluna_modificar = "STATUS_PEDIDO"                        
                                print('''                            [1] - Aguardando Pagamento
                                        [2] - Em Separação
                                        [3] - Pronto para transporte
                                        [4] - Em transporte
                                        [5] - Entregue''')
                                
                                
                                atualizar_pedido = 0
                                while atualizar_pedido != 1 or 2 or 3 or 4 or 5:
                                    atualizar_pedido = int(input("\nSelecione uma das opções acima: \n"))
                                    novo_atributo = ""
                                    
                                    if atualizar_pedido == 1:
                                        novo_atributo = ("Aguardando Pagamento")
                                        
                                    elif atualizar_pedido == 2:
                                        novo_atributo = ("Em Separação")
                                        
                                    elif atualizar_pedido == 3:
                                        novo_atributo = ("Pronto para transporte")
                                        
                                    elif atualizar_pedido == 4:
                                        novo_atributo = ("Em transporte")
                                        
                                    elif atualizar_pedido == 5:
                                        novo_atributo = ("Entregue")            
                                
                            
                                else:

                                    atualizar_statuspedidos = (f"UPDATE STATUS_PEDIDO SET {coluna_modificar} = '{novo_atributo}' WHERE (ID_PEDIDOS = {id_pedido} and CPF_CLIENTE = '{cpf_cliente}')")
                                    mycursor.execute(atualizar_statuspedidos)
                                    sucesso()
                                    
                                    time.sleep(2)
                                
                                    visualizar_pedido = input("\033[36mDeseja Visualizar este pedido? [S/N]\033[m ").strip().upper()[0]
                                    if visualizar_pedido in "N":
                                        True
                                            
                                    else:

                                        exibir_dados = f"SELECT * FROM STATUS_PEDIDO WHERE CPF_CLIENTE = '{cpf_cliente}'"
                                        pandas("STATUS_PEDIDO")
                                                                        
                                

            
                        if atualizar in "N":
                            print("Voltando ao Menu Anterior...")
                            time.sleep(2)
                      
                          
                      
                      
                      
        if perfilfuncionario == 7:
                print("\nVoltando ao Menu anterior... ")
                time.sleep(2)





if escolha == 4:
    print("\033[4;30;44m  FIM DO PROGRAMA!!   \033[m")                