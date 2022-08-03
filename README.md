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
 
 We try to see the distribution in the percentage of change and see how it develops over time to choose the period to use in our models and look for patterns prior to days with sharp price changes.
 
 <p align="center">
  <img width="700" height="300" src="https://user-images.githubusercontent.com/105368099/182581143-7ce1580e-44b2-485c-82a7-65958c07988f.png">
</p>
 
It can be seen that at the beginning, due to its lower market capitalization, the price of bitcoin is more sensitive to strong variations and that as time progresses, this deviation is reduced. Therefore for our models we will not use the data between 2012 and 2014.
 
  <p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/105368099/182582064-d77214ae-bacc-49d4-b783-01bd842fb7d8.png">
</p>
   <p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/105368099/182582282-9ee69cfa-2fd8-4609-bc01-1abb6937a0a5.png">
</p>
 
 
It is important to emphasize that most days the price fluctuates between 0/+1% and -1%/0 and therefore our classes are not balanced.

## MODELS

You can see the different classification and regression models used in the percentage of change and their results in the models folder:
  * Random Forest
  *XGBoost
  *SVM
  *Kmeans
  *AgglomerativeClustering
  *Dbscan
  *LSTM


Since the results from the classification models were not good enough, we later changed the focus to regression models for percentage change and price.

The best results were obtained with an LSTM neural network which works very well with time series problems.

![image](https://user-images.githubusercontent.com/105368099/182591010-813b21e6-d3a8-4699-a132-a0bcc49b1c06.png)


This is a backtest for a simple strategy developed from the results of the LSTM neural network. If our model predicts that the price will be higher, we buy, and if the model predicts that it will be lower, we close the trade and open a short position. It is not the optimal way to test this strategy, but with the results it can be seen that the LSTM is a very powerful structure that offers promising results for this type of problem.

![image](https://user-images.githubusercontent.com/105368099/182591686-63618fe3-5a6e-44a3-b628-5d3b00e2f6bc.png)

## Conclusions

* The factors that affect the price of an asset are very different and vary over time, so it is difficult to develop models that identify patterns and provide good predictions. However, using machine learning and having a good prior knowledge of the market you want to delve into, profitable trading strategies can be developed using machine learning.

* It is better to try to simplify the problem and use fewer variables when training the models.

* Neural networks are one of the best models when it comes to obtaining profitable solutions for time series problems.

## Future Work

Probar y optimizar estructuras mas potentes de las redes neuronales LSTM y realizar un backtest sus resultados en diferentes tipos de activos.

