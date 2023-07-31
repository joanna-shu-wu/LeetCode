'''
The output should include the year in ascending order, product ID, current years 
spend, previous years spend and year-on-year growth percentage, rounded to 2 decimal places.


user_transactions Example Input:
transaction_id	product_id	spend	    transaction_date
1341	          123424	    1500.60	  12/31/2019 12:00:00
1423	          123424    	1000.20	  12/31/2020 12:00:00
1623	          123424    	1246.44	  12/31/2021 12:00:00
1322	          123424	    2145.32	  12/31/2022 12:00:00



year	product_id	curr_year_spend	  prev_year_spend	  yoy_rate
2019	123424	    1500.60         	NULL	            NULL
2020	123424    	1000.20	          1500.60         	-33.35
2021	123424    	1246.44         	1000.20         	24.62
2022	123424    	2145.32	          1246.44	          72.12

'''

WITH yearly_spend AS (
  SELECT 
    EXTRACT(YEAR FROM transaction_date) AS year, 
    product_id,
    spend AS curr_year_spend
  FROM user_transactions
), 
yearly_variance AS (
  SELECT 
    *, 
    LAG(curr_year_spend, 1) OVER (
      PARTITION BY product_id
      ORDER BY product_id, year) AS prev_year_spend 
  FROM yearly_spend) 

SELECT 
  year,
  product_id, 
  curr_year_spend, 
  prev_year_spend, 
  ROUND(100 * (curr_year_spend - prev_year_spend)/ prev_year_spend,2) AS yoy_rate 
FROM yearly_variance;