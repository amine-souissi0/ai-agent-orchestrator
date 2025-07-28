class ListingAgent:
    def create_listing(self, product, price):
        listing = {
            "title": f"{product['title']} ({product['condition']})",
            "description": f"A {product['condition']} {product['title']} for sale at ${price:.2f}",
            "price": price
        }
        print(f"[ListingAgent] Created listing: {listing}")
        return listing
