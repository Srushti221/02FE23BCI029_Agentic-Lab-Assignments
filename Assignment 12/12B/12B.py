"""Assignment 12B - Require evaluation after every five proposals.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a rule that the agent must be re-evaluated (call `evaluate()` again) after every 5 proposals it has made. Track the proposal count, and demonstrate a 6th proposal being blocked with a clear message until `evaluate()` is called again.
"""
class GovernedAgent:
    def __init__(self):
        self.proposal_count = 0
        self.evaluation_required = False
    def evaluate(self):
        self.evaluation_required = False
        self.proposal_count = 0
        print("Evaluation completed. Proposal counter reset to 0.")
    def propose(self, proposal):
        if self.evaluation_required:
            print(f"BLOCKED: {proposal} cannot be submitted until evaluate() is called.")
            return False
        self.proposal_count += 1
        print(f"Proposal {self.proposal_count} accepted: {proposal}")
        if self.proposal_count == 5:
            self.evaluation_required = True
            print("Five proposals reached. Mandatory re-evaluation is now required.")
        return True

if __name__ == "__main__":
    agent = GovernedAgent()
    for number in range(1, 7): agent.propose(f"change-{number}")
    print("\nCalling evaluate():")
    agent.evaluate()
    agent.propose("change-6-after-evaluation")
