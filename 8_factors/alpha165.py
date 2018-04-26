#alpha165
def run_formula(dv):
    alpha165 = dv.add_formula('alpha165',
               '-(Ts_Max(Ts_Sum(close-Ts_Mean(close,48),{}),{})-Ts_Min(Ts_Sum(close-Ts_Mean(close,48),{}),{})/StdDev(close,48))'.format(5,5,5,5)
               , is_quarterly=False)
    return alpha165