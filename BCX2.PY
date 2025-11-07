import pandas as pd
df = pd.read_csv('./clean_data_after_eda.csv')

df["date_activ"]=pd.to_datetime(df["date_activ"],format='%Y-%m-%d')
df["date_end"]=pd.to_datetime(df["date_end"],format='%Y-%m-%d')
df["date_modif_prod"]=pd.to_datetime(df["date_modif_prod"],format='%Y-%m-%d')
df["date_renewal"]=pd.to_datetime(df["date_renewal"],format='%Y-%m-%d')

print(df.head(3))

price_df = pd.read_csv('./price_data (1).csv')
price_df["price_date"]=pd.to_datetime(price_df["price_date"], format='%Y-%m-%d')
print(price_df.head())


monthly_price_by_id= price_df.groupby(['id','price_date']).agg({'price_off_peak_var':'mean','price_off_peak_fix':'mean'}).reset_index()
jan_prices=monthly_price_by_id.groupby('id').first().reset_index()
dec_prices=monthly_price_by_id.groupby('id').last().reset_index()

diff=pd.merge(dec_prices.rename(columns={'price_off_peak_var':'dec_1','price_off_peak_fix':'dec_2'}),jan_prices.drop(columns='price_date'),on='id')
diff['offpeak_diff_dec_january_energy'] = diff['dec_1'] - diff['price_off_peak_var']
diff['offpeak_diff_dec_january_power'] = diff['dec_2'] - diff['price_off_peak_fix']
diff = diff[['id', 'offpeak_diff_dec_january_energy','offpeak_diff_dec_january_power']]
print(diff.head())


price_df["price_year"]=price_df["price_date"].dt.year
price_df["price_month"]=price_df["price_date"].dt.month
df["contract_duration_days"]=(df["date_end"]-df["date_activ"]).dt.days
price_df["price_difference"]=(price_df["price_peak_var"]-price_df["price_off_peak_var"])
merge_1=pd.merge(df,price_df,on="id")
print(merge_1.head())

