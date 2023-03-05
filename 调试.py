import pandas as pd
import re
from datetime import datetime

file_path = 'E:\\2022年1-10月份石油化工冶金行业装置开工率情况统计（由百川盈孚统计）.xlsx'
sheet_name = '2022.10'
skip_rows = [0, 1]
columns = [0, 1, 2, 3, 4, 5]
end_row = 71

# 读取数据
data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows, usecols=columns, header=None)
end_row = end_row - len(skip_rows)
data = data.iloc[0:end_row, :]


# 拆分合并单元格
data.columns
data.fillna(method='ffill', inplace=True)


# 初始化
# half_cols = len(columns) / 2
industry = []
breed = []
year_month_rate_operation = []
i = 1

# 处理循环问题
while i <= 2:
    right_col = 3 * i - 1
    mid_col = 3 * i - 2
    left_col = 3 * i - 3
    industry.extend(data.iloc[:, left_col].values.tolist())
    breed.extend(data.iloc[:, mid_col].values.tolist())
    year_month_rate_operation.extend(data.iloc[:, right_col].values.tolist())
    i = i + 1

# 获取数据日期

# date = '2022-10-01 00:00:00'
result_data = pd.DataFrame()

# date = datetime.datetime.strptime(sheet_name, '%Y-%m-%d %H:%M:%S')
date = ''.join(list(str(sheet_name))[:4]) + '-' + ''.join(list(str(sheet_name))[5:]) + '-' + '01' + ' ' + '00:00:00'
# 填入数据

# result_data['date'] = date
result_data['industry'] = industry
result_data['date'] = date
result_data['breed'] = breed
result_data['year_month_rate_operation'] = year_month_rate_operation
result_data = result_data.astype('object')
# result_data = result_data.where(data.notnull(), None)
result_data['source'] = '百川开工率'
# result_data['excel_name'] = re.findall('.*\/(.*)\.', file_path)[0]
result_data['excel_name'] = 'baichuan'
result_data['sheet_name'] = sheet_name
result_data['update_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(result_data)
print(date)