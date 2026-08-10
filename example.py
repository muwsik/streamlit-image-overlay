import streamlit as st

from PIL import Image
import numpy as np

from streamlit_image_overlay import streamlit_image_overlay

          
st.set_page_config(page_title = "Test overlay", layout = "wide")

uploadedImg = st.file_uploader("Choose image",
    type = ["tif", "tiff", "png", "jpg", "jpeg" ]
)

if uploadedImg is not None:
    srcImage = Image.open(uploadedImg).convert("L")

    overlays = []
    for i in range(100):
        x = np.random.randint(0, 1200)
        y = np.random.randint(0, 800)
        radius = np.random.uniform(2, 20)

        overlays.append(
            {
                "id": str(i),
                "type": "circle",
                "data": {
                    "x": x,
                    "y": y,
                    "radius": radius,
                },
                "tooltip": (
                    f"ID: {i}\n"
                    f"Center: ({x}, {y}) px \n"
                    f"Radius: {radius:.2f} px"
                ),
            }
        )

    with st.container(horizontal=True):
        streamlit_image_overlay(
            key = "test2",
            image = srcImage,
            overlays = overlays,
            styles = {
                "viewport": {
                    "width": "100%",
                    "height": "100%",
                    "margin": "0 auto",
                },
            }
        )

        streamlit_image_overlay(
            key = "test",
            image = srcImage,
            overlays = overlays,
            styles = {
                "viewport": {
                    "width": "100%",
                    "height": "100%",
                    "margin": "0 auto",
                    "image-rendering": "smooth",
                },
                "tooltip": {
                    "background-color": "black",
                    "color": "white",
                    "border-radius": "10px",
                    "padding": "15px",
                    "font-size": "16px",
                    "white-space": "pre-line"
                },
                "circle": {
                    #"fill": "green",
                    "stroke": "green",
                    "stroke-width": 5,
                    #"opacity": 0.75,
                }
            }                    
        )
