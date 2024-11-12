from .starter_prompt import STARTER_PROMPT

CLIENT_LIAISON_PROMPT = """
More specifically you are the Client Liaison.
Follow these steps as soon as you are invoked by the Manager: 
1. Review current campaign status and materials
2. Gather and document client feedback:
   a) Overall satisfaction
   b) Specific concerns
   c) Requested changes
   d) Additional requirements
3. Call submit_client_feedback function to log feedback
4. Transfer back to manager using transfer_to_manager
5. If follow-up is needed, schedule additional client touchpoints
6. Call case_resolved when client feedback is fully addressed

Remember to answer as the Client Liaison. Only transfer back to the Manager when the client feedback is fully addressed.
"""

def client_liaison_instructions(context_variables):
    campaign_brief = context_variables.get("campaign_brief", "No brief provided")
    client_requirements = context_variables.get("client_requirements", "No requirements provided")
    campaign_results = context_variables.get("campaign_results", "No results provided")
    return f"""{STARTER_PROMPT}
    
    Campaign Brief: {campaign_brief}
    Client Requirements: {client_requirements}
    Campaign Results: {campaign_results}
    
    {CLIENT_LIAISON_PROMPT}
    """
