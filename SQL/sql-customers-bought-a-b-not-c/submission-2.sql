-- Write your query below
select o.customer_id, c.customer_name
from orders o left join customers c on o.customer_id=c.customer_id
group by o.customer_id, c.customer_name
having 
string_agg(
    distinct product_name, ',' order by product_name
) like 'A,B%'
and string_agg(
    distinct product_name, ',' order by product_name
) not like '%C%'
order by c.customer_name;