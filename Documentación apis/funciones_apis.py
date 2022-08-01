import pandas as pd
import time
from twelvedata import TDClient
import numpy as np


api_messari = '69ff96a9-b882-49c8-816b-2f7edea5a90f'



def api_twelve(symbol : str, interval: str, start: str, end: str,outputsize : int, order: str, exchange: str):
    
    
    # Initialize client - apikey parameter is requiered
    td = TDClient(apikey="44ec61bab5ef4a9c8e5061515ae11dd2")

    # Construct the necessary time series
    ts = td.time_series(symbol=symbol,interval=interval,timezone="America/New_York",start_date = start,end_date=end
                        ,order=order,outputsize=outputsize,exchange=exchange)

    df = ts.as_pandas() #dataframe with ohlc prices 1D interval
    time.sleep(5)
    df1 = ts.without_ohlc().with_aroonosc().with_atr().with_avgprice().with_bbands().with_cci().with_cmo().as_pandas()
    time.sleep(60)
    df2 = ts.without_ohlc().with_bop().with_dx().with_ema().as_pandas()
    time.sleep(60)
    df3 = ts.with_heikinashicandles().as_pandas() #añadir al final del todo
    time.sleep(60)
    df4 = ts.without_ohlc().with_ichimoku().with_kama().with_keltner(ma_type = 'EMA').with_kst().as_pandas()
    time.sleep(60)
    df5 = ts.with_mama().with_max().with_min().with_hlc3().as_pandas()
    time.sleep(60)
    df6 = ts.without_ohlc().with_ht_dcperiod().with_ht_dcphase().with_ht_phasor().with_ht_sine().with_ht_trendline().with_ht_trendmode().as_pandas()
    time.sleep(60)
    df7 = ts.without_ohlc().with_ma(time_period=50).with_ma(time_period=100).with_ma(time_period=200).with_trima().as_pandas()
    time.sleep(60)
    df8 = ts.without_ohlc().with_ma(ma_type = 'EMA',time_period=9).with_ma(ma_type = 'EMA',time_period=12).with_ma(ma_type = 'EMA',time_period=21).with_ma(ma_type = 'EMA',time_period=55).as_pandas()
    time.sleep(60)
    df9 = ts.without_ohlc().with_ma(ma_type = 'DEMA',time_period=9).with_ma(ma_type = 'DEMA',time_period=12).with_ma(ma_type = 'DEMA',time_period=21).with_ma(ma_type = 'DEMA',time_period=55).as_pandas()
    time.sleep(60)
    df10 = ts.without_ohlc().with_ma(ma_type = 'TEMA',time_period=9).with_ma(ma_type = 'TEMA',time_period=12).with_ma(ma_type = 'TEMA',time_period=21).with_ma(ma_type = 'TEMA',time_period=55).as_pandas()
    time.sleep(60)
    df11 = ts.without_ohlc().with_linearreg().with_linearregangle().with_linearregslope().with_linearregintercept().as_pandas()
    time.sleep(60)
    df12 = ts.without_ohlc().with_macd().with_macd_slope().with_mcginley_dynamic().with_medprice().with_mfi().as_pandas()
    time.sleep(60)
    df13 = ts.without_ohlc().with_midprice().with_minus_di().with_minus_dm().with_mom().with_natr().with_obv().as_pandas()
    time.sleep(60)
    df14 = ts.without_ohlc().with_percent_b().with_pivot_points_hl().with_plus_dm().with_plus_di().with_roc().with_rocp().as_pandas()
    time.sleep(60)
    df15 = ts.without_ohlc().with_ppo().with_rocr().with_rocr100().with_rsi().with_rvol().with_sar().with_stoch().as_pandas()
    time.sleep(60)
    df16 = ts.without_ohlc().with_stochrsi().with_supertrend().with_trange().with_tsf().with_typprice().with_ultosc().as_pandas()
    time.sleep(60)
    df17 = ts.without_ohlc().with_vwap().with_wclprice().with_willr().with_wma().as_pandas()
    time.sleep(60)
    df18 = ts.with_ad().with_adosc().with_adx().with_adxr().with_apo(ma_type = 'EMA').with_aroon().as_pandas()
    
    dfti = pd.concat([df,df1,df2,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df3], axis = 1)
    
    dfti.columns = ('Open', 'High','Low','Close','Aroon Oscillator','Average True Range','Average Price 9','Bband upper_band','Bbands middle_band','Bbands lower_band','Balance of Power','Commodity Channel Index','Chande Momentum Oscillator',
 'Balance of Power','Directional Movement Index','Ema','Tenkan_sen','Kijun_sen','Senkou_span_a','Senkou_span_b','Chikou_span','Kaufmans Adaptive Moving Average','Keltner upper_line','Keltner middle_line','Keltner lower_line','Know sure things',
 'Kst_signal','High, Low, Close Average Values','MESA Adaptive Moving Average','Fama','Max Close Price 9','Min Close price 9','Ht_dcperiod','In_phase','Quadrature','Ht_sine','Ht_trendline','Ht_trendmode','SMA 50','SMA 100','SMA 200','TMA 9'               
 'EMA 9','EMA 12','EMA 55','DEMA 9','DEMA 12','DEMA 21','DEMA 55','TEMA 9','TEMA 12','TEMA 21','TEMA 55','Linear Regression','Linear Regression Angle','Linear Regression Intercept','Macd','Macd_signal','Macd_hist','Macd_slope','Macd_signal_slope',
 'Macd_hist_slope' 'Mcginley_dynamic' 'Median Price'  'Midpoint Price over period 9', 'Minus_dm'  'Normalized Average True Range', '%B Indicator', 'Pivot_point_high', 'Pivot_point_low',  'Plus_di', 'Rate Of CHange percentage',
 'Percentage Price Oscillator','Rate of Change Ratio','Rate of change ratio 100 scale','RSI 14','Relative Volume Indicator','Parabolic SAR','Stoch slow_d','Stch RSI fast_k','Stoch RSi fast_d','Supertrend','True Range','Time series forecast 9',
 'Typial price','Ultimate Oscilator','Volume Weighted Average Price','Weighted Close Price','Williams %R','Weighted Moving Average 9','open 1','high 1','low 1','close 1','Chaikin A/D Line','Chaikin A/D Oscillator','Average Directional Index',
 'Average Directional Movement Index Rating','Absolute Price Oscillator','Aroon_down','Aroon_up','Heikin highs','Heikin opens','Heikin closes','H ikinl ows')
    
    dfti.drop(['open 1' ,'high 1', 'low 1', 'close 1'], axis =1, inplace = True)  
    
    dfti["Cosine"] = dfti["Close"].map(lambda x: np.cos(x))
    dfti["Hyperbolic Cosine"] = dfti["Close"].map(lambda x: np.cosh(x))
    dfti["Arctan"] = dfti["Close"].map(lambda x: np.arctan(x))
    dfti["Tangent"] = dfti["Close"].map(lambda x: np.tan(x))
    dfti["Hyperbolic Tangent"] = dfti["Close"].map(lambda x: np.tanh(x))
    dfti["Std 2"] = dfti["Close"].rolling(2).std()
    dfti["Std 7"] = dfti["Close"].rolling(7).std()
    dfti["Std 9"] = dfti["Close"].rolling(9).std()
    dfti["Var 1"] = dfti["Close"].rolling(2).std()
    dfti["Var 7"] = dfti["Close"].rolling(7).std()
    dfti["Var 9"] = dfti["Close"].rolling(9).std()
    
    return df
    return dfti

def api_messarri():
    
    start = '2012-01-31'
    end = '2012-12-31'

    dataframes = {}

    for i in lista_idmetrics_sinerc:
        dataframes[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2012 = pd.concat(dataframes.values(), axis = 1)

    start = '2013-01-01'
    end = '2013-12-31'

    dataframes1 = {}

    for i in lista_idmetrics_sinerc:
        dataframes1[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2013 = pd.concat(dataframes1.values(), axis = 1)

    start = '2014-01-01'
    end = '2014-12-31'

    dataframes2 = {}

    for i in lista_idmetrics_sinerc:
        dataframes2[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2014 = pd.concat(dataframes2.values(), axis = 1)

    start = '2015-01-01'
    end = '2015-12-31'

    dataframes3 = {}

    for i in lista_idmetrics_sinerc:
        dataframes3[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2015 = pd.concat(dataframes3.values(), axis = 1)

    start = '2016-01-01'
    end = '2016-12-31'

    dataframes4 = {}

    for i in lista_idmetrics_sinerc:
        dataframes4[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2016 = pd.concat(dataframes4.values(), axis = 1)

    start = '2017-01-01'
    end = '2017-12-31'

    dataframes5 = {}

    for i in lista_idmetrics_sinerc:
        dataframes5[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2017 = pd.concat(dataframes5.values(), axis = 1)

    start = '2018-01-01'
    end = '2018-12-31'

    dataframes6 = {}

    for i in lista_idmetrics_sinerc:
        dataframes6[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2018 = pd.concat(dataframes6.values(), axis = 1)

    start = '2019-01-01'
    end = '2019-12-31'

    dataframes7 = {}

    for i in lista_idmetrics_sinerc:
        dataframes7[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2019 = pd.concat(dataframes7.values(), axis = 1)

    start = '2020-01-01'
    end = '2020-12-31'

    dataframes8 = {}

    for i in lista_idmetrics_sinerc:
        dataframes8[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2020 = pd.concat(dataframes8.values(), axis = 1)

    start = '2021-01-01'
    end = '2021-12-31'

    dataframes9 = {}

    for i in lista_idmetrics_sinerc:
        dataframes9[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2021 = pd.concat(dataframes9.values(), axis = 1)

    start = '2022-01-01'
    end = '2022-07-09'

    dataframes10 = {}

    for i in lista_idmetrics_sinerc:
        dataframes10[i]= messari.get_metric_timeseries2(asset_slugs='bitcoin',start= start,end = end,asset_metric=i)
        time.sleep(1.2)

    df2022 = pd.concat(dataframes10.values(), axis = 1)


    dfocm = pd.concat(df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019,df2020,df2021,df2022)
    
    return dfocm