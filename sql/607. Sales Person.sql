-- Write your MySQL query statement below
select sp.name from SalesPerson sp
left join Orders o on o.sales_id = sp.sales_id
inner join Company c on c.com_id = o.com_id and c.name != "RED"; 
