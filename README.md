Docker Conda
============

## Introduction

Base image for python projects using [conda](https://anaconda.org/) with [PostgreSQL](https://www.postgresql.org/) backend.

## Deploy and Usage

### Clone Repository

```bash
$ git clone -b postgres git@github.com:andrespp/docker-conda.git
```

### Build and test docker image

```bash
$ make setup
$ make run-test
```

### Run interactive session

```bash
$ make runi
```

### Run App

```bash
$ docker-compose up -d # db backend
$ make run
```

### Get Help

```bash
$ make
```

## Development

### Set image name

Edit `IMAGE_NAME` variable on `Makefile`

### Set docker container name

Edit `service` and `container_name` parameters on `docker-compose.yml`

### Set job commands

Define job commands through `Makefile`

