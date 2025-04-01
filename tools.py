from configuration_file import configure_gmail_connection, misc_config
from langchain_community.tools.gmail.search import GmailSearch, SearchArgsSchema
from langchain_google_community.gmail.create_draft import GmailCreateDraft, CreateDraftSchema
from langchain_google_community.gmail.send_message import GmailSendMessage
from langchain_google_community.gmail.get_message import GmailGetMessage
from langchain_google_community.gmail.get_message import SearchArgsSchema as GetSearchArgsSchema
from langchain_google_community.gmail.get_thread import GmailGetThread, GetThreadSchema
import utility
from crewai_tools import FileReadTool

from crewai.tools import BaseTool, tool
from pydantic import BaseModel, Field
from typing import Type, Optional
import json


google_api_resource = configure_gmail_connection()
config = misc_config()
CONTACT_FILEPATH = config['contact_db_path']

# class MailDraftSchema(BaseModel):
#     """Input for MailDraftTool and MailSendTool"""
#     bcc: Optional[list[str]] = Field(..., description="The list of BCC recipients")
#     cc: Optional[list[str]] = Field(..., description="The list of CC recipients")
#     message: str = Field(..., description="The message to include in the draft")
#     subject: str = Field(..., description="The subject of the message")
#     to: str = Field(..., description="The list of recipients")
    
class MailDraftTool(BaseTool):
    name: str = "Mail Drafter"
    description: str = "Tool that creates a draft email for Gmail"
    args_schema: Type[BaseModel] = CreateDraftSchema

    def _run(self, message:list, subject:str, to:str, bcc:Optional[list[str]] = [], cc:Optional[list[str]] = []) -> dict:
        draft = GmailCreateDraft(api_resource=google_api_resource)
        result = draft.invoke({
                                'bcc':bcc,
                                'cc':cc,
                                'message':message,
                                'subject':subject,
                                'to':to
                            })
        return f"\nDraft created: {result}\n"

class MailSendTool(BaseTool):
    name: str = "Mail Sender"
    description: str = "Tool that sends a draft email for Gmail"
    args_schema: Type[BaseModel] = CreateDraftSchema

    def _run(self, bcc:Optional[list[str]], cc:Optional[list[str]], message:list, subject:str, to:str) -> dict:
        draft = GmailSendMessage(api_resource=google_api_resource)
        result = draft.invoke({
                                'bcc':bcc,
                                'cc':cc,
                                'message':message,
                                'subject':subject,
                                'to':to
                            })
        return f"\nMail Sent: {result}\n"
    
    
class MailSearchTool(BaseTool):
    name : str = "Search Mail Tool"
    description : str  = "Schema for searching message or threads in Gmail"
    # arg_schema: Type[BaseModel] = SearchArgsSchema
    
    def _run(self, query:str):
        gtool = GmailSearch(api_resource=google_api_resource)
        result = gtool.invoke(query)
        return f"\nSearch responses: {result}\n"


class GetMailTool(BaseTool):
    name : str = "Mail ID extractor"
    description : str  = "Tool that gets a message by ID from Gmail."
    # arg_schema: Type[BaseModel] = GetSearchArgsSchema
    
    def _run(self, query:str):
        gtool = GmailGetMessage(api_resource=google_api_resource)
        result = gtool.invoke(query)
        return f"\nSearch responses: {result}\n"

class GetThreadTool(BaseTool):
    name : str = "Mail Thread Fetcher"
    description : str  = "Tool that gets a thread by ID from Gmail"
    # arg_schema: Type[BaseModel] = GetThreadSchema
    
    def _run(self, query:str):
        gtool = GmailGetThread(api_resource=google_api_resource)
        result = gtool.invoke(query)
        return f"\nSearch responses: {result}\n"
        
class ContactSchema(BaseModel):
    name: str = Field(..., description="The name of person")
    relation: Optional[str] = Field(None, description="relationship with the person")
    email: Optional[str] = Field(..., description="email id of the person")
    phone: Optional[str] = Field(..., description="Mobile number of the person")
    
class WriteContactDB(BaseTool):
    name:str = "Add contact Database"
    description:str = "Add contact details in the contact database"
    args_schema: Type[BaseModel] =  ContactSchema
    
    def _run(self, name: Optional[str] = None, email: Optional[str] = None, relation: Optional[str] = None, phone: Optional[str] = None, CONTACT_FILEPATH=CONTACT_FILEPATH):
        
        contact_details = {
            "name": name,
            "relation": relation,
            "email": email,
            "phone": phone
        }
        
        with open(CONTACT_FILEPATH, 'r') as f:
            contacts = json.load(f)
        
        # contact_dict = contact_details.dict(exclude_none=True)
        contacts.append(contact_details)

        with open(CONTACT_FILEPATH, 'w') as f:
            json.dump(contacts, f, indent=4)

        return f"Successfully added contact details"
    

class UpdateContactDB(BaseTool):
    name:str = "Update contact Database"
    description:str = "Update contact details in the contact database"
    args_schema: Type[BaseModel] =  ContactSchema
    
    def _run(self, name: Optional[str] = None, email: Optional[str] = None, relation: Optional[str] = None, phone: Optional[str] = None, CONTACT_FILEPATH=CONTACT_FILEPATH):
        
        contact_details = {
            "name": name,
            "relation": relation,
            "email": email,
            "phone": phone
        }              
        
        with open(CONTACT_FILEPATH, 'r') as f:
            contacts = json.load(f)
            
        # if contact_details["name"] is not None:
        #     similar_detail_dict,score = utility.find_similar_person(json_data = contacts, search_query = contact_details['name'])
        # elif contact_details["email"] is not None:
        #     similar_detail_dict,score = utility.find_similar_person(json_data = contacts, search_query = contact_details['email'])
        # else:
        #     similar_detail_dict,score = {},0
        
        udpated_contacts = utility.update_json_data(contacts, contact_details)
        with open(CONTACT_FILEPATH, 'w') as f:
            json.dump(udpated_contacts, f, indent=4)

        return f"Successfully updated details"
    
    
FindContactDBTool = FileReadTool(json_path = CONTACT_FILEPATH)