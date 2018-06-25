## Contando quantos usuários cadastrados:

```
python manage.py shell_plus
user_list = TimtecUser.objects.all()
len(user_list)
```

