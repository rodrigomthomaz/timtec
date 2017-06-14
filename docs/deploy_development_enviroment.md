# TIM Tec > Develop Enviroment Deploy

Se você quer desenvolver features para ferramenta timtec ou ainda resolver bugfixes, o primeiro passo é criar um ambiente adequado para isso. 

## Vagrant Local install
O primeiro passo recomendado é fazer uma instalação local. Recomendamos usar uma máquina virtual via commandline para isso, com Vagrant. Se você não quiser usar Vagrant, faça uma instalação de outra forma e siga para o próximo passo. 

1. Instale o vagrant e o virtualbox na sua máquina
![selecao_029](https://user-images.githubusercontent.com/641411/27147091-ee65787e-5111-11e7-877e-f59e0ceb4398.png)

2. Crie um diretório para hospedar uma máquina ubuntu 16.04: sugestão de nome ```vagrant_ubuntu_16_04_timtec```

```
user@server$ mkdir vagrant_ubuntu_16_04_timtec
user@server$ vagrant init ubuntu/xenial64; vagrant up --provider virtualbox
```
![selecao_030](https://user-images.githubusercontent.com/641411/27147228-5eb5eb68-5112-11e7-9af7-d78f9aedee06.png)

3. Clone o repositório dentro desta pasta:
```
user@server/vagrant_ubuntu_16_04_timtec$ git clone https://github.com/institutotim/timtec.git
```
Exemplo de como ficará seu diretório:
![selecao_028](https://user-images.githubusercontent.com/641411/27146350-7d277e0c-510f-11e7-8f6e-ddd3316b9d11.png)

4. Entre no arquivo Vagrantfile criado pelo Vagrant e edite a linha de pastas syncadas. Acrescente na opção synced_folder a pasta padrão do timtec. Ficará mais ou menos desta forma dependendo de onde você tenha feito o clone do repo:

```
  config.vm.synced_folder "timtec", "/home/timtec-development/timtec",
  owner: "timtec-development", group: "timtec-development"
```
Sugerimos que use o user ```timtec-development``` para o ambiente de desenvolvimento, por isso esse seria o nome do diretório do user da aplicação. Mas isso é totalmente opcional. 

5. Edite também o redirecionamento de portas do guest para o host. Deixe no host algo como 3131, ou qualquer outra porta alta sem uso. 

```
  config.vm.network "forwarded_port", guest: 80, host: 3131
```

Uma vez que você tenha clonado o repo do timtec dentro de um diretório vagrant ele irá aparecer na pasta /vagrant/timtec quando estiveres logado, certo? O que a linha acima faz é linkar isso com a pasta home do usuário da aplicação, no caso ```/home/timtec-development/timtec```. 

Por fim, o arquivo ```Vagrantfile``` vai ficar conforme exemplo abaixo.
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

# Tipo de máquina em uso
  config.vm.box = "ubuntu/xenial64"

# Redirecionamento de portas
  config.vm.network "forwarded_port", guest: 80, host: 3133

# Ip Fake para rodar no browser
  config.vm.network "private_network", ip: "192.168.10.99"

# Pasta syncada
  config.vm.synced_folder "timtec", "/home/timtec-production/timtec",
  owner: "timtec-production", group: "timtec-production"

end
```

6. Prossiga com o procedimento de deploy normal da aplicação dentro do Vagrant, isto é, entre no vagrant com ```vagrant ssh```, vire root com ```sudo su``` e execute os passos necessários como root, incluindo a criação de um user, que nesse caso ao contrário do que recomendado na documentação padrão do timtec, sugerimos que seja ```timtec-development```. 


## Ative o env


source env/bin/activate


## Runserver
O Django possui um servidor livein para desenvolvimento. Ao rodar esse servidor a aplicação fica em modo "watch" permitindo com que toda e qualquer alteração gere um logo ao vivo no terminal de comandos. Para ativar o ```runserver``` junto com vagrant no timtec, você seguir o exemplo abaixo:

```
./timtec/manage.py runserver 0.0.0.0:8000
```














