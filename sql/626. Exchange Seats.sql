# Write your MySQL query statement below
select case
            when (mod(id,2) = 0) then id - 1
            when (mod(id,2) = 1 and not id = (select max(s2.id) from Seat s2)) then id + 1
            else id
        end as id
        ,student
from Seat order by id asc;