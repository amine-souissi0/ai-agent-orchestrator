# agents/pricing_agent.py

class PricingAgent:
    """Agent responsible for suggesting a product price and a minimum price."""

    def suggest_price(self, product_info):
        """
        Suggest a price based on product condition.
        """
        base_price = 300
        condition = product_info.get('condition', 'used')
        if condition == 'new':
            price = base_price
        elif condition == 'good':
            price = base_price * 0.85
        else:
            price = base_price * 0.7

        print(f"[PricingAgent] Suggested price for '{product_info.get('name')}': ${price:.2f}")
        return price

    def suggest_min_price(self, listing):
        """
        Suggests the minimum price agent is willing to accept for negotiation.
        """
        min_price = listing['price'] * 0.75
        print(f"[PricingAgent] Minimum acceptable price: ${min_price:.2f}")
        return min_price
