Vamos criar um sistema completo de **Retrieval-Augmented Generation (RAG)** usando a estrutura fornecida. O sistema combinará recuperação de informações com a geração de texto, integrando o acesso ao modelo via API ou localmente.

### Estrutura do Projeto

Vamos seguir uma estrutura de projeto semelhante à anterior, mas agora incluindo a lógica completa para um sistema RAG.

**Arquivos:**

1. **`config.py`**: Configurações e informações de autenticação.
2. **`api_clients.py`**: Implementações de clientes para diferentes tipos de acesso.
3. **`retrieval.py`**: Implementação da recuperação de documentos.
4. **`rag_system.py`**: Integra recuperação e geração usando o modelo.
5. **`main.py`**: Código principal para executar o sistema RAG.

### 1. `config.py`

Este arquivo mantém as configurações e credenciais necessárias.

```python
# config.py

# API com Chave de API
API_KEY = 'YOUR_API_KEY_HERE'

# API com Token de Autenticação
AUTH_TOKEN = 'YOUR_AUTH_TOKEN_HERE'

# Configuração do modelo local
LOCAL_MODEL_PATH = 'path/to/your/local/model'

# Configuração do índice de documentos
DOCUMENTS = [
    {"id": "1", "text": "O LLaMA 3.1 é um modelo de linguagem avançado."},
    {"id": "2", "text": "O LlamaIndex é utilizado para criar e pesquisar índices de documentos."}
]
```

### 2. `api_clients.py`

Definimos os clientes para acessar o modelo.

```python
# api_clients.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests
from config import API_KEY, AUTH_TOKEN, LOCAL_MODEL_PATH

# Cliente para API com Chave de API
class APIClientWithKey:
    BASE_URL = 'https://api.ollama.com/v1/completions'  # Substitua com o URL real da API

    def __init__(self, api_key):
        self.api_key = api_key

    def query(self, prompt):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(
            self.BASE_URL,
            headers=headers,
            json={'model': 'llama3.1', 'prompt': prompt, 'max_tokens': 150}
        )
        response.raise_for_status()
        return response.json()['choices'][0]['text'].strip()

# Cliente para API com Token de Autenticação
class APIClientWithToken:
    BASE_URL = 'https://api.ollama.com/v1/completions'  # Substitua com o URL real da API

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def query(self, prompt):
        headers = {'Authorization': f'Bearer {self.auth_token}'}
        response = requests.post(
            self.BASE_URL,
            headers=headers,
            json={'model': 'llama3.1', 'prompt': prompt, 'max_tokens': 150}
        )
        response.raise_for_status()
        return response.json()['choices'][0]['text'].strip()

# Cliente para execução local
class LocalModelClient:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def query(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model.generate(inputs['input_ids'], max_length=150)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### 3. `retrieval.py`

Este módulo gerencia a recuperação de documentos.

```python
# retrieval.py

from config import DOCUMENTS

class SimpleIndex:
    def __init__(self):
        self.documents = DOCUMENTS

    def search(self, query):
        # Simples busca por palavras-chave
        results = [doc for doc in self.documents if query.lower() in doc['text'].lower()]
        return results

index = SimpleIndex()
```

### 4. `rag_system.py`

Integra a recuperação e a geração.

```python
# rag_system.py

from retrieval import index
from api_clients import APIClientWithKey, APIClientWithToken, LocalModelClient
from config import API_KEY, AUTH_TOKEN, LOCAL_MODEL_PATH

class RAGSystem:
    def __init__(self, client_type='api_key'):
        if client_type == 'api_key':
            self.client = APIClientWithKey(api_key=API_KEY)
        elif client_type == 'auth_token':
            self.client = APIClientWithToken(auth_token=AUTH_TOKEN)
        elif client_type == 'local':
            self.client = LocalModelClient(model_path=LOCAL_MODEL_PATH)
        else:
            raise ValueError("Tipo de cliente não reconhecido. Use 'api_key', 'auth_token' ou 'local'.")

    def generate_answer(self, query):
        # Recuperar documentos relevantes
        docs = index.search(query)
        context = " ".join(doc['text'] for doc in docs)
        
        # Criar o prompt para o modelo
        prompt = f"Contexto: {context}\nPergunta: {query}\nResposta:"
        
        # Gerar resposta com o modelo
        return self.client.query(prompt)
```

### 5. `main.py`

O ponto de entrada principal para o sistema RAG.

```python
# main.py

from rag_system import RAGSystem

def main():
    # Escolha o cliente com base na necessidade
    # Use 'api_key', 'auth_token', ou 'local'
    client_type = 'api_key'  # Mude conforme necessário

    rag_system = RAGSystem(client_type=client_type)
    
    # Testar o sistema RAG
    query = "Como o LlamaIndex pode ser utilizado com LLaMA 3.1?"
    answer = rag_system.generate_answer(query)
    print(f"Resposta para a consulta '{query}':")
    print(answer)

if __name__ == "__main__":
    main()
```

### Instruções para Rodar o Código

1. **Configure o Ambiente**: Certifique-se de ter todas as bibliotecas necessárias instaladas.

```bash
pip install transformers torch requests
```

2. **Preencha as Configurações**: Complete o arquivo `config.py` com suas informações reais.

3. **Escolha o Cliente**: No `main.py`, ajuste o tipo de cliente (`'api_key'`, `'auth_token'`, ou `'local'`).

4. **Execute o Código**: Execute o script `main.py` para testar o sistema RAG.

```bash
python main.py
```

### Observações

- **API e Tokens**: Certifique-se de que você tem as credenciais corretas e as permissões necessárias para usar a API.
- **Modelo Local**: Assegure-se de que o caminho para o modelo local esteja correto e que o modelo esteja instalado.

Esta estrutura modular deve ajudar a manter o código organizado e facilitar ajustes futuros. Se precisar de mais detalhes ou ajuda com qualquer parte, estou aqui para ajudar!