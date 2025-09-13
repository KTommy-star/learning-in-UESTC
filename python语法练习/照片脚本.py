import pandas as pd
import requests
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# 替换为你的Excel文件路径
excel_file_path = r'C:\Users\24540\Desktop\flow_20241014_20241021.xlsx'
# 替换为包含图片URL的列名
url_column = '打卡图片'
# 替换为图片将要插入的列名
image_column = 'image'

# 读取Excel文件
df = pd.read_excel(excel_file_path)

# 加载工作簿
wb = load_workbook(excel_file_path)
ws = wb.active

# 遍历DataFrame，下载并插入图片
for index, row in df.iterrows():
    url = row[url_column]
    if url:  # 如果URL列不为空
        try:
            # 发起请求，下载图片
            response = requests.get(url)
            if response.status_code == 200:
                # 创建图片对象
                img = Image(response.content)
                # 插入图片到Excel
                ws.add_image(img, f'{image_column}{index+2}')  # index+2是因为Excel行是从1开始的
            else:
                print(f"Failed to retrieve image from {url}")
        except Exception as e:
            print(f"An error occurred: {e}")

# 保存工作簿
wb.save(excel_file_path)