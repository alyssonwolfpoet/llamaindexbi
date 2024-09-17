from ollama import Llama
from recuperacao.recuperador import recuperar_informacao

class GeradorResposta:
    def __init__(self, modelo_caminho):
        """
        Inicializa o gerador de resposta com o modelo Llama.

        :param modelo_caminho: Caminho para o modelo Llama.
        """
        self.modelo = Llama.load(modelo_caminho)
    
    def formatar_prompt(self, consulta, informacoes):
        """
        Formata o prompt para o modelo Llama.

        :param consulta: A consulta do usuário.
        :param informacoes: Informações relevantes recuperadas.
        :return: O prompt formatado.
        """
        return (f"Consulta: {consulta}\n"
                f"Informações relevantes:\n"
                f"{chr(10).join(informacoes)}\n"
                "Resposta:")

    def gerar_resposta(self, consulta):
        """
        Gera uma resposta usando o modelo Llama.

        :param consulta: A consulta do usuário.
        :return: A resposta gerada pelo modelo.
        """
        informacoes = recuperar_informacao(consulta)
        prompt = self.formatar_prompt(consulta, informacoes)
        return self.modelo.generate(prompt)
