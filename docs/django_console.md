## Contando quantos usuários cadastrados:
```
python manage.py shell_plus
user_list = TimtecUser.objects.all()
len(user_list)
```

## Filtrando por `last_login`
```
total = 0
for user in TimtecUser.objects.all():
    if user.last_login.year == 2018:
        total = total + 1

print total
```



## Filtrando por `date_joined` e obtendo inscritos por mes do ano

```
jan = feb = mar = apr = may = jun = jul = aug = set = oct = nov = dec = 0
users = timtecuser.objects.all()
year = 2018

for user in users:
    if user.date_joined.month == 01 and user.date_joined.year == year:
        jan = jan + 1
    elif user.date_joined.month == 02 and user.date_joined.year == year:
        feb = feb + 1
    elif user.date_joined.month == 03 and user.date_joined.year == year:
        mar = mar + 1
    elif user.date_joined.month == 04 and user.date_joined.year == year:
        apr = apr + 1
    elif user.date_joined.month == 05 and user.date_joined.year == year:
        may = may + 1
    elif user.date_joined.month == 06 and user.date_joined.year == year:
        jun = jun + 1
    elif user.date_joined.month == 07 and user.date_joined.year == year:
        jul = jul + 1
    elif user.date_joined.month == 08 and user.date_joined.year == year:
        aug = aug + 1
    elif user.date_joined.month == 09 and user.date_joined.year == year:
        set = set + 1
    elif user.date_joined.month == 10 and user.date_joined.year == year:
        out = out + 1
    elif user.date_joined.month == 11 and user.date_joined.year == year:
        nov = nov + 1
    elif user.date_joined.month == 12 and user.date_joined.year == year:
        dez = dez + 1

	
print "janeiro : " + str(jan)
print "fevereiro : " + str(fev)
print "março : " + str(mar)
print "abril : " + str(abr)
print "maio : " + str(mai)
print "junho : " + str(jun)
print "julho : " + str(jul)
print "agosto : " + str(aug)
print "setembro : " + str(set)
print "outubro : " + str(out)
print "novembro : " + str(nov)
print "dezembro : " + str(dez)

```




## Quantos alunos estão matriculados no curso com id=1

```
Course(pk=1).coursestudent_set.all().count()
```

## Quantos alunos matriculados em cada curso

```
from django.core.exceptions import ObjectDoesNotExist
ids=range(1, 32)
for index in ids:
    curso = False
    try:
        curso  = Course.objects.get(id=index)
    except ObjectDoesNotExist:
        curso = False

    if (curso==False):
        print "O id não existe"
    else:
        print Course.objects.get(id=index)
        print Course(id=index).coursestudent_set.all().count()
```

## Quantas lições tem num curso
```
Course(pk=1).lessons.all().count()
User(pk=1).StudentProgress.objects.exclude(complete=None).filter(unit__lesson=lesson)
```



```
select
    email,
    c_name,
    l_name,
    tot_done,
    tot_len,
    course_id,
    (100 * (tot_done::float / tot_len)) as percent
from (
    select
        us.email,
        c.name as c_name,
        l.name as l_name,
        l.position,
        us.id as user_id,
	c.id as course_id,
        count(DISTINCT un.id) as tot_len,
        count(DISTINCT sp.id) as tot_done
    from
        core_unit un
            join core_lesson l
                on l.id = un.lesson_id
            join core_course c
                on c.id = l.course_id
            join core_class cl
                on cl.course_id = c.id
            join core_class_students cs
                on cl.id = cs.class_id
            join accounts_timtecuser us
                on us.id = cs.timtecuser_id
            left join core_studentprogress sp
                on un.id = sp.unit_id
                and us.id = sp.user_id
	    where c.id=1
    group by
        l.id,
        us.id,
	c.id,
        us.first_name

) t
order by
    tot_done DESC;
```
