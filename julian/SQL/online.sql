select artical_id, max(viewer_count) as max_uv
from (
    select artical_id, sum(diff) over(partition by artical_id order by dt, diff desc) as viewer_count
    from (
        select uid, artical_id, in_time as dt, 1 as diff
        from tb_user_log
        where artical_id != 0
        union all
        select uid, artical_id, out_time as dt, -1 as diff
        from tb_user_log
        where artical_id != 0
    ) t1
) t2
group by artical_id
order by max_uv desc