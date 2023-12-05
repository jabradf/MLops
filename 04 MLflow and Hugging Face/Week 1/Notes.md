# ML Flow
Notes from the Coursera course, and the github repository:
https://github.com/alfredodeza/mlflow-demo/tree/main


ML Flow streamlines machine learning development. If offers:
* Experiment tracking
* Code packaging
* Model packaging
* Model registry

It supports many common libraries such as scikit-learn, tensorflow, PyTorch, XGBoost, etc.


https://pypi.org/project/mlflow/

Documentatin including tutorials:
https://mlflow.org/docs/latest/index.html


## Using ML Flow
### Launching the Tracking UI

The MLflow Tracking UI will show runs logged in `./mlruns` at `http://localhost:5000`. Start it with:
```
mlflow ui
```

## ML Flow Models
Creates a standardised reusable model that can be implemented, hosted in code elsewhere.

A big repository of models can be found here:
https://github.com/onnx/models/blob/main/README.md

A model registry helps keep track of versioning of models, allowing for reproducability, fallbacks and forks like regular code.

### Using an Existing Model
```
from mlflow import MlflowClient

client = MlflowClient()
client.create_registered_model("onnx-t5")
```

### Fetch model example
```
model_name = "onnx-t5"
model_version = 1

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{model_version}"
)
```

### Update model example
```
client.update_model_version(
    name = "onnx-t5",
    version = 1,
    description = "This is the T5 model in an ONNX version 1.6 using Opset 12"
)
```

### Staging a model 
The three stages are: staging, production, archived
Configure using:
```
client.transition_model_version_stage(
    name="onnx-t5",
    version=1,
    stage="Production"
)
```