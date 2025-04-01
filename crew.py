from configuration_file import setup_environment, misc_config
from model_manager import ModelManager
from crewai import Crew, Process
from task import MailTasks, ContactManagementTasks
from agents import MailAgent, contactManagementAgent

config = misc_config()


setup_environment()
llm_model = ModelManager().get_llm_model()


get_mail_agent = MailAgent.getMailAgent()
post_mail_agent = MailAgent.postMailAgent()
getmail_task = MailTasks.getMailTask(get_mail_agent)
postmail_task = MailTasks.postMailTask(post_mail_agent)

find_contact_agent = contactManagementAgent.contact_manager()
find_contact_task = ContactManagementTasks.contact_manager_task(find_contact_agent, config['contact_db_path'])



class MailCrew:
    def gmail_crew():
        return Crew(
        agents=[get_mail_agent, post_mail_agent],
        tasks=[getmail_task, postmail_task],
        verbose=True
    )
    
class ContactCrew:
    def contact_management_crew():
        return Crew(
            agents = [find_contact_agent],
            tasks = [find_contact_task],
            verbose = True
        )