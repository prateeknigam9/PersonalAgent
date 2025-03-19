from langchain_groq import ChatGroq
from groq import Groq

# https://console.groq.com/dashboard/limits
class ModelManager:
    def __init__(self, llm_model_name = "Llama-3-Groq-70B-Tool-Use", embedding_model_name = "nomic-embed-text:latest", temperature=0.2):
        self.llm_model = ChatGroq(model=llm_model_name, temperature= temperature)
        self.embedding_model  = embedding_model_name
        
    def get_llm_model(self):
        return self.llm_model     
    def get_embedding_model(self):
        return self.embedding_model  
    def get_client(self):
        return Groq()  