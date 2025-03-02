import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image as OpenpyxlImage
import os

# 初始化Excel工作簿
wb = Workbook()
ws = wb.active

# 图片URL列表
urls = [
    "https://oa.feishu.cn/attendance/v2/admin/clock_in/download_photo?photo_type=0&file_key=2f64e13a298a837a108c61208f9086d7&token=aa874e5f326c9540f8605423d92ac630.jpg",
    # 添加更多URL...
]

# 用于保存图片的目录
image_dir = '../../downloaded_images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# 下载并保存图片
for i, url in enumerate(urls):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # 保存图片
            image_path = os.path.join(image_dir, f'image_{i + 1}.jpg')
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            # 将图片插入Excel
            img = OpenpyxlImage(image_path)
            ws.add_image(img, f'A{i + 1}')
        else:
            print(f"Failed to retrieve image from {url}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")

# 保存Excel文件
wb.save('images.xlsx')