import pandas as pd

accounts = pd.read_csv('accounts.csv')

# print(accounts.to_string()) 

chat1=pd.read_csv('chat_messages_1.csv')
#print(f"column types:\n{chat1.dtypes}")
chat1.sort_values(by=['alliance_id'])
print(chat1.to_string())
alliance_mem = pd.read_csv('alliance_membership.csv')
alliance_mem.sort_values(by=['alliance_id'])
print(alliance_mem.head())
#print(f"column types:\n{alliace_mem.dtypes}")

