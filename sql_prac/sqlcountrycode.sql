
select countrycode,
count(name)
from city
group by countrycode
order by count(name) desc
limit 1;

select distinct co.continent,
    count(ci.name)
from country co
inner join city ci
    on co.code = ci.countrycode
group by co.continent,ci.name;