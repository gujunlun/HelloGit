#Mean5_Std20
def run_formula(dv):
    Mean5_Std20 = dv.add_formula('Mean5_Std20',
               "Log(Ts_Mean(close,5)/StdDev(volume,20))"
               , is_quarterly=False)
    return Mean5_Std20