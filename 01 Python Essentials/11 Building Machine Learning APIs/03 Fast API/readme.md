This uses a slightly different technique to launch:

`uvicorn --host 0.0.0.0 main:app`

`main ` tells the script to use `main.py` and `app` to use the instantiated class from FastAPI()

Opening the web page with the listed port, 8000 goes to the main page.

Go to /docs will take you to the interactive page.

Expand the `post` section, click on "try it out" and edit the parameters, adding:
```
{
    "text": Unlike other programming languages, Python is"
}
```