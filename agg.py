import pandas as pd
Sealed = pd.read_csv('./rowdata/Sealed.csv')
PremierDraft = pd.read_csv('./rowdata/PremierDraft.csv')
TradDraft = pd.read_csv('./rowdata/TradDraft.csv')
OpenSealed_D1_Bo1 = pd.read_csv('./rowdata/OpenSealed_D1_Bo1.csv')
OpenSealed_D1_Bo3 = pd.read_csv('./rowdata/OpenSealed_D1_Bo3.csv')
df = pd.read_csv('./rowdata/STX_balance.csv',delimiter='\t')

df.columns.tolist()
df_wl = df['W/L'].str.split(' - ', expand=True)
df2 = pd.concat([df, df_wl], axis=1)
df3 = df2[df2['Date']!='Details']
df3.columns=df.columns.tolist() + ['wins', 'loses']
df3 = df3[~((df3['wins']=='0') & (df3['loses']=='0'))]

df_Sealed = df3[df3['Format']=='Sealed'].merge(Sealed, on='wins', how='left')
df_Sealed['Entry'] = 2000
df_PremierDraft = df3[df3['Format']=='PremierDraft'].merge(PremierDraft, on='wins', how='left')
df_PremierDraft['Entry'] = 1500
df_TradDraft = df3[df3['Format']=='TradDraft'].merge(TradDraft, on='wins', how='left')
df_TradDraft['Entry'] = 1500
df_OpenSealed_D1_Bo1 = df3[df3['Format']=='OpenSealed_D1_Bo1'].merge(OpenSealed_D1_Bo1, on='wins', how='left')
df_OpenSealed_D1_Bo1['Entry'] = 4500
df_OpenSealed_D1_Bo3 = df3[df3['Format']=='OpenSealed_D1_Bo3'].merge(OpenSealed_D1_Bo3, on='wins', how='left')
df_OpenSealed_D1_Bo3['Entry'] = 4500

df4 = pd.concat([df_Sealed, df_PremierDraft, df_TradDraft, df_OpenSealed_D1_Bo1, df_OpenSealed_D1_Bo3]).sort_values(by='Date')

df4.columns.tolist()
df4['balance'] = df4['gems']-df4['Entry']
df4.sort_values(by='Date', inplace=True)
df4.to_csv('./processed_data/data.csv', index=None)
