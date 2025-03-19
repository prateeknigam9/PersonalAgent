from configuration_file import configure_gmail_connection, setup_environment
from crewai import Agent, Task, Crew, LLM, Process


setup_environment()
api_resource = configure_gmail_connection()


from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDatabaseTool,
)

from langchain_community.utilities import SQLDatabase















    

