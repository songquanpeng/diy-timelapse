import os
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

# 定义命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, default="input", help='input directory path')
parser.add_argument('--output', '-o', type=str, default="output", help='output directory path')
args = parser.parse_args()

os.makedirs(args.output, exist_ok=True)

# 获取输入路径下的所有图片文件的文件名
input_path = args.input
file_names = os.listdir(input_path)
file_names.sort()

# 定义时间格式
time_format = '%Y-%m-%d_%H-%M-%S'

# 遍历所有文件进行处理
for i, file_name in tqdm(enumerate(file_names), total=len(file_names)):
    # 提取时间信息
    try:
        time_string = file_name.split('.')[0]
        time = datetime.strptime(time_string, time_format)
    except ValueError:
        # 文件名不符合时间格式，跳过
        continue

    # 读取图片
    image_path = os.path.join(input_path, file_name)
    with Image.open(image_path) as image:
        # 绘制时间字幕
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 30)
        text_width, text_height = draw.textsize(str(time), font=font)
        x = image.width - text_width - 10
        y = image.height - text_height - 10
        draw.text((x, y), str(time), font=font, fill=(255, 255, 255))

        # 生成新文件名并保存图片
        new_file_name = f'{i+1:04}.jpg'
        output_path = os.path.join(args.output, new_file_name)
        image.save(output_path)

print(f"重命名以及时间字母添加完成！")
