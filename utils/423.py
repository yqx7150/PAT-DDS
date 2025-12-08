from PIL import Image

def rgba_to_rgb(image_path, output_path, background_color=(255, 255, 255)):
    """
    将RGBA图像转换为RGB图像，通过指定背景颜色填充透明区域。

    参数:
        image_path (str): 输入的RGBA图像文件路径。
        output_path (str): 输出的RGB图像文件路径。
        background_color (tuple): 用于填充透明区域的背景颜色，默认为白色 (255, 255, 255)。
    """
    with Image.open(image_path) as img:
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            # 创建一个带有指定背景颜色的新图像
            background = Image.new("RGB", img.size, background_color)
            # 将原始图像粘贴到背景图像上，使用alpha通道作为掩码
            background.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
            # 保存转换后的图像
            background.save(output_path, "PNG")
        else:
            # 如果图像已经是RGB模式，直接保存
            img.save(output_path, "PNG")

if __name__ == "__main__":


    input_image_path = "/mnt/D/yxb/stable-diffusion-master/sample/sr/lr/00000334_original_suv.png"
    output_image_path = "/mnt/D/yxb/stable-diffusion-master/sample/sr/lr/00000334_original_suv_1.png"
    rgba_to_rgb(input_image_path, output_image_path)