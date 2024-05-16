# Write your MySQL query statement below
select query_name, round(avg(rating / position),2) as quality,  ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name
