WITH product_counts AS (
    SELECT
        user_city,
        product_name,
        COUNT(*) as product_count
    FROM
        ref('raw', 'full_denom')
    GROUP BY
        user_city,
        product_name
),
ranked_products AS (
    SELECT
        user_city,
        product_name,
        product_count,
        ROW_NUMBER() OVER(PARTITION BY user_city ORDER BY product_count DESC) as product_rank
    FROM
        product_counts
)
SELECT
    user_city,
    product_name,
    product_count
FROM
    ranked_products
WHERE
    product_rank <= 3
order by 1, 2, 3 desc