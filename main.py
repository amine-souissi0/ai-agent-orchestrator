from orchestrator import Orchestrator

if __name__ == "__main__":
    product = {
        "title": "Surplus iPhone 12",
        "condition": "good"
    }
    orchestrator = Orchestrator()
    result = orchestrator.run(product)
    print("\nFinal Output:", result)
