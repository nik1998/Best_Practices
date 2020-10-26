select * table qrtz_log;

SELECT MAX(pdate)job_name, job_status from table qrtz_log, 

FROM pay
GROUP BY (summ, ident)
insert into qrtz_log values(2,'jobA','G1','2020-09-01 07:00:00','2020-09-01 07:00:03','OK','host1'
);
insert into qrtz_log values(3,'jobA','G1','2020-09-01 06:00:00','2020-09-01 06:00:04','OK','host2'
);
insert into qrtz_log values(4,'jobA','G1','2020-09-01 05:00:00','2020-09-01 05:00:01','OK','host2'
);
insert into qrtz_log values(5,'jobB','G1','2020-09-01 08:00:00',NULL,'ERR','host1'
);
insert into qrtz_log values(6,'jobB','G1','2020-09-01 07:00:00','2020-09-01 07:00:03','OK','host1'
);
insert into qrtz_log values(7,'jobB','G1','2020-09-01 06:00:00','2020-09-01 06:00:04','OK','host1'
);
insert into qrtz_log values(8,'jobC','G1','2020-09-01 08:00:00','2020-09-01 08:00:01','OK','host3'
);
insert into qrtz_log values(9,'jobC','G1','2020-09-01 07:00:00',NULL,NULL,'host2'
);
insert into qrtz_log values(10,'jobC','G1','2020-09-01 06:00:00','2020-09-01 06:00:04','OK','host1'
);
insert into qrtz_log values(11,'jobD','G1','2020-09-01 09:59:59',NULL,NULL,'host1'
);
insert into qrtz_log values(12,'jobD','G1','2020-06-01 07:00:00','2020-06-01 10:00:00','OK','host1'
);
insert into qrtz_log values(13,'jobD','G1','2020-05-01 06:00:00','2020-05-01 10:00:00','OK','host1');
select max(trigger_fire_time),job_name,host_name from  qrtz_log group by job_name;
select(job_finished_time -trigger_fire_time),job_name,host_name from  qrtz_log where job_finished_time is not null;

select job_name,host_name
from  qrtz_log
group by job_name;

select min(t.av),job_name,host_name 
from
(select avg(julianday(job_finished_time) - julianday(trigger_fire_time))as av,job_name,host_name 
from qrtz_log 
where job_finished_time is not null
group by job_name,host_name
order by avg(julianday(job_finished_time) - julianday(trigger_fire_time))) t
group by job_name;

select  q.job_name as job_name, q.host_name as host_name,q.duration as duration, h.host_name as quick_host
from
(select 
CASE
WHEN job_status is null and strftime('%s','now') - strftime('%s',trigger_fire_time)<=2*t.tm
THEN strftime('%s','now') - strftime('%s',trigger_fire_time)
WHEN job_status = 'OK'
THEN strftime('%s',job_finished_time) - strftime('%s',trigger_fire_time)
ELSE 0
END as duration,
max(trigger_fire_time),q.job_name,q.host_name,t.tm,job_status 
from  qrtz_log q 
left join 
(select 
 CASE 
WHEN max(strftime('%s',job_finished_time) - strftime('%s',trigger_fire_time)) is NULL
THEN 1000000000
ELSE max(strftime('%s',job_finished_time) - strftime('%s',trigger_fire_time))
END as tm,
job_name,host_name from  qrtz_log group by job_name, host_name)t
on t.job_name=q.job_name and t.host_name=q.host_name
where not job_status is NULL or strftime('%s','now') - strftime('%s',q.trigger_fire_time)>2*t.tm
group by q.job_name )q
LEFT JOIN
(select min(t.av),job_name,host_name 
from
(select avg(julianday(job_finished_time) - julianday(trigger_fire_time))as av,job_name,host_name 
from qrtz_log 
where job_finished_time is not null
group by job_name,host_name) t
group by job_name)h
on h.job_name = q.job_name 



