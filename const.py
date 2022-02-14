from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent
SRC_DIR = ROOT_DIR / 'src'
WEIGHTS_DIR = ROOT_DIR / 'weights'
DATA_DIR = ROOT_DIR / 'data'
EXAMPLE_IMG = DATA_DIR / 'example.jpg'
EXAMPLE_ZIP = DATA_DIR / 'example.zip'
