#InvestCash_GrowRate
def run_formula(dv):
    InvestCash_GrowRate = dv.add_formula('InvestCash_GrowRate',
               "TTM(net_cash_flows_inv_act)/Delay(TTM(net_cash_flows_inv_act),1)-1"
               , is_quarterly=True)
    return InvestCash_GrowRate