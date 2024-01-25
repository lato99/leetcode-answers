-- Write your MySQL query statement below
select max(e2.salary) as SecondHighestSalary from Employee e2
where e2.salary <(select max(e.salary) from Employee e);