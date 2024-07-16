import pandas as pd

# 获取世界银行的金融普惠数据
url = "http://api.worldbank.org/v2/en/indicator/IT.NET.USER.ZS?downloadformat=csv"
data = pd.read_csv(url, skiprows=4)

# 显示前几行数据
print(data.head())
