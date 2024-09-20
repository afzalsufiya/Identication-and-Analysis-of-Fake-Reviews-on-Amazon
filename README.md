# Identification and Analysis of Fake Customer Reviews - An Empirical Study on Customer Reviews from Amazon (Master Thesis)


This repository contains the code and data for the master thesis project aimed at identifying and analysing fake consumer reviews on Amazon. The project leverages advanced machine learning and deep learning techniques, including the use of the RoBERTa model, to develop a robust review detection algorithm. Also, this thesis majorly focus on understanding the 


## Project Overview

The study aims to measure the frequency of fraudulent reviews on Amazon and investigate the factors that differentiate genuine reviews from fraudulent ones. The method classifies reviews as authentic or fraudulent by implementing deep learning techniques. The primary goals also include understanding the variation in review rates across various attributes like product categories, product ratings, review length and identifying specific classification patterns or relations between these attributes. The research includes best fitting of various machine learning models to understand the classification patterns in honest and fake customer reviews.

This thesis makes a substantial contribution to our knowledge of fraudulent reviews on Amazon and how they affect consumer behavior. The results will help consumers, researchers, and e-commerce platforms by shedding light on the prevalence, patterns, and identification of consumer reviews. Furthermore, the study shows how modern machine learning models can be used to improve the dependability of online customer evaluations.

## Installation

1. **Clone the repository**:
 ```sh
   git clone https://mygit.th-deg.de/as05480/identication-and-analysis-of-fake-reviews-on-amazon-master-thesis.git
   cd identication-and-analysis-of-fake-reviews-on-amazon-master-thesis
```

2. **Set up a virtual environment**:
 ```sh
python -m venv venv
```

3. **Activate the virtual environment**:

- Windows:
 ```sh
venv\Scripts\activate 
```
- macOS:
 ```sh
source venv/bin/activate
```


4. **Install the required libraries**:
 ```sh
pip install -r requirements.txt
```

## Usage

1. Data Preparation:
- To scrap the data from Amazon, the `DataScraper` can be used.
- To use the already scraped data, please download `AmazonReviews-row` from `DataScraper/` directory.

2. Pre-processing and Translation:
- Run the `Pre-Processing&Translation` script.

3. RoBERTa Implementation:
- Run `roberta-classification` script from `RoBERTa_Review_Classification/`

4. Classification Pattern Analysis:
- Please run script from `ClassificationPatterns` directory.

```sh
├── Data_Scraping/
│   ├── AmazonReviews-Row.db
│   ├── DataScraper.py
│   ├── Scraped Databases- Category wise/
├── Pre-processing_&_Translation/
│   ├── AmazonReviews-processed.db
│   ├── Translation&Pre-processing.ipynb
├── RoBERTa_Review_Classification/
│   ├── AmazonReviews-predicted.db
│   ├── DummyDataSet.csv
│   ├── roberta-classification.ipynb
│   ├──roberta-pretrained1.pt
├── ClassificationPatterns/
│   ├── AmazonReviews-predicted.db
│   ├── ClassificationPatterns.ipynb
├── requirements.txt
├── README.md
```
## Features

- Data Scraping: Script for scraping the review data from Amazon pages.
- Data Preprocessing: Scripts for cleaning and preparing the data for model training and analysis
- Model Training: Training scripts for RoBERTa model and other various machine learning models.
- Classification Patterns: Script for analysing the classification patterns using featuire analysis.

## Models and Techniques
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- RoBERTa Model for Sequence Classification
- SMOTE for Handling Class Imbalance
- ExtraTrees Classifier
- BeautifulSoup
- SMOTE

## Contact
For any questions or inquiries, please contact Afzal Sufiya at [afzal.sufiya@stud.th-deg.de](url).

