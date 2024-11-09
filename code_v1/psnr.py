from skimage import data, util,io
from skimage.metrics import peak_signal_noise_ratio 
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
from skimage.color import rgb2gray
from PIL import Image
import numpy as np

'''img_original = io.imread("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/test.bmp")
#img_original=np.array(Image.open("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/test.bmp").convert('RGB'))
print('original pic over')
img_test = io.imread("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/result.jpeg")
print('test pic over')

image = Image.open("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/test.bmp").convert('RGB')
img_original = np.array(image)

print(img_original.shape)
print(img_test.shape)
#img_test=resize(img_test,img_original.shape)
img_original=resize(img_original,img_test.shape)


psnr = peak_signal_noise_ratio(img_original, img_test)
ssim=structural_similarity(img_original, img_test,win_size=3)


print('psnr=',psnr)
print('ssim=',ssim)'''

from PIL import Image
import numpy as np

img1 = np.array(Image.open("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/test.bmp").convert('RGB'))
img2 = np.array(Image.open("/Users/cesar/Desktop/同步储存/net/code/code_v1/result.jpeg"))


print(img1.shape)
print(img2.shape)

def psnr(img1, img2):
    mse = np.mean((img1-img2)**2)
    if mse == 0:
        return 100
    else:
        return 20*np.log10(255/np.sqrt(mse))


if __name__ == "__main__":
    print('PSNR:',psnr(img1, img2))
    print('SSIM:',ssim(img1, img2, multichannel=True))