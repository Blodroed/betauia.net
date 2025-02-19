# BetaWEB

## Overview

**Description**: The student organization Beta's website.

**Purpose**: BetaDEV is trying to improve the old website.

## Table of Contents

- [Overview](#overview)
- [Installation and running a fullstack server with docker](#installation-and-running-a-fullstack-server-with-docker)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
  - [Running the application](#running-the-application)
  - [Stopping the application](#stopping-the-application)
- [Additional Docker Commands](#additional-docker-commands)
- [Frontend Development and Design](#frontend-development-and-design)
- [Gamejams](#gamejams)

---

## Installation and running a fullstack server with docker
These are the steps you need to do to run a fullstack development server on your local machine 🧙‍♂️!

For local frontend development without the bells and whistles of the backend you can follow the steps in the [Frontend Development and Design](#frontend-development-and-design) section. 🖌️🎨
## Table of Contents

- [Overview](#overview)
- [Installation and running a fullstack server with docker](#installation-and-running-a-fullstack-server-with-docker)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
  - [Running the application](#running-the-application)
  - [Stopping the application](#stopping-the-application)
- [Additional Docker Commands](#additional-docker-commands)
- [Frontend Development and Design](#frontend-development-and-design)
- [Gamejams](#gamejams)

---

## Installation and running a fullstack server with docker
These are the steps you need to do to run a fullstack development server on your local machine 🧙‍♂️!

For local frontend development without the bells and whistles of the backend you can follow the steps in the [Frontend Development and Design](#frontend-development-and-design) section. 🖌️🎨

### Prerequisites

- **Git**: Used to clone the repository, [download here](https://www.git-scm.com/downloads).
- **Docker**: Used to create and run containers, [download here](https://www.docker.com/products/docker-desktop).
- **Docker Compose**: Used to define and run multi-container Docker applications, included in Docker Desktop (or follow the [installation instructions](https://docs.docker.com/compose/install/)).

### Steps
1. Clone the repository:
```bash
git clone https://github.com/betauia/betauia.net
```
2. Navigate to the project directory:
```bash
cd betauia.net
```
3. Copy environment variables and edit them as needed:
```bash
```bash
cp .env.example .env
```
4. Build and start the Docker containers:
```bash
docker compose up --build
```

## Usage

### Running the application

- Start the application:
```bash
docker compose up  # Use -d to run detached
docker compose up  # Use -d to run detached
```

Access the application at port `3000` (frontend) and `8000` (backend). If `ENV` is set to `production`, the Astro project will be built to `frontend/dist/` and can be hosted via Nginx.
Access the application at port `3000` (frontend) and `8000` (backend). If `ENV` is set to `production`, the Astro project will be built to `frontend/dist/` and can be hosted via Nginx.

### Stopping the application

- Stop the application:
- Stop the application:
```bash
docker compose down
```

## Additional Docker Commands

- To view running containers:
```bash
docker compose ps
```
- To build containers:
```bash
docker compose build
```

- To remove volumes:
```bash
docker compose down -v
```

- To access the shell of the container (N.B.! intended be used for troubleshooting, e.g. check if something is installed correctly after `compose up`)
```bash
docker exec -it <container_name_or_id> sh
```

- To remove volumes:
```bash
docker compose down -v
```

- To access the shell of the container (N.B.! intended be used for troubleshooting, e.g. check if something is installed correctly after `compose up`)
```bash
docker exec -it <container_name_or_id> sh
```

## Frontend Development and Design
> **NOTE!** 
> This is only a temporary solution as the docker setup does not support "hot-reload"/"live-preview" of the changes to the frontend design or content changes. Resulting in you having to recompose with a 10-second wait time for changes on the frontend.

For local frontend development without the backend, follow these steps:

1. Navigate to the `/frontend` directory:
```sh
cd frontend
```
2. Install the dependencies:
```sh
npm install
```
3. Start the Astro development server:
```sh
npm run dev
```

Your log will display what port you should localhost into 🖥️. This will start the Astro development server and watch for changes, so you don't need to rebuild each time. 🚀

<!--
Currently not working, remove quotes when working
## Frontend Development and Design
> **NOTE!** 
> This is only a temporary solution as the docker setup does not support "hot-reload"/"live-preview" of the changes to the frontend design or content changes. Resulting in you having to recompose with a 10-second wait time for changes on the frontend.

For local frontend development without the backend, follow these steps:

1. Navigate to the `/frontend` directory:
```sh
cd frontend
```
2. Install the dependencies:
```sh
npm install
```
3. Start the Astro development server:
```sh
npm run dev
```

Your log will display what port you should localhost into 🖥️. This will start the Astro development server and watch for changes, so you don't need to rebuild each time. 🚀

<!--
Currently not working, remove quotes when working
## Gamejams 🎮 🎮

If you want to clone the games from *game jams*, use:
    ```sh
    git clone --recurse-submodules <repo name>
    ```

## Troubleshooting
> **Q: I got an error where the docker container can't find a module, and I did not add any modules**

A: This is probably because you built the images before and therefore some residual images for the container is still present. To resolve this run:
```bash
docker compose down -v
```
This ensures all images are removed ensuring you can start the server from scratch starting from [installation step 4](#steps) after a node.js package update
