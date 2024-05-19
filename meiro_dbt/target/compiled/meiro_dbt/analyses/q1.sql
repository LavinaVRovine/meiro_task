SELECT user_name, sum(price) spent


FROM ref('full_denom') WHERE extract(isodow from created_ts) = 5
group by user_name
order by spent desc
limit 1