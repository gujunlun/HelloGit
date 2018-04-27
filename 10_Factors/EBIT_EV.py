#EBIT_EV
def run_formula(dv):
    EBIT_EV = dv.add_formula('EBIT_EV',
               "(tot_profit+less_int_exp-int_income)/(capital_stk*Ts_Mean(close,60)+total_liab-end_bal_cash)"
               , is_quarterly=False)
    return EBIT_EV





