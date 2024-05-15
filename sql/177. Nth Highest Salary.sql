CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      SELECT e.salary 
      FROM Employee as e 
      GROUP BY e.salary
      ORDER BY e.salary DESC
      LIMIT 1 OFFSET N
  );
END