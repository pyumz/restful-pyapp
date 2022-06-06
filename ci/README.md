# CI/CD

## Work In Progress!

One way to deploy the `games-api` is with a CI/CD system such as Concourse. This is a demo of automating the build and deployment of a API. 

Note: You will need to have Concourse running locally. More information on how to set up can be found in this Concourse tutorial: https://concoursetutorial.com/index.html

## Pre-Requisites:

- Docker-Compose

## Makefile

There is a Makefile at the root level of the project that provides helpful commands to run concourse

To start run `make install-concourse` which will install Concourse on your local machine.

Then you will need to install the Fly CLI which controls API access to Concourse in order to use other `make` commands.

Fly installation: https://concoursetutorial.com/#fly-help

Then run `make up` to start up Concourse, you will be able to access it at `http://localhost:8080`

You can set the pipeline with `make pipeline` and type `y` when it asks you to `apply configuration? [yN]`

You can unpause the pipeline by running `make unpause`

![concourse](../docs/img/Concourse.png)

Once you are down tear it down with `make down`

