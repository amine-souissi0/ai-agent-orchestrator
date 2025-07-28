import ollama
from agents.pricing_agent import PricingAgent
from agents.listing_agent import ListingAgent
from agents.negotiation_agent import NegotiationAgent
from agents.logistics_agent import LogisticsAgent

class Orchestrator:
    def __init__(self):
        self.pricing_agent = PricingAgent()
        self.listing_agent = ListingAgent()
        self.negotiation_agent = NegotiationAgent()
        self.logistics_agent = LogisticsAgent()

    def ask_llm_next_action(self, product, last_price, scenario_desc):
        prompt = (
            f"You are an AI orchestration manager. The product is {product['title']} ({product['condition']}).\n"
            f"Last attempted price: ${last_price:.2f}. Situation: {scenario_desc}\n"
            "Should we (A) retry negotiation at a lower price, (B) wait for a new buyer, or (C) stop trying?\n"
            "Reply ONLY with A, B, or C, and one line explanation."
        )
        response = ollama.chat(model='llama3', messages=[{"role": "user", "content": prompt}])
        print(f"[Orchestrator LLM Decision] {response['message']['content']}")
        return response['message']['content']

    def run(self, product):
        print("[Orchestrator] Starting orchestration...")
        price = self.pricing_agent.suggest_price(f"{product['title']} ({product['condition']})")
        listing = self.listing_agent.create_listing(product, price)

        negotiation_result = self.negotiation_agent.handle_negotiation(listing)

        # LLM-powered scenario decision: what if negotiation fails?
        attempts = 0
        max_attempts = 2  # don’t loop forever
        while not negotiation_result.get("accepted") and attempts < max_attempts:
            attempts += 1
            scenario_desc = "Negotiation failed, buyer did not accept offer."
            llm_action = self.ask_llm_next_action(product, price, scenario_desc)

            if 'A' in llm_action:
                # Lower price 10%, create new listing, re-negotiate
                price = round(price * 0.9, 2)
                print(f"[Orchestrator] Retrying with new price: ${price:.2f}")
                listing = self.listing_agent.create_listing(product, price)
                negotiation_result = self.negotiation_agent.handle_negotiation(listing)
            elif 'B' in llm_action:
                print("[Orchestrator] Waiting for new buyer (simulated: retrying negotiation)...")
                negotiation_result = self.negotiation_agent.handle_negotiation(listing)
            elif 'C' in llm_action:
                print("[Orchestrator] Stopping workflow as per LLM advice.")
                break
            else:
                print("[Orchestrator] LLM response unclear, stopping.")
                break

        if negotiation_result.get("accepted"):
            shipping_info = self.logistics_agent.arrange_shipping(
                listing["title"], negotiation_result["price"], negotiation_result["buyer"]
            )
            print("[Orchestrator] Workflow complete.")
            return shipping_info
        else:
            print("[Orchestrator] Sale failed, shipping skipped.")
            return None
