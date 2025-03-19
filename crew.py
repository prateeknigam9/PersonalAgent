from configuration_file import setup_environment
from model_manager import ModelManager
from crewai import Crew, Process
from task import MailTasks
from agents import MailAgent



setup_environment()
llm_model = ModelManager().get_llm_model()


get_mail_agent = MailAgent.getMailAgent()
post_mail_agent = MailAgent.postMailAgent()
getmail_task = MailTasks.getMailTask(get_mail_agent)
postmail_task = MailTasks.postMailTask(post_mail_agent)


class MailCrew:
    def gmail_crew():
        return Crew(
        agents=[get_mail_agent, post_mail_agent],
        tasks=[getmail_task, postmail_task],
        verbose=False
    )