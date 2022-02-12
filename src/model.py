from pathlib import Path

import cv2
import numpy as np
import onnx
import onnxruntime as ort
from torchvision import transforms


def get_transforms(ort_session):
    size = ort_session.get_inputs()[0].shape[2:]

    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(size),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

def session(weights: Path):
    onnx.checker.check_model(onnx.load(str(weights)))
    return ort.InferenceSession(weights)


class EfficientNetOnnx:

    def __init__(self, weights):
        self.ort_session = session(weights)
        self.transforms = get_transforms(self.ort_session)
        self.input_name = self.ort_session.get_inputs()[0].name

    def run(self, img):
        return self.ort_session.run(None, {self.input_name: img.numpy()})[0]

    def __call__(self, img):
        img = self.transforms(img).unsqueeze(0)
        output = self.run(img)
        return np.argmax(output)


if __name__ == '__main__':

    effnet = EfficientNetOnnx(weights='/home/ji411/Downloads/efficientnet-b2.onnx')
    image = cv2.imread('/home/ji411/PycharmProjects/tiger_or_leopard/Princess_378.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(effnet(image))
