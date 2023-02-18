"""
ソート(sort_index, sort_values)
　日付データ
"""

import pandas as pd
import datetime as dt

ohlc_data1 = [
    [dt.date(2020, 4, 1), 107.607, 117.952, 96.929, 107.191],
    [dt.date(2020, 4, 2), 107.191, 118.104, 97.028, 107.922],
    [dt.date(2020, 4, 3), 107.922, 118.688, 97.811, 108.578],
    [dt.date(2020, 4, 4), 108.432, 119.393, 98.403, 109.252],
    [dt.date(2020, 4, 5), 109.252, 119.294, 98.680, 108.799],
    [dt.date(2020, 4, 6), 108.799, 119.109, 98.514, 108.854],
    [dt.date(2020, 4, 7), 108.854, 119.071, 98.218, 108.545],
    [dt.date(2020, 4, 8), 108.545, 118.615, 98.341, 108.515],
    [dt.date(2020, 4, 9), 108.453, 118.569, 97.510, 107.803],
    [dt.date(2020, 4, 10), 107.803, 117.811, 96.990, 107.235],
    [dt.date(2020, 4, 11), 107.235, 117.911, 96.934, 107.488],
    [dt.date(2020, 4, 12), 107.488, 118.092, 97.172, 107.935],
    [dt.date(2020, 4, 13), 107.935, 118.111, 97.309, 107.598],
    [dt.date(2020, 4, 14), 107.589, 117.958, 97.517, 107.638],
    [dt.date(2020, 4, 15), 107.682, 117.904, 97.289, 107.782],
    [dt.date(2020, 4, 16), 107.838, 117.950, 97.523, 107.758],
    [dt.date(2020, 4, 17), 107.806, 118.053, 97.354, 107.663],
    [dt.date(2020, 4, 18), 107.640, 117.769, 97.380, 107.553],
    [dt.date(2020, 4, 19), 107.624, 117.650, 97.000, 107.278],
    [dt.date(2020, 4, 20), 107.251, 117.347, 96.567, 106.880],
    [dt.date(2020, 4, 21), 106.884, 116.925, 96.367, 106.757],
    [dt.date(2020, 4, 22), 106.750, 117.506, 96.414, 107.249],
    [dt.date(2020, 4, 23), 107.242, 117.414, 96.614, 106.966],
]

ohlc_data2 = [
    ["2020/4/1", 107.607, 117.952, 96.929, 107.191],
    ["2020/4/2", 107.191, 118.104, 97.028, 107.922],
    ["2020/4/3", 107.922, 118.688, 97.811, 108.578],
    ["2020/4/4", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/5", 109.252, 119.294, 98.680, 108.799],
    ["2020/4/6", 108.799, 119.109, 98.514, 108.854],
    ["2020/4/7", 108.854, 119.071, 98.218, 108.545],
    ["2020/4/8", 108.545, 118.615, 98.341, 108.515],
    ["2020/4/9", 108.453, 118.569, 97.510, 107.803],
    ["2020/4/10", 107.803, 117.811, 96.990, 107.235],
    ["2020/4/11", 107.235, 117.911, 96.934, 107.488],
    ["2020/4/12", 107.488, 118.092, 97.172, 107.935],
    ["2020/4/13", 107.935, 118.111, 97.309, 107.598],
    ["2020/4/14", 107.589, 117.958, 97.517, 107.638],
    ["2020/4/15", 107.682, 117.904, 97.289, 107.782],
    ["2020/4/16", 107.838, 117.950, 97.523, 107.758],
    ["2020/4/17", 107.806, 118.053, 97.354, 107.663],
    ["2020/4/18", 107.640, 117.769, 97.380, 107.553],
    ["2020/4/19", 107.624, 117.650, 97.000, 107.278],
    ["2020/4/20", 107.251, 117.347, 96.567, 106.880],
    ["2020/4/21", 106.884, 116.925, 96.367, 106.757],
    ["2020/4/22", 106.750, 117.506, 96.414, 107.249],
    ["2020/4/23", 107.242, 117.414, 96.614, 106.966],
]

ohlc_data3 = [
    [dt.date(2020, 4, 6), 108.799, 119.109, 98.514, 108.854],
    [dt.date(2020, 4, 17), 107.806, 118.053, 97.354, 107.663],
    [dt.date(2020, 4, 2), 107.191, 118.104, 97.028, 107.922],
    [dt.date(2020, 4, 12), 107.488, 118.092, 97.172, 107.935],
    [dt.date(2020, 4, 22), 106.750, 117.506, 96.414, 107.249],
    [dt.date(2020, 4, 1), 107.607, 117.952, 96.929, 107.191],
    [dt.date(2020, 4, 19), 107.624, 117.650, 97.000, 107.278],
    [dt.date(2020, 4, 10), 107.803, 117.811, 96.990, 107.235],
    [dt.date(2020, 4, 15), 107.682, 117.904, 97.289, 107.782],
    [dt.date(2020, 4, 3), 107.922, 118.688, 97.811, 108.578],
    [dt.date(2020, 4, 7), 108.854, 119.071, 98.218, 108.545],
    [dt.date(2020, 4, 11), 107.235, 117.911, 96.934, 107.488],
    [dt.date(2020, 4, 23), 107.242, 117.414, 96.614, 106.966],
    [dt.date(2020, 4, 20), 107.251, 117.347, 96.567, 106.880],
    [dt.date(2020, 4, 16), 107.838, 117.950, 97.523, 107.758],
    [dt.date(2020, 4, 4), 108.432, 119.393, 98.403, 109.252],
    [dt.date(2020, 4, 18), 107.640, 117.769, 97.380, 107.553],
    [dt.date(2020, 4, 9), 108.453, 118.569, 97.510, 107.803],
    [dt.date(2020, 4, 21), 106.884, 116.925, 96.367, 106.757],
    [dt.date(2020, 4, 5), 109.252, 119.294, 98.680, 108.799],
    [dt.date(2020, 4, 14), 107.589, 117.958, 97.517, 107.638],
    [dt.date(2020, 4, 13), 107.935, 118.111, 97.309, 107.598],
    [dt.date(2020, 4, 8), 108.545, 118.615, 98.341, 108.515],
]

ohlc_data4 = [
    ["2020/4/6", 108.799, 119.109, 98.514, 108.854],
    ["2020/4/17", 107.806, 118.053, 97.354, 107.663],
    ["2020/4/2", 107.191, 118.104, 97.028, 107.922],
    ["2020/4/12", 107.488, 118.092, 97.172, 107.935],
    ["2020/4/22", 106.750, 117.506, 96.414, 107.249],
    ["2020/4/1", 107.607, 117.952, 96.929, 107.191],
    ["2020/4/19", 107.624, 117.650, 97.000, 107.278],
    ["2020/4/10", 107.803, 117.811, 96.990, 107.235],
    ["2020/4/15", 107.682, 117.904, 97.289, 107.782],
    ["2020/4/3", 107.922, 118.688, 97.811, 108.578],
    ["2020/4/7", 108.854, 119.071, 98.218, 108.545],
    ["2020/4/11", 107.235, 117.911, 96.934, 107.488],
    ["2020/4/23", 107.242, 117.414, 96.614, 106.966],
    ["2020/4/20", 107.251, 117.347, 96.567, 106.880],
    ["2020/4/16", 107.838, 117.950, 97.523, 107.758],
    ["2020/4/4", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/18", 107.640, 117.769, 97.380, 107.553],
    ["2020/4/9", 108.453, 118.569, 97.510, 107.803],
    ["2020/4/21", 106.884, 116.925, 96.367, 106.757],
    ["2020/4/5", 109.252, 119.294, 98.680, 108.799],
    ["2020/4/14", 107.589, 117.958, 97.517, 107.638],
    ["2020/4/13", 107.935, 118.111, 97.309, 107.598],
    ["2020/4/8", 108.545, 118.615, 98.341, 108.515],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data3, columns=["datetime", "open", "high", "low", "close"])
df.set_index("datetime", inplace=True)
print(df)
print("{:-<50}".format("----- データ確認 "))
print(df.index[0])
print(type(df.index[0]))

print("\n{:*<100}".format("***** インデックス・ソート（昇順）<datetime> "))
df_asc = df.sort_index(ascending=True)
print("{:-<50}".format("----- ソート後 "))
print(df_asc)

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data4, columns=["datetime", "open", "high", "low", "close"])
df.set_index("datetime", inplace=True)
print(df)
print("{:-<50}".format("----- データ確認 "))
print(df.index[0])
print(type(df.index[0]))

print("\n{:*<100}".format("***** インデックス・ソート（昇順）<str> "))
df_asc = df.sort_index(ascending=True)
print("{:-<50}".format("----- ソート後 "))
print(df_asc)
