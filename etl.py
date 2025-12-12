import pandas as pd
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Função para gerar notícias usando IA (MANTIDA)
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
        return "Invista hoje para um futuro melhor!"

def main():
    print("⚠️ API do Santander Indisponível. Iniciando Modo Mock (Simulação)...")
    
    # 1. Extract (SIMULADO - Criamos usuários na mão)
    users = [
        {"id": 1, "name": "João Lucas", "news": []},
        {"id": 2, "name": "Maria", "news": []},
        {"id": 3, "name": "Pep", "news": []}
    ]
    print(f"{len(users)} usuários simulados carregados na memória.")

    # 2. Transform (IA com Gemini - ISSO É REAL)
    print("\nIniciando Transformação (IA com Gemini)...")
    for user in users:
        news = generate_ai_news(user)
        print(f"✅ Mensagem gerada para {user['name']}: \"{news}\"")
        
        user['news'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news
        })

    # 3. Load (SIMULADO - Apenas salvamos num arquivo JSON local para provar que funcionou)
    print("\nIniciando Carga (Salvando em arquivo local)...")
    with open('users_processed.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
    
    print("\n🎉 Processo finalizado! Confira o arquivo 'users_processed.json'.")

if __name__ == "__main__":
    main()