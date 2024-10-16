import sqlite3
import streamlit as st
import pandas as pd


class CRUD:
    def __init__(self):
        # Conecta ao banco de dados SQLite
        self.conn = sqlite3.connect('cafevovo.db')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON') #Se não usar esse comando o ON DELETE CASCADE não funcionará corretamente.
        
    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def insert(self, table, **kwargs):
        '''
        Insere um novo registro na tabela especificada.
        '''
        match table:
            case 'funcionario':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO funcionario (id_pessoa, cpf, matricula, cargo, salario) VALUES (?, ?, ?, ?, ?);", (last_id, kwargs.get('cpf'), kwargs.get('matricula'), kwargs.get('cargo'), kwargs.get('salario')))
                    self.conn.commit()
                    st.success("Funcionário cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass  
            
            case 'estrangeiro':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO estrangeiro (id_pessoa, passaporte, descricao) VALUES (?, ?, ?);", (last_id, kwargs.get('doc_inter'), kwargs.get('descricao_es')))
                    self.conn.commit()
                    st.success("Pessoa estrangeira cadastrada com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass 
                    
            case 'p_juridica':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO p_juridica (id_pessoa, cnpj, descricao) VALUES (?, ?, ?);", (last_id, kwargs.get('cnpj'), kwargs.get('descricao')))
                    self.conn.commit()
                    st.success("Pessoa jurídica cadastrada com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass 
                
            case 'fornecedor':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO fornecedor (id_pessoa, nome_empresa, documento) VALUES (?, ?, ?);", (last_id, kwargs.get('nome_empresa'), kwargs.get('cnpj_fornecedor')))
                    self.conn.commit()
                    st.success("Fornecedor cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass 
                
            case 'produto':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO produto (nome_produto, categoria, margem_lucro) VALUES (?, ?, ?);", (kwargs.get('nome_produto'), kwargs.get('categoria'), kwargs.get('margem_lucro')))
                    self.conn.commit() 
                    st.success("Produto cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass 
                
            case 'item_insumo':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO item_insumo (nome_insumo, quantidade, custo) VALUES (?, ?, ?);", (kwargs.get('nome_insumo'), kwargs.get('quantidade'), kwargs.get('custo')))
                    self.conn.commit() 
                    st.success("Insumo cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao cadastrar: {e}")
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                finally:
                    pass 
                    
            case _:
                print("Tabela não encontrada")
                return None

    
    def read_all_user_data(self, user_id):
        query = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            CASE 
                WHEN funcionario.id_pessoa IS NOT NULL THEN 'funcionario'
                WHEN estrangeiro.id_pessoa IS NOT NULL THEN 'estrangeiro'
                WHEN p_juridica.id_pessoa IS NOT NULL THEN 'p_juridica'
                WHEN fornecedor.id_pessoa IS NOT NULL THEN 'fornecedor'
                ELSE 'nao_especializado'
            END AS tipo_usuario,
            funcionario.cpf,
            funcionario.matricula,
            funcionario.cargo,
            funcionario.salario,
            estrangeiro.passaporte,
            estrangeiro.descricao,
            fornecedor.nome_empresa,
            fornecedor.documento,
            p_juridica.cnpj,
            p_juridica.descricao AS descricao_pj
        FROM 
            pessoa
        LEFT JOIN 
            funcionario ON pessoa.pessoa_id = funcionario.id_pessoa
        LEFT JOIN 
            estrangeiro ON pessoa.pessoa_id = estrangeiro.id_pessoa
        LEFT JOIN 
            p_juridica ON pessoa.pessoa_id = p_juridica.id_pessoa
        LEFT JOIN 
            fornecedor ON pessoa.pessoa_id = fornecedor.id_pessoa
        LEFT JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        LEFT JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa
        WHERE 
            pessoa.pessoa_id = ?;

        """
        try:
            self.cursor.execute(query, (user_id,))
            resultado = self.cursor.fetchone()  # Use fetchone se você espera apenas um resultado
            return resultado
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            pass
    
    
    def join_by_type_id(self, tipo, id):
        
        query_funcionario = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            funcionario.cpf,
            funcionario.matricula,
            funcionario.cargo,
            funcionario.salario,
            pessoa.data_cadastro
        FROM 
            pessoa
        JOIN 
            funcionario ON pessoa.pessoa_id = funcionario.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa
        WHERE 
            pessoa.pessoa_id = ?;
        """

        query_estrangeiro = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            estrangeiro.passaporte,
            estrangeiro.descricao,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            estrangeiro ON pessoa.pessoa_id = estrangeiro.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa
        WHERE 
            pessoa.pessoa_id = ?;
        """

        query_p_juridica = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            p_juridica.cnpj,
            p_juridica.descricao,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            p_juridica ON pessoa.pessoa_id = p_juridica.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa
        WHERE 
            pessoa.pessoa_id = ?;
        """
        
        query_p_juridica_fornecedor = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            fornecedor.nome_empresa,
            fornecedor.documento,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            fornecedor ON pessoa.pessoa_id = fornecedor.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa
        WHERE 
            pessoa.pessoa_id = ?;
        """
        
        query = ""
        if tipo == 'funcionario':
            query = query_funcionario
        elif tipo == 'estrangeiro':
            query = query_estrangeiro
        elif tipo == 'p_juridica':
            query = query_p_juridica
        elif tipo == 'fornecedor':
            query = query_p_juridica_fornecedor
        
        self.cursor.execute(query, (id,))  
        resultado = self.cursor.fetchone()
        return resultado
    
    def join_all_users_information_by_type(self, tipo):
        # Carrega os dados das tabelas
        query_funcionario = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            funcionario.cpf,
            funcionario.matricula,
            funcionario.cargo,
            funcionario.salario,
            pessoa.data_cadastro
        FROM 
            pessoa
        JOIN 
            funcionario ON pessoa.pessoa_id = funcionario.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa;
        """

        query_estrangeiro = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            estrangeiro.passaporte,
            estrangeiro.descricao,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            estrangeiro ON pessoa.pessoa_id = estrangeiro.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa;
        """

        query_p_juridica = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            p_juridica.cnpj,
            p_juridica.descricao,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            p_juridica ON pessoa.pessoa_id = p_juridica.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa;
        """
        
        
        query_p_juridica_fornecedor = """
        SELECT 
            pessoa.pessoa_id,
            pessoa.nome,
            pessoa.email,
            telefone.telefone,
            pessoa.data_nascimento,
            endereco.pais,
            endereco.cep,
            endereco.estado,
            endereco.cidade,
            endereco.bairro,
            endereco.rua,
            endereco.numero,
            endereco.complemento,
            fornecedor.nome_empresa,
            fornecedor.documento,
            pessoa.data_cadastro

        FROM 
            pessoa
        JOIN 
            fornecedor ON pessoa.pessoa_id = fornecedor.id_pessoa
        JOIN 
            telefone ON pessoa.pessoa_id = telefone.id_pessoa
        JOIN 
            endereco ON pessoa.pessoa_id = endereco.id_pessoa;
        """
        
        
        query = ""
        if tipo == 'funcionario':
            query = query_funcionario
        elif tipo == 'estrangeiro':
            query = query_estrangeiro
        elif tipo == 'p_juridica':
            query = query_p_juridica
        elif tipo == 'fornecedor':
            query = query_p_juridica_fornecedor
        
        return pd.read_sql_query(query, self.conn)
    
    def read(self, table, condition=None, **kwargs):
        '''
        Busca registros na tabela especificada.
        
        Parâmetros:
        - table: Nome da tabela a ser consultada.
        - condition: Condição opcional para filtrar os resultados (ex: "id = ?").
        - kwargs: Colunas específicas a serem buscadas, padrão é todas (*).
        
        Exemplos de uso:
        
        1. Para buscar um produto específico pelo ID:
        resultado = self.read('produto', condition="id = ?", columns=['nome', 'quantidade', 'preco'], params=[1])
        
        2. Para buscar todos os produtos, sem condição:
        resultado = self.read('produto', columns=['nome', 'quantidade', 'preco'])
        
        3. Para buscar todos os produtos, sem condição e selecionando todas as colunas:
        resultado = self.read('produto', all=True)
        '''
        
        self.conn = sqlite3.connect('cafevovo.db')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON')
        
        # Verificando se "all" está no kwargs
        if kwargs.get('all', False):
            campos = '*'
        else:
            campos = ', '.join(kwargs.get('columns', []))  # Supondo que as colunas sejam passadas em 'columns'

        # Montando a query
        query = f"SELECT {campos} FROM {table}"
        if condition:
            query += f" WHERE {condition}"

        # Executando a consulta
        self.cursor.execute(query, kwargs.get('params', []))  # Passa os parâmetros se houver
        resultado = self.cursor.fetchall()
        
        return resultado

        
    def update_user_information(self, pessoa_id, novos_dados):
        print(novos_dados)
        # Atualizando a tabela pessoa
        update_pessoa = f"""
        UPDATE pessoa
        SET nome = '{novos_dados.get("Nome")}',
            email = '{novos_dados.get("E-mail")}',
            data_nascimento = '{novos_dados.get("Data de nascimento")}'
        WHERE pessoa_id = {pessoa_id};
        """

        # Atualizando a tabela telefone
        update_telefone = f"""
        UPDATE telefone
        SET telefone = '{novos_dados.get("Telefone")}'
        WHERE id_pessoa = {pessoa_id};
        """

        # Atualizando a tabela endereco
        update_endereco = f"""
        UPDATE endereco
        SET pais = '{novos_dados.get("País")}',
            cep = '{novos_dados.get("CEP")}',
            estado = '{novos_dados.get("UF")}',
            cidade = '{novos_dados.get("Cidade")}',
            bairro = '{novos_dados.get("Bairro")}',
            rua = '{novos_dados.get("Logradouro")}',
            numero = '{novos_dados.get("Nº")}',
            complemento = '{novos_dados.get("Complemento")}'
        WHERE id_pessoa = {pessoa_id};
        """

         # Atualizando a tabela funcionario, estrangeiro ou p_juridica dependendo do caso
        if novos_dados.get("CPF"):  # Exemplo: se for um funcionário
            update_funcionario = f"""
            UPDATE funcionario
            SET cpf = '{novos_dados.get("CPF")}',
                matricula = '{novos_dados.get("Matrícula")}',
                cargo = '{novos_dados.get("Profissão")}',
                salario = {novos_dados.get("Salário")}
            WHERE id_pessoa = {pessoa_id};
            """
            try:
                self.cursor.execute(update_funcionario)
            except Exception as e:
                st.error(f"Ocorreu um erro ao atualizar funcionário: {e}")
            finally:
                pass

        elif novos_dados.get("CNPJ"):  # Exemplo: se for uma pessoa jurídica
            update_pjuridica = f"""
            UPDATE p_juridica
            SET cnpj = '{novos_dados.get("CNPJ")}',
                descricao = '{novos_dados.get("Descrição")}'
            WHERE id_pessoa = {pessoa_id};
            """
            try:
                self.cursor.execute(update_pjuridica)
            except Exception as e:
                st.error(f"Ocorreu um erro ao atualizar Pessoa jurídica: {e}")
            finally:
                pass
            
        elif novos_dados.get("Passaporte"):  # Exemplo: se for uma pessoa jurídica
            update_pjuridica = f"""
            UPDATE estrangeiro
            SET passaporte = '{novos_dados.get("Passaporte")}',
                descricao = '{novos_dados.get("Descrição")}'
            WHERE id_pessoa = {pessoa_id};
            """
            try:
                self.cursor.execute(update_pjuridica)
            except Exception as e:
                st.error(f"Ocorreu um erro ao atualizar pessoa estrangeira: {e}")
            finally:
                pass


        # Executando as atualizações
        try:
            self.cursor.execute(update_pessoa)
            self.cursor.execute(update_telefone)
            self.cursor.execute(update_endereco)
        except Exception as e:
                st.error(f"Ocorreu um erro ao atualizar pessoa, telefone e endereço: {e}")
        finally:
            pass

        # Confirma as mudanças
        
        try:
            self.conn.commit()
            st.success("Informações atualizadas com sucesso!")
        except Exception as e:
                st.error(f"Ocorreu um erro na hora de confirmar as mudanças: {e}")
        finally:
            pass
        
    def delete(self, table, column, id):
        try:
            query = f"DELETE FROM {table} WHERE {column} = {id};"
            self.cursor.execute(query)
            self.conn.commit()
            st.success("Removido com sucesso!")
        except Exception as e:
            st.error(f"Ocorreu um erro ao remover: {e}")
        finally:
            pass 
    
    def close(self):
        # Fecha a conexão com o banco de dados
        self.conn.close()
    