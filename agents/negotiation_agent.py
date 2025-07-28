# agents/negotiation_agent.py

class NegotiationAgent:
    """Agent responsible for handling negotiation with buyers."""

    def handle_negotiation(self, listing):
        """
        Simulates negotiation:
        - Buyer offers 20% less than asking price.
        - Accepts offer if >= 75% of the current price.
        """
        asking_price = listing['price']
        buyer_offer = asking_price * 0.8
        print(f"[NegotiationAgent] Received offer: ${buyer_offer:.2f} for {listing['title']} (asking: ${asking_price:.2f})")

        if buyer_offer >= asking_price * 0.75:
            print(f"[NegotiationAgent] Offer accepted at ${buyer_offer:.2f}!")
            return {
                'final_price': buyer_offer,
                'buyer': 'John Doe',
                'listing': listing
            }
        else:
            print("[NegotiationAgent] Offer rejected. Too low!")
            return None
