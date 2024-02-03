# NYPD Motor Vehicle Collision Analysis

This repository contains data extraction, cleaning, preprocessing, and analysis of New York City motor vehicle collision data. We utilized the Socrata Open Data API (SODA) in Python to extract the raw data and the Polars library for data cleaning and preprocessing. The cleaned data was uploaded to the Google Cloud Platform (GCP) and analyzed using BigQuery. Finally, we created visualizations in Tableau to gain insights from the data.

## Table of Contents

- [Introduction](#introduction)
- [Data Extraction](#data-extraction)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Uploading Cleaned Data to GCP](#uploading-cleaned-data-to-gcp)
- [Data Analysis with BigQuery](#data-analysis-with-bigquery)
- [Data Visualizations in Tableau](#data-visualizations-in-tableau)
- [Future Works](#future-works)

## Introduction

The NYPD Motor Vehicle Collision dataset is a valuable resource for analyzing traffic accidents in New York City. This project aims to extract, clean, and analyze this data to gain insights into patterns and trends related to motor vehicle collisions.

## Data Extraction

We used the Socrata Open Data API (SODA) in Python to retrieve the NYPD Motor Vehicle Collision dataset. SODA provides a convenient way to access data from various sources, making it easier to collect and work with open data. You can find the extraction code in the `data_extraction.py` file.

## Data Cleaning and Preprocessing

We leveraged the Polars library in Python for data cleaning and preprocessing. Polars is a powerful DataFrame library that provides fast data manipulation capabilities similar to pandas but optimized for performance. It offers a wide range of operations, making it suitable for handling large datasets efficiently.

### About Polars
Polars is a modern DataFrame library that provides expressive and powerful data manipulation and analysis tools. Some key features of Polars include:
- High-performance query execution
- Support for complex data operations
- Easy integration with various data sources
- Memory-efficient operations
- Columnar data storage

You can view the complete data cleaning and preprocessing code in the `data_cleaning.ipynb` Jupyter Notebook.

## Uploading Cleaned Data to GCP

After cleaning and pre-processing the data, we uploaded it to Google Cloud Platform (GCP) for further analysis. GCP provides a scalable and reliable cloud infrastructure for storing and processing large datasets.

## Data Analysis with BigQuery

We used BigQuery, a fully managed, serverless data warehouse on GCP, to analyze in-depth data. BigQuery allows us to run SQL queries on large datasets quickly and efficiently, making it ideal for exploring the NYPD Motor Vehicle Collision data.

## Data Visualizations in Tableau

We used Tableau to create interactive data visualizations to gain insights from the dataset. You can find the Tableau visualization files in the `tableau_visualizations` directory.

## Future Works
- [ ] Add Insights
- [ ] Add Conclusion
