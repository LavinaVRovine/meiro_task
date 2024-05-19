SELECT
    r.id as order_id,
       r."user"->> 'id' as user_id ,
       to_timestamp(r.created) as created_ts,
       expanded_products.id as product_id
FROM
    "meiro"."public"."raw" r,
  json_to_recordset(r.products) AS expanded_products(name varchar, id bigint, price bigint)