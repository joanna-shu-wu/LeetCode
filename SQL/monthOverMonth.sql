'''
Aggregate to monthly data
Lag the month to get previous month
Apply the given formula to calculate percent_change
Clean up the result (column selection, renames, ordering, etc)
'''

WITH MY_STARTING_POINT AS (
SELECT *, 
  DATE_TRUNC(MONTH, created_at) as created_at_MONTH 
FROM 
  sf_transactions
)
, CTE_MONTHLY AS (
SELECT 
  created_at_MONTH, 
  SUM(value) as value_SUM 
FROM 
  MY_STARTING_POINT 
GROUP BY 
  created_at_MONTH
)
, CTE_LAGGED AS (
SELECT *, 
  lag(value_sum, 1) over ( partition by NULL order by created_at_MONTH) as Lag_VALUE_SUM_1 --there is no need for a partition by column
from 
  CTE_MONTHLY
)
, CTE_WITH_PCT AS (
SELECT *, 
  ROUND(
    (
      (VALUE_SUM - LAG_VALUE_SUM_1) / LAG_VALUE_SUM_1
    ) * 100, 
    2
  ) AS PERCENT_CHANGE 
FROM 
  CTE_LAGGED
)