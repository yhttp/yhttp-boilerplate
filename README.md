# yhttp-boilerplate

A simple template for yhttp framework.


## Development


### Install prerequisites

```bash
sudo apt install \
  # Needs for compile Python extensions. \
  python3-dev \

  # For make virtual environment with Python. \
  python3-venv \

  # For database comunications. \ 
  libpq-dev
```


### Setup development environment

```bash
make venv

source activate.sh

make env
```

### Running tests

```bash
make test
```

for test coverage

```bash
make cover
```

### Linter

```bash
make lint
```

### Create source distribution

```bash
make dist
```

### Clean distribution directory

```bash
make clean
```
