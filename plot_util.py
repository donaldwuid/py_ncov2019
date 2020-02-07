import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm
font_path = './STFANGSO.TTF'  # for displaying Chinese characters in plots
font_prop = mfm.FontProperties(fname=font_path)

def tsplot_conf_dead_cured(df, title_prefix, figsize=(13,6), fontsize=18, logy=False):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    plot_df = df.groupby('updateDate').agg('sum')
    plot_df.plot(y=['confirmed', 'suspected'], style='-*', grid=True, ax=ax1, figsize=figsize, logy=logy)


    ax2 = fig.add_subplot(212)
    plot_df.plot(y=['dead', 'cured'], style=':*', grid=True, ax=ax2, figsize=figsize, sharex=True, logy=logy)
    title = title_prefix + '确诊、疑似，死亡、治愈人数'

    if logy:
        title += '（指数）'
    fig.suptitle(title, fontproperties=font_prop, fontsize=fontsize)
    return fig