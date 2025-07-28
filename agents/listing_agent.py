# agents/listing_agent.py

class ListingAgent:
    """Agent responsible for creating product listings."""

    def create_listing(self, product_info, price):
        """
        Creates a product listing dictionary.
        """
        title = product_info.get('name', 'Unnamed Product')
        condition = product_info.get('condition', 'unknown')
        listing = {
            'title': f"{title} ({condition})",
            'description': f"A {condition} {title} for sale at ${price:.2f}",
            'price': price
        }
        print(f"[ListingAgent] Created listing: {listing}")
        return listing
