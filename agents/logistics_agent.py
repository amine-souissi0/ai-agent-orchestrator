# agents/logistics_agent.py

class LogisticsAgent:
    """Agent responsible for arranging shipping after a sale."""

    def arrange_shipping(self, negotiation_result):
        """
        Arranges shipping if a sale was made.
        """
        if negotiation_result is None:
            print("[LogisticsAgent] No sale made, skipping shipping.")
            return None
        shipping_info = {
            'recipient': negotiation_result['buyer'],
            'item': negotiation_result['listing']['title'],
            'address': '123 Buyer St, City, Country',
            'price': negotiation_result['final_price']
        }
        print(f"[LogisticsAgent] Shipping arranged: {shipping_info}")
        return shipping_info
