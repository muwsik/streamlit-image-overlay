import base64
import io

import numpy as np
import streamlit as st
from PIL import Image


_component = st.components.v2.component(
    "streamlit-image-overlay.streamlit_image_overlay",
    js="index-*.js",
    html='<div class="react-root"></div>',
)

SUPPORTED_STYLE_TYPES  = {
    "circle",
    "contour",
    "tooltip",
    "viewport",
    "image",
}

def streamlit_image_overlay(
    image = None,
    overlays = [],
    styles = None,
    key = None,
):
    # checking style types
    if styles is not None:
        unknownStyles = set(styles.keys()) - SUPPORTED_STYLE_TYPES

        if unknownStyles:
            raise ValueError(
                f"Unsupported style types: {sorted(unknownStyles)}"
            )
    
    # support image type is PIL and np.ndarray
    if isinstance(image, Image.Image):
        pass
    elif isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            image = image.astype(np.uint8)
        image = Image.fromarray(image)
    else:
        raise TypeError(f"Unsupported image type: {type(image)}")

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    width, height = image.size

    imageBase64 = (
        "data:image/png;base64,"
        + base64.b64encode(buffer.getvalue()).decode("utf-8")
    )

    return _component(
        key = key,
        data = {
            "image": imageBase64,
            "imageWidth": width,
            "imageHeight": height,
            "overlays": overlays,
            "styles": styles or {},
        },
        default = None
    )