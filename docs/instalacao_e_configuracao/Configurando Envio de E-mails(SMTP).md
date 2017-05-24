# Configurando Envio de E-mails

A configuração dos caminhos SMTP para o envio de e-mails é feita no arquivo settings_local.py e/ou no arquivo settings_production.py.

Basta adicionar as seguintes linhas ou alterar os valores, caso já existam. Essas chaves-valores são úteis quando você quer usar um serviço de email externo diretamente em contato com Django, como por exemplo serviços de email como mailgun, gmail, etc:

```
EMAIL_HOST = '[host name]'
EMAIL_PORT = [porta]
EMAIL_HOST_USER = '[usuario host]'
EMAIL_HOST_PASSWORD = '[senha]'
```
Caso queira redirecionar apenas para o postfix e deixar ele se virar para enviar os emails, use as configurações abaixo:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[timtec]'
DEFAULT_FROM_EMAIL = 'donotreply@m.timtec.com.br'
CONTACT_RECIPIENT_LIST = ['email@lista.com.br', ]

ACCOUNT_EMAIL_VERIFICATION = 'optional'
```

No arquivo /timtec/timtec/settings_production.py, busque a entrada CONTACT_RECIPIENT_LIST para configurar quais emails devem receber uma cópia dos emails enviados pelo form de contato. 

```
CONTACT_RECIPIENT_LIST = ['timtec-dev@listas.hacklab.com.br', 'bruna@lfdb.com.br', 'timtec@lfdb.com.br','timtec@timt$
```
