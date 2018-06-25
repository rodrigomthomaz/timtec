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
```

print total

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
