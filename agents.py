from crewai import Agent, LLM


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
            llm = LLM(model="gemma2-9b-it", base_url="https://api.groq.com/openai/v1")
            # llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
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
            llm = LLM(model="gemma2-9b-it", base_url="https://api.groq.com/openai/v1")
            # llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
        )