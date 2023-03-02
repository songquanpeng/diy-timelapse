import argparse
from PIL import Image
from tqdm import tqdm
import os

# 创建 argparse 对象并定义命令行参数
parser = argparse.ArgumentParser(description='给一系列图片添加滤镜效果')
parser.add_argument('--input', type=str, default="test", help='需要处理的图片所在目录')
parser.add_argument('--output', type=str, default="test_processed", help='处理后的图片要保存的目录')
parser.add_argument('--saturation', type=float,
                    default=1.5, help='饱和度增加的因子')
parser.add_argument('--temperature', type=float, default=0, help='色温调整的值，取值范围为-100到100，默认为0')
parser.add_argument('--tint', type=float, default=0, help='色调调整的值，取值范围为-100到100，默认为0')

# 解析命令行参数
args = parser.parse_args()

os.makedirs(args.output, exist_ok=True)

# 遍历输入路径下的所有图片
filenames = os.listdir(args.input)
for filename in tqdm(filenames):
    # 判断文件是否为图片
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # 打开图片
        with Image.open(os.path.join(args.input, filename)) as img:
            # 将图片的饱和度增加
            img = img.convert('HSV')
            h, s, v = img.split()
            s = s.point(lambda x: x * args.saturation)
            img = Image.merge('HSV', (h, s, v)).convert('RGB')
            # 调整图片的色温
            if args.temperature != 0:
                if args.temperature > 0:
                    r, g, b = 255, 255 - args.temperature, 255 - args.temperature
                else:
                    r, g, b = 255 + args.temperature, 255 + args.temperature, 255
                color_matrix = (r / 255, 0, 0, 0, 0, g / 255, 0, 0, 0, 0, b / 255, 0)
                img = img.convert('RGB', color_matrix)
            # 调整图片的色调
            if args.tint != 0:
                r, g, b = img.split()
                r = r.point(lambda x: x + args.tint)
                img = Image.merge('RGB', (r, g, b))
            output_filename = filename
            img.save(os.path.join(args.output, output_filename))

print('图像处理完成！')
