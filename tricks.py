import pandas as pd
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.monospace'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 一种可以在不预读取的情况下跳过一部分sheet的数据表格读取方式
def read_specific(f_path, skip_list):
    xlsx = pd.ExcelFile(f_path)
    # 获取所有工作表名称
    sheet_names = xlsx.sheet_names
    # 打印工作表名称，以便查看
    # print(sheet_names)
    # 选择性读取特定的工作表
    # 假设我们不想读取 'Sheet1' 和 'Sheet3'
    sheets_to_read = [sheet for sheet in sheet_names if sheet not in skip_list]
    # 读取选定的工作表
    dt = {}
    for sheet in sheets_to_read:
        df = pd.read_excel(xlsx, sheet_name=sheet, verbose=True)
        dt[sheet] = df
    # 关闭Excel文件
    xlsx.close()
    return dt

f_path = "example.xlsx"
skip_list = ["sheet1", "sheet3"]
data = read_specific(f_path, skip_list)

# 引用不同页面间（同一内核）数值的办法
%store -r df

# 同一文件写入多个sheet的办法
writer = pd.ExcelWriter(f_path, engine='xlsxwriter')
df1.to_excel(writer, "sheet_name1")
df2.to_excel(writer, "sheet_name2")
writer.save()
writer.close()

# 一种可以将timedelta 转为天数日期数值的方法
(pd.to_datetime(df['datetime1']).dt.date - pd.to_datetime(df['datetime2'])).apply(lambda x:x.days)
# 从日期时间格式里取日期
pd.to_datetime(df["datetime"]).dt.date

# 一种简单获得顺序号的办法
df.reset_index(drop=True, inplace=True)

# 通过分类level进行字符列排序
pd.Categorical(df["order"], ordered=True, categories = ns.natsorted(df["order"])) 

# 一种填充数字为字符串的方法
df["num"].astype(str).apply(lambda x: x.zfill(5))
df["seq"] = df.index+1

# 字符数值转换类型也可以强制
df2 = df1.astype(int, errors='ignore')
pd.to_numeric(df["string"], errors='coerce')

# 将字符列分为多列
df2 = df1["to_be_splited"].str.split(r',|，|\.|。|/|、|\\\\|\+', expand=True)

