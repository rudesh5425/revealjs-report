# analysis.py
# Email: 24ds2000104@ds.study.iitm.ac.in
# This Marimo notebook demonstrates variable dependencies, interactivity, and dynamic markdown.

import marimo as mo

# --- Cell 1: Input widget ---
# This slider controls the value used in downstream dependent cells.
slider = mo.ui.slider(1, 100, value=50)

mo.md("""
# Interactive Data Exploration  
Use the slider below to change the value dynamically.
""")

slider

# --- Cell 2: Computation depending on slider ---
# This computation depends directly on the slider's value.
# Changing the slider automatically updates this computation.
value_squared = slider.value ** 2

value_squared

# --- Cell 3: Dynamic Markdown Output ---
# Documenting data flow:
# slider.value → value_squared → dynamic markdown text
mo.md(f"""
### Dynamic Analysis Result

- **Slider Value:** {slider.value}  
- **Value Squared:** {value_squared}

The chart below updates automatically because Marimo reacts to dependencies.
""")
