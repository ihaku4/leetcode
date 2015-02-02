CREATE DATABASE IF NOT EXISTS leetcode;
USE leetcode;

DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee (
  Id int,
  Name varchar(255),
  Salary int,
  DepartmentId int
);

DROP TABLE IF EXISTS Department;
CREATE TABLE IF NOT EXISTS Department (
  Id int,
  Name varchar(255)
);

INSERT INTO Employee(Id, Name, Salary, DepartmentId)
VALUES (1, 'Joe', 70000, 1);
INSERT INTO Employee(Id, Name, Salary, DepartmentId)
VALUES (2, 'Henry', 80000, 2);
INSERT INTO Employee(Id, Name, Salary, DepartmentId)
VALUES (3, 'Sam', 60000, 2);
INSERT INTO Employee(Id, Name, Salary, DepartmentId)
VALUES (4, 'Max', 90000, 1);

INSERT INTO Department(Id, Name)
VALUES (1, 'IT');
INSERT INTO Department(Id, Name)
VALUES (2, 'Sales');

SELECT d.`Name`, e.`Name`, e.`Salary`
from Employee e 
left join Department d 
  on e.DepartmentId = d.Id
where (e.Salary, e.DepartmentId) in (
  select max(e.Salary), d.Id
  from Employee e 
  left join Department d 
    on e.DepartmentId = d.Id
  group by d.Id
)
order by d.Id
;

SELECT d.`Name`, e.`Name`, e.`Salary`
from Employee e 
left join Department d 
  on e.DepartmentId = d.Id
where (e.Salary, e.DepartmentId) in (
  select max(e.Salary), d.Id
  from Employee e 
  group by e.DepartmentId
)
order by d.Id
;

select max(e.Salary), d.Id
from Employee e 
left join Department d 
  on e.DepartmentId = d.Id
group by d.Id
;
