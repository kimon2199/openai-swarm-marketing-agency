from dotenv import load_dotenv
from marketing_agency.configs.agents import *
from swarm import Swarm
from swarm.repl.repl import process_and_print_streaming_response, pretty_print_messages

load_dotenv()

def run_demo(
    starting_agent, context_variables=None, stream=False, debug=False, messages = []
) -> None:
    client = Swarm()
    print("Starting Marketing Agency 💼 Swarm CLI 🐝")

    agent = starting_agent

    while any([message["content"] == "Case resolved." for message in messages]) == False:

        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables or {},
            stream=stream,
            debug=debug,
        )

        if stream:
            response = process_and_print_streaming_response(response)
        else:
            pretty_print_messages(response.messages)

        messages.extend(response.messages)
        agent = response.agent

context_variables = {
    "client_context": """Client: EcoBottle Inc.
Contact: Sarah Green
Industry: Sustainable Consumer Goods
Budget: $50,000
Timeline: 3 months""",
    
    "campaign_context": """Product: Reusable Water Bottle
Target Audience: Environmentally conscious consumers, 25-45
Key Features: 
- 100% recycled materials
- Temperature control technology
- Lifetime warranty
Campaign Goals:
- Increase brand awareness
- Drive online sales
- Highlight environmental impact""",
}

if __name__ == "__main__":
    run_demo(manager, context_variables=context_variables, stream=True, debug=False)
