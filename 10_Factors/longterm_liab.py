#longterm_liab
def run_formula(dv):
    longterm_liab = dv.add_formula('longterm_liab',
               "If((tot_non_cur_liab/(tot_assets-total_liab)<2.5) && (tot_non_cur_liab/(tot_cur_assets-tot_cur_liab)<1.1),-pe*pb,0)"
               , is_quarterly=False)
    return longterm_liab


