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
      <td>7982</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>271</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>2020-02-04 20:55:16.467</td>
      <td>2020-02-04</td>
      <td>0.0</td>
      <td>4.797048</td>
    </tr>
    <tr>
      <td>5751</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>291</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>2020-02-05 21:18:47.516</td>
      <td>2020-02-05</td>
      <td>0.0</td>
      <td>5.498282</td>
    </tr>
    <tr>
      <td>3481</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>316</td>
      <td>0</td>
      <td>22</td>
      <td>0</td>
      <td>2020-02-06 20:40:40.766</td>
      <td>2020-02-06</td>
      <td>0.0</td>
      <td>6.962025</td>
    </tr>
    <tr>
      <td>1169</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>339</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>2020-02-07 18:14:50.649</td>
      <td>2020-02-07</td>
      <td>0.0</td>
      <td>9.144543</td>
    </tr>
    <tr>
      <td>166</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>351</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>2020-02-08 09:33:34.004</td>
      <td>2020-02-08</td>
      <td>0.0</td>
      <td>8.831909</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data, city_name + '累计')
```


![svg](./Readme/output_7_0.png)



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
      <td>7982</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>26.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2020-02-04 20:55:16.467</td>
      <td>2020-02-04</td>
      <td>0.0</td>
      <td>0.715415</td>
    </tr>
    <tr>
      <td>5751</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>20.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2020-02-05 21:18:47.516</td>
      <td>2020-02-05</td>
      <td>0.0</td>
      <td>0.701234</td>
    </tr>
    <tr>
      <td>3481</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>25.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>2020-02-06 20:40:40.766</td>
      <td>2020-02-06</td>
      <td>0.0</td>
      <td>1.463744</td>
    </tr>
    <tr>
      <td>1169</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>23.0</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>2020-02-07 18:14:50.649</td>
      <td>2020-02-07</td>
      <td>0.0</td>
      <td>2.182517</td>
    </tr>
    <tr>
      <td>166</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2020-02-08 09:33:34.004</td>
      <td>2020-02-08</td>
      <td>0.0</td>
      <td>-0.312634</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(city_daily_data_1st_derivative, city_name + '增长速度')
```


![svg](./Readme/output_10_0.png)



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
      <td>7982</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-12.0</td>
      <td>0.0</td>
      <td>-2.0</td>
      <td>0.0</td>
      <td>2020-02-04 20:55:16.467</td>
      <td>2020-02-04</td>
      <td>0.0</td>
      <td>-0.950758</td>
    </tr>
    <tr>
      <td>5751</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2020-02-05 21:18:47.516</td>
      <td>2020-02-05</td>
      <td>0.0</td>
      <td>-0.014182</td>
    </tr>
    <tr>
      <td>3481</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2020-02-06 20:40:40.766</td>
      <td>2020-02-06</td>
      <td>0.0</td>
      <td>0.762510</td>
    </tr>
    <tr>
      <td>1169</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-2.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2020-02-07 18:14:50.649</td>
      <td>2020-02-07</td>
      <td>0.0</td>
      <td>0.718774</td>
    </tr>
    <tr>
      <td>166</td>
      <td>广东省</td>
      <td>深圳</td>
      <td>-11.0</td>
      <td>0.0</td>
      <td>-9.0</td>
      <td>0.0</td>
      <td>2020-02-08 09:33:34.004</td>
      <td>2020-02-08</td>
      <td>0.0</td>
      <td>-2.495151</td>
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
    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/textpath.py:90: RuntimeWarning: Glyph 8722 missing from current font.
      font.set_text(s, 0.0, flags=LOAD_NO_HINTING)
    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/textpath.py:203: RuntimeWarning: Glyph 8722 missing from current font.
      glyph = font.load_char(ccode, flags=LOAD_NO_HINTING)



![svg](./Readme/output_13_1.png)



```python
display(Markdown('### ' + city_name + '死亡治愈率'))
```


### 深圳死亡治愈率



```python
figure = plot_util.plot_conf_dead_cured_ratio(city_daily_data, city_name + '死亡治愈率%')
```


![svg](./Readme/output_15_0.png)



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


![svg](./Readme/output_21_0.png)



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
      <td>2020-02-04</td>
      <td>629.0</td>
      <td>2.0</td>
      <td>106.0</td>
      <td>-1.0</td>
      <td>-0.031389</td>
      <td>1.218453</td>
    </tr>
    <tr>
      <td>2020-02-05</td>
      <td>704.0</td>
      <td>0.0</td>
      <td>156.0</td>
      <td>2.0</td>
      <td>0.011587</td>
      <td>1.613539</td>
    </tr>
    <tr>
      <td>2020-02-06</td>
      <td>750.0</td>
      <td>-2.0</td>
      <td>184.0</td>
      <td>1.0</td>
      <td>-0.003200</td>
      <td>1.633704</td>
    </tr>
    <tr>
      <td>2020-02-07</td>
      <td>660.0</td>
      <td>0.0</td>
      <td>212.0</td>
      <td>4.0</td>
      <td>0.031948</td>
      <td>1.765627</td>
    </tr>
    <tr>
      <td>2020-02-08</td>
      <td>-251.0</td>
      <td>0.0</td>
      <td>-11.0</td>
      <td>3.0</td>
      <td>0.039569</td>
      <td>0.147383</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(white_daily_data_1st_derivative, '全国增长速度（除' + black_province_name + '）')
```


![svg](./Readme/output_24_0.png)



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
      <td>2020-02-04</td>
      <td>-335.0</td>
      <td>3.0</td>
      <td>55.0</td>
      <td>-3.0</td>
      <td>-0.034680</td>
      <td>0.869219</td>
    </tr>
    <tr>
      <td>2020-02-05</td>
      <td>75.0</td>
      <td>-2.0</td>
      <td>50.0</td>
      <td>3.0</td>
      <td>0.042976</td>
      <td>0.395086</td>
    </tr>
    <tr>
      <td>2020-02-06</td>
      <td>46.0</td>
      <td>-2.0</td>
      <td>28.0</td>
      <td>-1.0</td>
      <td>-0.014786</td>
      <td>0.020165</td>
    </tr>
    <tr>
      <td>2020-02-07</td>
      <td>-90.0</td>
      <td>2.0</td>
      <td>28.0</td>
      <td>3.0</td>
      <td>0.035148</td>
      <td>0.131923</td>
    </tr>
    <tr>
      <td>2020-02-08</td>
      <td>-911.0</td>
      <td>0.0</td>
      <td>-223.0</td>
      <td>-1.0</td>
      <td>0.007620</td>
      <td>-1.618244</td>
    </tr>
  </tbody>
</table>
</div>




```python
figure = plot_util.plot_conf_main(white_daily_data_2nd_derivative, '全国增长加速度（除' + black_province_name + '）')
```


![svg](./Readme/output_27_0.png)



```python
display(Markdown('## 全国增死亡治愈率（除' + black_province_name + '）'))
```


## 全国增死亡治愈率（除湖北省）



```python
figure = plot_util.plot_conf_dead_cured_ratio(white_daily_data, '全国增死亡治愈率%（除' + black_province_name + '）')
```


![svg](./Readme/output_29_0.png)



```python

```
