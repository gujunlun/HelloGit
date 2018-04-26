#alpha34
def run_formula(dv):
    alpha34 = dv.add_formula('alpha34',
               "Ts_Mean(close_adj,12)/close_adj"
               , is_quarterly=False)
    return alpha34


