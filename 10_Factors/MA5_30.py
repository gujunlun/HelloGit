#MA5_30
def run_formula(dv):
    MA5_30 = dv.add_formula('MA5_30',
               "-Ts_Mean(close,5)/Ts_Mean(close,30)"
               , is_quarterly=False)
    return MA5_30