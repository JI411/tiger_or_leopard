import numpy as np
import onnxruntime as ort
from torchvision import transforms


def get_transforms(ort_session):
    size = ort_session.get_inputs()[0].shape[2:]

    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(size),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


class ModelOnnx:

    def __init__(self, weights: str):
        self.ort_session = ort.InferenceSession(weights)
        self.transforms = get_transforms(self.ort_session)
        self.input_name = self.ort_session.get_inputs()[0].name

    def run(self, img):
        return self.ort_session.run(None, {self.input_name: img.numpy()})[0]

    def __call__(self, img):
        img = self.transforms(img).unsqueeze(0)
        output = self.run(img)
        return np.argmax(output)
