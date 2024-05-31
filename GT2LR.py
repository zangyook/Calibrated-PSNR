import cv2
from torchvision import transforms as T
import os
import numpy as np

hr_root = "ML_project/dataset/newdata" #original image root
save_root = "ML_project/dataset" #LR image 저장할 root

for img in os.listdir(hr_root):
    image_root = os.path.join(hr_root,img)
    image_name = img.replace(".jpg",".png")
    image = cv2.imread(image_root)
    
    LR_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    LR_image = cv2.resize(LR_image, (0,0), fx=0.25 ,fy=0.25, interpolation = cv2.INTER_AREA) #4배 줄임
    LR_image = T.ToPILImage()(LR_image)
    save_path = os.path.join(save_root, image_name)
    LR_image.save(save_path, 'png')