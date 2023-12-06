Deploy to azure easily:
https://www.youtube.com/watch?v=lqSXVBur_nQ
https://www.youtube.com/watch?v=cjXYjN2mNVM


# Quiz:
What is the right command to containerize an application?
```
docker build .
```

2. What is the default and recommended way to run a FastAPI web application?
```
Using the uvicorn server. In a container it is useful to use 0.0.0.0 as the host to serve.
```

3. What is the right prefix to tag a container in a repository named huggingface-ghcr so that it can be pushed to the GitHub Container Registry?

X Using the repository name, like huggingface-ghcr
- Using your username and then the repository name, for example: alfredodeza/huggingface-ghcr
- ghcr.io

_Incorrect. This would cause the container to be pushed to Docker Hub._

4. What are four common ways you can trigger a GitHub workflow in GitHub Actions?
   1. A code change in a branch
   2. Manually
   3. A timer, to build on a schedule
   4. On a pull-request

5. For an Azure Container Registry named `demo-acr` what would the right tag be for the container in the `huggingface-acr` repository so that when pushed, it goes to Azure?
```
demo-acr.azure.io/huggingface-acr
```

6. When packaging an API with a model, what are three steps you should follow before creating automation?
   1. Run the application to verify it works without containerization
   2. Build the container and verify it builds without issues
   3. Run the container and interact with the API to ensure it is functionally correct
   
7. Why would you want to register a model from Hugging Face into Azure ML Studio?
Because it would allow easier deployment, analysis, and fine tuning within the Azure cloud.

8. What are some possible scenarios that you can control that would prevent a successful deployment of a containerized HTTP API on a cloud service provider like Azure?
   1. Syntax error in the Python application
   2. Incorrect port mapping from the container to the service

9. Question 9
What are three ways you can upload a Hugging Face dataset onto Azure ML Studio?

* 1. Via File Upload
  2. Using the Python SDK
  3. Using the URL to the raw dataset

X 1. Via File Upload
  2. Using the Datasets library from Hugging Face
  3. Using the URL to the raw dataset

* 1. Via Azure's API
* 2. Using the Python SDK
* 3. Using the URL to the raw dataset

_Incorrect. The Datasets library doesn't have the ability to upload to Azure._

10. What is a good definition for what packaging an ML model is?
Packaging a machine learning model means to create a container that can be used to deploy the model on different platforms which includes everything the model needs to run. 