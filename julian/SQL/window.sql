LEAD(column, offset, default_value) OVER (
  [PARTITION BY partition_column] 
  ORDER BY order_column [ASC/DESC]
) -- 访问后一行

LAG(column, offset, default_value) OVER (
  [PARTITION BY partition_column] 
  ORDER BY order_column [ASC/DESC]
) -- 访问前一行

LAST_VALUE(column) OVER (
  [PARTITION BY partition_column] 
  ORDER BY order_column [ASC/DESC]
  [window_frame_clause]
) -- 访问最后一行

FIRST_VALUE(column) OVER (
  [PARTITION BY partition_column] 
  ORDER BY order_column [ASC/DESC]
  [window_frame_clause]
) -- 访问第一行

