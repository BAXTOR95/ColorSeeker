import numpy as np
from sklearn.cluster import KMeans
from PIL import Image


def process_image(filepath, n_colors=5):
    # Open the image file
    with Image.open(filepath) as img:
        # Convert image to RGB
        img = img.convert('RGB')

        # Resize for faster processing, maintaining aspect ratio
        img.thumbnail((100, 100))

        # Convert image data to a list of RGB
        pixels = np.array(img).reshape(-1, 3)

        # Use k-means clustering to find the most dominant colors
        kmeans = KMeans(n_clusters=n_colors)
        kmeans.fit(pixels)

        # Get the RGB values of the centroids (dominant colors)
        colors = kmeans.cluster_centers_

        # Convert floats to integers
        colors = colors.round(0).astype(int)

        # Format colors in 'rgb(r, g, b)' format
        return [f'rgb({color[0]}, {color[1]}, {color[2]})' for color in colors]
