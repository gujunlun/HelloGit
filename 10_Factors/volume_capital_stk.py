#volume_capital_stk
def run_formula(dv):
    volume_capital_stk = dv.add_formula('volume_capital_stk',
               "If((pb<3) && (pe<30),Ts_Mean(volume,10)/(capital_stk*Ts_Mean(close,10)),0)"
               , is_quarterly=False)
    return volume_capital_stk





