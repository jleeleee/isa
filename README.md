# Computer Part Exchange

## Structure
The main application is stored in the app direction.
The app is called 'partex' and the microservices are stored in 'app/partex/apps'

## Running the app
You can run the app with
```
docker-compose up
```
if a mysql database is already running.

You can start a database with
```
./admin.sh mysql    # Launch mysql
./admin.sh makedb   # Create user
./admin.sh resetdb  # Create db
```

Many other utilities are available through `admin.sh`.
