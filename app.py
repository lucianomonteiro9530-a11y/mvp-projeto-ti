def cadastrar_usuario(nome):
    if not nome.strip():
        return "Erro: nome obrigatório"
    return f"Usuário {nome} cadastrado com sucesso"


def consultar_usuario(nome):
    if not nome.strip():
        return "Erro: nome obrigatório"
    return f"Consulta realizada: {nome}"
