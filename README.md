# Cloth Management System 🧥

A simple Python + MySQL-based console application to manage customer records, view clothing types, and calculate bills.

## Features
- Customer registration (Insert, View, Update, Delete)
- Item rate selection and billing
- Database interaction using MySQL Connector
- Tabular data display using pandas

## Technologies Used
- Python
- MySQL
- Pandas

## How to Run
1. Install requirements: `pip install mysql-connector-python pandas`
2. Set up a MySQL database named `cloth` and a `customer` table with the required columns.
3. Run the script: `python cloth_management.py`

## Sample Schema
```sql
CREATE DATABASE cloth;

USE cloth;

CREATE TABLE customer (
  idno VARCHAR(10) PRIMARY KEY,
  date VARCHAR(20),
  cust_name VARCHAR(50),
  address VARCHAR(100),
  phno VARCHAR(15),
  amount FLOAT
);
