from configuration_file import configure_gmail_connection, setup_environment
from crew import MailCrew

setup_environment()
api_resource = configure_gmail_connection()


# Mail Handling
# Manager_agent

# Travel Arrangements

# Schedule Meeting

# Manage to do lists

# Contact Management

# Chat Model

final_response = MailCrew.gmail_crew().kickoff(inputs = {"order":"Can you setup a team meeting tonight with jeevanlowrence333@gmail.com, for 6pm, and send him the mail as well to confirm his availability"})
print(final_response)