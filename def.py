

#FUNÇÕES



def sucesso():
    print("\033[32;40mSUCESSO NA OPERAÇÃO!!\033[m")

def perfilAdm(int):
    print("\033[;36mPERFIL ADMINISTRADOR\033[m")
    time.sleep(2)
    print("\nSelecione uma opção: \n\
[1] - CLIENTES     || [2] PRODUTOS\n\
[3] - FUNCIONARIOS || [4] FORNECEDORES\n\
[5] - VOLTAR: ")
    
    
    
    
    
def cadastrarCliente(str):
    
    while True:
        cpf = input("CPF: ")
        while len(cpf) != 14: 
            print("\033[41m CPF INVÁLIDO!!\033[m")
            print("\033[41m O CPF PRECISA TER 11 DÍGITOS!!\033[m")
            cpf = (input("CPF: "))
        else:
            nome_cliente = (input("NOME: ")).strip().title()
            data_nasc = (input("DATA DE NASCIMENTO:  EX: [ANO-MES-DIA]")).strip().title()
            telefone = (input("TELEFONE: ")).strip()
            E_mail = (input("EMAIL: ")).strip()
            rua = (input("RUA: ")).strip().title()
            bairro = (input("BAIRRO: ")).strip().title()
            cidade = (input("CIDADE: ")).strip().title()
            cep = (input("CEP: ")).strip().title()
            estado = (input("ESTADO: [EX: PE] ")).strip().upper()
            inserir_cliente = f"INSERT INTO CLIENTES (CPF, NOME, DATA_NASC, TELEFONE, EMAIL, LOGRADOURO, BAIRRO, CIDADE, CEP, ESTADO)\
                            VALUES ('{cpf}', '{nome_cliente}', '{data_nasc}', '{telefone}', '{E_mail}', '{rua}', '{bairro}', '{cidade}', '{cep}', '{estado}')"
            mycursor.execute(inserir_cliente)
            mydb.commit()
            sucesso()
            print("\n\n\033[32mCLIENTE ADICIONADO COM SUCESSO!!!\033[m")
            cadastrar_cliente = input("\033[36mDeseja cadastrar um cliente? [S/N]\033[m").upper().strip()
    
    
    
    
    
    
def cadastrarFornecedor(str):
    
    
        cadastrar_fornecedor = input("Deseja cadastrar um fornecedor? [S/N]").upper().strip()[0]
        if cadastrar_fornecedor in "N":
            print("Voltando...")
            time.sleep(2)
            True
        else:
            cnpj = input("CNPJ: EX[00.000.000/0000-00] ")
            while len(cnpj) < 18: 
                print("\033[41m CNPJ INVÁLIDO!!\033[m")
                print("\033[41m O CNPJ PRECISA TER 14 DÍGITOS!!\033[m")
                cnpj = (input("CPF: EX[00.000.000/0000-00] "))
                            
                    
            else:
                nome_fornecedor = (input("NOME: ")).strip().title()
                telefone = (input("TELEFONE: ")).strip()
                E_mail = (input("EMAIL: ")).strip()
                rua = (input("RUA: ")).strip().title()
                bairro = (input("BAIRRO: ")).strip().title()
                cidade = (input("CIDADE: ")).strip().title()
                cep = (input("CEP: ")).strip().title()
                estado = (input("ESTADO: [EX: PE] ")).strip().upper()
                inserir_fornecedor = f"INSERT INTO FORNECEDORES (CNPJ, NOME, TELEFONE, EMAIL, LOGRADOURO, BAIRRO, CIDADE, CEP, ESTADO)\
                                            VALUES ('{cnpj}', '{nome_fornecedor }', '{telefone}', '{E_mail}', '{rua}', '{bairro}', '{cidade}', '{cep}', '{estado}')"
                mycursor.execute(inserir_fornecedor)
                mydb.commit()
                sucesso()
                print("\n\033[32mFORNECEDOR ADICIONADO COM SUCESSO!!!\033[m")


def verificarPorID(str):
    exibir_dados = f'''select pd.id_produto as ID_PRODUTO, pd.NOME as NOME_PRODUTO, pd.valor as VALOR, 
    pf.cnpj AS CNPJ from produtos pd  join produtos_fornecedores pf 
    where pd.id_produto = '{id_produto}' limit 1'''
    tabelas = pd.read_sql(exibir_dados, mydb)
    time.sleep(2)
    print("=" * 140)
    print(tabelas)
    print("=" * 140)
    
    verificarfornecedor = input("\033[32mDeseja visualizar o fornecedor desse produto? [S/N]\033[m ").upper().strip()

    if verificarfornecedor in "S":
        fornecedor = input("\033[32mInforme o CNPJ: \033[36m")
        
        exibir_dados = f'''SELECT pd.id_produto as ID_PRODUTO, pd.nome as NOME_PRODUTO,
        pd.valor as VALOR, f.cnpj as CNPJ, f.nome as NOME_FORNECEDOR, f.telefone as TELEFONE,
        f.email as EMAIL from produtos pd join fornecedores f where f.cnpj = '{fornecedor}'
        limit 1'''
        tabelas = pd.read_sql(exibir_dados, mydb)
        time.sleep(2)
        print("=" * 140)
        print(tabelas)
        print("=" * 140)
        
    else:
        True
        
        
        
        
def atualizar(str):
    
    nome_coluna = input("Qual coluna na tabela que você deseja modificar? ").upper().strip()
    novo_atributo = input("Atributo da nova coluna: ").title().strip()
    
    identificador = input("Localizador: ")
    
    
    exibir_dados = f"SELECT * FROM {nome_tabela} WHERE {nome_ColunaID} = '{identificador}'"
    tabelas = pd.read_sql(exibir_dados, mydb)
    print("=" * 140)
    print(tabelas)
    print("=" * 140)
    confirmar_atualização = input("Deseja atualizar os dados? [S/N] ").upper().strip()
   
    
    if confirmar_atualização in "S":
        atualizar = f"UPDATE {nome_tabela} SET {nome_coluna} = '{novo_atributo}' WHERE {nome_ColunaID} = '{identificador}'"
        mycursor.execute(atualizar)
        mydb.commit()
        
        print("Atualizando Dados...")
        time.sleep(2)
        sucesso()
        visualizar = input("\n\033[32mVocê deseja visualizar a linha novamente? [S/N]\033[36m ").upper().strip()
        
        
        if visualizar in "S":
            print("\n\033[32mDADOS ATUALIZADOS!!\n\033[36m")
            print("=" * 130)
            exibir_dados = f"SELECT * FROM {nome_tabela} WHERE {nome_ColunaID} = '{identificador}'"
            tabelas = pd.read_sql(exibir_dados, mydb)
            print("=" * 140)
            print(tabelas)
            print("=" * 140)

            
            
            
            
def subMenu(int):
    print('''\n Oque você deseja fazer? 
[1] - Visualizar || [2] - Modificar
[3] - Cadastrar  || [4] - Deletar")
[5] - VOLTAR AO MENU DE OPÇÕES 
''')
    
    
    
def visualizarEspecificos(str):
    selecionar_item = f"SELECT * FROM {nome_tabela} WHERE {coluna_identificador} = '{identificador}'"
    tabelas = pd.read_sql(selecionar_item, mydb)
    print("=" * 130)
    print(tabelas)
    print("=" * 130)    
    
    
    
                 
def cadastrarProdutos(str):    
    inserir_produto = f"INSERT INTO PRODUTOS (NOME, DESCRICAO, QNT_DISPONIVEL, VALOR)\
                        VALUES ('{nome_produto}', '{descricao}', '{qant}', '{valor}')"
    mycursor.execute(inserir_produto)
    mydb.commit()
    time.sleep(2)
    sucesso()
    

def deletar(str):
    nome_tabela =  str
    
    identificador = input("Localizador: ")
    exibir_dados = f"SELECT * FROM {nome_tabela} WHERE {coluna_identificador} = '{identificador}'"
    tabelas = pd.read_sql(exibir_dados, mydb)
    print("=" * 130)
    print(tabelas)
    print("=" * 130)
    print("\n")
    
    confirmar_delete = input("Deseja mesmo excluir o produto? [S/N] ").upper().strip()
    if confirmar_delete in "S":
        deletar = f"DELETE FROM {nome_tabela} WHERE {coluna_identificador} = '{identificador}'"
        mycursor.execute(deletar)
        time.sleep(2)
        sucesso()
    else:
        print("PRODUTO CONTINUA NA BASE DE DADOS!!\n")
        
        
        
        
        
def pandas(str):
    tabelas = pd.read_sql(exibir_dados, mydb)
    print("=" * 140)
    print(tabelas)
    print("=" * 140)
    
def exibirTabelas(str):
    print(f"\n\033[32mCarregando Dados de {str}...\033[m")
    time.sleep(2)
    selecionar_tabelas = f"SELECT * FROM {str}"
    tabelas = pd.read_sql(selecionar_tabelas, mydb)
    print("=" * 130)
    print(tabelas)
    print("=" * 130)
   
   
