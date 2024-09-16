# yhttp-boilerplate

A simple template for yhttp framework.


## Development

### Setup development environment

```bash
make venv
make activate.sh
make env
```
Or to delete the current environment and make a fresh one for project.
```
make fresh env
```

To activate the created python virtual environment
```
source activate.sh
```

### Running tests

```bash
make test
```

for code coverage

```bash
make cover
```

### Linter

```bash
make lint
```

### Serve
```
make serve
```
The default bind is localhost:8080 and you can check it by curl
```
curl localhost:8080
curl -X describe localhost:8080
```

### Create source distribution

```bash
make dist
```

### Clean distribution directory

```bash
make clean
```
