# ノンパラメトリック値の正規化
# x' = (x - xmedian) / xIQR
# x : 元データ
# xmedian : 中央値
# xIQR : xの四分位範囲
def nonpara_norm(data):
    import numpy as np
    sort_data = sorted(data)
    box = np.percentile(sort_data, q=[0, 25, 50, 75, 100])
    data -= box[2]
    data /= box[3] - box[1]
    return data
