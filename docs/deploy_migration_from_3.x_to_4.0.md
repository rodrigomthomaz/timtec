Migração de ambientes 3.x para 4.0
==================================

Banco de dados
--------------

Na atualização para a versão 4.0 houve algumas alterações e reorganizações na estrutura de migrações de banco de dados.
Então, **antes de executar o comando para atualização**, é preciso fazer alguns pequenos preparos no ambiente e na base para
que tudo corra bem.

**OBS: Como em qualquer outra migração, NÃO SE ESQUEÇA DE FAZER BACKUP DO SEU BANCO E DE SEU AMBIENTE.**

Com o seu virtualenv ativado e seu cursor localizado dentro do diretório raiz da aplicação, execute o comando abaixo:
```
bash ./scripts/prepare-to-migrate-from-3.3-to-4.1.sh
```

Configurações locais
--------------------

A partir desta nova versão houve algumas alterações no gerenciamento interno de temas. A partir de agora eles ficarão
em repositórios separados e totalmente independentes. Os temas *timtec* e o tema *if* (antigo *ifs-colors*) já vêm
instalado por padrão.

Para ativar o tema correspondente, vá até o seu `settings_local.py` e adicione o seguinte trecho:
```
INSTALLED_APPS += (
  # 'if_theme',      # Use this to IF theme
  # 'timtec_theme',  # Use this to Timtec theme
)
```

Retire o comentário do tema que você utilizará. Feito isso, troque a variável `TIMTEC_THEME` para o mesmo valor
utilizado.

No exemplo abaixo, estamos configurando para que seja usado o tema **if**:
```

INSTALLED_APPS += (
  'if_theme',      # Use this to IF theme
  # 'timtec_theme',  # Use this to Timtec theme
)
TIMTEC_THEME = 'if_theme'
```

Realizando a migração
---------------------

Levando em conta os dois pontos levantados acima, faça sua migração executando o comando (dentro do diretório raiz):
```
make update
```
