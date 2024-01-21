-- Write your MySQL query statement below
SELECT firstName,lastName,city,state
from Person
left join Address on Person.personId = Address.personId;

-- Since the personID are same in both tables, we can also use 'USING' with left join
-- Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a USING (personID);