from crewai import Task
from tools import GetMailTool, GetThreadTool, MailSearchTool, MailSendTool, MailDraftTool
from tools import FindContactDBTool, WriteContactDB, UpdateContactDB


class MailTasks:
    def getMailTask(agent):
        return Task(
            description = (
                "Search for email messages or threads by id, or message or thread"
                "ref name/id - {order}"
                ),
            expected_output = "A mail thread or a single mail",
            agent = agent,
            tools=[GetMailTool(), GetThreadTool(), MailSearchTool()]
        )
    def postMailTask(agent):
        return Task(
            description = (
                "Draft Or Send Mail to the mentioned recipients based on the order"
                "Use one of the tool at a time"
                "Mail Sender - If the order is to send the mail use the tool"
                "Mail Drafter - If the order is to draft the mail"
                "order - {order}"
                "NOTE : If required you can run both the tools one by one, but based on the order"
            ),
            expected_output = "All emails must be formatted professionally in HTML and signed off a `Prateek`",
            agent = agent,
            tools=[MailSendTool(), MailDraftTool()]
        )

class ContactManagementTasks:
    def contact_manager_task(agent,contact_db_file:str='contacts.json'):
        return Task(
            description=(
                "The user has mentioned a query \n"
                "Classify the query as intents : save_contact, query_contact, update_contact\n"
                "if the query is to save_contact use tool : WriteContactDB\n"
                "if the query is to query_contact use tool : FindContactDBTool\n"
                "if the query is to update_contact use tool : UpdateContactDB\n"
                "if the query is to save_contact or update_contact: Extract and return user_inp: dict(name: , relation: , phone: , email_id:)\n"
                "query : {query} \n"
                f"the database to refer is {contact_db_file} .\n"
                "Note: if you do not find the contact information in the database, return None \n"
                "if finding contact: Return format should be dictionary"
            ),
            expected_output = "user_inp: dict(name: , relation: , phone: , email_id:)",
            agent = agent,
            tools =[FindContactDBTool, WriteContactDB(),UpdateContactDB()]

        )

