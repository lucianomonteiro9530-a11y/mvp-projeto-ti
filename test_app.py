import unittest
from app import cadastrar_usuario, consultar_usuario


class TestMVP(unittest.TestCase):

    def test_cadastro_sucesso(self):
        resultado = cadastrar_usuario("Carlos")
        self.assertEqual(
            resultado,
            "Usuário Carlos cadastrado com sucesso"
        )

    def test_cadastro_sem_nome(self):
        resultado = cadastrar_usuario("")
        self.assertEqual(
            resultado,
            "Erro: nome obrigatório"
        )

    def test_consulta_sucesso(self):
        resultado = consultar_usuario("Carlos")
        self.assertEqual(
            resultado,
            "Consulta realizada: Carlos"
        )

    def test_consulta_sem_nome(self):
        resultado = consultar_usuario("")
        self.assertEqual(
            resultado,
            "Erro: nome obrigatório"
        )


if __name__ == "__main__":
    unittest.main()
