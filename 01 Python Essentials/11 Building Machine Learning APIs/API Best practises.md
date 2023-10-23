# API Best practises
Although there are a few best practices for using the FastAPI framework, there are many different other suggestions to build solid HTTP APIs that can be applicable anywhere.

## Use HTTP Error codes
The HTTP specification has several error codes available. Make use of the appropriate error code to match the condition that caused it. For example the 401 HTTP code can be used when access is unauthorized. You shouldn't use a single error code as a catch-all error.

Here are some common scenarios associated with HTTP error codes:

* 400 Bad request: Use this to indicate a schema problem. For example if the server expected a string but got an integer
* 401 Unauthorized: When authentication is required and it wasn't present or satisfied
* 404 Not found: When the resource doesn't exist

Note that it is a good practice to use `404 Not Found` to protect from requests that try to find if a resource exists without being authenticated. A good example of this is a service that doesn't want to expose usernames unless you are authenticated.

Accept request types sparingly
|GET |	POST |	PUT	| HEAD|
|---|---|---|---|
|Read Only |	Write Only|	Update existing |	Does it exist?