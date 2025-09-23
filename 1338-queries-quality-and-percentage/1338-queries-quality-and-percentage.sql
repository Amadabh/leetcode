# Write your MySQL query statement below

select q.query_name, round(avg(rating/position),2) as quality, round( avg( case when rating<3 then 1 else 0 end) *100,2) as poor_query_percentage from Queries q group by q.query_name;