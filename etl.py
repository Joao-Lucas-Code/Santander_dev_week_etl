import pandas as pd
import requests
import json
import os
import openai
from dotenv import load_dotenv

# Carrega variáveis de ambiente (sua API Key)
load_dotenv()

# Configurações
openai.api_key = os.getenv("OPENAI_API_KEY")
SDW2023_API_URL = 'https://sdw-2023-prd.up.railway.app'

def get_user(id):
    response = requests.get(f'{SDW2023_API_URL}/users/{id}')
    return response.json() if response.status_code == 200 else None

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing bancário."},
            {"role": "user", "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"}
        ]
    )
    return completion.choices[0].message.content.strip('\"')

def update_user(user):
    response = requests.put(f"{SDW2023_API_URL}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

def main():
    # 1. Extract
    print("Iniciando Extração...")
    try:
        df = pd.read_csv('SDW2023.csv')
        user_ids = df['UserID'].tolist()
        users = [user for id in user_ids if (user := get_user(id)) is not None]
        print(f"{len(users)} usuários encontrados.")
    except Exception as e:
        print(f"Erro na extração: {e}")
        return

    # 2. Transform
    print("\nIniciando Transformação (IA)...")
    for user in users:
        try:
            news = generate_ai_news(user)
            print(f"Mensagem gerada para {user['name']}: {news}")
            user['news'].append({
                "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
                "description": news
            })
        except Exception as e:
            print(f"Erro ao gerar IA para {user['name']}: {e}")

    # 3. Load
    print("\nIniciando Carga...")
    for user in users:
        success = update_user(user)
        print(f"Usuário {user['name']} atualizado? {success}!")

if __name__ == "__main__":
    main()