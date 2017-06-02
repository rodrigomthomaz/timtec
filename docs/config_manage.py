# Shell python

Você pode usar o shell do python para efetuar uma série de tarefas com os objetos de sua aplicação. 

Para usá-lo, siga os passos a seguir.

1 - Ative o env

2 - Com env ativado, chame o shell
```
python manage.py shell
```
Importe um objeto e/ou um registro em específico

```
from django.contrib.auth.models import User
user = User.objects.get(username="myname")
```
Como fazer para mudar uma role (papel) de um usuário? Exemplo de alteração para role superadmin: 

```
user.is_superuser = True
user.is_staff = True
user.is_admin = True
user.save()

```


