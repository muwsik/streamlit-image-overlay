import streamlit as st

from PIL import Image
import numpy as np

from streamlit_image_overlay import streamlit_image_overlay

def randomCircle(_n, _size, _border):
    overlaysCircle = []
    for i in range(_n):
        x = np.random.randint(0, _size[0])
        y = np.random.randint(0, _size[1])
        radius = np.random.uniform(_border[0], _border[1])

        overlaysCircle.append(
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
    return overlaysCircle


def randomPath(_n, _size, _border, _holeCount = 1):
    overlaysPath = []

    for i in range(_n):
        # Center of the path
        x = np.random.randint(_border[1], _size[0] - _border[1])
        y = np.random.randint(_border[1], _size[1] - _border[1])

        # Outer contour
        radius = np.random.uniform(_border[0], _border[1])
        pointsCount = np.random.randint(15, 30)

        angles = np.sort(
            np.random.uniform(0, 2 * np.pi, pointsCount)
        )

        radii = radius * np.random.uniform(
            0.8,
            1.2,
            pointsCount
        )

        outerPoints = [
            (
                x + r * np.cos(angle),
                y + r * np.sin(angle)
            )
            for angle, r in zip(angles, radii)
        ]

        path = (
            f"M {outerPoints[0][0]:.1f} "
            f"{outerPoints[0][1]:.1f}"
        )

        for px, py in outerPoints[1:]:
            path += f" L {px:.1f} {py:.1f}"

        path += " Z"

        # Holes
        for _ in range(_holeCount):

            holeRadius = radius * np.random.uniform(0.15, 0.3)

            # Keep the hole inside the outer contour
            angle = np.random.uniform(0, 2 * np.pi)
            distance = np.random.uniform(
                0,
                radius * 0.35
            )

            hx = x + distance * np.cos(angle)
            hy = y + distance * np.sin(angle)

            holePointsCount = np.random.randint(8, 15)

            holeAngles = np.sort(
                np.random.uniform(
                    0,
                    2 * np.pi,
                    holePointsCount
                )
            )

            holeRadii = holeRadius * np.random.uniform(
                0.8,
                1.2,
                holePointsCount
            )

            holePoints = [
                (
                    hx + r * np.cos(angle),
                    hy + r * np.sin(angle)
                )
                for angle, r in zip(holeAngles, holeRadii)
            ]

            path += (
                f" M {holePoints[0][0]:.1f} "
                f"{holePoints[0][1]:.1f}"
            )

            for px, py in holePoints[1:]:
                path += f" L {px:.1f} {py:.1f}"

            path += " Z"

        overlaysPath.append(
            {
                "id": str(i),
                "type": "path",
                "data": {
                    "d": path,
                },
                "tooltip": (
                    f"ID: {i}\n"
                    f"Center: ({x}, {y}) px\n"
                    f"Radius: {radius:.2f} px\n"
                    f"Holes: {_holeCount}"
                ),
            }
        )

    return overlaysPath


#### MAIN       
st.set_page_config(page_title = "Test overlay", layout = "wide")

uploadedImg = st.file_uploader("Choose image",
    type = ["tif", "tiff", "png", "jpg", "jpeg" ]
)

if uploadedImg is not None:
    srcImage = Image.open(uploadedImg).convert("L")
    

    with st.container(horizontal=True):
        streamlit_image_overlay(
                    key = "test3",
                    image = srcImage,
                    overlays = randomPath(5, (1200, 1000), (20, 150), 1),
                )

        streamlit_image_overlay(
            key = "test2",
            image = srcImage,
            overlays = randomPath(150, (1000, 800), (20, 50), 0),
        )

        streamlit_image_overlay(
            key = "test",
            image = srcImage,
            overlays = randomCircle(1000, (1000, 800), (2, 10)),
            styles = {
                "viewport": {
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
                    "stroke-width": 2,
                    #"opacity": 0.75,
                }
            }                    
        )
