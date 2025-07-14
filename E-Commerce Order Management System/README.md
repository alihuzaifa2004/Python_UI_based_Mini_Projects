# 🛒 E-Commerce Management System (Python + Streamlit + SQL Server)

This is a complete **E-Commerce Management System** built using **Python Streamlit** for the frontend and **SQL Server** as the backend database. The application allows customers to view products and place orders, while admins can add new products and manage customer data.

---

## 🚀 Features

### 👨‍💼 Admin Features
- 🔐 Secure Admin Login
- ➕ Add new products with images
- 📦 View all customer orders
- 🧍 View all registered customers

### 🧍 Customer Features
- 📝 Register as a new customer
- 🛒 View all available products
- 📤 Place new orders
- 🔎 View individual order history using a stored procedure

---

## 🛠️ Technologies Used

| Component          | Tech Stack                    |
|--------------------|-------------------------------|
| Frontend           | [Streamlit](https://streamlit.io) |
| Backend (Database) | SQL Server                    |
| Language           | Python                        |
| Database Access    | `pyodbc`                      |
| Data Handling      | `pandas`                      |
| File Handling      | `os`, Image Uploads           |

---

## 📂 Project Structure

```plaintext
ecommerce_app/
│
├── product_images/               # Stores uploaded product images
├── Main.py              # Main Streamlit app code
├── SQL_Query.sql              
└── README.md                     # Project documentation (this file)
````

---

## 🖼️ Screenshots

| Home Page                                                         | Admin Add Product                                              |
| ----------------------------------------------------------------- | -------------------------------------------------------------- |
| ![Home](https://via.placeholder.com/400x250?text=Product+Listing) | ![Admin](https://via.placeholder.com/400x250?text=Admin+Panel) |

---

## 🧾 SQL Server Setup

### ✅ Required Tables

```sql
CREATE TABLE Customer (
    CustomerID INT IDENTITY PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

CREATE TABLE Product (
    ProductID INT IDENTITY PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2),
    Stock INT,
    ImagePath VARCHAR(255)
);

CREATE TABLE Orders (
    OrderID INT IDENTITY PRIMARY KEY,
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
    Quantity INT,
    TotalAmount DECIMAL(10,2)
);
```

### 🛠 Stored Procedure

```sql
CREATE PROCEDURE GetCustomerOrders
    @cust_id INT
AS
BEGIN
    SELECT o.OrderID, p.Name AS Product, od.Quantity, od.TotalAmount
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Product p ON od.ProductID = p.ProductID
    WHERE o.CustomerID = @cust_id;
END
```

---

## 🔁 Transaction and Rollback Logic

The system ensures database consistency using SQL transactions. When placing an order:

1. It checks stock availability.
2. Inserts the order into `Orders` and `OrderDetails`.
3. Updates product stock.
4. If any step fails, the transaction is rolled back.

---

## 🔐 Admin Credentials (Default)

```
Username: admin
Password: admin123
```

---

## 🧪 How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Make sure your SQL Server instance is running and update the connection string if needed:

   ```python
   SERVER=DESKTOP-I1VB32G\SQLEXPRESS;
   ```

3. Run the app:

   ```bash
   streamlit run ecommerce_app.py
   ```

---

## 📦 `requirements.txt`

```txt
streamlit
pyodbc
pandas
```

---

## 📌 Notes

* Make sure the folder `product_images` exists or is automatically created for image storage.
* Ensure the SQL Server has TCP/IP enabled and the correct instance name is used.
* All admin-only features are protected by a basic login.

---


## 👨‍🎓 Author

**Ali Huzaifa Nadeem**  
[GitHub Profile](https://github.com/alihuzaifa2004)


## 📜 License

This project is for **educational purposes** only.
