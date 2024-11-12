from ..configs.tools import *
from ..data.routines import (
    client_liaison_instructions,
    copywriter_instructions,
    creative_director_instructions,
    data_analyst_instructions,
    graphic_designer_instructions,
    manager_instructions
)


from swarm import Agent

manager = Agent(
    name="Project Manager",
    instructions=manager_instructions,
    model="gpt-4o-mini",
    functions=[
        transfer_to_creative_director,
        approve_campaign_theme,
        transfer_to_copywriter,
        approve_copy,
        transfer_to_designer,
        approve_design,
        transfer_to_analyst,
        transfer_to_client_liaison,
        case_resolved
    ]
)

creative_director = Agent(
    name="Creative Director",
    instructions=creative_director_instructions,
    model="gpt-4o-mini",
    functions=[
        # generate_creative_direction,
        transfer_to_manager,
    ]
)

copywriter = Agent(
    name="Copywriter",
    instructions=copywriter_instructions,
    model="gpt-4o-mini",
    functions=[
        transfer_to_manager,
    ]
)

graphic_designer = Agent(
    name="Graphic Designer",
    instructions=graphic_designer_instructions,
    model="gpt-4o-mini",
    functions=[
        transfer_to_manager,
    ]
)

data_analyst = Agent(
    name="Data Analyst",
    instructions=data_analyst_instructions,
    model="gpt-4o-mini",
    functions=[
        generate_performance_report,
        transfer_to_manager,
    ]
)

client_liaison = Agent(
    name="Client Liaison",
    instructions=client_liaison_instructions,
    model="gpt-4o-mini",
    functions=[
        submit_client_feedback,
        transfer_to_manager,
    ]
)
