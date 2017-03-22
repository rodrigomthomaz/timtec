Migração de ambientes 3.x para 4.0
==================================

Na atualização para a versão 4.0 houve algumas alterações e reorganizações na estrutura de migrações de banco de dados.
Então, **antes de executar o comando para atualização**, é preciso fazer alguns pequenos preparos no ambiente e na base para
que tudo corra bem.

**OBS: Como em qualquer outra migração, NÃO SE ESQUEÇA DE FAZER BACKUP DO SEU BANCO E DE SEU AMBIENTE.**

Com o seu virtualenv ativado e seu cursor localizado dentro do diretório raiz da aplicação, execute o comando abaixo:
```
bash ./scripts/prepare-to-migrate-from-3.3-to-4.1.sh
```

Feito isso, pode continuar com sua migração normalmente!
