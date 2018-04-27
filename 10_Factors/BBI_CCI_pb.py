#BBI_CCI_pb
def run_formula(dv):
    BBI_after=dv.add_formula('BBI_after','(Ts_Mean(close,3)+Ts_Mean(close,6)+Ts_Mean(close,12)+Ts_Mean(close,24))/4',overwrite=True, is_quarterly=False, add_data=True)
    TYP=dv.add_formula('TYP','(close+high+low)/3',overwrite=True, is_quarterly=False, add_data=True)
    MATYP=dv.add_formula('MATYP','Ts_Mean(TYP,20)',overwrite=True, is_quarterly=False, add_data=True)
    DEV=dv.add_formula('DEV','Ts_Sum(Abs(TYP-MATYP),20)',overwrite=True, is_quarterly=False, add_data=True)
    CCI=dv.add_formula('CCI','(TYP-MATYP)/0.015/DEV',overwrite=True, is_quarterly=False, add_data=True)
    BBI_CCI_pb = dv.add_formula('BBI_CCI_pb',
               "(-Log(BBI_after)-Log(CCI))*pb"
               , is_quarterly=False)
    return BBI_CCI_pb




