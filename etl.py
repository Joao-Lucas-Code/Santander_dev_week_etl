import pandas as pd
import requests
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
sdw_api_url = os.getenv("SDW_API_URL", "https://sdw-2023-prd.up.railway.app")

def get_user(id):
    response = requests.get(f'{sdw_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

def generate_ai_news(user):
    # Instancia o modelo Gemini Pro
    model = genai.GenerativeModel('gemini-pro')
    
    # Prompt enviado para a IA
    prompt = f"Você é um especialista em marketing bancário. Crie uma mensagem curta e impactante para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)."
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Erro na geração do Gemini: {e}")
        return "Invista hoje para um futuro melhor!" # Fallback em caso de erro

def update_user(user):
    response = requests.put(f"{sdw_api_url}/users/{user['id']}", json=user)
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

    # 2. Transform (Com Gemini)
    print("\nIniciando Transformação (IA com Gemini)...")
    for user in users:
        news = generate_ai_news(user)
        print(f"Mensagem para {user['name']}: {news}")
        
        user['news'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news
        })

    # 3. Load
    print("\nIniciando Carga...")
    for user in users:
        success = update_user(user)
        print(f"Usuário {user['name']} atualizado? {success}!")

if __name__ == "__main__":
    main()