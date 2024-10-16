import streamlit as st
from setup import setup
from random import randrange
from SQL import CRUD

setup('CADASTRAR PRODUTO')

st.markdown("""
            <style>
                .stSuccess { background-color: green; border-radius: 10px; }
                .stWarning { background-color: green; border-radius: 10px; }
                .stError { background-color: green; border-radius: 10px; }
                .stAlert { background-color: green; border-radius: 10px; }
            </style>
            """, unsafe_allow_html=True)

crud = CRUD()

def insertInto():
    loteid = randrange(1,200000000)
    return loteid

if 'num_fields' not in st.session_state:
    st.session_state.num_fields = 1

def add_new_field():
    st.session_state.num_fields += 1

def clear_added_fields():
    st.session_state.num_fields = 1

col1, col2, col3, col4 = st.columns([1.4,2,0.5,0.5])
with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME DO PRODUTO </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CATEGORIA </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>MARGEM DE LUCRO </h2>",unsafe_allow_html=True) 
    st.write('#')
    st.markdown(f"<h1 style= 'color:Black;'>CADASTRAR INSUMO</h1>",unsafe_allow_html=True)


with col2:
    nomeprod = st.text_input('',key='nameprod')
    categoria = st.text_input('',key='categ')
    m_lucro = st.text_input('',key='m_lucro')
    if st.button('ADICIONAR'):
        crud.insert("produto", nome_produto=nomeprod, categoria=categoria, margem_lucro=m_lucro)
    st.write('#')
with col3:
    st.write('#')
    st.write('#')
    st.write('#')
with col4:
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')


col1, col2, col3, col4 = st.columns([1.4,2,0.5,0.5])
with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME DO INSUMO </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>QUANTIDADE </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CUSTO </h2>",unsafe_allow_html=True)
    st.write('#')

with col2:
    nome_insumo = st.text_input('',key='w')
    qntd_insumo = st.text_input('',key='rr')
    preco_custo = st.text_input('',key='rt')
    if st.button('ADICIONAR', key='fdf'):
        crud.insert("item_insumo", nome_insumo=nome_insumo, quantidade=qntd_insumo, custo=preco_custo)
with col3:
    st.write('#')
    
    
with col4:
    st.write('#')
    

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h1 style= 'color:Black;'>PRODUTO = INSUMO x QNTD</h1>",unsafe_allow_html=True)

for i in range(st.session_state.num_fields):
    col1_1, col2_2, col3_3, col4_4 = st.columns([1,1,1.3,1])
    with col1_1:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PRODUTO</h2>",unsafe_allow_html=True)
        consulta_produtos = crud.read("produto", all=True)
        listar_em_produtos = [produto[1] for produto in consulta_produtos]
        produto_insumo = st.selectbox('',options = listar_em_produtos, key=f'ins_prod_sel_{i}')
    with col2_2:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>INSUMO</h2>",unsafe_allow_html=True)
        consulta_insumos = crud.read("item_insumo", all=True)
        listar_em_insumos = [insumo[1] for insumo in consulta_insumos]
        insumo_produto = st.selectbox('',options = listar_em_insumos, key=f'ins_ins_sel_{i}')
    with col3_3:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>QUANTIDADE DE INSUMO</h2>",unsafe_allow_html=True)
        quantidade_insumo = st.text_input('',key=f'ins_quan_{i}')
    with col4_4:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 50px;'></h2>",unsafe_allow_html=True)
        st.button(f"Mais", on_click=add_new_field, key=f'i_{i}')

col1_1_1, col2_2_2 = st.columns([1,1])
with col1_1_1:
    st.button('ADICIONAR TODOS', on_click=add_new_field, key=f'a_{i}')
with col2_2_2:
    st.button('REMOVER TODOS', on_click=clear_added_fields, key=f'b_{i}')
