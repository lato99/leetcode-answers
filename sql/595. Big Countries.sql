-- Write your MySQL query statement below
select name, World.population, World.area from World
where (3 * power(10,6)) <= World.area or population >= (25*Power(10,6)) ;