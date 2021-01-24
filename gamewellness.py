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


# RRIBLEによって取得したHRVデータからあるイベント発生時から前後（updownで指定）range_分間を取り出す
# condition_id : あるイベントのid
# range_ : 取り出す長さ（分）
# updown
#    True : イベント記録時から前にrange_分
#    False : イベント記録時から後ろにrange_分

def hrv_split(data, condition_id, range_, updown):
    start = data[data['condition_id'] == condition_id]['time(sec)']
    first_index = start.index.values[0]
    if updown:
        op = -1
    else:
        op = 1
    
    new_index = first_index + op
    new = data.iloc[new_index, 1]
    
    if updown:
        while start.values[0] - new < range_ * 60:
            new = data.iloc[new_index, 1]
            new_index += op
    else:
        while new - start.values[0] < range_ * 60:
            new = data.iloc[new_index, 1]
            new_index += op
        
    if updown:
        return data.iloc[new_index:first_index, :]
    else:
        return data.iloc[first_index:new_index, :]
'''    
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
'''

# 外れ値除去関数（外れ値の一つ前の値で補間）補間済みリストとインデックスを返す
# data : pd.series
def remove_outliers(data):
    import numpy as np
    c_array = np.percentile(data, q=[25, 50, 75])
    iqr = c_array[2] - c_array[0]
    #median = c_array[1]
    #print(c_array)
    max_ = c_array[2] + 1.5 * iqr
    min_ = c_array[0] - 1.5 * iqr
    modified = []
    indexs = []
    for index, data_i in data.items():
        indexs.append(index)
        #val = data.iloc[index-1, :][column]
        if data_i > max_ or data_i < min_:
            print('outlier!!')
            modified.append(data.iloc[index-1])
        else:
            modified.append(data_i)
    return modified, indexs

