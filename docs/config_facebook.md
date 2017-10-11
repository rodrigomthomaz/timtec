## Configurando integração com Facebook

O TIM Tec tem suporte a integração de login com Facebook atraveś do protocolo oauth2. Para habilitar corretamente essa funcionalidade, esteja atento aos seguintes pontos abaixo. 

1. **Versão**
Use a versão 4.1.6 do TIM tec ou superior: https://github.com/institutotim/timtec/releases

2. **Settings.py**
Certifique-se de que seu arquivo settings.py contém as seguintes linhas: 
![selecao_210](https://user-images.githubusercontent.com/641411/31461909-3e7a0fa4-aea1-11e7-98e5-348ab206ae6f.png)

3. **API Facebook Key**
O Facebook exige que você cadastre uma app-key para conectar com sua aplicação via protocolo oauth2. Essa exigência serve para verificar a origem da solicitação e dar mais segurança ao processo. 

3.1 Como cadastrar uma api key? Você precisa de uma conta aqui: 
https://developers.facebook.com

3.2 Onde devo cadastrar a api key no facebook? 
O facebook está sempre mudando a página e a forma de cadastro das keys de desenvolvimento. Acesse a página acima e busque pela informação adequada. Atualmente a página é mostrada dessa forma: 

![selecao_212](https://user-images.githubusercontent.com/641411/31462386-ffc3610a-aea2-11e7-8c22-88c429c6c4e1.png)

4. **Django Admin Panel**
Depois de obter sua facebook api key, você precisa entrar no Django Admin Painel de sua instalação TIM Tec e cadastrar o facebook como um provider de autenticação. Como fazer isso? 

4.1 Primeiro acesse o Django Admin Panel com senha super admin. Você vai cair numa tela exatamente assim: 

![selecao_213](https://user-images.githubusercontent.com/641411/31462969-d331240e-aea4-11e7-80b1-9bd689a5cad1.png)

4.2 Vá ao menu "Contas Sociais" e adicione um "aplicativo social"

![selecao_214](https://user-images.githubusercontent.com/641411/31463032-0d28d738-aea5-11e7-8a24-010ebd8c96d0.png)


![selecao_208](https://user-images.githubusercontent.com/641411/31462793-380de700-aea4-11e7-945d-a22a419ce228.png)




