#vr_vol24
def run_formula(dv):
    avs=dv.add_formula('avs','Ts_Sum(If(close>Delay(close,1),volume,0),24)',overwrite=True,is_quarterly=False, add_data=True)
    bvs=dv.add_formula('bvs','Ts_Sum(If(close<Delay(close,1),volume,0),24)',overwrite=True,is_quarterly=False, add_data=True)
    cvs=dv.add_formula('cvs','Ts_Sum(If(close>Delay(close,1),volume,0),24)',overwrite=True,is_quarterly=False, add_data=True)
    vr=dv.add_formula('vr','(avs+cvs)/(bvs+cvs)',overwrite=True,is_quarterly=False, add_data=True)
    vr_vol24 = dv.add_formula('vr_vol24', "-vr*Ts_Mean(volume,24)/capital_stk" , is_quarterly=False)
    return vr_vol24