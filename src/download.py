import gdown
from const import DATA_DIR, WEIGHTS_DIR


def load_data() -> None:
    gdown.cached_download(
        id='1NX4fOcCl4ybmoGAiLivlsjy8sJaNSVwU',
        path=str(DATA_DIR / 'example.jpg'),
        md5='4ebfb4ce62c35bc4935b2e2a3c97fd42'
    )
    gdown.cached_download(
        id='1_escQijM6W94c3RMG3z7kQ6HtV4by8YG',
        path=str(DATA_DIR / 'example.zip'),
        md5='1589aeed00f431827eb13bc13c20788d',
    )


def load_weights() -> None:
    gdown.cached_download(
        id='1xbiz1ibZ227g6_V-6oJWVrRjo6QhOfOw',
        path=str(WEIGHTS_DIR / 'efficientnet-b0.onnx'),
        md5='d76dd5d236a3ead450bb25565b069256'
    )
    gdown.cached_download(
        id='19sqePLYKEWFQdmaiOhTyeg0uNQ3yz4f_',
        path=str(WEIGHTS_DIR / 'resnet-18.onnx'),
        md5='325030f24ef5f184120886806b102dff'
    )
