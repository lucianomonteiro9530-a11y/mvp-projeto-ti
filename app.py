def cadastrar_usuario(nome):
    if not nome.strip():
        return "Erro: nome obrigatório"
    return f"Usuário {nome} cadastrado com sucesso"


def consultar_usuario(nome):
    if not nome.strip():
        return "Erro: nome obrigatório"
    return f"Consulta realizada: {nome}"


def iniciar_interface():
    import tkinter as tk
    from tkinter import ttk

    janela = tk.Tk()
    janela.title("MVP - Cadastro e Consulta")
    janela.geometry("480x320")

    ttk.Label(
        janela,
        text="Sistema de Cadastro e Consulta",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    ttk.Label(janela, text="Nome do usuário:").pack()
    entrada = ttk.Entry(janela, width=40)
    entrada.pack(pady=8)

    resultado = ttk.Label(janela, text="")
    resultado.pack(pady=12)

    ttk.Button(
        janela,
        text="Cadastrar usuário",
        command=lambda: resultado.config(
            text=cadastrar_usuario(entrada.get())
        )
    ).pack(pady=5)

    ttk.Button(
        janela,
        text="Consultar usuário",
        command=lambda: resultado.config(
            text=consultar_usuario(entrada.get())
        )
    ).pack(pady=5)

    janela.mainloop()


if __name__ == "__main__":
    iniciar_interface()
