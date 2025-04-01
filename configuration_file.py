from dotenv import load_dotenv
import os
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
import json

def misc_config():
    
    return{
        "contact_db_path" : "contacts.json",
        "llm_model": "llama-3.2-3b-preview",
        "agent_model" : "llama-3.3-70b-versatile",
        "base_url" : "https://api.groq.com/openai/v1" #"http://localhost:11434"
    } 

def setup_environment():
    load_dotenv()
    os.environ['GROQ_API_KEY'] = str(os.getenv('GROQ_KEY'))
    os.environ['OTEL_SDK_DISABLED'] = 'True'
    os.environ['share_crew'] = 'False'
    
    os.environ['LANGCHAIN_API_KEY'] = str(os.getenv('LANGCHAIN_API_KEY'))
    os.environ['LANGCHAIN_PROJECT'] = str(os.getenv('LANGCHAIN_PROJECT'))
    os.environ["LANGCHAIN_TRACING_V2"] = "False"
    
    if not os.path.exists("contacts.json"):
        contact_db_schema = [{
            "name":"",
            "relation":"",
            "email":"",
            "phone":""
        }]
        with open("contacts.json", 'w') as dbFile:  
            json.dump(contact_db_schema, dbFile)
        
    

def configure_gmail_connection():
    credentials = get_gmail_credentials(
        token_file="token.json",
        scopes=["https://mail.google.com/"],
        client_secrets_file="credentials.json",
    )

    api_resource = build_resource_service(credentials=credentials)
    
    return api_resource