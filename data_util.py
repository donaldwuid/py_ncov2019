import pandas as pd
import numpy as np

REMOTE_DATA_PATH = 'http://raw.githubusercontent.com/BlankerL/DXY-2019-nCoV-Data/master/csv/DXYArea.csv'

LOCAL_DATA_PATH = './data/csv/DXYArea.csv'

DATA_PATH = LOCAL_DATA_PATH

def load_data():
    data = pd.read_csv(DATA_PATH)
    data['updateTime'] = pd.to_datetime(data['updateTime'])  # original type of updateTime after read_csv is 'str'
    data['updateDate'] = data['updateTime'].dt.date    # add date for daily aggregation
    return data


def clean(df):
    '''
    On some dates, very little provinces have reports (usually happens when just pass mid-night)
    Remove these dates for now.  When I have time, I can fill in previous value
    '''
    province_count_frm = df.groupby('updateDate').agg({'provinceName': pd.Series.nunique})
    invalid_ind = province_count_frm[province_count_frm['provinceName'] < 25].index  # 
    return df[~df['updateDate'].isin(invalid_ind)]

def aggregate_daily(df, city_name = ""):
    '''Aggregate the frequent time series data into a daily frame, ie, one entry per (date, province, city)'''
    frm_list = []

    if city_name:
        df = df[df.cityName == city_name]

    drop_cols = ['province_' + field for field in ['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount']]  # these can be computed later
    for key, frm in df.drop(columns=drop_cols).sort_values(['updateDate']).groupby(['cityName', 'updateDate']):
        frm_list.append(frm.sort_values(['updateTime'])[-1:])    # take the lastest row within (city, date)
    out = pd.concat(frm_list).sort_values(['updateDate', 'provinceName', 'cityName'])
    to_names = [field for field in ['confirmed', 'suspected', 'cured', 'dead']]
    out = out.rename(columns=dict([('city_' + d + 'Count', d) for d in to_names]))   # the suspected column from csv is not reliable
    return out

def aggregate_daily_except(df, province_name = ""):
    '''Aggregate the frequent time series data into a daily frame, ie, one entry per (date, province, city)'''
    frm_list = []

    if province_name:
        df = df[df.provinceName != province_name]

    drop_cols = ['province_' + field for field in ['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount']]  # these can be computed later
    for key, frm in df.drop(columns=drop_cols).sort_values(['updateDate']).groupby(['cityName', 'updateDate']):
        frm_list.append(frm.sort_values(['updateTime'])[-1:])    # take the lastest row within (city, date)
    out = pd.concat(frm_list).sort_values(['updateDate', 'provinceName', 'cityName'])
    to_names = [field for field in ['confirmed', 'suspected', 'cured', 'dead']]
    out = out.rename(columns=dict([('city_' + d + 'Count', d) for d in to_names]))   # the suspected column from csv is not reliable

    out = out.groupby('updateDate').agg('sum')

    return out

def calculate_dead_cured_rate(df):
    df_ret = df.copy()

    df_ret['dead_rate'] = 100.0 * df_ret['dead'] / df_ret['confirmed']
    df_ret['cured_rate'] = 100.0 * df_ret['cured'] / df_ret['confirmed']

    return df_ret

def diff(df):

    de_ret = df.copy()

    fields = ['confirmed', 'suspected', 'cured', 'dead', 'dead_rate', 'cured_rate']
    df_nums = de_ret[fields]
    df_nums = df_nums.diff(axis = 0, periods = 1)
    
    de_ret[fields] = df_nums[fields]

    return de_ret