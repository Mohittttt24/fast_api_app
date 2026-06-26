# fast_api_app


# creating fastapi application
## git add . -> stage changed means commit
## git commit -m 'test git' -> comitting the changes
## git push -> add to git hub  

# error codes
### 200 ok
### 201 created
### 204 no content
### 400 bad request
### 401 unauthorized
### 403 forbideden 
### 404 not found 
### 405 method not allowed
### 409 conflict
### 500 internal server error

# Architecture of fastapi application
### Model - database table
### Router - routes request to controllers
### controller - controller logic
### Service -- business logic
### repository -- data access layer
### midleware -- request processing pipline
### schema -- pydantic models for validation
