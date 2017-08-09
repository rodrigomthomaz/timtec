## Extendendo traduções (com engine rosetta)

Você está usando a ferramenta timtec com tema próprio, mas quer traduzir de um modo diferente alguma das labels espalhadas pelo front-end. É preciso hardcodar uma tradução diferente ou mudar a origem da tradução? Não! Você pode extender para dentro do seu tema uma tradução (versão) do file-text do [rosetta](https://django-rosetta.readthedocs.io)

1. Dentro do diretório do tema, certifique-se de que há arquivos de tradução da língua (file-text) em que está operando.
Exemplo: aqui ```themes/themes_custom/SEU-TEMA/timtec-theme-nutrir/locale/pt_BR/LC_MESSAGES``` é possível ver:

![selecao_114](https://user-images.githubusercontent.com/641411/29129625-ce4c2ab6-7cfd-11e7-96d0-be377ca814f8.png)

2. Adicione o path do novo file-text do seu tema à sua aplicação. Você precisa fazer o Django entender que existe um file-text do rosetta disponível no seu tema e que este deve ser usado em detrimento do primeiro(default). Sendo assim, no ```settings_local.py``` de sua aplicação, acrescente info sobre locale path:

```
LOCALE_PATHS = (
    os.path.join(THEMES_DIR, TIMTEC_THEME, 'locale'),
) + LOCALE_PATHS
```

3. Verifique: veja se funcionou acessando ```http://YOUR-URL/rosetta```. Você deve encontrar algo assim:
![selecao_115](https://user-images.githubusercontent.com/641411/29130114-46fda4ca-7cff-11e7-8f81-1c00712bdce7.png)


4. Altere as labels! Agora que já fez as mudanças necessárias para que o sistema entenda que você quer usar tradução customizadas vindas do seu tema você pode proceder de 2 formas: mudar a label que desejar pelo painel ou alterar diretamenta no arquivo django.po de seu tema (o mesmo que você copiou para dentro do seu tema no item 1.)

![selecao_116](https://user-images.githubusercontent.com/641411/29130388-0c96eebc-7d00-11e7-9d3b-0afbb6623ce6.png)





