class LogisticsAgent:
    def arrange_shipping(self, item, price, buyer):
        shipping_info = {
            "recipient": buyer,
            "item": item,
            "address": "123 Buyer St, City, Country",
            "price": price
        }
        print(f"[LogisticsAgent] Shipping arranged: {shipping_info}")
        return shipping_info
