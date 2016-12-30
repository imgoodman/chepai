import numpy as np
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf
from skimage.measure import label,regionprops

from sklearn.utils import check_random_state

from sklearn.preprocessing import OneHotEncoder

from matplotlib import pyplot as plt

def create_captcha(text, shear=0, size=(100,24)):
    im =Image.new('L',size,'black')
    draw = ImageDraw.Draw(im)

    font=ImageFont.truetype('',22)
    draw.text((2,2),text,fill=1,font=font)

    image = np.array(im)

    affine_tf = tf.AffineTransform(shear=shear)
    image = tf.warp(image,affine_tf)
    return image/image.max()#对图像特征进行归一化处理 确保特征值落在0-1之间


def test_create_captcha():
    image = create_captcha("GENE",shear=0.5)
    plt.imshow(image,cmap='Greys')


def segment_image(image):
    labeled_image = label(image>0)
    subimages=[]
    for region in regionprops(labeled_image):
        start_x,start_y,end_x,end_y = region.bbox
        subimages.append(image[start_x:end_x,start_y:end_y])
    if len(subimages)==0:
        return [image,]
    return subimages


def test_segment_image():
    image = create_captcha("GENE",shear=0.5)
    subimages = segment_image(image)
    f,axes = plt.subplots(1,len(subimages),figsize=(10,3))
    for i in range(len(subimages)):
        axes[i].imshow(subimages[i],cmap='gray')

random_state=check_random_state(14)
letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
shear_values= np.arange(0,0.5,0.05)

def generate_sample(random_state=None):
    random_state=check_random_state(random_state)
    letter = random_state.choice(letters)
    shear=random_state.choice(shear_values)
    return create_captcha(letter,shear,size=(20,20)),letters.index(letter)

def generate_train_data():
    dataset,targets = zip( *(generate_sample(random_state) for i in range(3000)  )  )
    dataset=np.array(dataset,dtype='float')
    targets=np.array(targets)

    onehot =OneHotEncoder()
    y=onehot.fit_transform(targets.reshape(targets.shape[0],1))
    y=y.todense()