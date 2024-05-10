# ColorSeeker

ColorSeeker is a web application built with Flask and Bootstrap5 that allows users to upload images and identify the most dominant colors present in those images. The application uses k-means clustering from the `scikit-learn` library to analyze and determine the main colors.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Built With](#built-with)
- [Authors](#authors)
- [License](#license)

## Features

- **Image Upload**: Users can upload images to the application to analyze them.
- **Dominant Color Extraction**: Utilizes k-means clustering to find and display the 5 most dominant colors in the uploaded image.
- **Responsive UI**: Built with Bootstrap5, the interface is user-friendly and responsive, adapting to various devices.
- **Color Display**: Shows the dominant colors as color swatches next to the uploaded image.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you can run the app, you will need to have Python installed on your system. The app was developed using Python 3.9, but it should be compatible with any Python 3.x version. You will also need `pip` to install Python dependencies.

### Installing

Follow these steps to get your development environment running:

1. **Clone the repository**

   ```bash
   git clone https://github.com/BAXTOR95/ColorSeeker.git
   cd ColorSeeker
   ```

2. **Set up a Python virtual environment (Optional but recommended)**

   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Flask application**

   ```bash
   python app.py
   ```

   Your app should now be running on [http://localhost:5000](http://localhost:5000).

## Usage

To use ColorSeeker, follow these steps:

1. Navigate to [http://localhost:5000](http://localhost:5000) in your web browser.
2. Click the **Choose File** button and select an image from your computer.
3. Click the **Submit** button to upload the image and analyze it.
4. View the dominant colors displayed as color swatches and the image preview on the result page.

## How It Works

ColorSeeker processes images using the following steps:

1. **Image Upload**: The user uploads an image file through the web interface.
2. **Color Analysis**: The backend reads the image, resizes it for faster processing, and then uses the k-means clustering algorithm to find the most common colors.
3. **Results Display**: The frontend displays these colors as swatches and shows the uploaded image for comparison.

## Built With

- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used.
- [Bootstrap5](https://getbootstrap.com/) - The front-end framework used for responsive design.
- [NumPy](https://numpy.org/) - Handles data structures and transformations for image processing.
- [Pillow](https://python-pillow.org/) - Used for opening, manipulating, and saving many different image file formats.
- [scikit-learn](https://scikit-learn.org/stable/) - Used for applying the k-means clustering algorithm.

## Authors

- **Brian Arriaga** - _Initial work_ - [BAXTOR95](https://github.com/BAXTOR95)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
