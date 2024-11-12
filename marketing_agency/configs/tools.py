def transfer_to_creative_director():
    """Transfer the conversation to the Creative Director for campaign ideation."""
    from ..configs.agents import creative_director  # Import inside function instead
    return creative_director

def transfer_to_copywriter():
    """Transfer the conversation to the Copywriter for ad copy creation."""
    from ..configs.agents import copywriter  # Import inside function instead
    return copywriter

def transfer_to_designer():
    """Transfer the conversation to the Graphic Designer for visual concept creation."""
    from ..configs.agents import graphic_designer  # Import inside function instead
    return graphic_designer

def transfer_to_analyst():
    """Transfer the conversation to the Data Analyst for performance review."""
    from ..configs.agents import data_analyst  # Import inside function instead
    return data_analyst

def transfer_to_client_liaison():
    """Transfer the conversation to the Client Liaison for feedback handling."""
    from ..configs.agents import client_liaison  # Import inside function instead
    return client_liaison

def transfer_to_manager():
    """Transfer back to the Manager for task coordination."""
    from ..configs.agents import manager  # Import inside function instead
    return manager

def approve_campaign_theme():
    """Approve the proposed campaign theme and creative direction."""
    return "Campaign theme approved"

def approve_copy():
    """Approve the proposed ad copy."""
    return "Ad copy approved"

def approve_design():
    """Approve the proposed visual design concepts."""
    return "Design concepts approved"

def generate_performance_report():
    """Generate a simulated performance report for the campaign."""
    return "Performance report generated"

def submit_client_feedback():
    """Submit client feedback for processing."""
    return "Client feedback submitted"

def case_resolved():
    """Mark the current case as resolved."""
    return "Case resolved."
