import sqlite3
import random

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

locations = ["Hyderabad","Delhi","Mumbai","Chennai"]
devices = ["Mobile","Laptop","Tablet"]

for i in range(20):

    amount = random.randint(100,20000)
    hour = random.randint(0,23)

    risk = round(random.random(),2)

    cursor.execute("""
    INSERT INTO transactions
    (user_id,amount,location,device,hour,risk_score)
    VALUES (?,?,?,?,?,?)
    """,(random.randint(1000,2000),amount,
         random.choice(locations),
         random.choice(devices),
         hour,
         risk))

conn.commit()
conn.close()

print("Fake transactions added")