# 🏦 Santander Dev Week 2023 - ETL com Python & Gemini AI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5-orange?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

Este projeto é um pipeline de **ETL (Extract, Transform, Load)** reestruturado a partir do desafio da Santander Dev Week. O objetivo é criar mensagens de marketing personalizadas para clientes bancários utilizando a potência da **Inteligência Artificial Generativa** do Google.

> **Nota:** Devido à indisponibilidade da API original do desafio, este projeto foi adaptado para rodar em **Modo Mock (Simulação)**, garantindo a execução completa do fluxo de engenharia de dados.

## 🚀 Tecnologias Utilizadas

* **Python** (Linguagem Principal)
* **Google Gemini API (Modelo `gemini-2.5-flash`)** (Geração de conteúdo via IA)
* **Pandas** (Manipulação e estruturação de dados)
* **Dotenv** (Gerenciamento de variáveis de ambiente e segurança)

## ⚙️ Funcionalidades do Pipeline

1.  **Extract (Extração):** * Simula uma base de dados de clientes bancários (IDs e Nomes) em memória (substituindo a requisição GET da API original).
2.  **Transform (Transformação):** * Integração com a API do **Google Gemini**.
    * A IA analisa o perfil do usuário e gera uma mensagem de marketing única e impactante sobre investimentos.
3.  **Load (Carga):** * Salva os dados enriquecidos (com a mensagem gerada) em um arquivo local `users_processed.json`, simulando a persistência dos dados (substituindo o PUT na API).

## 🛠️ Como executar

### 1. Clone o repositório

git clone [https://github.com/SEU-USUARIO/nome-do-seu-repo.git](https://github.com/SEU-USUARIO/nome-do-seu-repo.git)
cd nome-do-seu-repo

### 2. Crie o ambiente virtual (Recomendado)

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Configuração de Segurança (.env)
Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Google Gemini:
GEMINI_API_KEY=sua-chave-aqui

### 5. Execute o pipeline ETL
python etl.py

✅ Resultado Esperado
Após a execução, um arquivo `users_processed.json` será gerado na raiz do projeto, contendo os dados dos usuários com as mensagens de marketing personalizadas.

---

👨‍💻 Autor
Feito por João Lucas 🚀 Estudante de Engenharia de Computação - Facens