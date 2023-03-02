import argparse
from PIL import Image
from tqdm import tqdm
import os

# 创建 argparse 对象并定义命令行参数
parser = argparse.ArgumentParser(description='给一系列图片添加滤镜效果')
parser.add_argument('--input', type=str, default="test", help='需要处理的图片所在目录')
parser.add_argument('--output', type=str, default="test_processed", help='处理后的图片要保存的目录')
parser.add_argument('--saturation_factor', type=float,
                    default=1.5, help='饱和度增加的因子')

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
            s = s.point(lambda x: x * args.saturation_factor)
            img = Image.merge('HSV', (h, s, v)).convert('RGB')
            # 将图片的天空颜色更改为蓝色
            # pixels = img.load()
            # for i in range(img.size[0]):
            #     for j in range(img.size[1]):
            #         r, g, b = pixels[i, j]
            #         if b > r and b > g:
            #             pixels[i, j] = (r, g, int(b * 1.2))
            # 将处理后的图片保存到输出路径
            # output_filename = os.path.splitext(filename)[0] + '_filtered.jpg'
            output_filename = filename
            img.save(os.path.join(args.output, output_filename))

print('饱和度调整处理完成！')
