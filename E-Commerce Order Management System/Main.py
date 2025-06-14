import streamlit as st
import pyodbc
import pandas as pd
import os

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Session state initialization
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"
if "selected_product_id" not in st.session_state:
    st.session_state.selected_product_id = None

# Ensure images folder exists
if not os.path.exists("product_images"):
    os.makedirs("product_images")

# DB Connection
def get_connection():
    return pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-I1VB32G\SQLEXPRESS;'
        r'DATABASE=ecommerce_db;'
        r'Trusted_Connection=yes;'
    )

# Fetch all products
def fetch_all_products():
    with get_connection() as conn:
        query = "SELECT ProductID, Name, Price, Stock, ImagePath FROM Product"
        return pd.read_sql(query, conn)

# Fetch all customers
def fetch_customers():
    with get_connection() as conn:
        query = "SELECT * FROM Customer"
        return pd.read_sql(query, conn)

# Fetch all orders
def fetch_orders():
    with get_connection() as conn:
        query = """
        SELECT o.OrderID, c.Name AS CustomerName, p.Name AS Product,
               od.Quantity, od.TotalAmount
        FROM Orders o
        JOIN Customer c ON o.CustomerID = c.CustomerID
        JOIN OrderDetails od ON o.OrderID = od.OrderID
        JOIN Product p ON od.ProductID = p.ProductID;
        """
        return pd.read_sql(query, conn)

# Stored procedure call
def get_customer_orders(customer_id):
    with get_connection() as conn:
        query = f"EXEC GetCustomerOrders @cust_id = {customer_id}"
        return pd.read_sql(query, conn)

# Insert a new order
def insert_order(customer_id, product_id, quantity):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Price, Stock FROM Product WHERE ProductID = ?", product_id)
        row = cursor.fetchone()
        if not row:
            return "❌ Product not found."
        price, stock = row
        if stock < quantity:
            return "❌ Insufficient stock."
        total = price * quantity
        try:
            cursor.execute("BEGIN TRANSACTION")
            cursor.execute("INSERT INTO Orders (CustomerID) VALUES (?)", customer_id)
            order_id = cursor.execute("SELECT @@IDENTITY").fetchval()
            cursor.execute("""
                INSERT INTO OrderDetails (OrderID, ProductID, Quantity, TotalAmount)
                VALUES (?, ?, ?, ?)
            """, order_id, product_id, quantity, total)
            cursor.execute("UPDATE Product SET Stock = Stock - ? WHERE ProductID = ?", quantity, product_id)
            cursor.execute("COMMIT")
            return f"✅ Order {order_id} placed successfully!"
        except Exception as e:
            cursor.execute("ROLLBACK")
            return f"❌ Transaction failed: {e}"

# Add customer 
def add_customer(name, email, phone, address):
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Customer (Name, Email, Phone, Address)
                VALUES (?, ?, ?, ?)
            """, name, email, phone, address)
            conn.commit()
            return "✅ Customer added successfully!"
        except Exception as e:
            return f"❌ Error: {str(e)}"
# Add product with image
def add_product(name, price, stock, image_path):
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Product (Name, Price, Stock, ImagePath)
                VALUES (?, ?, ?, ?)
            """, name, price, stock, image_path)
            conn.commit()
            return "✅ Product added successfully!"
        except Exception as e:
            return f"❌ Error: {str(e)}"


# Admin login function
def admin_login():
    st.subheader("🔐 Admin Login")
    if not st.session_state.is_admin:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.is_admin = True
                st.success("Logged in as admin")
            else:
                st.error("Invalid credentials")
    else:
        st.success("You are logged in as admin.")
        if st.button("Logout"):
            st.session_state.is_admin = False
            st.success("Logged out successfully.")

# Main UI
st.title("🛒 E-Commerce Management")

menu_options = ["🏠 Home", "Add Customer", "View Customers", "View Orders", "Place Order", 
                "Get Customer Orders", "Admin Login", "Add Product"]

menu = st.sidebar.selectbox("Menu", menu_options, index=menu_options.index(st.session_state.menu))

# Menu routing
if menu == "🏠 Home":
    st.subheader("📋 Available Products")
    products = fetch_all_products()
    cols = st.columns(4)
    for idx, row in products.iterrows():
        with cols[idx % 4]:
            if row['ImagePath'] and os.path.exists(row['ImagePath']):
                st.image(row['ImagePath'], use_container_width=True)
            else:
                st.image("https://via.placeholder.com/150", use_container_width=True)

            st.markdown(f"**{row['Name']}**")
            st.markdown(f"💰 **Rs {row['Price']:,}**")
            st.markdown(f"📦 Stock: {row['Stock']}")
            if st.button("🛒 Buy Now", key=f"buy_{row['ProductID']}"):
                st.session_state.selected_product_id = row['ProductID']
                st.session_state.menu = "Place Order"
                st.rerun()

elif menu == "Add Customer":
    st.subheader("🧍 New Customer Registration")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")
    if st.button("Register"):
        msg = add_customer(name, email, phone, address)
        st.success(msg) if msg.startswith("✅") else st.error(msg)

elif menu == "View Customers":
    st.subheader("👥 All Customers")
    st.dataframe(fetch_customers())

elif menu == "View Orders":
    st.subheader("📦 All Orders")
    st.dataframe(fetch_orders())

elif menu == "Place Order":
    st.subheader("🛒 Place New Order")
    if st.session_state.selected_product_id:
        prod_id = st.number_input("Product ID", min_value=1, value=st.session_state.selected_product_id)
    else:
        prod_id = st.number_input("Product ID", min_value=1)
    cust_id = st.number_input("Customer ID", min_value=1)
    qty = st.number_input("Quantity", min_value=1)
    if st.button("Place Order"):
        msg = insert_order(cust_id, prod_id, qty)
        if msg.startswith("✅"):
            st.success(msg)
            st.session_state.selected_product_id = None
        else:
            st.error(msg)

elif menu == "Get Customer Orders":
    st.subheader("🔍 Customer Order Lookup")
    cust_id = st.number_input("Enter Customer ID", min_value=1)
    if st.button("Get Orders"):
        st.dataframe(get_customer_orders(cust_id))

elif menu == "Admin Login":
    admin_login()

elif menu == "Add Product":
    st.subheader("📦 Add Product (Admin Only)")
    if not st.session_state.is_admin:
        st.warning("Admin login required to add products.")
    else:
        name = st.text_input("Product Name")
        price = st.number_input("Price", min_value=0.01, format="%.2f")
        stock = st.number_input("Stock", min_value=0)
        uploaded_image = st.file_uploader("Upload Product Image", type=["png", "jpg", "jpeg"])

        image_path = None
        if uploaded_image is not None:
            image_path = f"product_images/{uploaded_image.name}"
            with open(image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())

        if st.button("Add Product"):
            msg = add_product(name, price, stock, image_path)
            st.success(msg) if msg.startswith("✅") else st.error(msg)
