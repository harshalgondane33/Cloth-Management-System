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
3. Run the script:
   ```bash
   python "cloth management system python code.py"
   ```


## Sample Schema
```sql
CREATE DATABASE cloth;

USE cloth;

CREATE TABLE customer (
  idno CHAR(5) PRIMARY KEY,
  date DATE,
  cust_name VARCHAR(50),
  address VARCHAR(100),
  phno VARCHAR(15),
  amount INT
);

``````
---

## 📂 File
- `cloth management system python code.py` – Main Python script

---

## 🧪 Sample Actions in App
- Register a new customer
- View/update/delete existing customer details
- View types of clothing
- Calculate and update bill based on selected items

---

## 📎 Notes
- You can modify item rates directly in the code (inside the `prices` dictionary).
- Ensure the MySQL service is running and accessible before executing the script.

---

## 📬 Author
**Harshal Gondane**  
[GitHub Profile](https://github.com/harshalgondane33)
