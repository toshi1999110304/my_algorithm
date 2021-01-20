# ノンパラメトリック値の正規化
# x' = (x - xmedian) / xIQR
# x : 元データ
# xmedian : all_dataの中央値
# xIQR : all_dataの四分位範囲
# all_data : 
def nonpara_norm(data, all_data):
    import numpy as np
    sort_data = sorted(all_data)
    box = np.percentile(sort_data, q=[0, 25, 50, 75, 100])
    data -= box[2]
    data /= box[3] - box[1]
    return data


# RRIBLEによって取得したHRVデータからあるイベント発生時から前range_分間を取り出す
# condition_id : あるイベントのid
# range_ : 取り出す長さ（分）
def hrv_split(data, condition_id, range_):
    start = data[data['condition_id'] == condition_id]['Current Time']
    s = start.values[0][11:19]
    first = start.index.values[0]
    new_index = first - 1
    new = data.iloc[new_index, 0][11:19]
    while int(s[:2]) * 60 * 60 + int(s[3:5]) * 60 + int(s[6:]) - (int(new[:2]) * 60 * 60 + int(new[3:5]) * 60 + int(new[6:])) < range_ * 60:
        new = data.iloc[new_index, 0][11:19]
        new_index -= 1
    return data.iloc[new_index:first, :]
