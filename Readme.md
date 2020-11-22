# Brazilian Pizza - MoBerries

Espaço destinado a descrição breve do projeto.

# Requisitos


## Introdução

Estas instruções farão com que você consiga buildar o projeto e rodar em sua própria maquina local para propósitos de desenvolvimento e de testes. Acompanhe abaixo as notas sobre como realizar o deploy do sistema.

### Pré-requisitos

Os itens que você deve possuir para construir o projeto:

* Docker - version 19.03.4+

### Tecnologias

* [Django]() - v2.1.13
* [Django CMS]() - v3.6.0
* [Python]() - v3.6
* [Gulp]() - v
* [JavaScript]() - v
* [Sass]() - v1.13.1
* [Bootstrap]() - v4.3.1
* [Node]() - v4.12.0
* [JQuery]() - v3.4.1

### Instalação

Para instalação do projeto, seguindo os pré-requisitos, basta possuir o Docker instalado na máquina na versão mais atualizada possível.

Após baixado o projeto, basta construir o container no local que estiver presente o arquivo `docker-compose.yml` com o seguinte comando:

```
docker-compose build
```

Com isso, você conseguirá subir o container em sua máquina com o seguinte comando:

```
docker-compose up -d
```

Após esses passos, a instalação do container foi finalizada e podemos preparar para realizar as seguintes instruções para configuração do projeto no novo container.

## Configuração do container

Para a configuração do container, será necessário acessá-lo, os comandos abaixo fora do container comprometerá o funcionamento adequado da sua própria máquina, o contrário também é verídico, por isso, atenção sobre qual ambiente você está localizado.

```
docker exec -it tramontina-revista-dev sh
```

Dentro do container instale os pacotes com npm:

```
npm install
```

E faça o primeiro build:

```
npm run build
```

## Versionamento

Partiremos do conceito de atualização **simultânea** de branches, utilizada em alguns de nossos projetos em produção, visto que, desta forma, não seguimos uma lineariedade de publicação de features ou fixes e sim, focado em agilidade e velocidade de resolução de problemas.

Todas as novas branchs, **são criadas** a partir da branch **master**, visto que, a mesma é a **única devidamente atualizada** com as funcionalidades completadas e **aprovadas** pelo cliente.
 
Por padrão, todas as branch possuem pré-fixos definindo seu principal objetivo:

- Novas funcionalidades do sistema, atribuí-se assim o **pré-fixo**: `feature-branch`
- Correção de funcionalidades já desenvolvidas, atribuí-se assim o **pré-fixo**: `fix-branch`

Posterior a isso, envolve-se os merges requests para aplicação efetiva das atualizações nas branchs de desenvolvimento *(develop)* ou de produção *(master)*

Segue-se a sequinte sequência de versionamento:

```
branch ⇨ develop
branch ⇨ master
```

Faz-se necessário realizar a atualização da branch tanto na *develop*, como na *master*.

## Conhecimentos

Para ver os logs de erro da aplicação

```
docker logs -f --tail 100 tramontina-revista-dev
```

## Acessos Django CMS PROD
* Login: ```root```
* Senha: ```root```

## Vendo logs de erro da aplicação
* <code>docker logs -f --tail 100 tramontina-revista-dev</code>

## Credits

* **Gabriel Andrade** - [Desenvolvedor Back-end](https://malu.ncgroup.com.br/gabriel.andrade)