# AI Multi-Agent Orchestration System

---

## **Overview**

This project demonstrates a multi-agent orchestration system in Python using CrewAI-style patterns.  
It simulates a realistic e-commerce workflow: pricing, listing, negotiation, and logistics.  
**Key features:** modular agent design, clear task delegation, agent-to-agent communication, and robust error handling.

---

## **Project Structure**


ai-agent-orchestrator/
│
├── agents/
│ ├── pricing_agent.py
│ ├── listing_agent.py
│ ├── negotiation_agent.py
│ └── logistics_agent.py
├── orchestrator.py
├── main.py
├── README.md
├── .gitignore
├── mermaid.png
└── seq.png





---

## **How to Run**

1. **Install Ollama (local LLM runtime):**
    - [Download and install from Ollama.com](https://ollama.com/download)
    - Pull the model:
      ```bash
      ollama pull llama3
      ```
    - Start the server (if not already running):
      ```bash
      ollama serve
      ```

2. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-agent-orchestrator.git
    cd ai-agent-orchestrator
    ```

3. **Set up the Python environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Or simply `pip install ollama` if you only use Ollama as LLM client.)

5. **Run the main script:**
    ```bash
    python main.py
    ```

---

## **System Architecture**

### **System Flowchart**

![System Flowchart](./mermaid.png)

### **Sequence Diagram**

![Sequence Diagram](./seq.png)

---

## **Agent Responsibilities**

| Agent               | Responsibility                                                  |
|---------------------|----------------------------------------------------------------|
| **PricingAgent**        | Uses Llama 3 LLM to suggest product price dynamically.            |
| **ListingAgent**        | Creates product listing details (title, description, price).     |
| **NegotiationAgent**    | Uses Llama 3 LLM to negotiate: accept, counter-offer, or reject. |
| **LogisticsAgent**      | Arranges shipping if a sale occurs.                             |

---

## **Key LLM Features & CrewAI Principles**

- **LLM-powered Pricing:**  
  The price suggestion is not hardcoded but comes directly from Llama 3, taking into account product condition and context.
- **LLM-powered Negotiation:**  
  Buyer’s offer and scenario are provided to Llama 3, which returns an intelligent negotiation strategy (accept/counter/reject with counter-offer price).
- **LLM Orchestration Decisions (NEW!):**  
  If negotiation fails, the main orchestrator itself asks Llama 3 what to do next—retry, wait for new buyer, or stop—making the workflow adaptive.
- **Modular, extensible, and readable code:**  
  Follows CrewAI-inspired agent patterns for clear role separation and easy future upgrades.

---

## **Sample Output (Real LLM Reasoning)**

[Orchestrator] Starting orchestration...
[PricingAgent] LLM suggested price for 'Surplus iPhone 12 (good)': $450.0
[ListingAgent] Created listing: {'title': 'Surplus iPhone 12 (good)', ...}
[NegotiationAgent] Buyer offers $353.72 (asking: $450.00)
[NegotiationAgent] LLM response: {'decision': 'counter', 'counter_offer': 400.00}
[NegotiationAgent] Offer accepted at $353.72!
[LogisticsAgent] Shipping arranged: {...}
[Orchestrator] Workflow complete.

Final Output: {'recipient': 'John Doe', 'item': 'Surplus iPhone 12 (good)', ...}


---

## **How This Project Meets Assessment Requirements**

| Requirement                            | How Addressed                                                 |
|-----------------------------------------|--------------------------------------------------------------|
| Central AI Orchestrator                 | `orchestrator.py`, coordinates all agents and workflow       |
| 3-4 Specialized Agents                  | Pricing, Listing, Negotiation, Logistics in `agents/`        |
| Communication Between Agents            | Orchestrator passes info between agents and collects results |
| Simple Data Flow Management             | Each step’s output is input for the next, coordinated by orchestrator |
| Orchestrator Delegates Tasks            | `orchestrator.py` calls agent methods in sequence            |
| At least 2-3 LLM-powered agents         | Pricing and Negotiation agents use real Llama 3 via Ollama   |
| Inter-agent Communication               | Negotiation agent receives listing/pricing info, returns results to orchestrator |
| Error Handling & Task Coordination      | Orchestrator manages retries/alternatives based on LLM advice |
| Diagrams/Architecture Documentation     | `mermaid.png`, `seq.png` included in README                  |
| Bonus: LLM-powered Orchestrator Decision| Orchestrator queries Llama 3 for next actions on failed negotiation |

---

## **Design Decisions & Improvements (vs Previous Version)**

- **Upgraded from hardcoded logic to real AI decision-making at each stage.**
- **LLM added to both pricing and negotiation for more realistic, context-aware responses.**
- **Main orchestrator now makes adaptive, scenario-driven decisions based on LLM reasoning, not fixed rules.**
- **Code is modular for easy extension (e.g., swap to Gemini API or add more agent roles).**

---



## **Author**

Amine Souissi  
*Built for SurplusLoop Technical Assessment*

---

## **Contact**

[aminisouissi@gmail.com}





amine souissi  
*Built for SurplusLoop Technical Assessment*
