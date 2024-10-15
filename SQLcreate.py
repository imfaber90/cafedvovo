from databases import Database as db
import asyncio
# Inicializa a conexão com o banco de dados usando SQLite com suporte a async
database = db('sqlite+aiosqlite:///cafevovo.db')

async def criar():
    # Conecta ao banco de dados de forma assíncrona
    await database.connect()
    
    #*************************************
    # TABELA CADASTROS DE PESSOAS .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query)
    #Codigo para Adicionar Foreigh Key, após o último campo iserir o codigo
    # FOREIGN KEY(idpessoa) REFgiERENCES CADASTROS_DE_PESSOAS(idpessoa)

    query = """
        CREATE TABLE IF NOT EXISTS pessoa (
        pessoa_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        data_nascimento DATE NOT NULL,
        data_cadastro DATE NOT NULL
    );
    """
    await database.execute(query=query)

    
    #*************************************
    # TABELA TELEFONE . 
    query = """
        CREATE TABLE IF NOT EXISTS telefone (
        telefone_id INTEGER PRIMARY KEY,
        telefone TEXT NOT NULL,
        tipo TEXT,
        id_pessoa INTEGER NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );
    """  
    await database.execute(query=query)

    
    #*************************************
    # TABELA ENDERECOS .        
    query = """
        CREATE TABLE IF NOT EXISTS endereco (
        endereco_id INTEGER PRIMARY KEY,
        pais TEXT NOT NULL,
        cep TEXT NOT NULL,
        estado TEXT NOT NULL,
        cidade TEXT NOT NULL,
        bairro TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT NOT NULL,
        tipo TEXT,
        id_pessoa INTEGER NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

    """
    await database.execute(query=query)


    #*************************************
    # TABELA FUNCIONARIOS .
    query = """
        CREATE TABLE IF NOT EXISTS funcionario (
        pessoa_id INTEGER PRIMARY KEY,
        cpf TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL,
        matricula TEXT NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );

    """
    await database.execute(query=query)
    
    
    #*************************************
    # TABELA FISICA .
    query = """
        CREATE TABLE IF NOT EXISTS p_fisica (
        id_pessoa INTEGER PRIMARY KEY,
        cpf_rg TEXT NOT NULL UNIQUE,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );
    """
    await database.execute(query=query)


    #*************************************
    # TABELA JURIDICA . 
    query = """
        CREATE TABLE IF NOT EXISTS p_juridica (
        id_pessoa INTEGER PRIMARY KEY,
        cnpj TEXT NOT NULL UNIQUE,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );
    """
    await database.execute(query=query)
    

    #*************************************
    # TABELA ESTRANGEIRO . 
    query = """
        CREATE TABLE IF NOT EXISTS estrangeiro (
        id_pessoa INTEGER PRIMARY KEY,
        passaporte TEXT NOT NULL UNIQUE,
        descricao TEXT,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );
    """
    await database.execute(query=query)
     

    #*************************************
    # TABELA Fornecedor .
    query = """
        CREATE TABLE IF NOT EXISTS fornecedor (
        id_pessoa INTEGER PRIMARY KEY,
        nome_empresa TEXT NOT NULL,
        documento TEXT NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES pessoa (pessoa_id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    );
    """
    await database.execute(query=query)


asyncio.run(criar())
