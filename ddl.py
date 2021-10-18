

mycursor.execute("CREATE DATABASE Infortech")



mycursor.execute = ("CREATE TABLE CLIENTES(\
                 ID int not null auto_increment,\
                 CPF varchar(32) not null,\
                 NOME varchar(64) not null,\
                 DATA_NASC date not null,\
                 TELEFONE varchar(32) not null,\
                 EMAIL varchar(64) not null,\
                 LOGRADOURO varchar(64) not null,\
                 BAIRRO varchar(32) not null,\
                 CIDADE varchar(64) not null,\
                 CEP varchar(32) not null,\
                 COMPLEMENTO varchar(64),\
                 ESTADO varchar(32) not null,\
                 primary key(ID, CPF))")


mycursor.execute = ("CREATE TABLE FUNCIONARIOS(\
                 ID int not null auto_increment,\
                 CPF varchar(32) not null,\
                 NOME varchar(64) not null,\
                 DATA_NASC date not null,\
                 CARGO varchar(64) not null,\
                 LOGRADOURO varchar(64) not null,\
                 BAIRRO varchar(64) not null,\
                 CIDADE varchar(64) not null,\
                 CEP varchar(32) not null,\
                 COMPLEMENTO varchar(64),\
                 ESTADO varchar(32) not null,\
                 primary key(ID, CPF))")


mycursor.execute("CREATE TABLE FORNECEDORES(\
                    CNPJ varchar(32) unique primary key,\
                    NOME varchar(64) not null,\
                    TELEFONE varchar(32) not null,\
                    EMAIL varchar(64) not null,\
                    LOGRADOURO varchar(64) not null,\
                    BAIRRO varchar(64) not null,\
                    CIDADE varchar(64) not null,\
                    CEP varchar(32) not null,\
                    ESTADO varchar(32) not null\
                    )")



mycursor.execute("CREATE TABLE PEDIDOS(\
                    ID int not null primary key,\
                    ID_FUNCIONARIO int not null,\
                    CPF_CLIENTE varchar(16) not null,\
                    NOME varchar(32) not null,\
                    ID_PRODUTO int not null,\
                    DATA_PEDIDO date not null,\
                    HORARIO time,\
                    QUANTIDADE int not null,\
                    VALOR float not null,\
                    foreign key (ID_FUNCIONARIO) references FUNCIONARIOS(ID),\
                    foreign key (CPF_CLIENTE) references CLIENTE(CPF),\
                    foreign key (ID_PRODUTO) references PRODUTO(ID_PRODUTO))")
'''

mycursor.execute("""CREATE TABLE PRODUTOS(
                    ID_PRODUTO int auto_increment primary key not null,
                    NOME varchar(32) not null,
                    DESCRICAO varchar(128) not null,
                    QNT_DISPONIVEL int not null,
                    VALOR float not null)""")


mycursor.execute("""CREATE TABLE STATUS_PEDIDO(
                    ID int primary key auto_increment not null,
                    ID_PEDIDOS int not null,
                    CPF_CLIENTE varchar(32) not null,
                    STATUS_PEDIDO varchar(128) not null,
                    foreign key (ID_PEDIDOS) references PEDIDOS(ID),
                    foreign key (CPF_CLIENTE) references CLIENTE(CPF))""")



mycursor.execute("""CREATE TABLE PRODUTOS_FORNECEDORES(
                    ID int not null auto_increment primary key not null,
                    CNPJ varchar(32) not null,
                    ID_PRODUTO int not null)""")