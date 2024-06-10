
# Top5 Flicks

Top5 Flicks is a machine learning-based movie recommendation system that suggests the top 5 movies based on the user's taste. The project leverages TMDB data and TMDB API for fetching movie details and user preferences. The model is built using Jupyter Notebook, and the website is developed using PyCharm with the Streamlit library.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Model Building](#model-building)
- [Website Development](#website-development)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Top5 Flicks aims to provide personalized movie recommendations by analyzing users' tastes and preferences. The system recommends five movies that the user is likely to enjoy.

## Features

- Personalized movie recommendations
- Utilizes TMDB data and API
- Interactive web interface using Streamlit
- Easy-to-use and intuitive UI

## Data Sources

- Movie data: [Kaggle](https://www.kaggle.com/)
- Movie details and user preferences: [TMDB API](https://www.themoviedb.org/documentation/api)

## Installation

To get started with Top5 Flicks, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Top5Flicks.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Top5Flicks
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Jupyter Notebook

1. Open Jupyter Notebook.
2. Navigate to the `notebooks` directory.
3. Open `Top5Flicks_Model.ipynb` and run all cells to train the model.

### Running the Streamlit App

1. Navigate to the `app` directory.
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the app.

## Model Building

The model is built using collaborative filtering techniques to provide personalized movie recommendations. The Jupyter Notebook `movie.ipynb` contains all the steps for data preprocessing, model training, and evaluation.

## Website Development

The website is developed using the Streamlit library, providing an interactive and user-friendly interface. The main script `app.py` in the `app` directory contains the code for the Streamlit app.
