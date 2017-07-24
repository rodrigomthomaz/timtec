# Themes

## Editar um tema

Se você deseja editar um tema, siga os seguintes procedimentos

1. Fork um tema que deseja modificar

2. Clone, dentro da pasta ```themes_custom``` o tema que deseja habilitar. Tudo que estiver dentro dessa pasta será ignorado pelo git principal da aplicação. 

3. No arquivo ```settings_local.py```, mude a variável ```TIMTEC_THEME``` para o path e nome do seu tema. Veja exemplo: 

```
# Use this to IF theme
TIMTEC_THEME = 'themes_custom/YOUR-THEME-NAME/YOUR-THEME-NAME'
```
