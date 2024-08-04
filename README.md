## Create migrations
```
python manage.py makemigrations
```

## Apply migrations
```
python manage.py migrate
```

## Generate Dummy Data
This command will generate dummy data for testing purposes.
```
python manage.py dummydata
```

## Run Server
```
python manage.py runserver
```

## EXAMPLE USAGE with `curl`
```
# Get all reports
curl -X GET http://127.0.0.1:8000/reports/

# Get all sources
curl -X GET http://127.0.0.1:8000/sources/

# Get all modifications
curl -X GET http://127.0.0.1:8000/modifications/

# Get all strategies
curl -X GET http://127.0.0.1:8000/strategies/
```
