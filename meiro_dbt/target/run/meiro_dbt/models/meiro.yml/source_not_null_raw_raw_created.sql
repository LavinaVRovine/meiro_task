select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select created
from "meiro"."public"."raw"
where created is null



      
    ) dbt_internal_test