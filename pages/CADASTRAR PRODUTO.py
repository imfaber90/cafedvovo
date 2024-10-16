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
                
                /* Estilizando os botões do Streamlit */
                div.stButton > button {
                    color: white;
                    border-radius: 10px;
                    font-size: 16px;
                    font-weight: bold;
                }
                div.stFormSubmitButton > button {
                    color: white; /* Cor do texto */
                    border-radius: 10px;
                    font-size: 16px;
                    font-weight: bold;
                }
            </style>
            
            """, unsafe_allow_html=True)

crud = CRUD()

def insertInto():
    loteid = randrange(1,200000000)
    return loteid

if 'num_fields' not in st.session_state:
    st.session_state.num_fields = 1
    
if 'lista_insumo_id_e_qntd' not in st.session_state:
    st.session_state.id_produto_selecionado = ""
    st.session_state.lista_insumo_id_e_qntd = []
    
if 'produto_selecionado' not in st.session_state:
    st.session_state.produto_selecionado = None

def add_new_field():
    st.session_state.num_fields += 1

def clear_added_fields():
    st.session_state.num_fields = 1
    st.session_state.id_produto_selecionado = ""
    st.session_state.lista_insumo_id_e_qntd.clear()
    st.session_state.produto_selecionado = None

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
        listar_em_produtos = [(produto[0],produto[1]) for produto in consulta_produtos]
        if i == 0:
            produto_insumo = st.selectbox('',options = listar_em_produtos, key=f'ins_prod_sel_{i}', format_func=lambda x: x[1])
            st.session_state.produto_selecionado = produto_insumo[0]
        else:
            # Para os outros selectboxes, usa o valor do primeiro
            produto_insumo = st.selectbox('', options=['O de cima'], key=f'ins_prod_sel_{i}', disabled=True)
            # Define o valor selecionado baseado no session_state
            
    with col2_2:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>INSUMO</h2>",unsafe_allow_html=True)
        consulta_insumos = crud.read("item_insumo", all=True)
        listar_em_insumos = [(insumo[0], insumo[1]) for insumo in consulta_insumos]
        insumo_produto = st.selectbox('',options = listar_em_insumos, key=f'ins_ins_sel_{i}', format_func=lambda x: x[1])
    with col3_3:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>QUANTIDADE DE INSUMO</h2>",unsafe_allow_html=True)
        quantidade_insumo = st.text_input('',key=f'ins_quan_{i}')
    with col4_4:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 50px;'></h2>",unsafe_allow_html=True)
        if st.button(f"Mais", on_click=add_new_field, key=f'i_{i}'):
            st.session_state.id_produto_selecionado = produto_insumo[0]
            st.session_state.lista_insumo_id_e_qntd.append((insumo_produto[0], quantidade_insumo))
            #st.write(st.session_state.lista_insumo_id_e_qntd)
            
col1_1_1, col2_2_2 = st.columns([2.45,1])
with col1_1_1:
    if st.button('CRIAR', key=f'a_{i}'):
        lista_insumo_qntd = st.session_state.lista_insumo_id_e_qntd
        print(st.session_state.lista_insumo_id_e_qntd)
        if st.session_state.id_produto_selecionado == "":
            print(produto_insumo, insumo_produto, quantidade_insumo)
            crud.insert("produto_insumo", produto_id = produto_insumo[0], insumo_id = insumo_produto[0], qntd = quantidade_insumo)
        else:
            for insumo_e_qntd in lista_insumo_qntd:
                crud.insert("produto_insumo", produto_id = st.session_state.produto_selecionado, insumo_id = insumo_e_qntd[0], qntd = insumo_e_qntd[1])
            crud.insert("produto_insumo", produto_id = st.session_state.produto_selecionado, insumo_id = insumo_produto[0], qntd = quantidade_insumo)
        #clear_added_fields()
with col2_2_2:
    st.button('REMOVER CAMPOS', on_click=clear_added_fields, key=f'b_{i}')


st.write("#")    
# Título da aplicação
st.markdown(f"<h2 style= 'color:black;padding-top: 25px;'>Lista de produtos e insumos </h2>",unsafe_allow_html=True)

# Obter os dados
dados = crud.get_produtos_e_insumos()

# Agrupar por produto
produtos = dados.groupby('nome_produto')

# Exibir os dados de forma formatada
for produto, grupo in produtos:
    st.markdown(f"<h3 style= 'color:black;padding-top: 25px;'>Produto: {produto} </h3>",unsafe_allow_html=True)
    st.markdown(f"<h4 style= 'color:black;padding-top: 0px;'>Insumos </h4>",unsafe_allow_html=True)
    for _, row in grupo.iterrows():
        st.write(f"- {row['nome_insumo']}: {row['qntd_insumo_produto']}")
    st.write("")  # Linha em branco para espaçamento
