from crewai import Task
from tools import GetMailTool, GetThreadTool, MailSearchTool, MailSendTool, MailDraftTool




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