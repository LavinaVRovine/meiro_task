with expanded as (
    select
       r."user"->> 'id' as id,
       r."user"->> 'name' as name ,
       r."user"->> 'city' as city
from {{ source('raw', 'raw') }} r
)

select id, name, city from expanded r group by id, name, city


