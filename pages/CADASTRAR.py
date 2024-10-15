import streamlit as st
from SQL import CRUD  # Importando as operações CRUD do módulo SQL
from setup import setup
from utils.validacao_form import verifica_campos
from utils.datetime_converter import convert_to_datetime_format
from random import randrange
import requests
from datetime import datetime


# Estilo pro botão ficar com o texto branco:
st.markdown("""
    <style> 
    /* Estilizando os botões do Streamlit */
    div.stButton > button {
        color: white;
    }                              
    </style>
""", unsafe_allow_html=True)


setup('CADASTRO')

# Instanciando a classe CRUD
crud = CRUD()

data_e_hora_atual = datetime.now()
data_atual = data_e_hora_atual.date()
data_formatada = data_atual.strftime('%Y-%m-%d')

# Função para gerar ID de lote
def insertInto():
    loteid = randrange(1,200000000)
    return loteid

# Função para buscar o endereço via API
def buscar_endereco(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        response.raise_for_status()  # Levanta um erro para códigos de status de erro
        dados = response.json()
        return dados
    except Exception as e:
        st.error("Erro ao buscar endereço. Verifique o CEP e tente novamente.")
        return None

col1, col2 = st.columns([0.8, 3])

# Coluna para os títulos dos campos
with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>EMAIL: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>TELEFONE: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NASCIMENTO: </h2>", unsafe_allow_html=True)
    st.write("#")
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PAÍS: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CEP: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>ESTADO: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CIDADE: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>BAIRRO: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>LOGRADOURO: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NÚMERO: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>COMPLEMENTO: </h2>", unsafe_allow_html=True)
    st.write("#")
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PESSOA: </h2>", unsafe_allow_html=True)

# Coluna para os campos de entrada
with col2:
    nome = st.text_input('', key='name')
    email = st.text_input('', key='email')
    tel = st.text_input('', key='tel')
    nascimento = st.text_input('', key='nasc')
    st.write("#")
    pais = st.text_input('', key='pais')

    # Colunas para o campo de CEP e botão de busca
    col_cep, col_btn = st.columns([3, 1])

    with col_cep:
        cep = st.text_input('', key='cep')

    with col_btn:
        st.markdown(f"<div style= 'padding-top: 27px;'></div>", unsafe_allow_html=True)
        if st.button('Buscar Endereço'):
            if cep:
                dados_endereco = buscar_endereco(cep)
                if dados_endereco and 'erro' not in dados_endereco:
                    # Armazenar os dados do CEP no st.session_state
                    st.session_state['estado'] = dados_endereco.get('uf', '')
                    st.session_state['cidade'] = dados_endereco.get('localidade', '')
                    st.session_state['bairro'] = dados_endereco.get('bairro', '')
                    st.session_state['logradouro'] = dados_endereco.get('logradouro', '')
                    st.session_state['complemento'] = dados_endereco.get('complemento', '')

    # Recuperar valores salvos no st.session_state (se existirem)
    estado = st.text_input('Estado', value=st.session_state.get('estado', ''))
    cidade = st.text_input('Cidade', value=st.session_state.get('cidade', ''))
    bairro = st.text_input('Bairro', value=st.session_state.get('bairro', ''))
    logradouro = st.text_input('Logradouro', value=st.session_state.get('logradouro', ''))
    numero = st.text_input('', key='numero')
    complemento = st.text_input('Complemento', value=st.session_state.get('complemento', ''))
    st.write("#")

    # Selectbox para tipo de pessoa
    select = st.selectbox('', options = ['Jurídica','Física'], key='selec1',)

# Lógica para "Fisica" e "Jurídica"
if select == 'Física':
    with col1:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CPF: </h2>", unsafe_allow_html=True)
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>TIPO: </h2>", unsafe_allow_html=True)
    with col2:
        cpf = st.text_input('', key='cpf')
        select2 = st.selectbox('', ['Funcionário', 'Estrangeiro'], key='selec2')

    # Lógica para tipo de funcionário
    if select2 == 'Funcionário':
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>MATRÍCULA: </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CARGO: </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>SALÁRIO: </h2>", unsafe_allow_html=True)
        with col2:
            matricula = st.text_input('', key='matr')
            cargo = st.text_input('', key='carg')
            salario = st.text_input('', key='sala')
            if st.button('CADASTRAR', key='cadfun'):
                campos_ok, formatted_salary, mensagem = verifica_campos(nome, email, tel, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, select=select, cpf=cpf, tipo=select2, matricula=matricula, cargo=cargo, salario=salario)
                if not campos_ok:
                    st.warning(mensagem)
                else:
                    data_nascimento_formatada =  convert_to_datetime_format(nascimento)
                    crud.insert('funcionario', nome=nome, email=email, tel=tel, nascimento=data_nascimento_formatada, data_cadastro=data_formatada, pais=pais, cep=cep, estado=estado, cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, complemento=complemento, cpf=cpf, matricula=matricula, cargo=cargo, salario=formatted_salary)
                     

    elif select2 == 'Estrangeiro':
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DOCUMENTO INTERNACIONAL:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DESCRIÇÃO: </h2>", unsafe_allow_html=True)
        with col2:
            doc_inter = st.text_input('', key='cnpj')
            descricao_es = st.text_input('', key='desc')
            if st.button('CADASTRAR', key='cadest'):
                campos_ok, formatted_salary, mensagem = verifica_campos(nome, email, tel, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, tipo = select2, doc_inter = doc_inter, descricao_es = descricao_es)
                if not campos_ok:
                    st.warning(mensagem)
                else:
                    data_nascimento_formatada =  convert_to_datetime_format(nascimento)
                    crud.insert('estrangeiro', nome=nome, email=email, tel=tel, nascimento=data_nascimento_formatada, data_cadastro=data_formatada, pais=pais, cep=cep, estado=estado, cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, complemento=complemento, doc_inter=doc_inter, descricao_es=descricao_es)
                    
elif select == 'Jurídica':
    with col1:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>TIPO: </h2>", unsafe_allow_html=True)
    with col2:
        select3 = st.selectbox('', ['Cliente PJ', 'Fornecedor'], key='selec2')
    if select3 == 'Cliente PJ':    
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CNPJ: </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DESCRIÇÃO: </h2>", unsafe_allow_html=True)
        with col2:
            cnpj = st.text_input('', key='cnpj')
            descricao = st.text_input('', key='desc')
            if st.button('CADASTRAR', key='cadjur'):
                campos_ok, formatted_salary, mensagem = verifica_campos(nome, email, tel, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, tipo=select3, cnpj=cnpj, descricao=descricao)
                if not campos_ok:
                    st.warning(mensagem)
                else:
                    data_nascimento_formatada =  convert_to_datetime_format(nascimento)
                    crud.insert('p_juridica', nome=nome, email=email, tel=tel, nascimento=data_nascimento_formatada, data_cadastro=data_formatada, pais=pais, cep=cep, estado=estado, cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, complemento=complemento, cnpj=cnpj, descricao=descricao)
    if select3 == 'Fornecedor':    
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>EMPRESA: </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CNPJ: </h2>", unsafe_allow_html=True)
        with col2:
            nome_empresa = st.text_input('', key='nome_emp')
            cnpj_fornecedor = st.text_input('', key='cnpj_forn')
            if st.button('CADASTRAR', key='cadfor'):
                campos_ok, formatted_salary, mensagem = verifica_campos(nome, email, tel, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, tipo=select3, nome_empresa=nome_empresa, cnpj_fornecedor=cnpj_fornecedor)
                if not campos_ok:
                    st.warning(mensagem)
                else:
                    data_nascimento_formatada = convert_to_datetime_format(nascimento)
                    crud.insert('fornecedor', nome=nome, email=email, tel=tel, nascimento=data_nascimento_formatada, data_cadastro=data_formatada, pais=pais, cep=cep, estado=estado, cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, complemento=complemento, nome_empresa=nome_empresa, cnpj_fornecedor=cnpj_fornecedor)
                    
                    
# to continue