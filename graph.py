from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from cv_parser import parse_cv
from linkedin_scraper import search_jobs
from notify_agent import send_whatsapp_notification
from typing import TypedDict, List

class JobSearchState(TypedDict):
    cv_path: str
    profile: dict
    jobs: List[dict]

def parse_cv_step(state: JobSearchState) -> dict:
    profile = parse_cv(state["cv_path"])
    print("🧠 Extracted profile:", profile)
    return {"profile": profile}

def search_jobs_step(state: JobSearchState) -> dict:
    jobs = search_jobs(state["profile"])
    print("📌 Jobs found:", jobs)
    return {"jobs": jobs}

def notify_step(state: JobSearchState) -> dict:
    send_whatsapp_notification(state["jobs"])
    return {}

def build_job_search_graph():
    builder = StateGraph(JobSearchState)

    builder.add_node("ParseCV", RunnableLambda(parse_cv_step))
    builder.add_node("SearchJobs", RunnableLambda(search_jobs_step))
    builder.add_node("NotifyUser", RunnableLambda(notify_step))

    builder.set_entry_point("ParseCV")
    builder.add_edge("ParseCV", "SearchJobs")
    builder.add_edge("SearchJobs", "NotifyUser")

    return builder.compile()
