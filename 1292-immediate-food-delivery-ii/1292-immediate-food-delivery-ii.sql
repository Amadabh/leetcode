# Write your MySQL query statement below
-- select customer_id, order_date, rank() over(partition by customer_id order by order_date) as rnk from Delivery;
-- select customer_id,order_date, count(cusotmer_id) as cnt  from Delivery where order_date=customer_pref_delivery_date group by customer_id;

select round(avg(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100,2) as immediate_percentage from delivery t right join (
select customer_id,min(order_date) as mn from Delivery group by customer_id) as q on t.customer_id=q.customer_id and t.order_date=q.mn;
