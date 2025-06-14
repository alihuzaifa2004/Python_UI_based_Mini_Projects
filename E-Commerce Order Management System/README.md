
# 🛒 E-Commerce Management System

This is a Streamlit-based desktop web app that simulates an **E-Commerce Management System** backed by a SQL Server database. The application allows users to view and place orders for products, and provides administrative functionality for managing products and customers.

---

## 🔧 Features

### 👥 Customers
- Add new customers
- View all registered customers
- View individual customer order history

### 🛒 Products
- Browse all available products with images
- Buy products (place orders)
- Admins can add new products with images

### 📦 Orders
- Place new orders
- View all orders
- View specific customer's order history via a stored procedure

### 🔐 Admin
- Login system for admin access
- Admin-only features (like product addition)

---

## 📁 Folder Structure

```
├── app.py                  # Main Streamlit application
├── product_images/         # Folder for storing uploaded product images
├── README.md               # Project documentation (this file)
```

---

## 🛠️ Technologies Used

- **Frontend & App UI:** [Streamlit](https://streamlit.io/)
- **Database:** Microsoft SQL Server
- **Python Libraries:**
  - `pyodbc` – for database connection
  - `pandas` – for data manipulation
  - `os` – for file handling

---

## 🗃️ Database Schema

Ensure the following tables exist in your `ecommerce_db` database:

### `Customer`  
| Column     | Type        |
|------------|-------------|
| CustomerID | INT (PK)    |
| Name       | VARCHAR     |
| Email      | VARCHAR     |
| Phone      | VARCHAR     |
| Address    | TEXT        |

### `Product`  
| Column     | Type        |
|------------|-------------|
| ProductID  | INT (PK)    |
| Name       | VARCHAR     |
| Price      | FLOAT       |
| Stock      | INT         |
| ImagePath  | VARCHAR     |

### `Orders`  
| Column     | Type        |
|------------|-------------|
| OrderID    | INT (PK)    |
| CustomerID | INT (FK)    |

### `OrderDetails`  
| Column     | Type        |
|------------|-------------|
| DetailID   | INT (PK)    |
| OrderID    | INT (FK)    |
| ProductID  | INT (FK)    |
| Quantity   | INT         |
| TotalAmount| FLOAT       |

---

## 🧠 Stored Procedure

Make sure to create the following stored procedure in your database:

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

## ▶️ Running the App

### Step 1: Install Required Libraries
```bash
pip install streamlit pyodbc pandas
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

> Make sure your SQL Server is running and accessible.

---

## 🔑 Default Admin Login

- **Username:** `admin`
- **Password:** `admin123`

---

## 📸 Screenshots

> Add screenshots of UI here (optional)

---

## 📌 Notes

- Ensure SQL Server has TCP/IP enabled and your Python environment has the correct ODBC driver installed.
- Image files are stored locally in the `product_images/` folder.

---

## 📃 License

This project is for educational purposes. Feel free to use and modify.
