# Não alterar os valores sem alterar suas referências em SQL.py, e em VER CADASTRO.PY!

def titulo(nome):
    dicionario = {
        'pessoa_id': 'ID',
        'nome': 'Nome',
        'email': 'E-mail',
        'telefone': 'Telefone',
        'data_nascimento': 'Data de nascimento',
        'pais': 'País',
        'cep': 'CEP',
        'estado': 'UF',
        'cidade': 'Cidade',
        'bairro': 'Bairro',
        'rua': 'Logradouro',
        'numero': 'Nº',
        'complemento': 'Complemento',
        'cnpj': 'CNPJ',
        'descricao': 'Descrição',
        'data_cadastro': 'Data de cadastro',
        'rua': 'Logradouro',
        'passaporte': 'Passaporte',
        'cpf': 'CPF',
        'matricula': 'Matrícula',
        'cargo': 'Profissão',
        'salario': 'Salário',   
        'nome_empresa': 'Empresa',
        'documento': 'Documento',
    }
    return dicionario[nome]

# Não alterar os valores sem alterar suas referências em SQL.py, e em VER CADASTRO.PY!