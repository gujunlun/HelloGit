#alpha168
def run_formula(dv):
    alpha168 = dv.add_formula('alpha168',
               "(-1*volume/Ts_Mean(volume,20))"
               , is_quarterly=False)
    return alpha168