# Streamlit Image Overlay

A Streamlit component for displaying images with interactive overlays.

The component is designed for image analysis tasks where geometric objects need to be displayed over an image and remain aligned during zooming and panning.

## Features

* Image display with zoom and pan
* SVG-based overlays
* Hover interaction and optional tooltips
* Multiple overlay types in a single component
* Per-type and per-class styling
* Class-specific hover styles
* Support for filled and unfilled shapes
* SVG paths with arbitrary geometry and holes
* Image-coordinate-based overlay positioning

## Installation

Install the package from [PyPI](https://pypi.org/project/streamlit-image-overlay/):

```bash
pip install streamlit-image-overlay
```

## Basic usage

```python
from streamlit_image_overlay import streamlit_image_overlay

streamlit_image_overlay(
    image = image,
    overlays = overlays,
)
```

The component accepts PIL images and NumPy arrays.

## Overlay model

Overlays are passed as a list of objects. Each overlay contains:

* `id` — object identifier
* `type` — overlay type
* `class` — visual class used to select the corresponding style
* `data` — geometry-specific data
* `tooltip` — optional text displayed on hover

Currently supported overlay types:

* `circle` — defined by center coordinates and radius
* `path` — defined by an SVG `path` `d` attribute

The `path` type can represent arbitrary shapes, including shapes with holes. Complex geometry can be generated in Python before being passed to the component.

## Styles

Styles are passed through the `styles` parameter.

Styles can be specified for:

* `viewport`
* `tooltip`
* `circle`
* `path`

Each overlay type contains styles organized by class. Each class can define:

* `style` — appearance of the overlay in its normal state
* `hover` — appearance of the overlay when the pointer is over it

The `"default"` class can be used when no visual class distinction is needed.

For example:

```python
styles = {
    "circle": {
        "default": {
            "style": {
                "stroke": "white",
                "strokeWidth": 1,
            },
            "hover": {
                "stroke": "yellow",
            },
        },
        "bacteria": {
            "style": {
                "stroke": "red",
            },
            "hover": {
                "stroke": "yellow",
                "strokeWidth": 3,
            },
        },
    },
}
```

Class-specific styles are applied on top of the component's default overlay style. During hover, the built-in default hover style is applied first, and class-specific `hover` properties can override it.

This allows different semantic classes of the same overlay type to have independent visual and hover behavior without storing visual styles inside individual overlay objects.

## Development

The `example.py` file contains interactive examples demonstrating:

* circles
* paths with holes
* multiple overlay classes
* class-specific styles
* class-specific hover styles
* viewport and tooltip customization

These examples serve as the primary reference for the current API.

## License

Permission is granted to use this software for personal,
educational and research purposes.

Commercial use, redistribution, modification, or creation
of derivative works is prohibited without prior written
permission from the copyright holder.

For commercial licensing: [muwsik@mail.ru](mailto:muwsik@mail.ru)