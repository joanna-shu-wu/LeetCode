'''
Sometimes, payment transactions are repeated by accident;
It could be due to user error, API failure or a retry error that causes a credit card to be charged twice.

Using the transactions table, identify any payments made at the same merchant with the same credit card for the same amount within 10 minutes of each other. 
Count such repeated payments.

transactions Example Input:
transaction_id	merchant_id	credit_card_id	amount	transaction_timestamp
1	            101	        1	            100	    09/25/2022 12:00:00
2	            101	        1	            100	    09/25/2022 12:08:00
3	            101	        1	            100	    09/25/2022 12:28:00
4	            102	        2	            300	    09/25/2022 12:00:00
6	            102	        2	            400	    09/25/2022 14:00:00


'''
WITH payments AS (
  SELECT 
    merchant_id, 
    EXTRACT(EPOCH FROM transaction_timestamp - 
            LAG(transaction_timestamp) OVER( PARTITION BY merchant_id, credit_card_id, amount 
                                             ORDER BY transaction_timestamp)
            )/60 AS minute_difference 
  FROM transactions
) 
SELECT COUNT(merchant_id) AS payment_count
FROM payments 
WHERE minute_difference <= 10;