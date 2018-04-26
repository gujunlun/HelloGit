#CapitalSurplusFundPS
def run_formula(dv):
    CapitalSurplusFundPS = dv.add_formula('CapitalSurplusFundPS',
               "capital_reser/capital_stk"
               , is_quarterly=False)
    return CapitalSurplusFundPS