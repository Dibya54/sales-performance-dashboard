-- Use the database
USE sales_db;

-- 1. Check total revenue
SELECT SUM(Sales) AS Total_Revenue
FROM sales;

-- 2. Region-wise revenue
SELECT Region, SUM(Sales) AS Region_Revenue
FROM sales
GROUP BY Region
ORDER BY Region_Revenue DESC;

-- 3. Top-performing products
SELECT Product, SUM(Sales) AS Product_Revenue
FROM sales
GROUP BY Product
ORDER BY Product_Revenue DESC;

-- 4. Monthly sales trend
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month;

-- 5. Profit analysis
SELECT
    Product,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product
ORDER BY Total_Profit DESC;
