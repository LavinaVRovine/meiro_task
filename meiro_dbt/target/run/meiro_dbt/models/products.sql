
  
    

  create  table "meiro"."public"."products__dbt_tmp"
  
  
    as
  
  (
    SELECT
    expanded_products.*
FROM
    "meiro"."public"."raw" r,
  json_to_recordset(r.products) AS expanded_products(name varchar, id bigint, price bigint)
group by expanded_products.name, expanded_products.id, expanded_products.price
  );
  