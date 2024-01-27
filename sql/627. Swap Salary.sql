-- Write your MySQL query statement below
update Salary s
set s.sex = 
case sex 
when "m" then "f"
else "m"
end;

-- Different syntax
-- update salary set sex = 
-- case 
-- when sex = "m" then "f"
-- else "m"
-- end;