Create Table Orders(
    ord_no int,
    purch_amt decimal(6,2),
    ord_date date,
    customer_id int,
    salesman_id int
)

-- Write a query to count the number of salesman. Return number of salesman

-- use distinct to choose the unique salesman
select count(distinct salesman_id) from orders