import base64
import io

import numpy as np
import streamlit as st
from PIL import Image


def validate_image(_image):
    if isinstance(_image, Image.Image):
        pass
    elif isinstance(_image, np.ndarray):
        if _image.dtype != np.uint8:
            _image = _image.astype(np.uint8)
        _image = Image.fromarray(_image)
    else:
        raise TypeError(f"Unsupported image type: {type(_image)}")

    return _image


SUPPORTED_STYLE_TYPES  = {
    "circle",
    "path",
    "tooltip",
    "viewport"
}

def validate_styles(_styles):
    if _styles is not None:
        unknownStyles = set(_styles.keys()) - SUPPORTED_STYLE_TYPES
        if unknownStyles:
            raise ValueError(f"Unsupported style types: {sorted(unknownStyles)}")


SUPPORTED_OVERLAY_TYPES = {
    "circle",
    "path",
}

def validate_overlays(_overlays):
    if not isinstance(_overlays, list):
        raise TypeError("overlays must be a list")

    for i, overlay in enumerate(_overlays):
        if not isinstance(overlay, dict):
            raise TypeError(f"Overlay {i} must be a dict")

        if "id" not in overlay:
            raise ValueError(f"Overlay {i}: missing 'id'")

        if "type" not in overlay:
            raise ValueError(f"Overlay '{overlay['id']}': missing 'type'")

        if overlay["type"] not in SUPPORTED_OVERLAY_TYPES:
            raise ValueError(f"Overlay '{overlay['id']}': "
                f"unsupported type '{overlay['type']}'")

        if "data" not in overlay:
            raise ValueError(f"Overlay '{overlay['id']}': missing 'data'")

        if not isinstance(overlay["data"], dict):
            raise TypeError(f"Overlay '{overlay['id']}': "
                "'data' must be a dict")

        # Type-specific fields
        if overlay["type"] == "circle":
            required = {"x", "y", "radius"}
            missing = required - overlay["data"].keys()
            if missing:
                raise ValueError(f"Circle overlay '{overlay['id']}': "
                    f"missing {sorted(missing)}")   
        elif overlay["type"] == "path":
            if "d" not in overlay["data"]:
                raise ValueError(f"Path overlay '{overlay['id']}': "
                    "missing 'd'")
        # Default class
        overlay.setdefault("class", "default")


#### MAIN

_component = st.components.v2.component(
    "streamlit-image-overlay.streamlit_image_overlay",
    js = "index-*.js",
    html = '<div class="react-root"></div>',
)

def streamlit_image_overlay(
    image = None,
    overlays = None,
    styles = None,
    showHelp = True,
    key = "overlay",
):   
    # support image type is PIL and np.ndarray
    validate_image(image)

    validate_overlays(overlays)

    validate_styles(styles)    

    buffer = io.BytesIO()
    image.save(buffer, format = "PNG")
    width, height = image.size
    imageBase64 = (
        "data:image/png;base64,"
        + base64.b64encode(buffer.getvalue()).decode("utf-8")
    )

    return _component(
        key = key,
        data = {
            "image": {
                "src": imageBase64,
                "width": width,
                "height": height,
            },
            "overlays": overlays,
            "styles": styles or {},
            "showHelp": showHelp
        },
        default = None
    )
