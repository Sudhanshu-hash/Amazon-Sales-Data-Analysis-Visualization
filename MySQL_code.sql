-- select * from amazon_data.shorted_data; 

USE amazon_data;
-- 1. Daily Sales Summary
CREATE VIEW daily_sales_summary AS
SELECT Date,SUM(Amount) AS Total_Revenue,SUM(Qty) AS Total_Units_Sold,COUNT(DISTINCT Order_ID) AS Total_Orders FROM amazon_data.shorted_data GROUP BY Date ORDER BY Date;


-- 2. State Performance
CREATE VIEW state_performance AS
SELECT ship_state,SUM(Amount) AS State_Revenue,COUNT(Order_ID) AS State_Order_Count FROM amazon_data.shorted_data GROUP BY ship_state ORDER BY State_Revenue DESC;


-- 3. Product Performance
CREATE VIEW product_performance AS
SELECT SKU,Category,Style,SUM(Amount) AS Product_Revenue,SUM(Qty) AS Units_Sold FROM amazon_data.shorted_data GROUP BY SKU, Category, Style ORDER BY Product_Revenue DESC;


-- 4. Fulfilment Summary
CREATE VIEW fulfilment_summary AS
SELECT Fulfilment,fulfilled_by,COUNT(Order_ID) AS Order_Count,SUM(Amount) AS Total_Revenue FROM amazon_data.shorted_data GROUP BY Fulfilment, fulfilled_by;
