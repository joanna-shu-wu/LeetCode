/*
Return a second highest salary from the employee table

Employee table
+----+--------+
| id | salary | 
+----+--------+
| 1  | 100    | 
| 2  | 200    | 
| 3  | 300    |     
+----+--------+

*/

-- Method 1. 
    -- Pro: handles null well. 
    -- Con: it will have issue if question is asking 3rd, 4th...highest salary
select max(salary) as SecondHighestSalary
from employee
where salary not in (select max(salary) from employee)

-- Method 2
    -- Pro: can handle 3rd, 4th...highest salary well
    -- Con: does not handle null well
select salary as SecondHighestSalary
from employee 
order by salary desc
limit 1 offset 1
