# Engineering Assignment

## Installation - on Docker

```bash
# clone repo to your machine
git clone git@github.com:yunusovbekir/Training-AIHomework.git
```

## Usage

```bash
# run with docker
docker-compose up --build

# run tests
docker-compose run --rm <service name> sh -c "pytest"

# run linting
docker-compose run --rm <service name> sh -c "flake8"
```