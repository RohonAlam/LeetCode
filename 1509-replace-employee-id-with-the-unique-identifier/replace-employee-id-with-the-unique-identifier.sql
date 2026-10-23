# Write your MySQL query statement below
select t2.unique_id , t1.name 
from EmployeeUNI as t2
right join Employees as t1
on t2.id = t1.id

