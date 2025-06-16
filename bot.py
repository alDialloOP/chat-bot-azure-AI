from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OP"),
    deployment_name=os.getenv("gpt-35-turbo"),
    #deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.7
)

# Mémoire pour garder le fil de la conversation
memory = ConversationBufferMemory()

# Création de la chaîne conversationnelle
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Boucle interactive avec l'utilisateur
print("🤖 Le bot est prêt. Tape 'exit' pour quitter.\n")
while True:
    user_input = input("Vous : ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Fin de la conversation.")
        break
    response = conversation.predict(input=user_input)
    print("Bot :", response)
