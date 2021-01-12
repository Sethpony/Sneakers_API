'''
We will use this to upload data from csv into the postgres database
'''

import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()

#data = (Index_ID, Order_Date, Brand, Sneaker_Name, Sale_Price, Retail_Price, Release_Date, Shoe_Size, Buyer_Region)
with open('stockX.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)#Skips the header row
    for row in reader:
        cur.execute("INSERT INTO sneaker_model (Index_ID, Order_Date, Brand, Sneaker_Name, Sale_Price, Retail_Price, Release_Date, Shoe_Size, Buyer_Region) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s);", (Index_ID, Order_Date, Brand, Sneaker_Name, Sale_Price, Retail_Price, Release_Date, Shoe_Size, Buyer_Region))
