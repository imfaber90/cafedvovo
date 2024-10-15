from setup import setup
from SQL import CRUD
from utils.db_conversao_campo_titulo import titulo
from utils.conversao_valor_monetario import convert_float_to_monetary, convert_monetary_to_float
from utils.datetime_converter import convert_from_datetime_to_string, convert_to_datetime_format
import pandas as pd
import streamlit as st

# Configura o título da página
setup('Gestão de Cadastros')

crud = CRUD()

clientes_pj = crud.join_all_users_information_by_type("p_juridica")
estrangeiros = crud.join_all_users_information_by_type("estrangeiro")
funcionarios = crud.join_all_users_information_by_type("funcionario")
fornecedores = crud.join_all_users_information_by_type("fornecedor")

# Aplica estilo global para fundo e cores de texto
st.markdown("""
    <style>
    h1, h2, h3 {
        color: #8B4513 !important; /* Títulos e subtítulos marrom escuro */
    }
    
    /* Estilizando os botões do Streamlit */
    div.stButton > button {
        color: white;
        background-color: brown; /* Cor de fundo */
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    div.stFormSubmitButton > button {
        color: white; /* Cor do texto */
        background-color: brown; /* Cor de fundo */
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
                                
    </style>
""", unsafe_allow_html=True)


# Função para exibir as tabelas com botões de ação do sidebar
# por padrão "todos" vem selecionado, entãos erá mostrado todos os cadastros
def exibir_com_acoes(df, categoria):
    for index, row in df.iterrows():
        cols = st.columns(3)
        for i, col in enumerate(df.columns):
            
            if col == 'data_nascimento': # converte de data americana pra brasileira 
                date_american_format = row[col]
                data_brazilian_format = convert_from_datetime_to_string(date_american_format)
                row[col] = data_brazilian_format
            if col == 'data_cadastro': # converte de data americana pra brasileira 
                date_american_format = row[col]
                data_brazilian_format = convert_from_datetime_to_string(date_american_format)
                row[col] = data_brazilian_format
            
            if i < 6:
                cols[0].write(f"**{titulo(col)}:** {row[col]}")
            elif i < 12:
                cols[1].write(f"**{titulo(col)}:** {row[col]}")
            else:
                cols[2].write(f"**{titulo(col)}:** {row[col]}")

        button_cols = st.columns(12, gap="small")

        if 'pessoa_id' in row.index:
            # Botão Atualizar
            if button_cols[0].button(f"Atualizar", key=f"update_{categoria}_{index}"):
                st.session_state[f"edit_mode_{index}"] = True  # Armazenando estado no session_state

            # Checa se o modo de edição foi ativado
            if st.session_state.get(f"edit_mode_{index}", False):
                dados_gerais_usuario = crud.read_all_user_data(row['pessoa_id'])
                tipo_usuario = dados_gerais_usuario[13]
                print(tipo_usuario)
                
                dados_especificos_tipo_usuario = crud.join_by_type_id(tipo_usuario, row['pessoa_id'])

                #st.success(dados_especificos_tipo_usuario)
                
                # Expandir o formulário para editar os dados
                with st.expander("Formulário de Edição", expanded=True):
                    if dados_especificos_tipo_usuario:
                        d_frame = pd.DataFrame([dados_especificos_tipo_usuario])
                        novos_dados = {}

                        # Início do formulário
                        with st.form(key=f"edit_form_{categoria}_{index}"):
                            for _, edit_row in d_frame.iterrows():
                                cols = st.columns(3)
                                for i, col in enumerate(df.columns):
                                    nome_campo = titulo(col)    
                                    
                                    if col == 'data_nascimento': # converte de data americana pra brasileira 
                                        date_american_format = edit_row[i]
                                        data_brazilian_format = convert_from_datetime_to_string(date_american_format)
                                        edit_row[i] = data_brazilian_format
                                    
                                    if i < 6:
                                        if col == 'pessoa_id': # Essa condição é pra tornar o campo pessoa_id não editável
                                            novo_valor = cols[0].text_input(f"**Campo {i + 1}:**", value=edit_row[i], key=f"{categoria}_{index}_edit_{i}", disabled=True)
                                        else:
                                            novo_valor = cols[0].text_input(f"**Campo {i + 1}:**", value=edit_row[i], key=f"{categoria}_{index}_edit_{i}")
                                    elif i < 12:
                                        novo_valor = cols[1].text_input(f"**Campo {i + 1}:**", value=edit_row[i], key=f"{categoria}_{index}_edit_{i}")
                                    else:  
                                        if col == "salario": # Isso aqui é pra mudar o valor de float armazenado no banco de dados assim 0000.00 para moeda BR com R$ 0.000,00 para visualização na página
                                            not_monetary_value = edit_row[i]
                                            monetary_value = convert_float_to_monetary(not_monetary_value)
                                            novo_valor = cols[2].text_input(f"**Campo {i + 1}:**", value=monetary_value, key=f"{categoria}_{index}_edit_{i}")
                                        elif col == 'data_cadastro': # Essa condição é pra tornar o campo data_cadastro não editável
                                            novo_valor = cols[2].text_input(f"**Campo {i + 1}:**", value=edit_row[i], key=f"{categoria}_{index}_edit_{i}", disabled=True)
                                        else:
                                            novo_valor = cols[2].text_input(f"**Campo {i + 1}:**", value=edit_row[i], key=f"{categoria}_{index}_edit_{i}")
                                    novos_dados[nome_campo] = novo_valor

                            # Botão dentro do form que não causa reload
                            submit_button = st.form_submit_button("Salvar")

                            if submit_button:
                                if 'Salário' in novos_dados: # desconverte de valor moeda para valor float pra armazenar no banco de dados
                                    monetary_value = novos_dados['Salário']
                                    not_monetary_value = convert_monetary_to_float(monetary_value)
                                    novos_dados['Salário'] = not_monetary_value
                                    
                                if 'Data de nascimento' in novos_dados: # converte de data brasileira para americana (p/ armazenar no DB)
                                    date_brazilian_format = novos_dados['Data de nascimento']
                                    print(date_brazilian_format)
                                    data_american_format = convert_to_datetime_format(date_brazilian_format)
                                    novos_dados['Data de nascimento'] = data_american_format
                                    print(data_american_format)
                                
                                try:
                                    crud.update_user_information(row['pessoa_id'], novos_dados)
                                    st.success("Atualizado com sucesso!")
                                    st.session_state[f"edit_mode_{index}"] = False  # Reseta o modo de edição
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Erro ao atualizar informações: {e}")

            # Botão Remover
            if button_cols[1].button(f"Remover", key=f"remove_{categoria}_{row['pessoa_id']}"):
                st.warning(f"Remover {row['nome']}")
                crud.delete("pessoa", "pessoa_id", row['pessoa_id'])
                st.rerun()
        else:
            st.warning("Coluna 'pessoa_id' não encontrada na linha.")

        st.write("---")


# Sidebar com filtros
st.sidebar.header("Filtros")
tipo_cadastro = st.sidebar.selectbox("Selecionar Tipo de Cadastro", ["Todos", "Clientes PJ", "Estrangeiros", "Funcionários", "Fornecedores"])

# Exibição condicional de acordo com o filtro
if tipo_cadastro == "Todos":
    st.subheader("Clientes - Pessoas Jurídicas")
    exibir_com_acoes(clientes_pj, 'Clientes PJ')

    st.subheader("Estrangeiros")
    exibir_com_acoes(estrangeiros, 'Estrangeiros')

    st.subheader("Funcionários")
    exibir_com_acoes(funcionarios, 'Funcionários')
    
    st.subheader("Fornecedores")
    exibir_com_acoes(fornecedores, 'Fornecedores')

elif tipo_cadastro == "Clientes PJ":
    st.subheader("Clientes - Pessoas Jurídicas")
    exibir_com_acoes(clientes_pj, 'Clientes PJ')

elif tipo_cadastro == "Estrangeiros":
    st.subheader("Estrangeiros")
    exibir_com_acoes(estrangeiros, 'Estrangeiros')

elif tipo_cadastro == "Funcionários":
    st.subheader("Funcionários")
    exibir_com_acoes(funcionarios, 'Funcionários')
    
elif tipo_cadastro == "Fornecedores":
    st.subheader("Fornecedores")
    exibir_com_acoes(fornecedores, 'Fornecedores')

# Botão de ação para adicionar novos cadastros
st.sidebar.markdown("## Ações")

