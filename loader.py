import os
import json
from PIL import Image

def main():
    # 读取文件路径
    current_path = os.path.abspath(os.getcwd())
    img_path = os.path.join(current_path,'img')
    imgs = sorted(os.listdir(img_path))

    # 转换图片大小与格式
    for img_name in imgs:
        img = Image.open(os.path.join(img_path,img_name))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((300,300),Image.ANTIALIAS)
        img.save(os.path.join(img_path,img_name))

    # 生成json文件
    imgs_name = dict(enumerate(imgs))
    json_str = json.dumps(imgs_name, ensure_ascii=False, indent=4)
    with open('imgs_indices.json', 'w') as json_file:
        json_file.write(json_str)

    

if __name__ == '__main__':
    main()