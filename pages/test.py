import streamlit as st

# Criação do expander
with st.expander("Clique para Expandir"):
    # Botão que altera o estado
    if st.button("Clique Aqui"):
        st.write("O botão foi clicado!")
    else:
        st.write("O botão ainda não foi clicado.")


