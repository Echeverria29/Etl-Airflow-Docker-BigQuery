import requests
import pandas as pd

df = pd.DataFrame([requests.get('https://randomuser.me/api/').json()['results'][0] for _ in range(100)])
df.to_csv('customers.csv', index=False)
print('Generated customers.csv!')
