class AutomobileLoan(object):
    def __init__(self, loanNumber, makeOfAutomobile, modelOfAutomobile, balance):
        self.loanNumber = loanNumber
        self.makeOfAutomobile = makeOfAutomobile
        self.modelOfAutomobile = modelOfAutomobile
        self.balance = balance

auto = AutomobileLoan(
    "94930045322",
    "Honda",
    "Civic",
    "$1,000,000"
)

print("Loan number:", auto.loanNumber)
print("Make:",auto.makeOfAutomobile)
print("Model:",auto.modelOfAutomobile)
print("Balance:",auto.balance)
