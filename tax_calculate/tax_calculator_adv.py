"""
    1. Create a method which takes state & gross income as arguments & return the net income after deducting the tax
    Federal Tax: 10%
    State Tax: varies
    100 : ON -> 77
"""
FEDERAL_TAX = 0.1
states = {"ON": 0.13, "BC": 0.12, "MN": 0.1}

def tax_calc(state, gross_income):
    after_federal = gross_income - (gross_income * FEDERAL_TAX)

    if state in states:
        net_income = after_federal - (gross_income * states[state])
        return net_income
    else:
        print("State not in the list")
        return None


on_tax = tax_calc("ON", 100)
bc_tax = tax_calc("BC", 100)
mn_tax = tax_calc("MN", 100)
print(on_tax)
print(bc_tax)
print(mn_tax)


