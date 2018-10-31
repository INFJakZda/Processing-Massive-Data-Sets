# Lab 3 Data processing in Databases

## Download Million Song Dataset
```
bash get_dataset.sh
```

## To build example SQLite Docker image:

```
docker build sqlite_example .
```

## To run example container:
```
docker run --name sqlite_example_container sqlite_example
```

## To stop and remove example container:
```
docker stop sqlite_example_container
docker rm sqlite_example_container
```

## To run example container in an interactive mode:
```
docker run -i -t sqlite_example /bin/bash
```
