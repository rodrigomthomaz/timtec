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
jan = fev = mar = abr = mai = jun = 0
users = TimtecUser.objects.all()

for user in users:
    if user.date_joined.month == 01 and user.date_joined.year == 2018:
        jan = jan + 1
    elif user.date_joined.month == 02 and user.date_joined.year == 2018:
        fev = fev + 1
    elif user.date_joined.month == 03 and user.date_joined.year == 2018:
        mar = mar + 1
    elif user.date_joined.month == 04 and user.date_joined.year == 2018:
        abr = abr + 1
    elif user.date_joined.month == 05 and user.date_joined.year == 2018:
        mai = mai + 1
    elif user.date_joined.month == 06 and user.date_joined.year == 2018:
        jun = jun + 1
	
print "janeiro : " + str(jan)
print "fevereiro : " + str(fev)
print "março : " + str(mar)
print "abril : " + str(abr)
print "maio : " + str(mai)
print "junho : " + str(jun)
```
