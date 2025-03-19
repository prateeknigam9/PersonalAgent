from configuration_file import configure_gmail_connection
from langchain_community.tools.gmail.search import GmailSearch, SearchArgsSchema
from langchain_google_community.gmail.create_draft import GmailCreateDraft, CreateDraftSchema
from langchain_google_community.gmail.send_message import GmailSendMessage
from langchain_google_community.gmail.get_message import GmailGetMessage
from langchain_google_community.gmail.get_message import SearchArgsSchema as GetSearchArgsSchema
from langchain_google_community.gmail.get_thread import GmailGetThread, GetThreadSchema
from crewai.tools import BaseTool, tool
from pydantic import BaseModel, Field
from typing import Type, Optional


google_api_resource = configure_gmail_connection()


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
        
    
    