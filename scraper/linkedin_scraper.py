import json
import traceback
from datetime import datetime
from playwright.sync_api import sync_playwright
import agentql
from config.settings import EMAIL, PASSWORD
from queries.linkedin_query import JOBS_QUERY

LOGIN_URL = "https://www.linkedin.com/login"
JOBS_URL = "https://www.linkedin.com/jobs/search/?keywords=AI%20engineer&location=Morocco"

def scrape_linkedin_jobs():
    jobs_data = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = agentql.wrap(browser.new_page())

        try:
            page.goto(LOGIN_URL)
            page.fill("input[name='session_key']", EMAIL)
            page.fill("input[name='session_password']", PASSWORD)
            page.click("button[type='submit']")
            page.wait_for_load_state("networkidle")

            if "feed" not in page.url:
                print("Login failed or blocked.")
                browser.close()
                return []

        except Exception as e:
            print(f"Login error: {str(e)}\n{traceback.format_exc()}")
            browser.close()
            return []

        try:
            page.goto(JOBS_URL)
            page.wait_for_timeout(5000)

            results = page.query_data(JOBS_QUERY)
            if results and isinstance(results.get("jobs"), list):
                jobs_data.extend(results["jobs"])
            else:
                print("No jobs found.", results)

        except Exception as e:
            print(f"Scraping error: {str(e)}\n{traceback.format_exc()}")

        finally:
            browser.close()

    return jobs_data