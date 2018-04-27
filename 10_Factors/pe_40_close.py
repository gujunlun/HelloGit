#pe_40_close
def run_formula(dv):
    pe_40_close = dv.add_formula('pe_40_close',
               "If((pe<40) && (close/Delay(close,10)-1<0.1),close/Delay(close,10),0)"
               , is_quarterly=False)
    return pe_40_close



