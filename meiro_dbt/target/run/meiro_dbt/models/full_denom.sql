
  create view "meiro"."public"."full_denom__dbt_tmp"
    
    
  as (
    


select po.order_id, po.user_id, po.created_ts, po.product_id,  p.name as product_name, p.price,
       u.name as user_name, u.city as user_city
from "meiro"."public"."product_order" po
    join "meiro"."public"."products" p on po.product_id = p.id
left join "meiro"."public"."users" u on po.user_id = u.id
  );