-- Write your MySQL query statement below
select d.name Department,e.name Employee ,e.salary Salary
from Employee e
left join Department d on d.id = e.departmentId
where salary = (select max(e2.salary) from Employee e2 where e2.departmentId = e.departmentId group by e2.departmentId)