from geracao.gerador import GeradorResposta
from utils.configuracoes import CONFIGURACOES

def main():
    # Inicializa o gerador de resposta
    gerador = GeradorResposta(CONFIGURACOES['modelo_caminho'])
    
    consulta = "Qual é a importância da energia renovável?"
    resposta = gerador.gerar_resposta(consulta)
    
    print("Resposta gerada:", resposta)

if __name__ == "__main__":
    main()
