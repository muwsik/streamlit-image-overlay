import streamlit as st

from PIL import Image
import numpy as np

from streamlit_image_overlay import streamlit_image_overlay

          
uploadedImg = st.file_uploader("Choose image",
    type = ["tif", "tiff", "png", "jpg", "jpeg" ]
)

if uploadedImg is not None:
    srcImage = Image.open(uploadedImg).convert("L")

    particles = []
    for i in range(50):
        particles.append(
            {
                "id": i,
                "x": np.random.randint(0, 500),
                "y": np.random.randint(0, 500),
                "diameter": np.random.uniform(5, 25),
                "projectionArea": np.random.uniform(50, 500),
                "volume": np.random.uniform(100, 2000),
                "c0": np.random.randint(80, 255),
                "approxError": np.random.uniform(0, 0.2),
            }
        )

    streamlit_image_overlay(
        image = srcImage,
        overlays = particles,
        key = "main-imageViewer"                    
    )
