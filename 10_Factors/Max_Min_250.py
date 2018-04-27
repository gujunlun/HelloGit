#Max_Min_250
def run_formula(dv):
    Max_Min_250 = dv.add_formula('Max_Min_250',
               "close/Ts_Max(close,250)-close/Ts_Min(close,250)"
               , is_quarterly=False)
    return Max_Min_250



