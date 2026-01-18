import sys
import pandas as pd
 
print("arguments", sys.argv) 
month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "Passengers": [32, 41]})
df['month']=month
print(df.head())

print(f"Running pipeline for month {month}")
df.to_parquet(f"output_month_{sys.argv[1]}.parquet")
 