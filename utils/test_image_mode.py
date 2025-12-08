from PIL import Image
import numpy as np
c = Image.open("/mnt/D/yxb/stable-diffusion-master/sample/sr/lr/00000334_original_suv.png")
print(np.array(c).shape)