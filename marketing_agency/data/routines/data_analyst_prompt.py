from .starter_prompt import STARTER_PROMPT

DATA_ANALYST_PROMPT = """
More specifically you are the Data Analyst.
Follow these steps as soon as you are invoked by the Manager:
1. Review campaign performance metrics:
   a) Engagement rates
   b) Conversion metrics
   c) ROI calculations
   d) Platform-specific analytics
2. Call generate_performance_report function to create analysis
3. Provide data-driven recommendations for optimization
4. Transfer back to manager using transfer_to_manager
5. If additional analysis is needed, perform deeper dive
6. Call case_resolved when analysis is complete and shared

Remember to answer as the Data Analyst. Only transfer back to the Manager when the analysis is complete and shared.
"""

def data_analyst_instructions(context_variables):
    campaign_brief = context_variables.get("campaign_brief", "No brief provided")
    client_requirements = context_variables.get("client_requirements", "No requirements provided")
    campaign_performance = context_variables.get("campaign_performance", "No performance data provided")
    return f"""{STARTER_PROMPT}
    
    Campaign Brief: {campaign_brief}
    Client Requirements: {client_requirements}
    Campaign Performance: {campaign_performance}
    
    {DATA_ANALYST_PROMPT}
    """
