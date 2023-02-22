import argparse
from PIL import Image

# 定义 argparse
parser = argparse.ArgumentParser(description='合并两张尺寸相同的图片')
parser.add_argument('--image1', default="cover/day.jpg", help='第一张图片的文件路径')
parser.add_argument('--image2', default="cover/night.jpg", help='第二张图片的文件路径')
parser.add_argument('--output', default="cover/cover.jpg", help='合并后的图片的输出文件路径')
args = parser.parse_args()

# 打开两张图片并将它们合并
image1 = Image.open(args.image1)
image2 = Image.open(args.image2)
width, height = image1.size
new_image = Image.new('RGB', (width, height))
new_image.paste(image1.crop((0, 0, width//2, height)), (0, 0))
new_image.paste(image2.crop((width//2, 0, width, height)), (width//2, 0))

# 保存合并后的图片
new_image.save(args.output)
print(f"已将两张图片合并到 {args.output}")
