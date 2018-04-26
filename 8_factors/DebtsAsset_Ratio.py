#DebtsAsset_Ratio
def run_formula(dv):
    DebtsAsset_Ratio = dv.add_formula('DebtsAsset_Ratio',
               "total_liab/tot_assets"
               , is_quarterly=False)
    return DebtsAsset_Ratio