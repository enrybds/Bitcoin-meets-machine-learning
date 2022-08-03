<p align="center">
  <img width="460" height="460" src="https://user-images.githubusercontent.com/105368099/182561824-ee67e315-b609-4e57-ba31-3030ce21986f.png">
</p>

The project aims to test different machine learning models to predict the percentage of change and the price of Bitcoin. 

## Technologies
* Python
* Jupyter

### Python Libraries

* Numpy
* Pandas
* Matpltlib
* Seaborn
* Plotly
* Time
* Twelvedata
* Messari
* Sklearn
* Keras
* Lime
* Backtesting

## Data

For the creation of our dataset we have used three types of data:
  * Price of bitcoin between 2012 and 2022
  * Technical Indicators
  * On chain metrics
 
 We have extracted the prices and technical indicators from the twelvedata API and the on-chain metrics from the Messari API. In the json files is the information of each of the technical indicators and on chain metrics used.
 
 The main objective is to try to predict the range of the percentage change in the price for the next day and to study its probabilities. To do this, we create 9 lagged periods for each variable in our dataset so that we can later use classification models in previously created price change percentage ranges.
 
 
 ![dfeje](https://user-images.githubusercontent.com/105368099/182575492-f9e3e3d2-c428-438a-bb76-0de02c8ddf7c.png)

 ## EDA
 
 
 
 
 
