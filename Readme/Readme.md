# nCov2019数据分析

## 数据来源

本数据来源于[2019新型冠状病毒疫情时间序列数据仓库](https://github.com/BlankerL/DXY-2019-nCoV-Data)，其数据来源为[丁香园](https://3g.dxy.cn/newh5/view/pneumonia)。


```python
%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_util
import plot_util

from IPython.display import display, Markdown
```


```python
raw_data = data_util.load_data()
```

## 全国数据校验

全国数据是数值较大、自然增长、概率分布、应不受人为干预的数据，所以它应该满足[本福特定律](https://baike.baidu.com/item/本福特定律)（Benford's Law, First-Digit Law），即数据首位数字越小它出现概率越高。比如首位数字是1的概率比9高很多。


```python
raw_city_confirmed = raw_data['city_confirmedCount']

benford_raw = data_util.benford(raw_city_confirmed)
figure = plot_util.plot_bar(benford_raw, '全国数据校验（本福特定律）', 'Digit', 'Percent')
```


![png](./Readme/output_5_0.png)



```python
city_name = '深圳'
```


```python
display(Markdown('## ' + city_name + '数据'))
```


## 深圳数据



```python
raw_data = data_util.load_data()
```


```python
display(Markdown('### ' + city_name + '累计数量'))
```


### 深圳累计数量



```python

city_daily_data = data_util.aggregate_daily(raw_data, city_name)
city_daily_data = data_util.calculate_dead_cured_rate(city_daily_data)
city_daily_data.tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6342</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>366</td>
      <td>0</td>
      <td>46</td>
      <td>0</td>
      <td>2020-02-09 23:00:53.855</td>
      <td>2020-02-09</td>
      <td>0.0</td>
      <td>12.568306</td>
    </tr>
    <tr>
      <td>4735</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>369</td>
      <td>0</td>
      <td>56</td>
      <td>0</td>
      <td>2020-02-10 21:36:08.643</td>
      <td>2020-02-10</td>
      <td>0.0</td>
      <td>15.176152</td>
    </tr>
    <tr>
      <td>2780</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>375</td>
      <td>0</td>
      <td>66</td>
      <td>0</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>0.0</td>
      <td>17.600000</td>
    </tr>
    <tr>
      <td>638</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>386</td>
      <td>0</td>
      <td>82</td>
      <td>0</td>
      <td>2020-02-12 20:15:15.388</td>
      <td>2020-02-12</td>
      <td>0.0</td>
      <td>21.243523</td>
    </tr>
    <tr>
      <td>43</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>386</td>
      <td>0</td>
      <td>82</td>
      <td>0</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>0.0</td>
      <td>21.243523</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data, city_name + '累计')
```


![png](./Readme/output_11_0.png)



```python
display(Markdown('### ' + city_name + '增长速度'))
```


### 深圳增长速度



```python
city_daily_data_1st_derivative = data_util.diff(city_daily_data)
city_daily_data_1st_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6342</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>2020-02-09 23:00:53.855</td>
      <td>2020-02-09</td>
      <td>0.0</td>
      <td>1.551357</td>
    </tr>
    <tr>
      <td>4735</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>2020-02-10 21:36:08.643</td>
      <td>2020-02-10</td>
      <td>0.0</td>
      <td>2.607846</td>
    </tr>
    <tr>
      <td>2780</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>0.0</td>
      <td>2.423848</td>
    </tr>
    <tr>
      <td>638</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>16.0</td>
      <td>0.0</td>
      <td>2020-02-12 20:15:15.388</td>
      <td>2020-02-12</td>
      <td>0.0</td>
      <td>3.643523</td>
    </tr>
    <tr>
      <td>43</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>0.0</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data_1st_derivative, city_name + '增长速度')
```


![png](./Readme/output_14_0.png)



```python
display(Markdown('### ' + city_name + '增长加速度'))
```


### 深圳增长加速度



```python
city_daily_data_2nd_derivative = data_util.diff(city_daily_data_1st_derivative)
city_daily_data_2nd_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6342</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-3.0</td>
      <td>0.0</td>
      <td>-1.0</td>
      <td>0.0</td>
      <td>2020-02-09 23:00:53.855</td>
      <td>2020-02-09</td>
      <td>0.0</td>
      <td>-0.321050</td>
    </tr>
    <tr>
      <td>4735</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-9.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2020-02-10 21:36:08.643</td>
      <td>2020-02-10</td>
      <td>0.0</td>
      <td>1.056489</td>
    </tr>
    <tr>
      <td>2780</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>0.0</td>
      <td>-0.183998</td>
    </tr>
    <tr>
      <td>638</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>2020-02-12 20:15:15.388</td>
      <td>2020-02-12</td>
      <td>0.0</td>
      <td>1.219675</td>
    </tr>
    <tr>
      <td>43</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-11.0</td>
      <td>0.0</td>
      <td>-16.0</td>
      <td>0.0</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>0.0</td>
      <td>-3.643523</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data_2nd_derivative, city_name + '增长加速度')
```

    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:211: RuntimeWarning: Glyph 8722 missing from current font.
      font.set_text(s, 0.0, flags=flags)
    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:180: RuntimeWarning: Glyph 8722 missing from current font.
      font.set_text(s, 0, flags=flags)



![png](./Readme/output_17_1.png)



```python
display(Markdown('### ' + city_name + '死亡治愈率'))
```


### 深圳死亡治愈率



```python
figure = plot_util.plot_conf_dead_cured_ratio(city_daily_data, city_name + '死亡治愈率%')
```


![png](./Readme/output_19_0.png)



```python
black_province_name = '湖北省'
```


```python
display(Markdown('## 全国数据（除' + black_province_name + '）'))
```


## 全国数据（除湖北省）



```python
display(Markdown('因' + black_province_name + '灾情特别严重且现已隔离（' + black_province_name + '加油），它的数据可能和全国其他地区有较大差别。为更精确预计其他地区的未来发展趋势，这里考虑排除其以外的全国其他地区情况。'))
```


因湖北省灾情特别严重且现已隔离（湖北省加油），它的数据可能和全国其他地区有较大差别。为更精确预计其他地区的未来发展趋势，这里考虑排除其以外的全国其他地区情况。



```python
display(Markdown('## 全国累计（除' + black_province_name + '）'))
```


## 全国累计（除湖北省）



```python
white_daily_data = data_util.aggregate_daily_except(raw_data, province_name=black_province_name)
white_daily_data = data_util.calculate_dead_cured_rate(white_daily_data)
```


```python
figure = plot_util.plot_conf_main(white_daily_data, '全国累计（除' + black_province_name + '）')
```


![png](./Readme/output_25_0.png)



```python
display(Markdown('## 全国增长速度（除' + black_province_name + '）'))
```


## 全国增长速度（除湖北省）



```python
white_daily_data_1st_derivative = data_util.diff(white_daily_data)
white_daily_data_1st_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
    <tr>
      <th>updateDate</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2020-02-09</td>
      <td>466.0</td>
      <td>0.0</td>
      <td>267.0</td>
      <td>3.0</td>
      <td>0.017723</td>
      <td>2.106149</td>
    </tr>
    <tr>
      <td>2020-02-10</td>
      <td>433.0</td>
      <td>0.0</td>
      <td>264.0</td>
      <td>7.0</td>
      <td>0.055008</td>
      <td>1.941016</td>
    </tr>
    <tr>
      <td>2020-02-11</td>
      <td>337.0</td>
      <td>0.0</td>
      <td>277.0</td>
      <td>2.0</td>
      <td>0.008100</td>
      <td>2.061066</td>
    </tr>
    <tr>
      <td>2020-02-12</td>
      <td>438.0</td>
      <td>0.0</td>
      <td>400.0</td>
      <td>4.0</td>
      <td>0.022179</td>
      <td>2.848562</td>
    </tr>
    <tr>
      <td>2020-02-13</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.008768</td>
      <td>-0.003629</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(white_daily_data_1st_derivative, '全国增长速度（除' + black_province_name + '）')
```


![png](./Readme/output_28_0.png)



```python
display(Markdown('## 全国增长加速度（除' + black_province_name + '）'))
```


## 全国增长加速度（除湖北省）



```python
white_daily_data_2nd_derivative = data_util.diff(white_daily_data_1st_derivative)
white_daily_data_2nd_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
    <tr>
      <th>updateDate</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2020-02-09</td>
      <td>-92.0</td>
      <td>0.0</td>
      <td>19.0</td>
      <td>-4.0</td>
      <td>-0.043383</td>
      <td>0.089064</td>
    </tr>
    <tr>
      <td>2020-02-10</td>
      <td>-33.0</td>
      <td>0.0</td>
      <td>-3.0</td>
      <td>4.0</td>
      <td>0.037285</td>
      <td>-0.165132</td>
    </tr>
    <tr>
      <td>2020-02-11</td>
      <td>-96.0</td>
      <td>0.0</td>
      <td>13.0</td>
      <td>-5.0</td>
      <td>-0.046908</td>
      <td>0.120049</td>
    </tr>
    <tr>
      <td>2020-02-12</td>
      <td>101.0</td>
      <td>0.0</td>
      <td>123.0</td>
      <td>2.0</td>
      <td>0.014079</td>
      <td>0.787496</td>
    </tr>
    <tr>
      <td>2020-02-13</td>
      <td>-436.0</td>
      <td>0.0</td>
      <td>-400.0</td>
      <td>-3.0</td>
      <td>-0.013411</td>
      <td>-2.852191</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(white_daily_data_2nd_derivative, '全国增长加速度（除' + black_province_name + '）')
```


![png](./Readme/output_31_0.png)



```python
display(Markdown('## 全国增死亡治愈率（除' + black_province_name + '）'))
```


## 全国增死亡治愈率（除湖北省）



```python
figure = plot_util.plot_conf_dead_cured_ratio(white_daily_data, '全国增死亡治愈率%（除' + black_province_name + '）')
```


![png](./Readme/output_33_0.png)



```python
city_name = '武汉'
```


```python
display(Markdown('## ' + city_name + '数据'))
```


## 武汉数据



```python
raw_data = data_util.load_data()
```


```python
display(Markdown('### ' + city_name + '累计数量'))
```


### 武汉累计数量



```python
city_daily_data = data_util.aggregate_daily(raw_data, city_name)
city_daily_data = data_util.calculate_dead_cured_rate(city_daily_data)
city_daily_data.tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6784</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>14982</td>
      <td>0</td>
      <td>878</td>
      <td>608</td>
      <td>2020-02-09 19:09:33.896</td>
      <td>2020-02-09</td>
      <td>4.058203</td>
      <td>5.860366</td>
    </tr>
    <tr>
      <td>4756</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>16902</td>
      <td>0</td>
      <td>1046</td>
      <td>681</td>
      <td>2020-02-10 21:30:02.904</td>
      <td>2020-02-10</td>
      <td>4.029109</td>
      <td>6.188617</td>
    </tr>
    <tr>
      <td>2763</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>18454</td>
      <td>0</td>
      <td>1242</td>
      <td>748</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>4.053322</td>
      <td>6.730248</td>
    </tr>
    <tr>
      <td>487</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>19558</td>
      <td>0</td>
      <td>1380</td>
      <td>820</td>
      <td>2020-02-12 22:07:03.407</td>
      <td>2020-02-12</td>
      <td>4.192658</td>
      <td>7.055936</td>
    </tr>
    <tr>
      <td>26</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>19558</td>
      <td>0</td>
      <td>1380</td>
      <td>820</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>4.192658</td>
      <td>7.055936</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data, city_name + '累计')
```


![png](./Readme/output_39_0.png)



```python
display(Markdown('### ' + city_name + '增长速度'))
```


### 武汉增长速度



```python
city_daily_data_1st_derivative = data_util.diff(city_daily_data)
city_daily_data_1st_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6784</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>1379.0</td>
      <td>0.0</td>
      <td>131.0</td>
      <td>63.0</td>
      <td>2020-02-09 19:09:33.896</td>
      <td>2020-02-09</td>
      <td>0.051734</td>
      <td>0.368930</td>
    </tr>
    <tr>
      <td>4756</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>1920.0</td>
      <td>0.0</td>
      <td>168.0</td>
      <td>73.0</td>
      <td>2020-02-10 21:30:02.904</td>
      <td>2020-02-10</td>
      <td>-0.029094</td>
      <td>0.328251</td>
    </tr>
    <tr>
      <td>2763</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>1552.0</td>
      <td>0.0</td>
      <td>196.0</td>
      <td>67.0</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>0.024213</td>
      <td>0.541631</td>
    </tr>
    <tr>
      <td>487</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>1104.0</td>
      <td>0.0</td>
      <td>138.0</td>
      <td>72.0</td>
      <td>2020-02-12 22:07:03.407</td>
      <td>2020-02-12</td>
      <td>0.139336</td>
      <td>0.325688</td>
    </tr>
    <tr>
      <td>26</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data_1st_derivative, city_name + '增长速度')
```


![png](./Readme/output_42_0.png)



```python
display(Markdown('### ' + city_name + '增长加速度'))
```


### 武汉增长加速度



```python
city_daily_data_2nd_derivative = data_util.diff(city_daily_data_1st_derivative)
city_daily_data_2nd_derivative.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>provinceName</th>
      <th>cityName</th>
      <th>confirmed</th>
      <th>suspected</th>
      <th>cured</th>
      <th>dead</th>
      <th>updateTime</th>
      <th>updateDate</th>
      <th>dead_rate</th>
      <th>cured_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6784</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>-606.0</td>
      <td>0.0</td>
      <td>-74.0</td>
      <td>-4.0</td>
      <td>2020-02-09 19:09:33.896</td>
      <td>2020-02-09</td>
      <td>0.159570</td>
      <td>-0.457331</td>
    </tr>
    <tr>
      <td>4756</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>541.0</td>
      <td>0.0</td>
      <td>37.0</td>
      <td>10.0</td>
      <td>2020-02-10 21:30:02.904</td>
      <td>2020-02-10</td>
      <td>-0.080828</td>
      <td>-0.040679</td>
    </tr>
    <tr>
      <td>2763</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>-368.0</td>
      <td>0.0</td>
      <td>28.0</td>
      <td>-6.0</td>
      <td>2020-02-11 21:55:20.587</td>
      <td>2020-02-11</td>
      <td>0.053307</td>
      <td>0.213380</td>
    </tr>
    <tr>
      <td>487</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>-448.0</td>
      <td>0.0</td>
      <td>-58.0</td>
      <td>5.0</td>
      <td>2020-02-12 22:07:03.407</td>
      <td>2020-02-12</td>
      <td>0.115123</td>
      <td>-0.215943</td>
    </tr>
    <tr>
      <td>26</td>
      <td>湖北省</td>
      <td>武汉</td>
      <td>-1104.0</td>
      <td>0.0</td>
      <td>-138.0</td>
      <td>-72.0</td>
      <td>2020-02-13 00:19:12.057</td>
      <td>2020-02-13</td>
      <td>-0.139336</td>
      <td>-0.325688</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data_2nd_derivative, city_name + '增长加速度')
```


![png](./Readme/output_45_0.png)



```python
display(Markdown('### ' + city_name + '死亡治愈率'))
```


### 武汉死亡治愈率



```python
figure = plot_util.plot_conf_dead_cured_ratio(city_daily_data, city_name + '死亡治愈率%')
```


![png](./Readme/output_47_0.png)



```python
display(Markdown('### ' + city_name + '数据校验'))
```


### 武汉数据校验



```python
city_confirmed = city_daily_data['confirmed']

benford_raw = data_util.benford(city_confirmed)
figure = plot_util.plot_bar(benford_raw, city_name + '数据校验（本福特定律）', 'Digit', 'Percent')
```


![png](./Readme/output_49_0.png)



```python

```