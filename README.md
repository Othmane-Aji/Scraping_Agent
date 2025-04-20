# LinkedIn Job Scraper Agent

This project provides an automated system to scrape AI engineering job listings from LinkedIn using Playwright for browser automation and LangChain for agent orchestration. It can optionally be controlled via natural language using an LLM such as Gemini or GPT. The system supports login with LinkedIn credentials and returns job listings in structured JSON format.

## Technologies Used

- **LangChain** – for defining and managing tools and agents
- **Playwright** – for headless browser automation and scraping
- **dotenv** – for secure environment variable management
- **Gemini (Google Generative AI)** or **OpenAI** – optional LLM integration for reasoning
- **(Optional) AgentQL** – for scraping via LLM and semantic selectors

## Features

- Secure login to LinkedIn using credentials from `.env`
- Searches for jobs with custom keywords and location (default: "AI Engineer" in Morocco)
- Extracts:
  - Job title
  - Company name
  - Job location
- Returns job results in structured JSON
- LangChain agent interface allows queries like:  
  "Get 10 latest AI engineer jobs in Morocco"



## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/linkedin-job-agent.git
cd linkedin-job-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

EMAIL=your_linkedin_email@example.com  
PASSWORD=your_linkedin_password  
GEMINI_API_KEY=your_google_genai_api_key

## Running the Job Scraper Agent

To start the agent and interact with it:

```python
from agent.job_scraper_agent import run_job_scraper_agent

agent = run_job_scraper_agent()
response = agent.run("Get 10 latest AI engineer jobs in Morocco")
print(response)
```

## Sample Output

[
  {
    "title": "AI Engineer",
    "company": "DeepMind",
    "location": "Casablanca, Morocco"
  },
  {
    "title": "Machine Learning Specialist",
    "company": "InstaTech",
    "location": "Rabat, Morocco"
  }
]


## License

This project is licensed under the MIT License.
