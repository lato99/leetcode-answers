-- Write your MySQL query statement below
select temp.customer_number from (select o1.order_number, o1.customer_number
from Orders o1
group by o1.customer_number order by count(*) desc limit 1) as temp;