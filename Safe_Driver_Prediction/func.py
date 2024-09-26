import pandas as pd
import numpy as np 
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt 
import seaborn as sns

# 데이터 프레임 feature들의 요약 정보
def resumetable(df:pd.DataFrame) -> pd.DataFrame:
    print(f"데이터셋 형상: {df.shape}")
    summary= pd.DataFrame(df.dtypes, columns=["데이터 타입"])
    summary["결측치 개수"] = (df == -1).sum().values  #  feature 별 결측치(-1) 개수
    summary["고윳값 개수"] = df.nunique().values
    summary["데이터 종류"] = None

    for col in df.columns:
        if 'bin' in col or col == 'target':
            summary.loc[col, '데이터 종류'] = '이진형'
        elif 'cat' in col:
            summary.loc[col, '데이터 종류'] = '명목형'
        elif df[col].dtype == float:
            summary.loc[col, '데이터 종류'] = '연속형'
        elif df[col].dtype == int:
            summary.loc[col, '데이터 종류'] = '순서형'
    
    return summary


# 막대 그래프 위에 글자 기입
def text_on_bars(bar, type="count", size=10, color="black"):
    if type == "count":
        for rect in bar:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{int(height)}', 
                     ha='center', va='bottom', size=size, color=color)
    elif type == "ratio":
        total = sum([rect.get_height() for rect in bar])  # bar를 통해 total 계산
        for rect in bar:
            height = rect.get_height()
            ratio = (height / total) * 100
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{ratio:.1f}%', 
                     ha='center', va='bottom', size=size, color=color)


# 히스토그램 위에 글자 기입
def text_on_hist(bar, bins, type="count", size=10, color="black"):
    # bins: 히스토그램의 구간 (bins)
    # bar: 히스토그램 막대의 높이 (plt.hist의 반환 값)
    
    if type == "count":
        for i in range(len(bar)):
            height = bar[i]
            plt.text((bins[i] + bins[i+1])/2, height, int(height), 
                     ha='center', va='bottom', size=size, color=color)
    elif type == "ratio":
        total = sum(bar)  # 전체 데이터 포인트 수
        for i in range(len(bar)):
            height = bar[i]
            ratio = (height / total) * 100  # 비율 계산
            plt.text((bins[i] + bins[i+1])/2, height, "%.1f%%" % ratio, 
                     ha='center', va='bottom', size=size, color=color)
            

# 해당 데이터 프레임의 target feature의 분포 시각화
def target_distribution(df, target, figsize):
    plt.figure(figsize=figsize)
    # plt.hist()
    bar = plt.bar(x=df[target].unique(), height=df.groupby("target")["ps_ind_01"].count().values)
    plt.xlabel("target")
    plt.xticks(list(df[target].unique()))
    plt.ylabel("count")
    plt.title("Target Distribution")
    text_on_bars(bar=bar, type="ratio")
    plt.show()


def plot_target_ratio_by_features(df, features, num_rows, num_cols, figsize=(12,18)):
    mpl.rc('font', size=9)
    plt.figure(figsize=figsize)
    grid = gridspec.GridSpec(num_rows, num_cols)
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    for idx, feature in enumerate(features):
        ax = plt.subplot(grid[idx])
        sns.barplot(x=feature, y="target", hue=feature, data=df, palette="Set2", ax=ax)
        ax.legend().remove()


def eval_gini(y_true, y_pred):
    assert y_true.shape == y_pred.shape

    n_samples = y_true.shape[0]  # 데이터 개수 
    L_mid = np.linspace(1 / n_samples, 1, n_samples)  # 대각선 값

    # 1. 예측 값에 대한 지니계수 
    pred_order = y_true[y_pred.argsort()]  # y_pred 크기 순으로 y_true 값 정렬
    L_pred = np.cumsum(pred_order) / np.cumsum(pred_order)  # 로렌츠 곡선
    G_pred = np.sum(L_mid - L_pred)  # 예측 값에 대한 지니 계수 

    # 2. 예측이 완벽할 때의 지니계수 
    true_order = y_true[y_true.argsort()]  # y_true 크기 순으로 y_true 값 정렬
    L_true = np.cumsum(true_order) / np.cumsum(true_order)  # 로렌츠 곡선
    G_true = np.sum(L_mid - L_true)  # 예측이 완벽할 때의 지니계수 

    # 정규화 된 지니계수
    return G_pred / G_true


def gini(preds, dtrain):
    labels = dtrain.get_label()
    return 'gini', eval_gini(labels, preds), True 