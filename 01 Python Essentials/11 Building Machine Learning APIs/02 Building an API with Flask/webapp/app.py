from flask import Flask, request, jsonify
import torch
import numpy as np
from transformers import RobertaTokenizer
import onnxruntime


app = Flask(__name__)
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
# this model needs to be downloaded for the script to work. It's around 500mb so can't be uploaded to git directly without git LFS.
# can be downloaded form here however: https://github.com/innovad/MLOps-roberta-onnx/blob/master/roberta-sequence-classification-9.onnx
session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")


def to_numpy(tensor):
    return (
        tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
    )


@app.route("/")
def home():
    return "<h2>RoBERTa sentiment analysis</h2>"


@app.route("/predict", methods=["POST"])
def predict():
    input_ids = torch.tensor(
        tokenizer.encode(request.json[0], add_special_tokens=True)  # request is an odd method rather than being passed through to the function itself
    ).unsqueeze(
        0
    )

    inputs = {session.get_inputs()[0].name: to_numpy(input_ids)}
    out = session.run(None, inputs)

    result = np.argmax(out)

    return jsonify({"positive": bool(result)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)