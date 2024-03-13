import sys
import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

# 检查命令行参数是否正确
if len(sys.argv) != 3:
    print("用法示例: python data_processing.py 要处理的文件名 输出的文件名")
    sys.exit(1)

input_file = sys.argv[1] # 要处理的文件名
output_file = sys.argv[2] # 输出的文件名
print(f'此程序会将输入的文件：{input_file}，处理后保存为Excel文件：{output_file}')
try:
    data = pd.read_excel(input_file) # 数据读取
except:
    data = pd.read_csv(input_file, header=True, encoding='utf8')  # 数据读取
deal_data = data[['里程数','购车时间','车保状态','诉求','投诉问题']] # 筛选需要处理的列

for i in tqdm(deal_data.index): # 循环处理每行数据
    null_rows = deal_data.loc[i].isnull().sum()  # 判断是否有缺失
    if null_rows > 0:
        null_data = pd.DataFrame(deal_data.loc[i]).T  # 找到有缺失的数据
        # 将包含空值的行数据往后挪一位,里程数用99999999替换
        null_data = null_data.shift(periods=1, axis=1, fill_value=99999999)
        deal_data.loc[i] = list(null_data.values.tolist()[0]) # 替换原来的值

# deal_data替换原来的数据
data[['里程数','购车时间','车保状态','诉求','投诉问题']] = deal_data
# 重新保存数据
data.to_excel(output_file)

print(f'处理成功！')