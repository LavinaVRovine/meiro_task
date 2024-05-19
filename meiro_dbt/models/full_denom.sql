{{ config(
    materialized="view"
) }}


select po.order_id, po.user_id, po.created_ts, po.product_id,  p.name as product_name, p.price,
       u.name as user_name, u.city as user_city
from {{ ref('product_order') }} po
    join {{ ref('products') }} p on po.product_id = p.id
left join {{ ref('users') }} u on po.user_id = u.id