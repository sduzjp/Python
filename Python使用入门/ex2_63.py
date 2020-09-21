#程序文件ex2_63.py
import tushare as ts
import pandas as pd

year = 2020
df1 = ts.get_profit_data(year, 1)  #读入第一季度的数据
df2 = ts.get_growth_data(year, 1)
df3 = ts.get_cashflow_data(year, 1)
merge = pd.merge(df1[['code', 'net_profit_ratio', 'roe', 'eps']],
                    df2[['code', 'nprg', 'nav']], on='code', how='left')
merge = pd.merge(merge, df3[['code', 'cf_nm', 'cashflowratio']],
                    on='code', how='left').dropna()
focus = merge.sort_values(['nprg', 'net_profit_ratio', 'cf_nm',
                           'nav', 'roe', 'eps', 'cashflowratio'],
                          ascending=False)
if len(focus) >= 30:
    select = focus[['code', 'nprg', 'net_profit_ratio', 'cf_nm', 'nav',
                    'roe', 'eps', 'cashflowratio']].head(30)
else:
     select = focus[['code', 'nprg', 'net_profit_ratio', 'cf_nm', 'nav',
                    'roe', 'eps', 'cashflowratio']]
select.to_csv('focus'+str(year)+str(1)+'.csv')
