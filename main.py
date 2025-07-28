# main.py

from orchestrator import Orchestrator

if __name__ == "__main__":
    # Example product info (customize for testing)
    product = {
        "name": "Surplus iPhone 12",
        "condition": "good"
    }

    orchestrator = Orchestrator()
    result = orchestrator.run_workflow(product)
    print("\nFinal Output:", result)
