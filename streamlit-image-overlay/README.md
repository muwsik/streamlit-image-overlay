# streamlit-image-overlay

Interactive image overlay component for Streamlit

## Installation instructions

```sh
uv pip install streamlit-image-overlay
```

### Development install (editable)

When developing this component locally, install it in editable mode so Streamlit picks up code changes without rebuilding a wheel. Run this from the directory that contains `pyproject.toml`:

```sh
uv pip install -e . --force-reinstall
```

## Usage instructions

```python
import streamlit as st

from streamlit_image_overlay import streamlit_image_overlay

value = streamlit_image_overlay()

st.write(value)
```

## Build a wheel

To package this component for distribution:

1. Build the frontend assets (from `streamlit_image_overlay/frontend`):

   ```sh
   npm i
   npm run build
   ```

2. Build the Python wheel using UV (from the project root):
   ```sh
   uv build
   ```

This will create a `dist/` directory containing your wheel. The wheel includes the compiled frontend from `streamlit_image_overlay/frontend/build`.

### Requirements

- Python >= 3.10
- Node.js >= 24 (LTS)

### Expected output

- `dist/streamlit_image_overlay-0.0.1-py3-none-any.whl`
- If you run `uv run --with build python -m build` (without `--wheel`), you’ll also get an sdist: `dist/streamlit-image-overlay-0.0.1.tar.gz`
