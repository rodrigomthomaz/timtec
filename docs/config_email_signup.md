## Configurando mensagem de email para novos cadastros

Quando um aluno se cadastra na ferramenta, ele recebe um email de boas-vindas e um link de ativação da conta. O texto padrão é o seguinte: 

```
Assunto: Registro na plataforma EAD IF

Email: 

Caro(a) usuário, bem vindo(a) à plataforma EAD Mooc!

Estamos felizes por poder ajudá-lo(a) a conquistar uma qualificação técnica e construir um futuro melhor.

Para garantir que você tenha acesso a todos os recursos e cursos que temos para oferecer, clique no link abaixo e confirme o seu endereço de e-mail.

{{ activate_url }}


Até já!
IF - Instituto Federal de Educação, Ciência e Tecnologia

```

Para editar essa mensagem você precisa fazer uma **customização do tema padrão**. Para isso, siga os procedimentos descritos abaixo. 

## Customizando template padrão > mudança de mensagem de email para novos cadastros

1. Siga os procedimentos descritos em  [configurando um novo tema](config_theme.md) e ative o tema preterido. Obs: tenha certeza de que está com o tema ativo em uso e que não está mais usando o mesmo tema como pacote. 

2. Dentro do seu tema, na pasta **templates** > **account** > **email** você vai encontrar dois arquivos: email_confirmation_message.txt e email_confirmation_subject.txt. Edite esses dois arquivos com o texto que deseja. 

![selecao_220](https://user-images.githubusercontent.com/641411/31837891-4b642ffa-b5b9-11e7-86e2-9d1ab58bef8f.png)

3. Salve, de um make update na sua aplicação, reinicie o nginx e o uwsgi. Pronto! Os novos usuários receberão essa nova mensagem! Não esqueça de commitar essas alterações no seu tema e no seu remote para que você as tenha em uma ocasião futura. 
