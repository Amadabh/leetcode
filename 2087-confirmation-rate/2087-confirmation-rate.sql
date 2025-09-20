# Write your MySQL query statement below
with total as (select s.user_id, count(s.user_id) as total_cnt from SignUps s left join Confirmations c on s.user_id=c.user_id group by s.user_id),

confirmed as (select s.user_id, count(s.user_id) as confirm_cnt from SignUps s left join Confirmations c on s.user_id=c.user_id where action='confirmed' group by s.user_id)

select t.user_id, round(IFNULL(c.confirm_cnt/t.total_cnt,0),2) as confirmation_rate from total t left join confirmed c on c.user_id=t.user_id;

