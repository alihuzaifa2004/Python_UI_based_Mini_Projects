CREATE DATABASE ecommerce_db;
USE ecommerce_db;
GO

-- Customer Table
CREATE TABLE Customer (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Address TEXT NOT NULL
);
GO

-- Product Table
CREATE TABLE Product (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price > 0),
    Stock INT NOT NULL CHECK (Stock >= 0),
    ImagePath VARCHAR(255) -- <-- updated column name
);
GO

-- Orders Table
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
GO

-- OrderDetails Table
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    TotalAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
GO

-- Indexes for optimization
CREATE INDEX idx_customer_email ON Customer(Email);
CREATE INDEX idx_product_name ON Product(Name);
GO

-- Insert sample data
INSERT INTO Customer (Name, Email, Phone, Address) VALUES 
('Alice', 'alice@example.com', '1234567890', 'Karachi'),
('Bob', 'bob@example.com', '9876543210', 'Lahore'),
('Charlie', 'charlie@example.com', '1122334455', 'Islamabad');
GO

INSERT INTO Product (Name, Price, Stock, ImagePath) VALUES 
('Laptop', 1200.00, 10, 'product_images/laptop.jpg'),
('Mouse', 25.00, 100, 'product_images/mouse.jpg'),
('Keyboard', 45.00, 80, 'product_images/keyboard.jpg'),
('Monitor', 250.00, 50, 'product_images/monitor.jpeg');
GO

INSERT INTO Orders (CustomerID) VALUES (1), (2), (3);
GO

INSERT INTO OrderDetails (OrderID, ProductID, Quantity, TotalAmount) VALUES 
(1, 1, 1, 1200.00),
(1, 2, 2, 50.00),
(2, 2, 3, 75.00),
(2, 3, 1, 45.00),
(3, 4, 1, 250.00);
GO

-- Stored Procedure: GetCustomerOrders
IF OBJECT_ID('GetCustomerOrders', 'P') IS NOT NULL
    DROP PROCEDURE GetCustomerOrders;
GO

CREATE PROCEDURE GetCustomerOrders
    @cust_id INT
AS
BEGIN
    SELECT o.OrderID, o.OrderDate, p.Name AS Product, od.Quantity, od.TotalAmount
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Product p ON od.ProductID = p.ProductID
    WHERE o.CustomerID = @cust_id
    ORDER BY o.OrderDate DESC
END;
GO

-- Trigger to prevent negative stock (keep it for extra safety)
IF OBJECT_ID('trg_PreventNegativeStock', 'TR') IS NOT NULL
    DROP TRIGGER trg_PreventNegativeStock;
GO

CREATE TRIGGER trg_PreventNegativeStock
ON OrderDetails
AFTER INSERT
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM inserted i
        JOIN Product p ON i.ProductID = p.ProductID
        WHERE i.Quantity > p.Stock
    )
    BEGIN
        RAISERROR('Not enough stock available.', 16, 1);
        ROLLBACK TRANSACTION;
    END
END;
GO

-- SELECT example to view orders
SELECT 
    o.OrderID, 
    c.Name AS CustomerName, 
    p.Name AS Product, 
    od.Quantity, 
    od.TotalAmount
FROM Orders o
JOIN Customer c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Product p ON od.ProductID = p.ProductID;
GO
