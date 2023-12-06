# Week 4 Quiz
There's some really strange comments when you get an answer wrong, but here are my answers.
1. What are two important aspects of fine-tuning a model?
    1. Reduces computation costs
    2. Reuse state-of-the-art models without having to train it from scratch

2. What are some components needed for automating deploying to Hugging Face Spaces?
   1. GitHub Actions
   2. Hugging Face Token
   3. Gradio application

3. What are some problems you may run into when deploying a containerized model to Azure Container Apps?
   1. Wrong port number
   2. Not enough CPU and memory for the container

4. What are the three main services needed when deploying and automating a Hugging Face container?
   1. GitHub Actions for automation
   2. A container registry like the GitHub container registry
   3. Azure Container Apps for hosting the running container
5. What is one benefit of using Azure Container Registry (ACR) instead of using Docker Hub?
    - It is easier to consume images from ACR within the Azure cloud. 

6. What are two ways you can view the runtime logs after deploying to Azure Container Apps?
   1. On Azure directly using the web UI for container apps
   2. Using the `az` CLI to tail the logs

7. What are the definitions for supervised learning and transfer learning? 
   1. Supervised learning is performing a task by being repeatedly presented with example data.
   2. Transfer learning uses a pre-trained model to learn a new task.

8. What is an advantage of using transfer learning?
   - You can use a high-quality model that is trained efficiently on another domain

9. Which one of the following options is the correct one to define a Gradio interface for text input using the `prediction()` function?
    - `gradio.Interface(fn=prediction, inputs="text", outputs="text").launch()`

10. What is a compelling reason to use Hugging Face Spaces?
    - It allows to demonstrate how a model works in an interactive demo with small amount of code.