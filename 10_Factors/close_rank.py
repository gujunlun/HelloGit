#close_rank
def run_formula(dv):
    close_rank = dv.add_formula('close_rank',
               "If(close/Delay(close,10)-1>0.01 ,-Ts_Rank(close,60),0)"
               , is_quarterly=False)
    return close_rank



