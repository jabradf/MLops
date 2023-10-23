Run the app:
`python webapp\app.py`

The webserver needs to see a POST at the address using a JSON file, so use this command to interact:
`curl -X POST --header "Content-Type: application/json" --data '["This is a CURL test. I like learning this stuff!"]' http:/localhost:5000/predict`