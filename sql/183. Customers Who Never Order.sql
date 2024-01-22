-- Write your MySQL query statement below
select C.name as Customers from Customers C
where not exists (select * from Orders O where O.customerId = C.id);

-- Write your MySQL query statement below
select C.name as Customers from Customers C 
where C.id not in (Select O.customerId from Orders O);