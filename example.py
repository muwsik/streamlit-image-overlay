import streamlit as st

from PIL import Image
import numpy as np

from streamlit_image_overlay import streamlit_image_overlay

          
uploadedImg = st.file_uploader("Choose image",
    type = ["tif", "tiff", "png", "jpg", "jpeg" ]
)

if uploadedImg is not None:
    srcImage = Image.open(uploadedImg).convert("L")

    overlays = []
    for i in range(5000):
        x = np.random.randint(0, 1200)
        y = np.random.randint(0, 800)
        radius = np.random.uniform(2, 4)

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
                    f"Center: ({x}, {y})\n"
                    f"Radius: {radius:.2f}"
                ),
            }
        )

    streamlit_image_overlay(
        image = srcImage,
        overlays = overlays,
        key = "main-imageViewer",
        styles = {
            "viewport": {
                #"background-color": "none",
            },
            "image": {
                #"opacity": 0.1,
            },
            "tooltip": {
                "background-color": "black",
                "color": "white",
                "border-radius": "10px",
                "padding": "15px",
                "font-size": "16px",
                #"whiteSpace": "pre-line"
            },
            "circle": {
                #"fill": "green",
                "stroke": "green",
                "stroke-width": 3,
                #"opacity": 0.75,
            }
        }                    
    )
