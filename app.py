from configuration_file import configure_gmail_connection, setup_environment, misc_config
from crew import MailCrew, ContactCrew
from task import ContactManagementTasks
from langchain_groq import chat_models
from crewai import LLM


setup_environment()
api_resource = configure_gmail_connection()

config = misc_config()

# llm = LLM(
#     model="whisper-large-v3-turbo",   
# )
llm = LLM(model=config['llm_model'], base_url=config['base_url'])


# Mail Handling
# Manager_agent

# Travel Arrangements

# Schedule Meeting

# Manage to do lists

# Contact Management

# Chat Model

# final_response = MailCrew.gmail_crew().kickoff(inputs = {"order":"Can you setup a team meeting tonight with jeevanlowrence333@gmail.com, for 6pm, and send him the mail as well to confirm his availability"})
# print(final_response)

def llm_fn_dummy(user_input:str,context:str):
    return f"\nUser: {user_input} \nCONTEXT {context}"
    
def handle_conversation():
    context = ""
    print("Hi! My name is Dr. Osbo")
    while True:
        user_input = input("Ask me question: ")
        if user_input == "exit":
            break
        
        result = llm_fn_dummy(user_input, context)
        print("Dr. Osbo: ", result)
        context +=f"\nUser: {user_input} \nAI: {result}"



if __name__ =="__main__":
    
    query = "Jeevan's surname is Lowrence, please update in my contacts"
    # query = "Please correct my girlfriends id as supriyaa.g66@gmail.com "
    crew_response = ContactCrew.contact_management_crew().kickoff({'query':query})
    
    
    response = llm.call(
        f"user input: {query} "
        f"agent response : {crew_response} " 
        "return format: Natural language - simple english"
    )
    print(response)


# goal
# return format
# warnings
# context