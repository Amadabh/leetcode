# Write your MySQL query statement below
with total_users as (select  count(distinct user_id) as total from Users),
cnt_users as (select contest_id, count(r.user_id) as cnt from Users u right join Register r on u.user_id=r.user_id group by contest_id)
select contest_id, round((cnt/total) * 100, 2) as percentage from cnt_users cross join total_users order by percentage desc, contest_id;
