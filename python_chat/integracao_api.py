import openai
import dotenv
import os

dotenv.load_dotenv()


# No futuro separar por organização do openai
# openai.organization = os.getenv("")

openai.api_key = os.getenv("OPENAI_API_KEY")

resposta = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role" : "system",
            "content" : "Gere nomes de produtos fictícios sem descrição de acordo coma requisição do usuário"
        },
        {
            "role": "user",
            "content": "Gere 5 produtos"
        }
    ]
)

print(resposta)