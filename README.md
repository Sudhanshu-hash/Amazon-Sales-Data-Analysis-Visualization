# Amazon-Sales-Data-Analysis-Visualization

Goal: To transform raw e-commerce sales data into an interactive Power BI dashboard, providing actionable insights into daily trends, geographical performance, top-selling products, and fulfillment efficiency.

1. Data Source and Cleaning
Source: [https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data]
Initial Data: Raw data was stored in amazon_sale.csv.
Cleaning: The Python script (pandy.py) was used to perform the following steps:
*Handle missing values in 'ship_state'.
*Convert 'Date' column to datetime format.
*Cast 'Amount' and 'Qty' columns to numeric types for aggregation.

2. Database (MySQL) Aggregation
Purpose: Data was loaded into a MySQL database (amazon_data schema) to leverage SQL for efficient pre-aggregation.
Logic: The script (MySQL_code) created four optimized views to manage complexity and improve dashboard performance:
*daily_sales_summary (For time trends)
*state_performance (For geospatial analysis)
*product_performance (For top seller analysis)
*fulfilment_summary (For operational analysis)

3. Key Findings and Dashboard Components
   Visual Component	      Insight Provided	                                    SQL View Used
1. KPI Cards              Total Revenue, Total Orders, AOV.                     All Views
2. Line Chart             Daily Revenue Trends (Seasonal spikes/drops).         daily_sales_summary
3. Ranked Bar Chart       Top 10 Best Selling Product Categories/SKUs           product_performance
4. Filled Map             Geographical performance ranking by state revenue.    state_performance
5. Donut Chart	          Operational Efficiency by fulfillment types.          fulfilment_summary

4. Conclusion
This project successfully demonstrates technical proficiency across the data stack, resulting in an accurate and performant dashboard that is ready for business decision-making.

---

5. ***Connect with Me***
If you have any questions about this project, want to discuss data strategy, or are interested in collaboration, feel free to connect!
| **LinkedIn** | Sudhanshu Joshi (https://www.linkedin.com/in/sudhanshu-joshi15) |
| **Email** | sudhanshujoshi6009@gmail.com |

