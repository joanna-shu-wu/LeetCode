/*
Return a person name that can fit the elevator max weight 1000 lbs.

Queue table
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+----------------+--------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+----------------+--------------+--------+------+

*/

-- https://www.youtube.com/watch?v=Td452uOq-80
-- use self-join to do the running-sum
select main.person_name
from queue main
join queue sec
on main.turn>=sec.turn
group by main.turn
having sum(sec.weight)<=1000
order by main.turn desc
limit 1