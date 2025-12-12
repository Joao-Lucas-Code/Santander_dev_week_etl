# Santander Dev Week 2023 - ETL com Python

Este projeto é um pipeline de **ETL (Extract, Transform, Load)** desenvolvido durante o bootcamp da Santander Dev Week. O objetivo é criar mensagens de marketing personalizadas para clientes bancários utilizando **Inteligência Artificial Generativa**.

## 🚀 Tecnologias Utilizadas

* **Python** (Linguagem Principal)
* **Pandas** (Manipulação de dados)
* **OpenAI API (GPT-4)** (Geração de mensagens)
* **Requests** (Consumo de API REST)

## ⚙️ Funcionalidades

1.  **Extract:** Lê uma planilha CSV (`SDW2023.csv`) contendo IDs de usuários e busca os detalhes de cada cliente na API do Santander Dev Week.
2.  **Transform:** Utiliza a API da OpenAI (GPT-4) para gerar frases de marketing personalizadas sobre investimentos para cada usuário.
3.  **Load:** Envia as mensagens geradas de volta para a API do banco, atualizando o cadastro do usuário.

## 🛠️ Como executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/nome-do-repo.git](https://github.com/SEU-USUARIO/nome-do-repo.git)

2. Instale as dependências:
   ```bash  
   pip install -r requirements.txt

3. Configure as variáveis de ambiente
    - `OPENAI_API_KEY`: Sua chave de API da OpenAI.

4. Execute o script ETL:
   ```bash
    python etl.py

---

Feito por João Lucas 🚀
