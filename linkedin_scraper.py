from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_jobs(profile: dict) -> list:
    title = profile.get("title", "")
    skills = " ".join(profile.get("skills", []))
    query = f"{title} {skills}".strip() or "Python Developer"
    print("🔍 Searching for:", query)

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    url = f"https://www.linkedin.com/jobs/search/?keywords={query.replace(' ', '%20')}"
    driver.get(url)
    time.sleep(5)

    jobs = []
    job_cards = driver.find_elements(By.CLASS_NAME, "base-search-card")

    for card in job_cards[:5]:
        try:
            job = {
                "title": card.find_element(By.CLASS_NAME, "base-search-card__title").text.strip(),
                "company": card.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip(),
                "location": card.find_element(By.CLASS_NAME, "job-search-card__location").text.strip(),
                "link": card.find_element(By.TAG_NAME, "a").get_attribute("href")
            }
            jobs.append(job)
        except Exception as e:
            print("⚠️ Skipping one job card:", e)
            continue

    driver.quit()
    return jobs
