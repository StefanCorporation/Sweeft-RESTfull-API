## User creation and registration
URL: http://127.0.0.1:8000/api/v1/auth/  
Via GET request

Example of creating a user (you must specify the fields as in the example, request via POST request)

###### email cesar123@gmail.com
###### password cesar_is_last 
______


## Obtaining a JWT token for the user token for further authorization

URL: http://127.0.0.1:8000/api/v1/token/
Via POST request

Example of receiving a token (you must specify the fields as in the example, request via POST request)

###### username cesar
###### password cesar_is_last
_____
## Authorization using JWT token

Example of receiving a token (you must specify the fields as in the example, request via POST request)

###### Authorization Bearer "2131jioh123hug432HIUHU34"

If the "access" token has timed out, then you need to go either this url's  bellow

URL: http://127.0.0.1:8000/api/v1/token/refresh/ 
OR
URL: http://127.0.0.1:8000/api/v1/auth/jwt/refresh/
_____

## Authorization with regular tokens (Djoser) (receiving a token)
URL: http://127.0.0.1:8000/api/v1/auth/token/login/ 

Example of authorization with regular tokens via POST request

Auth token 2088c9013fa154d1acfd83e5791ea96f83c7cb34
_____

## Logout 

To log out, you need to use the POST method to specify the user who is logging out.
URL: http://127.0.0.1:8000/api/v1/auth/token/logout/

Example:
###### username cesar
###### password cesar_is_last
____

## To populate the database with categories and exercises, use fixtures.
Example:

###### python manage.py loaddata workout_system/fixtures/workout_categories.json
_____

## SWAGGER
URL: http://127.0.0.1:8000/swagger/
_____

## Categories
#### Any user can view category data (GET request only)
URL: http://127.0.0.1:8000/api/v1/category/
___

## Exercises
#### Any user can view category data (GET request only)
URL: http://127.0.0.1:8000/api/v1/exercise/
___

## Users
#### Receiving data about a specific user is only possible for an authorized or Admin user
URL: http://127.0.0.1:8000/api/v1/user/

If you need to change the user data, be sure to indicate the user id at the end of the url, which was received when you followed the link! (127.0.0.1:8000/api/v1/user/1/)
___

## Personal Plans
#### Receiving data about a specific personal plans is only possible for an authorized or Admin user
URL: http://127.0.0.1:8000/api/v1/personal-plans/

If you need to change the personal data, be sure to indicate the user id at the end of the url, which was received when you followed the link! (127.0.0.1:8000/api/v1/user/1/)
___

## Goal-Traking
#### Receiving data about a specific personal goal traking is only possible for an authorized or Admin user
URL: http://127.0.0.1:8000/api/v1/goal-traking/

If you need to change the personal goal traking data, be sure to indicate the user id at the end of the url, which was received when you followed the link! (127.0.0.1:8000/api/v1/user/1/)

___
## The admin has access to the entire list of users of personal category plans, etc. He can also change all data
___

# P.S. 
For easier reading README
file, I recommend using extensions in VScode
Markdown Preview Enhanced



















