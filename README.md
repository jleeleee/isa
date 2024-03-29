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
./admin.sh mysql        # Launch mysql
./admin.sh makedbuser   # Create user
./admin.sh makedb       # Create db
```

If these don't work, use the commands given in the project description.

Many other utilities are available through `admin.sh`.

## Microservices
### Users
Users contain email addresses, usernames, first names, and last names.
The user microservice use these URLs:
* GET  /api/v1/users
* POST /api/v1/users/create
* GET  /api/v1/users/\<id\>
* POST /api/v1/users/\<id\>/update
* GET  /api/v1/users/\<id\>/delete

Parameters for create: 
* REQUIRED: `username`
* REQUIRED: `first_name`
* REQUIRED: `last_name`
* REQUIRED: `password`

All optional for update.

### Listings
The listing microservice use these URLs:
* GET  /api/v1/listings
* POST /api/v1/listings/create
* GET  /api/v1/listings/\<id\>
* POST /api/v1/listings/\<id\>/update
* GET  /api/v1/listings/\<id\>/delete

Parameters for create: 
* REQUIRED: `name`
* REQUIRED: `price`
* REQUIRED: `seller`

All optional for update.

Also available for update:
* OPTIONAL: `description`
* OPTIONAL: `status`
* OPTIONAL: `base_item`

### Reviews
The reviews microservice URLs are split for user reviews and item reviews.
* GET  /api/v1/reviews/user
* POST /api/v1/reviews/user/create
* GET  /api/v1/reviews/user/\<id\>
* POST /api/v1/reviews/user/\<id\>/update
* GET  /api/v1/reviews/user/\<id\>/delete
* GET  /api/v1/reviews/item
* POST /api/v1/reviews/item/create
* GET  /api/v1/reviews/item/\<id\>
* POST /api/v1/reviews/item/\<id\>/update
* GET  /api/v1/reviews/item/\<id\>/delete

Parameters for create (user and item): 
* REQUIRED: `title`
* REQUIRED: `rating`
* REQUIRED: `body`
* REQUIRED: `subject` - ID of the User/AbstractItem subject of the review

All optional for update.

## Fixtures
Fixtures are located in `app/partex/db/fixtures` as JSON files. They can be loaded inside a Django container with
```
./manage.py loaddata app/partex/db/fixtures/app.json
```

Fixtures are automatically loaded when `docker-compose up` is run.

## Unit Tests
Unit tests for the models can be run inside the django container with
```
./manage.py test partex.apps
```
