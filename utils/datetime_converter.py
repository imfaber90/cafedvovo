import streamlit as st
from datetime import datetime

def convert_to_datetime_format(data_str):
    formatos = ['%d-%m-%Y', '%d-%m-%y', '%d/%m/%Y', '%d/%m/%y'] 
    
    for formato in formatos:
        try:
            date = datetime.strptime(data_str, formato).date()
            return str(date)
        except ValueError:
            continue


def convert_from_datetime_to_string(data):
    if isinstance(data, str):
        # Se a entrada for uma string, converte para um objeto datetime
        try:
            data = datetime.strptime(data, '%Y-%m-%d').date()  # ou .datetime() se for necessário com hora
        except ValueError:
            st.error(f"Formato de data inválido: {data}") 
    
    # Agora, 'data' é um objeto datetime ou date, e podemos usar strftime
    return data.strftime('%d-%m-%Y')

