import ollama

class PricingAgent:
    def suggest_price(self, product_info):
        prompt = (
            f"Suggest a reasonable USD price (number only, no $) for this product: {product_info}."
        )
        response = ollama.chat(model='llama3', messages=[
            {"role": "user", "content": prompt}
        ])
        price_str = response['message']['content']
        try:
            # Extract first number from LLM response
            price = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_str)))
        except Exception:
            price = 250.0  # fallback
        print(f"[PricingAgent] LLM suggested price for '{product_info}': ${price}")
        return price
