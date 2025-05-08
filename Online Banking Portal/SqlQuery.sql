CREATE DATABASE BankSystemDB;
GO

USE BankSystemDB;
GO

CREATE TABLE Accounts (
    Name NVARCHAR(100) PRIMARY KEY,
    DOB DATE,
    Age INT,
    City NVARCHAR(100),
    NIC NVARCHAR(50),
    Address NVARCHAR(255),
    Password NVARCHAR(100),
    Balance FLOAT
);

select *from Accounts;