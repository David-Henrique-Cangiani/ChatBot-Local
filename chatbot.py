import requests

# URL da API Hugging Face para geração de linguagem natural
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"
API_TOKEN = "sua_api_key_aqui"  # Substitua pela sua chave da Hugging Face

# Headers da requisição para autenticação
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Função para enviar perguntas à API
def perguntar_huggingface(pergunta):
    payload = {
        "inputs": pergunta,
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        resposta = response.json()
        return resposta["generated_text"]
    else:
        return f"Erro na API: {response.status_code}, {response.text}"

# Chatbot principal
def chatbot():
    print("Chatbot: Olá! Como posso ajudar você hoje? (Digite 'sair' para encerrar)")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Chatbot: Até logo!")
            break
        resposta = perguntar_huggingface(pergunta)
        print(f"Chatbot: {resposta}")

# Executar chatbot
if __name__ == "__main__":
    chatbot()