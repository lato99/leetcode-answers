--  Write your MySQL query statement below
Select max(x.SingleNumbers) as num from
(Select num SingleNumbers from MyNumbers 
group by num
having count(num) = 1) as x;