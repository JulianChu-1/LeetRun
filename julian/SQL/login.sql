SELECT user_id, max(max_consec_days) AS max_consec_days
FROM (
    SELECT user_id, max(date_num) - min(date_num) + 1 as max_consec_days
    FROM (
        SELECT user_id, fdate, 
            ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY fdate) AS date_num,
            fdate - INTERVAL ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY fdate) DAY AS init
        FROM tb_dau
        WHERE fdate >= '2023-01-01' and fdate <= '2023-01-31'
    ) t1
    GROUP BY user_id, init
) t2
GROUP BY user_id

