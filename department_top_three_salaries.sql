show databases;
use leetcode;
show tables;

desc Employee;
desc Department;

select * from Employee;
select * from Employee
order by DepartmentId, Salary desc;

select * from Employee e1, Employee e2
where e1.DepartmentId = e2.DepartmentId;
select * from Employee e1, Employee e2
where e1.DepartmentId = e2.DepartmentId
and e1.Salary > e2.Salary;

select 5;
select (select 5);
select (select 5) from Employee;

select t.row1 from (
  select 5 as row1
) as t;

select 6 as kk from Employee
where 4 in (select 4)
and 2 < (select 6);

select * from Employee;
select *, count(*), count(*) = 1 from Employee e1, Employee e2
where e1.Salary >= e2.Salary
group by e2.Salary;
# having count(*) = 2;

select (1 or null);
select Id or null from Employee where 1 = 1;
select Id from Employee where 1 = 1;
select Id from Employee where 1 = 1
union
select null
limit 2;

explain (select Id from Employee where 1 = 1 order by Id desc)
union all
(select null)
union all
(select null)
order by Id desc
limit 13;

explain select max(Salary) from Employee
where Salary < (select max(Salary) from Employee);
