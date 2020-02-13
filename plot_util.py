import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'Songti SC'

def plot_conf(df, fig, subplot_index, title, fields, field_names, style='-*', figsize=(13,6), fontsize=16, logy=False):
    ax1 = fig.add_subplot(subplot_index)
    ax1.tick_params(labelright=True)
    plot_df = df.groupby('updateDate').agg('sum')
    lines = plot_df.plot(y=fields, style='-*', grid=True, ax=ax1, figsize=figsize, logy=logy)
    ax1.legend(field_names)

    if logy:
        title += '（指数）'
    ax1.set_title(title, fontsize=fontsize, va='baseline')

    # ax1.set_xlabel(xlabel, fontsize=fontsize - 2, va='bottom')
    
    return fig


def plot_conf_main(df, title, figsize=(13,6), fontsize=18, logy=False):
    fig = plt.figure()

    fig.subplots_adjust(hspace=0.5)

    plot_conf(df, fig, 211, '确诊、疑似', ['confirmed', 'suspected'], ['确诊', '疑似'], style='-*', logy=logy)
    plot_conf(df, fig, 212, '死亡、治愈', ['dead', 'cured'], ['死亡', '治愈'], style=':*', logy=logy)
    
    fig.suptitle(title, fontsize=fontsize)

    return fig

def plot_conf_dead_cured_ratio(df, title, figsize=(13,6), fontsize=18, logy=False):
    fig = plt.figure()

    plot_conf(df, fig, 211, '', ['dead_rate', 'cured_rate'], ['死亡率%', '治愈率%'], style=':*', logy=logy)
    
    fig.suptitle(title, fontsize=fontsize)

    return fig

def plot_bar(df, title, xName, yName, figsize=(13,6), fontsize=18):
    fig = plt.figure()

    ax = fig.add_subplot(211)
    df.plot.bar(x=xName, y=yName, ax=ax, figsize=figsize)

    fig.suptitle(title, fontsize=fontsize)

