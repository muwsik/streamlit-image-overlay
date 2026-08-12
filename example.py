import streamlit as st

from PIL import Image
import numpy as np

from streamlit_image_overlay import streamlit_image_overlay as overlay

def randomCircle(_n, _size, _border, _class = "default",):
    overlaysCircle = []
    for i in range(_n):
        x = np.random.randint(0, _size[0])
        y = np.random.randint(0, _size[1])
        radius = np.random.uniform(_border[0], _border[1])

        overlaysCircle.append(
            {
                "id": str(i) + _class,
                "type": "circle",
                "class": _class,
                "data": {
                    "x": x,
                    "y": y,
                    "radius": radius,
                },
                "tooltip": (
                    f"ID: {i}\n"
                    f"Center: ({x}, {y}) px \n"
                    f"Radius: {radius:.2f} px\n"
                    f"Class: {_class} "
                ),
            }
        )
    return overlaysCircle


def randomPath(_n, _size, _border, _holeCount = 1, _class = "default", ):
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

        overlaysPath.append( {
            "id": str(i) + _class,
            "type": "path",
            "class": _class,
            "data": {
                "d": path,
            },
            "tooltip": (
                f"ID: {i}\n"
                f"Center: ({x}, {y}) px\n"
                f"Radius: {radius:.2f} px\n"
                f"Holes: {_holeCount}\n"
                f"Class: {_class}"
            ),
        } )

    return overlaysPath


#### MAIN       
st.set_page_config(page_title = "Test overlay", layout = "wide")

uploadedImg = st.file_uploader("Choose image",
    type = ["tif", "tiff", "png", "jpg", "jpeg", "bmp" ]
)

if uploadedImg is not None:
    srcImage = Image.open(uploadedImg).convert("L")
    
    # path examples
    with st.container(horizontal = True):
        overlay(
            key = "path-test1",
            image = srcImage,
            overlays = randomPath(5, (1200, 1000), (50, 150), 1),
        )

        overlay(
            key = "path-test2",
            image = srcImage,
            overlays = randomPath(150, (1000, 800), (20, 50), 0),
            styles = {
                "path": {
                    "default": {
                        "stroke": "blue",
                        "strokeWidth": 1,
                    }
                }
            }    
        )

        overlay(
            key = "path-test3",
            image = srcImage,
            overlays = 
                randomPath(2, (500, 500), (100, 200), 2) 
                +
                randomPath(10, (1000, 800), (10, 20), 0, "bacteria", )                
                +
                randomPath(1, (1000, 1000), (100, 400), 2, "biofilm", )
                ,
            styles = {
                "path": {
                    "default": {
                        "stroke": "blue",
                        "strokeWidth": 2,
                    },
                    "class": {
                        "bacteria": {
                            "stroke": "red",
                            "strokeWidth": 3,
                        },
                        "biofilm": {
                            "stroke": "green",
                            "strokeWidth": 1,
                        }
                    }
                }
            }                
        )

    # circle examples
    with st.container(horizontal = True):
        overlay(
            key = "circle-test1",
            image = srcImage,
            overlays = randomCircle(250, (1000, 1000), (10, 15)),
        )

        overlay(
            key = "circle-test2",
            image = srcImage,
            overlays = randomCircle(150, (1000, 800), (20, 50)),
            styles = {
                "circle": {
                    "default": {
                        "stroke": "blue",
                        "strokeWidth": 1,
                    }
                }
            }      
        )

        overlay(
            key = "circle-test3",
            image = srcImage,
            overlays = 
                randomCircle(100, (1000, 800), (10, 20))
                +
                randomCircle(10, (1000, 800), (50, 60), "large")
                +
                randomCircle(10, (1000, 800), (1, 5), "small")
                ,
            styles = {
                "circle": {
                    "default": {
                        "stroke": "blue",
                        "strokeWidth": 5,
                    },
                    "class": {
                        "large": {
                            "stroke": "red",
                            "strokeWidth": 10,
                        },                        
                        "small": {
                            "stroke": "yellow   ",
                            "strokeWidth": 3,
                        }
                    }
                }
            }                      
        )

    # styles examples
    with st.container(horizontal = True):
        overlay(
            key = "styles-test1",
            image = srcImage,
            overlays = 
                randomCircle(250, (1000, 1000), (10, 15))
                +                
                randomPath(2, (1100, 1100), (100, 200), 0) 
                ,
            styles = {
                "viewport": {
                    "width": "250px",
                    "height": "250px",           
                    "outline": "1px dotted #fff",
                },
                "tooltip": {
                    "backgroundColor": "black",
                    "color": "white",
                    "borderRadius": "10px",
                    "padding": "15px",
                    "fontSize": "16px",
                    "whiteSpace": "pre-line"
                },
            }
        )

        overlay(
            key = "styles-test2",
            image = srcImage,
            overlays = randomCircle(250, (1000, 1000), (10, 15)),
            styles = {
                "viewport": {
                    "width": "700px",                 
                    "border": "5px dashed #fff",
                    "outline": "5px dotted #555",
                },
                "tooltip": {
                    "background-color": "white",
                    "color": "black",
                    "border-radius": "1px",
                    "padding": "5px",
                    "font-size": "10px",
                },
            }
        )