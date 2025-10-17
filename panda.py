import pandas as pd
data = pd.read_csv("amazon_sale.csv")
df=pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')
df['ship-postal-code'] = df['ship-postal-code'].fillna(0).astype(int)

cancelled_or_missing_amount = (df['Status'] == 'Cancelled') | (df['Amount'].isna())
df.loc[cancelled_or_missing_amount, 'Amount'] = df.loc[cancelled_or_missing_amount, 'Amount'].fillna(0.0)
df.loc[df['currency'].isna(), 'currency'] = 'INR'

df.loc[df['Status'] == 'Cancelled', 'Courier Status'] = 'Cancelled by Customer'
df['Courier Status'] = df['Courier Status'].fillna('Unknown Status')

df.loc[df['Fulfilment'] == 'Amazon', 'fulfilled-by'] = 'FBA'
df.loc[df['Fulfilment'] == 'Merchant', 'fulfilled-by'] = 'Easy Ship'
print(df.isna().sum())

df['ship-state'] = df['ship-state'].astype(str).str.upper().str.strip()

state_mapping = {
    "RJ": "RAJASTHAN", 
    "RAJSHTHAN": "RAJASTHAN",
    "RAJSTHAN": "RAJASTHAN",
    "PB": "PUNJAB",
    "PUNJAB/MOHALI/ZIRAKPUR": "PUNJAB",
    "NL": "NAGALAND",
    "AR": "ARUNACHAL PRADESH",
    "APO": "ANDHRA PRADESH",
    "NEW DELHI": "DELHI",
    "ORISSA": "ODISHA", 
    "PONDICHERRY": "PUDUCHERRY",
    "": "NOT AVAILABLE",
    }
df['ship-state'] = df['ship-state'].replace(state_mapping)
df = df.dropna(subset=['ship-city', 'ship-state', 'ship-country'])

print("Top 5 Cleaned States:\n", df['ship-state'].value_counts().head(5).to_string())

cleaned_file_name = "shorted_data.csv"
df.to_csv(cleaned_file_name, index=False)
print(df)
