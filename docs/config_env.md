# Sobre o env
O ambiente virtual do python/django é uma ferramenta que mantém as dependências requeridas por diferentes projetos de maneira organizada. Ele existe para resolver questões como "O projeto x depende da versão 1.x, mas o projeto y precisa da versão 4.x" e mantém o sistema global de pacotes limpo e gerenciável. 

Com env, o desenvolvedor pode por exemplo trabalhar em um projeto que requer Django 1.10 enquanto também mantém um projeto que requer Django 1.8.

## Instalando 
É possível instalar o virtualenv com pip:

```
user@server$ pip install virtualenv
```

Para testar (verificar) a versão já instalada:
```
user@server$ virtualenv --version
```

## Criando o env
No contexto do TIM Tec, a criação do env deve ser feita dessa forma:

```
timtec-production@server$ virtualenv /home/timtec-production/env
```

## Deletando o env
Para deletar um ambiente virtual já criado, no contexto do TIM Tec, faça isso:
```
timtec-production@server$ rm -rf /home/timtec-production/env
```

## Ativando o env
Para ativar o env no TIM Tec, faça:

```
timtec-production@server$ source /home/timtec-production/env/bin/activate
```

## Desativando o env
Para ativar o env no TIM Tec, faça:

```
timtec-production@server$ deactivate
```
