"""
    1. Create a method which takes state & gross income as arguments & return the net income after deducting the tax
    Federal Tax: 10%
    State Tax: varies
    100 : ON -> 77
"""
ON_TAX = 0.13
BC_TAX = 0.12
MN_TAX = 0.1


def tax_calc(state, gross_income):
    FEDERAL_TAX = float(gross_income * 0.1)
    match state:
        case "ON":
            STATE_TAX = float(gross_income * ON_TAX)
            net_income = float(gross_income - FEDERAL_TAX - STATE_TAX)
            return net_income

        case "BC":
            STATE_TAX = float(gross_income * BC_TAX)
            net_income = float(gross_income - FEDERAL_TAX - STATE_TAX)
            return net_income

        case "MN":
            STATE_TAX = float(gross_income * MN_TAX)
            net_income = float(gross_income - FEDERAL_TAX - STATE_TAX)
            return net_income


on_tax = tax_calc("ON", 100)
bc_tax = tax_calc("BC", 100)
mn_tax = tax_calc("MN", 100)
print(on_tax)
print(bc_tax)
print(mn_tax)


