#MA_5
def run_formula(dv):
    MA_5 = dv.add_formula('MA_5',
               "-Ts_Mean(close,5)"
               , is_quarterly=False)
    return MA_5