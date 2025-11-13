from google.adk.agents.llm_agent import Agent

hello_world_agent = Agent(
    model='gemini-2.5-flash',
    name='hello_world_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

root_agent = hello_world_agent