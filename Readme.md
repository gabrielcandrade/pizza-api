# Brazilian Pizza - MoBerries

This projects was asked by MoBerries as a tech review about my REST API habilities. Django REST Framework was used to solve all requirements write below. This Brazilian Pizza API was made as flexible as I could to attend all kind of Pizzerias. I hope you enjoy it. :)
## Requirements

### Pizza

- [x] It should be possible to specify the desired flavors of pizza (margarita, marinara, salami), the number of pizzas and their size (small, medium, large).
- [x] An order should contain information regarding the customer.
- [x] It should be possible to track the status of delivery.
- [x] It should be possible to order the same flavor of pizza but with different sizes multiple times.

### Order

- [x] It should be possible to update the details — flavours, count, sizes — of an order.
- [x] It should not be possible to update an order for some statutes of delivery (e.g. delivered).
- [x] It should be possible to change the status of delivery.
- [x] Remove an order.
- [x] It should be possible to retrieve the order by its identifier.
- [x] It should be possible to retrieve all the orders at once.
- [x] Allow filtering by status / customer.

## Tasks

- [x] Design the model / database structure, use PostgreSQL for a backend with Django.
- [x] Design and implement an API with the Django REST framework for the web service described above.
- [x] Write test(s) for at least one of the API endpoints that you implemented.
- [x] Provide a Docker setup.
- [x] Write a brief README with instructions on how to run the app (Here you are! :D)

## Setup

To run this project, you'll just need a **Docker** installed on you machine, if you don't have it, you can download it here:

* [Docker](https://www.docker.com/products/docker-desktop) - version stable

## Technologies

* **Docker** - v19.03.11
* **Python** - v3.6
* **Django** - v3.1.3
* **Django REST Framework** - v3.12.2
* **Django Filters** - v2.4.0

## Getting Start

Right down, i'll write the Quickstart based on steps to make it easier to understand and execute on any machine.

**1º -** Download all this code to any folder from your computer.

**2º -** Execute the docker-compose.yml file with the following command:

```
docker-compose build
```

**3º -** After the build, we need to up our container to access all system running at your localhost, to that, type this command:

```
docker-compose up -d
```

Now, the database container and the system container are getting up. Wait some seconds for database server get up and the system gets connect on it. The nice of it, that, it's not necessary to has PostgreSQL server on your machine to run this project. All dependecies are inside the container.

**4º -** Now, we need to access the container, executing the following command:

```
docker exec -it pizza-api sh
```

**5º -** To create your **own user**, you need to type this command:

```
python manage.py createsuperuser
```

**6º -** Now you already has permission to access the manager and see the structure developed based on my database modeling below.

**7º -** To run the python tests developed inside the code, have to type this following command:

```
python manage.py test
```

There are 6 testsCases inside the code. All endpoints has been tested, one on each.

## Knowledge

### Database Modeling

![Data Modeling](https://github.com/gabrielcandrade/pizza-api/blob/master/media/database.png?raw=true)

### Containers

On *docker-compose.yml* there are **2 services running** on the same time. The **pizza-api** and the **pizzaapi_postgres_1**. They has a **wait** configuration (as you could see on /app/DockerFile) that ensure that the pizza-api runs all his commands after the PostgreSQL are up and connectable.

### Log Errors

```
docker logs -f --tail 100 pizza-api
```

## Creator

* **Gabriel Andrade** - [Back-end Developer](https://github.com/gabrielcandrade/)