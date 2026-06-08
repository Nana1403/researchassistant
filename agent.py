from agents import Agent
from ai_tools import search_google_books, web_search
from instructions import google_search_instructions, web_search_instructions, planner_instructions, source_instructions, research_manager
from  dotenv import load_dotenv

load_dotenv()


research_planner_agent = Agent(
    name="Research Planner Agent",
    instructions=planner_instructions,
    tools=[web_search, search_google_books],
)

search_agent = Agent(
    name="Research Assistant Agent",
    instructions=web_search_instructions,
    tools=[web_search]
)

search_google_agent = Agent(
    name="Search Books Agent",
    instructions=google_search_instructions,
    tools=[search_google_books]
)

source_agent = Agent( 
    name="Source Agent",
    instructions=source_instructions,
    tools=[web_search, search_google_books]
)

main_agent = Agent(
    name="Research Manager Agent",
    instructions=research_manager,
    handoffs=[research_planner_agent, 
              search_agent, 
              source_agent,
              search_google_agent
             ],
)

