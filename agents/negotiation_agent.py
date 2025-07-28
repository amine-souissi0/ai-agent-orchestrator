import ollama

class NegotiationAgent:
    def handle_negotiation(self, listing):
        # Simulate a buyer offer
        import random
        buyer_offer = round(listing['price'] * random.uniform(0.75, 0.95), 2)
        print(f"[NegotiationAgent] Buyer offers ${buyer_offer:.2f} (asking: ${listing['price']:.2f})")

        # LLM prompt: Should we accept, counter, or reject?
        prompt = (
            f"You are a negotiation agent. The product is: {listing['title']}. Asking price: ${listing['price']:.2f}. "
            f"Buyer offers: ${buyer_offer:.2f}.\n"
            f"Should we 'accept', 'counter', or 'reject'? If counter, suggest a counter-offer price. "
            "Reply in JSON as: {{'decision': 'accept/counter/reject', 'counter_offer': price or null}}"
        )
        response = ollama.chat(model='llama3', messages=[{"role": "user", "content": prompt}])
        print(f"[NegotiationAgent] LLM response: {response['message']['content']}")
        # Attempt to parse the JSON-like answer
        import re, json
        # Try to extract a JSON object from the LLM response
        match = re.search(r'\{.*\}', response['message']['content'], re.DOTALL)
        if match:
            try:
                decision_data = json.loads(match.group(0).replace("'", '"'))
            except Exception:
                # Fallback: guess from text
                decision_data = {"decision": "accept", "counter_offer": None}
        else:
            # Fallback if LLM doesn't output JSON
            if "accept" in response['message']['content'].lower():
                decision_data = {"decision": "accept", "counter_offer": None}
            elif "counter" in response['message']['content'].lower():
                decision_data = {"decision": "counter", "counter_offer": listing['price'] * 0.92}
            else:
                decision_data = {"decision": "reject", "counter_offer": None}

        # Make decision
        if decision_data["decision"] == "accept":
            print(f"[NegotiationAgent] Offer accepted at ${buyer_offer:.2f}!")
            return {"accepted": True, "price": buyer_offer, "buyer": "John Doe"}
        elif decision_data["decision"] == "counter" and decision_data["counter_offer"]:
            print(f"[NegotiationAgent] Counter-offering at ${decision_data['counter_offer']:.2f}")
            # For demo, let's say buyer accepts if within 90% of original price
            if decision_data['counter_offer'] <= listing['price'] * 0.9:
                print(f"[NegotiationAgent] Buyer accepts counter-offer at ${decision_data['counter_offer']:.2f}!")
                return {"accepted": True, "price": decision_data['counter_offer'], "buyer": "John Doe"}
            else:
                print("[NegotiationAgent] Buyer rejects counter-offer. No deal.")
                return {"accepted": False}
        else:
            print("[NegotiationAgent] Offer rejected by agent. No deal.")
            return {"accepted": False}
