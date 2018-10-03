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

## Listings
The listing microservice use these URLs:
* GET  /api/v1/listings
* POST /api/v1/listings/create
* GET  /api/v1/listings/\<id\>
* POST /api/v1/listings/\<id\>/update
* GET  /api/v1/listings/\<id\>/delete

## Reviews
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
