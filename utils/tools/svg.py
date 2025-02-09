import os


def load_svg_icon(path):
    """Load all SVG icons from the specified folder."""
    icons = {}  # Initialize a dictionary to store icons
    if os.path.exists(path) and os.path.isdir(path):
        for svg_file in os.listdir(path):
            if svg_file.endswith('.svg'):
                icon_name = os.path.splitext(svg_file)[0]  # Remove the .svg extension
                icon_path = os.path.join(path, svg_file)  # Construct full path
                with open(icon_path, 'r') as f:
                    icons[icon_name] = f.read()  # Read and store the SVG content
    else:
        raise FileNotFoundError(f"The path '{path}' does not exist or is not a directory.")

    return svg_icons

