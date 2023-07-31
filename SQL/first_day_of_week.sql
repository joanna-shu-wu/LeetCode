WITH first_day_week AS (
    SELECT 
        EXTRACT(WEEK FROM TO_DATE(invoicedate, 'DD/MM/YYYY')) AS week_number,
        DATE(DATE_TRUNC('week', TO_DATE(invoicedate, 'DD/MM/YYYY'))) AS start_of_the_week,
        SUM(quantity * unitprice) AS total_sales
    FROM early_sales
    where Date(TO_DATE(invoicedate, 'DD/MM/YYYY'))=DATE(DATE_TRUNC('week', TO_DATE(invoicedate, 'DD/MM/YYYY')))
    GROUP BY week_number,start_of_the_week
)
SELECT * FROM first_day_week;