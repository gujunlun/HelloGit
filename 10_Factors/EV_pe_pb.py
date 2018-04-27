#EV_pe_pb
def run_formula(dv):
    EV_pe_pb = dv.add_formula('EV_pe_pb',
               "Log((capital_stk*Ts_Mean(close,60)+total_liab-end_bal_cash))/(pb*pe)"
               , is_quarterly=False)
    return EV_pe_pb



