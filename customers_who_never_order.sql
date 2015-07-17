select Name from Customers
left join Orders
on Customers.Id = Orders.CustomerId
where Orders.Id is null;
