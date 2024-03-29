# restful-pyapp
Simple REST APIs written in Python for Video Games! A demo application of using the Flask framework to continue my Python learning journey.

This restful app allows users to perform CRUD operations related to Video Games.

Clone repo locally to use:

```
git clone https://github.com/pyumz/restful-pyapp.git 
```

# Pre-Requisites

You will need the following tools installed on your local machine:

- Python3 (https://www.python.org/downloads/)
- Docker (https://docs.docker.com/get-docker/)
- Minikube (https://minikube.sigs.k8s.io/docs/start/)
- Ansible (https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

# Game APIs
List of API calls that can be made to interact with the app

``` 
Name                    |   Method      |
/games                  |    GET        |
/games/<game_id>        |    GET        |
/games/add              |    POST       |
/games/update<game_id>  |    PUT        |
/games/delete/>game_id> |    DELETE     |
/swagger
```

# How To(s):

## Run the app locally

You can run the following command to install the depdendencies via your favorite terminmal tool:

```
cd '/path/to/restful-pyapp/app`

pip install -r requirements.txt

###
Set environment variable `FLASK_APP`
###
export FLASK_APP=../main.py
``` 

Once that is complete you can run the app with:

```
flask run
```

It will run on your localhost on port 5000 (default port by Flask)

Visit a browser and you will see a simple welcome message!

![Welcome](/docs/img/games_welcome.png)

## Deploy Docker Image onto Kubernetes

Visit [the infra directory](./infra/README.md) for more information on how to access through a Kubernetes cluster

## Use the APIs
You can either run `curl` commands from your terminal or use your favorite API testing tool such as Postman.

For example to get a list of all video games from the database:

![postman](./docs/img/postman.png)


# Swagger
More information on the APIs can be found in the Swagger UI

![swagger](./docs/img/swagger.png)