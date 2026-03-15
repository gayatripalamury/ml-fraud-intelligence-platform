import pandas as pd
import numpy as np
np.random.seed(42)
rows = 10000
data = {
 "user_id": np.random.randint(1000,2000,size=rows),
 "amount": np.random.exponential(scale=3000,size=rows),
 "hour": np.random.randint(0,24,size=rows),
 "device_change": np.random.randint(0,2,size=rows),
 "location_change": np.random.randint(0,2,size=rows)
}
df = pd.DataFrame(data)
df["fraud"] = (
 (df["amount"] > 10000) |
 ((df["hour"] < 5) & (df["location_change"]==1))
).astype(int)
df.to_csv("data/sample_transactions.csv",index=False)
print("Dataset generated")