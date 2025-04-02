from dotenv import load_dotenv
load_dotenv()

# Step1: Setup API Keys for Groq, OpenAI, and Tavily
import os

# Set the environment variables explicitly
os.environ["GROQ_API_KEY"] = "use your api key here"
os.environ["TAVILY_API_KEY"] = "use your api key here"

# Also assign them to variables if needed later.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize clients with explicit API key passing
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

# Initialize the Tavily search tool; passing tavily_api_key is optional now since it's set in the environment,
# but we include it for clarity.
search_tool = TavilySearchResults(max_results=3, tavily_api_key=TAVILY_API_KEY)

# Step3: Setup AI Agent with Search Tool Functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
    else:
        raise ValueError("Unsupported provider")
    
    # Include the Tavily API key for the search tool, if search is enabled.
    tools = [TavilySearchResults(max_results=2, tavily_api_key=TAVILY_API_KEY)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]
