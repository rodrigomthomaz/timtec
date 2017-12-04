[![Stories in Ready](https://badge.waffle.io/institutotim/timtec.png?label=ready&title=Ready)](https://waffle.io/institutotim/timtec) [![Coverage](https://coveralls.io/repos/hacklabr/timtec/badge.png)](https://coveralls.io/r/hacklabr/timtec)

# TIM Tec

A plataforma de cursos online TIM Tec é um software livre que utiliza o conceito de MOOC (Massive Open Online Courses), cursos abertos e livres que podem ser feitos simultaneamente por muitas pessoas.

O sistema pode hospedar múltiplos cursos que utilizam videoaulas, além de materiais de apoio e outros links. A ferramenta permite a criação de testes e o uso de emuladores desenvolvidos para que alunos exercitem os conhecimentos abordados. Alunos podem fazer e responder perguntas, ver respostas e favoritar as perguntas dos colegas em um fórum, além de fazer anotações em seu caderno virtual. Gestores podem gerar relatórios de acompanhamento dos cursos, turmas e alunos, acompanhar o progresso de cada participante e habilitar professores tutores quando necessário.

A tecnologia e os conteúdos da plataforma TIM Tec estão sendo compartilhados com instituições públicas de ensino da Rede e-Tec Brasil, com o apoio da Secretaria de Educação Profissional e Tecnológica do Ministério da Educação (Setec/MEC). Entre as instalações já implementadas estão:

* Instituto Federal Sul-rio-grandense http://mooc.ifsul.edu.br/
* Instituto Federal do Paraná http://mooc.ifpr.edu.br/
* Instituto Federal Sul de Minas https://mooc.ifsuldeminas.edu.br/
* Instituto Federal do Acre http://mooc.ifac.edu.br/
* Instituto Federal Fluminense  http://mooc.iff.edu.br/
* Instituto Federal de São Paulo http://mooc.ifsp.edu.br/
* Instituto Federal de Santa Catarina http://mooc.ead.ifsc.edu.br/
* Instituto Federal do Amazonas http://mooc.ifam.edu.br/
* Instituto Federal de Minas Gerais – Campus Ouro Preto http://mooc.ifmg.edu.br/
* Instituto Federal Farroupilha http://mooc.iffarroupilha.edu.br/
* Instituto Federal do Tocantins http://mooc.ifto.edu.br/
* Instituto Federal Baiano http://mooc.ifbaiano.edu.br/

Algumas outras iniciativas fora do universo dos IFs:

* http://tecsaladeaula.com.br (consultoria de cursos de gestão na área de educação)
* http://escoladejornalismo.org (agência de comunicação que usou a ferramenta para ofertar cursos gratuitos sobre jornalismo)
* http://ead.nutrirnasescolas.com.br (Iniciativa da Fundação Nestle para o projeto "Nutrir Crianças Saudáveis")

## Instalação e configurações
Para acessar a documentação completa, veja a pasta [docs](docs) na raiz da aplicação.

* [Instalação (Deploy)](docs/deploy.md)
* [Atualização (Update)](docs/deploy_update.md)
* [Atualização a partir da versão 3.0.10 ou inferior](docs/config_update_from_3.0.10_or_less.md)
* [Atualização da versão 3.x para 4.0](docs/deploy_migration_from_3.x_to_4.0.md)
* [Configurações v3.2 ou superior](docs/config.md)
* [Configurações (Versão 3.0.10 e inferiores)](docs/config_under_3.0.10_and_less.md)


## Licença - AGPLV3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see LICENSE file here or
    [AGPLv3](http://www.gnu.org/licenses).

## Requisitos de instalação

* Operating system: Debian (8, 9) or Ubuntu (16.04);
* Proxy server: uwsgi (>= 2.0.7);
* Web Server: nginx (>= 1.6.2);
* javascript server-side interpreter: node.js (>= 0.10.40);
* Data base server: postgresql (>= 9.2);
* Python language package: python (= 2.7 ou < 3);
* Virtual Enviroment Python: virtualenv (>=1.11.6);

### Pacotes e módulos importantes
* http://django-rest-framework.org/ -> Rest API and AngularJS
* https://github.com/cobrateam/splinter and https://github.com/olegpidsadnyi/pytest-bdd -> Acceptance tests (full browser support)
* https://github.com/vandersonmota/model_mommy -> mocking of objects
* https://github.com/omab/django-social-auth -> facebook/twitter/gmail logins
* https://github.com/DeadWisdom/django-fixie -> fixture tools
* https://github.com/eldarion/brabeion -> badges
* Para traduções: https://django-rosetta.readthedocs.io/en/latest/

## Requisitos de Desenvolvimento
* all the above requirements
* build essentials and many dev packages if on apt/rpm based systems
    * libpq-dev, libjpeg-dev, libpng12-dev, build-essential, python-dev, gettext
* nodejs (0.10+) (you will need a ppa for ubuntu < 14.04)

### Production Environment Requirements
#### UP to 6000 users
* Processor: Dual Core
* RAM: 2 to 4 GB
* Disk Space: 10 GB
* Network Total Transfer/mo: ~12GB
* Incoming: 1GB
* Outgoing: 11 GB

#### UP to 10k/12k users
* Processor: Quad Core
* RAM: 4 to 6 GB
* Disk Space: 25 GB
* Network Total Transfer/mo: ~25GB
* Incoming: 2GB
* Outgoing: 23 GB



## Running Tests

We made a bunch of tests for the system. They are separated into python tests
(that includes selenium full stack tests) and Karma/AngularJS tests. To run all
of them together just type

    make all_tests

remember that you need to have your virtualenv activated and has installed
everything from the `dev-requirements.txt` file.

### python

Activate virtual env, then:

    make python_tests


