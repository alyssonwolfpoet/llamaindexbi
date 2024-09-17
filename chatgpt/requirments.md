Para configurar um ambiente virtual (venv) em Python, siga estas etapas. O ambiente virtual ajuda a manter as dependências do projeto isoladas e organizadas. Aqui está um guia passo a passo para configurar e usar um ambiente virtual para o seu projeto Python:

### 1. Criar um Ambiente Virtual

1. **Navegue até o diretório do seu projeto**:
   Abra um terminal ou prompt de comando e use o comando `cd` para navegar até o diretório onde você deseja configurar o ambiente virtual.

   ```bash
   cd caminho/para/seu/projeto
   ```

2. **Crie o ambiente virtual**:
   Execute o comando a seguir para criar um ambiente virtual. O diretório `venv` é onde o ambiente virtual será armazenado. Você pode nomeá-lo como preferir.

   ```bash
   python -m venv venv
   ```

### 2. Ativar o Ambiente Virtual

- **No Windows**:
  Execute o seguinte comando no terminal ou prompt de comando:

  ```bash
  venv\Scripts\activate
  ```

- **No macOS e Linux**:
  Execute o seguinte comando no terminal:

  ```bash
  source venv/bin/activate
  ```

  Após a ativação, você verá o nome do ambiente virtual prefixado no prompt, indicando que está ativo (ex: `(venv)`).

### 3. Instalar Dependências

Depois de ativar o ambiente virtual, você pode instalar as dependências necessárias para o seu projeto usando `pip`. Normalmente, você tem um arquivo chamado `requirements.txt` que lista todas as dependências do projeto. Se não tiver um, você pode criá-lo posteriormente.

Para instalar pacotes, execute:

```bash
pip install nome_do_pacote
```

Para instalar todas as dependências listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Criar um Arquivo `requirements.txt`

Se você ainda não tiver um arquivo `requirements.txt`, você pode criar um com todas as dependências instaladas no ambiente virtual. Após instalar todos os pacotes necessários, execute o seguinte comando:

```bash
pip freeze > requirements.txt
```

Isso gerará um arquivo `requirements.txt` com a lista de pacotes e suas versões.

### 5. Desativar o Ambiente Virtual

Quando você terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o comando:

```bash
deactivate
```

### 6. Estrutura do Projeto com `venv`

Após configurar o ambiente virtual, a estrutura do seu projeto pode parecer assim:

```
rag_project/
│
├── venv/               # Ambiente virtual
│
├── main.py
├── recuperacao/
│   ├── __init__.py
│   └── recuperador.py
├── geracao/
│   ├── __init__.py
│   └── gerador.py
└── utils/
    ├── __init__.py
    └── configuracoes.py
└── requirements.txt    # Arquivo com dependências do projeto
```

### 7. Comandos Adicionais

- **Atualizar `requirements.txt` após adicionar novas dependências**:

  Após instalar novos pacotes, atualize `requirements.txt`:

  ```bash
  pip freeze > requirements.txt
  ```

- **Instalar pacotes de um projeto existente**:

  Se você clonar um projeto existente, instale as dependências do projeto com:

  ```bash
  pip install -r requirements.txt
  ```

Seguindo essas etapas, você terá um ambiente virtual bem configurado para isolar e gerenciar as dependências do seu projeto Python.