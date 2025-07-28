# orchestrator.py

from agents.pricing_agent import PricingAgent
from agents.listing_agent import ListingAgent
from agents.negotiation_agent import NegotiationAgent
from agents.logistics_agent import LogisticsAgent

class Orchestrator:
    """
    Central orchestrator that coordinates the workflow, delegates tasks, and manages inter-agent communication.
    """

    def __init__(self):
        self.pricing_agent = PricingAgent()
        self.listing_agent = ListingAgent()
        self.negotiation_agent = NegotiationAgent()
        self.logistics_agent = LogisticsAgent()

    def delegate_task(self, agent, task, **kwargs):
        """
        Generic CrewAI-style delegation method to assign a task to an agent.
        """
        print(f"[Orchestrator] Delegating '{task}' to {agent.__class__.__name__}")
        method = getattr(agent, task)
        return method(**kwargs)

    def run_workflow(self, product_info):
        print("[Orchestrator] Starting orchestration...")

        status = {'steps': []}

        try:
            # Step 1: Pricing
            price = self.delegate_task(self.pricing_agent, 'suggest_price', product_info=product_info)
            status['steps'].append('pricing: success')

            # Step 2: Listing
            listing = self.delegate_task(self.listing_agent, 'create_listing', product_info=product_info, price=price)
            status['steps'].append('listing: success')

            # Step 3: Negotiation
            negotiation_result = self.delegate_task(self.negotiation_agent, 'handle_negotiation', listing=listing)
            status['steps'].append('negotiation: attempted')

            # Step 3B: If negotiation fails, ask PricingAgent for min price and retry
            if negotiation_result is None:
                min_price = self.delegate_task(self.pricing_agent, 'suggest_min_price', listing=listing)
                print("[Orchestrator] Sending minimum price to NegotiationAgent for retry.")
                listing['price'] = min_price
                negotiation_result = self.delegate_task(self.negotiation_agent, 'handle_negotiation', listing=listing)
                if negotiation_result:
                    status['steps'].append('negotiation: succeeded on second try')
                else:
                    status['steps'].append('negotiation: failed')
            else:
                status['steps'].append('negotiation: success')

            # Step 4: Logistics (may be skipped)
            shipping_info = self.delegate_task(self.logistics_agent, 'arrange_shipping', negotiation_result=negotiation_result)
            if shipping_info:
                status['steps'].append('logistics: shipped')
            else:
                status['steps'].append('logistics: skipped')

            print("[Orchestrator] Task status summary:", status)
            print("[Orchestrator] Workflow complete.")
            return shipping_info
        except Exception as e:
            print(f"[Orchestrator][Fatal Error]: {e}")
            status['error'] = str(e)
            return status
