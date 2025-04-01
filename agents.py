from crewai import Agent, LLM
from configuration_file import misc_config

config = misc_config()
llm_model = LLM(model=config['agent_model'], base_url=config['base_url'])

class MailAgent:
    def getMailAgent():
        return Agent(
            role = "Expert Mail Strategist",
            backstory = (
                "You work as an Expert at searching and fetching out emails"
                "You can filter mails based on name or id"
            ),
            goal = "Handle Prateek's Mail",
            verbose=True,
            llm = llm_model
            
        )
        
    def postMailAgent():
        return Agent(
            role = "Expert Mail Writer",
            backstory = (
                "You work as an Expert Email Writing Assistant to Prateek"
                "You are an expert at writing mails Professionally"
            ),
            goal = "Write Mails for prateek",
            verbose=True,
            llm = llm_model
        )
    
class contactManagementAgent:
    def contact_manager():        
        return Agent(
            role = "Contact Manager",
            backstory = (
                "You have been managing the contact book"
                "You work as an Expert in contact management."
                "You have a file based contact database, that you can query, add the details to and update the details. " 
                "You are efficient in reading, editing and updating a JSON File."               
            ),
            goal = "Manging contact details in the document for Prateek",
            verbose=True,
            llm = llm_model
        )
    
