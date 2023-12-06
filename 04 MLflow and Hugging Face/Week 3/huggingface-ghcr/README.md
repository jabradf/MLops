# 🤗 Hugging Face packaging using GitHub Container Registry
Originally from:
https://github.com/alfredodeza/huggingface-ghcr/blob/main/.devcontainer/devcontainer.json

Learn how to create a container and package it with GitHub Actions. This repository gives you a good starting point for a Dockerfile, GitHub Actions workflow, and Python code.

The web application uses FastAPI with Hugging Face and exposes a single endpoint that you can interact with it. 

Fork this repository and run the GitHub Actions as-is so that you can register your own containerized application with no modifications needed.


## Building and Running
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Check if uvicorn is accessible:
```
which uvicorn
```

Launch uvicorn and bind to any connection:
```
cd webapp
uvicorn -host 0.0.0.0 main:app
```

### Building in Docker
Ensure you're at the root of the project. Ensure you have the trailing full stop at the end:
```
docker build -t huggingface:local .
```

Run docker, exposing port 8000 on both container and local host:
```
docker run -i  -o 8000:8000 huggingface:local
```

