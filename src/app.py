import streamlit as st
from PIL import Image
import io

from const import SRC_DIR, WEIGHTS_DIR, EXAMPLE_IMG, EXAMPLE_ZIP
from zipfile import ZipFile
from src.model import ModelOnnx


@st.cache(allow_output_mutation=True)
def load_resnet():
    return ModelOnnx(weights=str(WEIGHTS_DIR / 'resnet-18.onnx'))

@st.cache(allow_output_mutation=True)
def load_efficientnet():
    return ModelOnnx(weights=str(WEIGHTS_DIR / 'efficientnet-b0.onnx'))

def get_model(model_type):
    resnet = load_resnet()
    efficientnet = load_efficientnet()
    return resnet if model_type == 'resnet' else efficientnet

def app():

    st.set_page_config(
        page_title="Tiger or leopard"
    )

    with open(SRC_DIR / 'st_form_wo_border.css') as form_style_file:
        st.markdown(f'<style>{form_style_file.read()}</style>', unsafe_allow_html=True)

    st.sidebar.header("Configuration")

    PAGES = {
        'From Images': from_images,
        'From ZIP': from_zip,
        'Examples': examples,
    }

    page = st.sidebar.selectbox('Page:', options=list(PAGES.keys()), key='PAGE_selection')

    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made with &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" '
            'alt="Streamlit logo" height="16">&nbsp with a source code from '
            '<a href="https://github.com/andfanilo/streamlit-drawable-canvas">@andfanilo</a> '
            'by <a href="https://github.com/JI411">@A. Lekomtsev</a></h6>',
            unsafe_allow_html=True,
        )
    PAGES[page]()

def from_images():
    st.markdown("From Images")

    model_type = st.selectbox(
        'Select model type',
        ('ResNet', 'EfficientNet')
    )
    model = get_model(model_type)

    uploaded_images = st.file_uploader('Upload photos here', type=['jpg', 'jpeg', 'png'],  accept_multiple_files=True)
    for image in uploaded_images:
        name = image.name
        image = image.read()

        image = Image.open(io.BytesIO(image))
        label = 'tiger' if model(image) == 1 else 'leopard'

        st.markdown(f'<h1 align="center"> {label} </h1>', unsafe_allow_html=True)
        st.markdown(name)
        st.image(image)

def from_zip():
    st.markdown("From ZIP")

    model_type = st.selectbox(
        'Select model type',
        ('ResNet', 'EfficientNet')
    )
    model = get_model(model_type)

    uploaded_zip = st.file_uploader('Upload zip here', type=['zip'])
    if uploaded_zip is not None:
        with ZipFile(uploaded_zip) as archive:
            for entry in archive.infolist():
                with archive.open(entry) as file:
                    with Image.open(file) as image:
                        label = 'tiger' if model(image) == 1 else 'leopard'
                        st.markdown(f'<h1 align="center"> {label} </h1>', unsafe_allow_html=True)
                        st.markdown(entry.filename)
                        st.image(image)


def examples():
    st.markdown("Посмотреть на примеры")

    model_type = st.selectbox(
        'Select model type',
        ('ResNet', 'EfficientNet')
    )
    model = get_model(model_type)

    if st.button('From Image'):
        image = Image.open(EXAMPLE_IMG)
        label = 'tiger' if model(image) == 1 else 'leopard'
        st.markdown(f'<h1 align="center"> {label} </h1>', unsafe_allow_html=True)
        st.markdown('Example')
        st.image(image)

    if st.button('From ZIP'):
        with ZipFile(EXAMPLE_ZIP) as archive:
            for entry in archive.infolist():
                with archive.open(entry) as file:
                    with Image.open(file) as image:
                        label = 'tiger' if model(image) == 1 else 'leopard'
                        st.markdown(f'<h1 align="center"> {label} </h1>', unsafe_allow_html=True)
                        st.markdown(entry.filename)
                        st.image(image)
