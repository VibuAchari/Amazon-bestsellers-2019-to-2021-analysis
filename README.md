# Amazon Best-Selling Books Analysis (2009-2021)

This repository contains a machine learning project that analyzes Amazon's best-selling books from 2009 to 2021. The analysis focuses on trends in genre distribution, author performance, book pricing, and user engagement metrics like ratings and reviews.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Analysis Topics](#analysis-topics)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project aims to provide insights into the trends and patterns among Amazon's best-selling books over a span of 12 years. The analysis includes genre distribution, comparison of fiction and non-fiction sales, top authors, price trends, and more.

## Project Structure
The project is organized into several folders to separate different components:

- **data/**: Contains the raw and processed data files.
- **notebooks/**: Jupyter notebooks used for analysis and their HTML exports.
- **images/**: Visualizations generated from the analysis, stored as PNG files.
- **scripts/**: Python scripts used for data processing and generating plots.
- **README.md**: This file, providing an overview and instructions for the project.
- **requirements.txt**: Lists the Python dependencies required to run the project.

## Analysis Topics
1. **Distribution of Genres (2019-2021)**:
   - Visualizations:
     - Horizontal Bar Graph
     - Pie Chart
   - Key Findings: Non-fiction books dominate the market with 55.51% of sales, followed by fiction (44.09%) and a small fraction of unknown genres (0.40%).

2. **Distribution of Fiction vs. Non-Fiction (2009-2019)**:
   - Visualization: Line chart showing trends over time.
   - Key Findings: Trend analysis of how the popularity of fiction and non-fiction genres has evolved.

3. **Top 10 Best-Selling Authors (2009-2021)**:
   - Visualization: Solarize_light2 styled plot.
   - Key Findings: Identification of authors who consistently performed well over the years.

4. **Top 20 Best-Selling Authors Details**:
   - Visualization: Combination of different plots showcasing traits of the top 20 authors.
   - Key Findings: Deep dive into the characteristics that made these authors successful.

5. **Trend of Average Book Prices Over Time by Genre**:
   - Key Findings: Insights into how the pricing of books in different genres has changed over the years.

6. **Scatter Plot of Ratings vs. Number of Reviews**:
   - Visualization: Scatter plot.
   - Key Findings: Exploration of the relationship between book ratings and the number of reviews.

## Installation
To run this project, you will need Python 3.x and the required libraries listed in `requirements.txt`. You can install them using pip:

```bash
pip install -r requirements.txt
