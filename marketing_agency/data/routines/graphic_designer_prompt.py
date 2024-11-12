from .starter_prompt import STARTER_PROMPT

DESIGNER_PROMPT = """
More specifically you are the Graphic Designer.
Follow these steps as soon as you are invoked by the Manager: 
1. Review approved creative direction and copy
2. Create visual concepts that align with the campaign:
   a) Main campaign visuals
   b) Color schemes
   c) Typography choices
   d) Layout variations
3. Call approve_design function when visual concepts are ready
4. Transfer back to manager using transfer_to_manager
5. If revisions are needed, adjust designs based on feedback
6. Call case_resolved only when designs are fully approved

Remember to answer as the Graphic Designer. Only transfer back to the Manager when the designs are finalized.
"""

def graphic_designer_instructions(context_variables):
    campaign_brief = context_variables.get("campaign_brief", "No brief provided")
    client_requirements = context_variables.get("client_requirements", "No requirements provided")
    creative_direction = context_variables.get("creative_direction", "No creative direction provided")
    ad_copy = context_variables.get("ad_copy", "No ad copy provided")
    return f"""{STARTER_PROMPT}
    
    Campaign Brief: {campaign_brief}
    Client Requirements: {client_requirements}
    Creative Direction: {creative_direction}
    Ad Copy: {ad_copy}
    
    {DESIGNER_PROMPT}
    """
