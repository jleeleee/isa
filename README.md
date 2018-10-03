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

If these don't work, use the commands given in the project description.

Many other utilities are available through `admin.sh`.

## Microservices
### Users
Users contain email addresses, usernames, first names, and last names.
The user microservice use these URLs:
* /api/v1/users
* /api/v1/users/create
* /api/v1/users/\<id\>
* /api/v1/users/\<id\>/update
* /api/v1/users/\<id\>/delete

## Listings
The listing microservice use these URLs:
* /api/v1/listings
* /api/v1/listings/create
* /api/v1/listings/\<id\>
* /api/v1/listings/\<id\>/update
* /api/v1/listings/\<id\>/delete

## Reviews
The reviews microservice URLs are split for user reviews and item reviews.
* /api/v1/reviews/user
* /api/v1/reviews/user/create
* /api/v1/reviews/user/\<id\>
* /api/v1/reviews/user/\<id\>/update
* /api/v1/reviews/user/\<id\>/delete
* /api/v1/reviews/item
* /api/v1/reviews/item/create
* /api/v1/reviews/item/\<id\>
* /api/v1/reviews/item/\<id\>/update
* /api/v1/reviews/item/\<id\>/delete
