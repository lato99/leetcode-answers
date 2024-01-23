-- Write your MySQL query statement below
delete from Person
where id not in 
(select id from (Select min(Pe.id) as id from Person Pe group by Pe.email ) as minIDs );

-- Write your MySQL query statement below
delete P1
from Person P1
Join Person P2 on P1.id>P2.id and P1.email = P2.email;