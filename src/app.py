import streamlit as st
from PIL import Image
import io

from const import DATA_DIR, SRC_DIR, WEIGHTS_DIR
from src.model import ModelOnnx


@st.cache(allow_output_mutation=True)
def model_load():
    return ModelOnnx(weights=str(WEIGHTS_DIR / 'resnet-18.onnx'))


def app():

    st.set_page_config(
        page_title="Demo"
    )

    with open(SRC_DIR / 'st_form_wo_border.css') as form_style_file:
        st.markdown(f'<style>{form_style_file.read()}</style>', unsafe_allow_html=True)

    st.title("Tiger or leopard")
    st.sidebar.header("Configuration")

    PAGES = {
        'From Image': from_image,
        'From ZIP': from_zip,
        # 'Gallery': gallery,

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

def from_image():
    st.markdown("Загрузите своё фото")
    st.write('')

    model = model_load()

    image = st.file_uploader('Upload photo here', type=['jpg', 'jpeg', 'png'])
    if image is not None:
        image = image.read()

        image = Image.open(io.BytesIO(image))
        label = 'tiger' if model(image) == 1 else 'leopard'

        st.markdown(f'**{label}**')
        st.image(image)

def from_zip():
    st.markdown("Загрузите архив с фото")
    st.write('')

    model = model_load()

    image = st.file_uploader('Upload photo here', type=['jpg', 'jpeg', 'png'])
    if image is not None:
        image = image.read()

        image = Image.open(io.BytesIO(image))
        label = 'tiger' if model(image) == 1 else 'leopard'

        st.markdown(f'**{label}**')
        st.image(image)
