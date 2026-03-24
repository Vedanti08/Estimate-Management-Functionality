# Estimation Management System (Single File Project)

import mysql.connector
from datetime import datetime

# 🔹 Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword"   # 🔸 Change your MySQL password
)

cursor = db.cursor()

# 🔹 Step 1: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS estimation_db")
cursor.execute("USE estimation_db")

# 🔹 Step 2: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS estimation (
    estimated_id INT PRIMARY KEY AUTO_INCREMENT,
    chain_id INT,
    group_name VARCHAR(50),
    brand_name VARCHAR(50),
    zone_name VARCHAR(50),
    service VARCHAR(100),
    qty INT,
    cost_per_unit FLOAT,
    total_cost FLOAT,
    delivery_date DATE,
    delivery_details VARCHAR(100),
    created_at DATETIME,
    updated_at DATETIME
)
""")

# 🔹 Step 3: Insert Sample Data
chain_id = 1
group_name = "Group A"
brand_name = "Brand X"
zone_name = "Zone 1"
service = "Cleaning Service"
qty = 10
cost_per_unit = 50

total_cost = qty * cost_per_unit
delivery_date = "2026-03-30"
delivery_details = "Fast Delivery"
now = datetime.now()

cursor.execute("""
INSERT INTO estimation 
(chain_id, group_name, brand_name, zone_name, service, qty, cost_per_unit, total_cost, delivery_date, delivery_details, created_at, updated_at)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (chain_id, group_name, brand_name, zone_name, service, qty, cost_per_unit, total_cost, delivery_date, delivery_details, now, now))

db.commit()

# 🔹 Step 4: Display Data (Dashboard Output)
print("\n📊 ESTIMATION DASHBOARD\n")
cursor.execute("SELECT * FROM estimation")

for row in cursor.fetchall():
    print(f"""
ID: {row[0]}
Chain ID: {row[1]}
Group: {row[2]}
Brand: {row[3]}
Zone: {row[4]}
Service: {row[5]}
Quantity: {row[6]}
Cost per Unit: {row[7]}
Total Cost: {row[8]}
Delivery Date: {row[9]}
Details: {row[10]}
Created At: {row[11]}
Updated At: {row[12]}
----------------------------------------
""")

# 🔹 Close Connection
cursor.close()
db.close()