Docker Conda
============

## Introduction

Base image for python projects using [conda](https://anaconda.org/)

## Deploy and Usage

### Clone Repository

```bash
$ git clone git@github.com:andrespp/docker-conda.git
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

### Run Job

```bash
$ make run
```

### Get Help

```bash
$ make
```

## Development

### Set image name

Edit `IMAGE_NAME` variable on `Makefile`

### Set job commands

Define job commands through `Makefile`

