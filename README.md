# Streamlit Image Overlay

A Streamlit component for displaying images with interactive overlays.

The component is designed for image analysis tasks where geometric objects need to be displayed over an image and remain aligned during zooming and panning.

## Features

* Image display with zoom and pan
* SVG-based overlays
* Hover interaction and optional tooltips
* Multiple overlay types in a single component
* Per-type and per-class styling
* Support for filled and unfilled shapes
* SVG paths with arbitrary geometry and holes
* Image-coordinate-based overlay positioning

## Basic usage

```python
from streamlit_image_overlay import streamlit_image_overlay

streamlit_image_overlay(
    image=image,
    overlays=overlays,
)
```

The component accepts PIL images and NumPy arrays.

## Overlay model

Overlays are passed as a list of objects. Each overlay contains:

* `id` — object identifier
* `type` — overlay type
* `class` — optional visual class; `"default"` is used when omitted
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

Overlay types support a default style and optional class-specific styles. Class-specific styles override the default style, while unspecified properties retain their default values.

This allows different semantic classes of the same overlay type to be displayed differently without storing visual styles inside individual overlay objects.

## Development

The `example.py` file contains interactive examples demonstrating:

* circles
* paths with holes
* multiple overlay classes
* class-specific styles
* viewport and tooltip customization

These examples serve as the primary reference for the current API.


## License

Permission is granted to use this software for personal,
educational and research purposes.

Commercial use, redistribution, modification, or creation
of derivative works is prohibited without prior written
permission from the copyright holder.

For commercial licensing: muwsik@mail.ru