#roe_profitgrowth_pe
def run_formula(dv):
    roe_profitgrowth_pe = dv.add_formula('roe_profitgrowth_pe',
               "Log(TTM(roe)*TTM(net_profit)/Delay(TTM(net_profit),4)/(TTM(pe)*TTM(pb)))"
               , is_quarterly=True)
    return roe_profitgrowth_pe

