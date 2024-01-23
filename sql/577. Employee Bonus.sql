

-- Write your MySQL query statement below
select E.name, B.bonus from Employee E
Left Join Bonus B on E.empId = B.empId where B.bonus < 1000 or not exists (select * from3 Bonus B2 where B2.empId = E.empId);


-- Write your MySQL query statement below
select e.name, b.bonus from Employee e
left join Bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus is null;