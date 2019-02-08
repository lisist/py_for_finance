import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dax_index.csv")


def correlation_graph(df):
    df_corr = df.corr()

    data = df_corr.values
    fig = plt.figure()                                      ## Figure 설정
    ax = fig.add_subplot(1,1,1)                             ## (1X1) 의 layout에 첫 번째(1) 그래프 판 설정

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)           ## Heatmap 생성
    fig.colorbar(heatmap)                                   ## Heatmap color 범례 생성
    ax.set_xticks(np.arange(data.shape[1])+0.5,minor=False) ## x축 tick 설정 (0.5부터 1만큼 증가하며 생성)
    ax.set_yticks(np.arange(data.shape[1])+0.5,minor=False) ## y축 tick 설정 (0.5부터 1만큼 증가하며 생성)
    ax.invert_yaxis()                                       ## y축 역전
    ax.xaxis.tick_top()                                     ## x축 tick이 상방에 놓이도록 설정

    column_labels = df_corr.columns                         ## 열(x축) 라벨 정의
    row_labels = df_corr.index                              ## 행(y축) 라벨 정의

    ax.set_xticklabels(column_labels)                       ## x축 tick에 미리 설정해놓은 라벨 적용
    ax.set_yticklabels(row_labels)                          ## y축 tick에 미리 설정해놓은 라벨 ㅈ거용

    plt.xticks(rotation=90)                                 ## x축 tick 라벨 글자를 90도 회전하여 보여줌

    heatmap.set_clim(-1,1)                                  ## heatmap 범례의 범위를 (-1,1)로 설정
    plt.tight_layout()                                      ## tight한 layout 설정

    plt.show()

