from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain.agents.agent_types import AgentType
import json
from scraper.linkedin_scraper import scrape_linkedin_jobs
from config.settings import GEMINI_API_KEY  # Get the Gemini API key
import os

def run_job_scraper_agent():
    def scrape_tool_func(_):
        jobs = scrape_linkedin_jobs()
        return json.dumps(jobs, indent=2)

    tools = [
        Tool(
            name="LinkedIn Job Scraper",
            func=scrape_tool_func,
            description="Scrapes job listings from LinkedIn using AgentQL."
        )
    ]

    # Use Gemini LLM
    llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.2
)


    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    prompt = "Scrape the latest AI engineering jobs from LinkedIn."
    result = agent.run(prompt)
    print(result)
