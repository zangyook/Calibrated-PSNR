import csv
from PIL import Image
import numpy as np
import os
import math

def PSNR_score(hrimage, srimage):

        srimage = np.array(srimage)
        hrimage = np.array(hrimage)

        mse = np.mean((hrimage-srimage)**2)
        if mse ==0:
            return ("Can't calculate / mse = 0")
        else:
            return 20* math.log10(255.0 / math.sqrt(mse))

def PSNR_HJS(hrdirroot, srdirroot, threshold, result_csv):
    filedir = os.listdir(srdirroot)
    filedir = filedir[:101]
    for file in filedir:
        srimg = Image.open(os.path.join(srdirroot,file))
        #file = file.replace("_0.png",".jpg")
        hrimg = Image.open(os.path.join(hrdirroot, file))

        grid_w = 32
        grid_h = 32
        #print(himg.width, himg.height)
        range_w = (int)(hrimg.width/grid_w)
        range_h = (int)(hrimg.height/grid_h)
        #print(range_w, range_h)
        save = open(r'PSNR_HJS.txt', 'w')
        i = 0
        batchnum=float(0)
        mses=float(0)
        R=float(255)
        for w in range(range_w):
            for h in range(range_h):
                bbox = (h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
                crop_himg = hrimg.crop(bbox)
                crop_simg = srimg.crop(bbox)
                if isinstance(PSNR_score(crop_himg, crop_simg), str)==False and PSNR_score(crop_himg, crop_simg)< threshold:
                
                    batchnum+=1.0
                    mse_i=R**2/(10**(PSNR_score(crop_himg,crop_simg)/10) )
                    mses+=mse_i
                a=str(h*grid_h)+' '+str(w*grid_w)+' '+str((h+1)*(grid_h))+' '+str((w+1)*(grid_w))+'=>'+str(PSNR_score(crop_himg,crop_simg))+'\n'
                save.write(a)
                i += 1
        save.close
        
        if mses==0 and batchnum ==0:
            result = [threshold, round(PSNR_score(hrimg,srimg))]
        else:
            mses/=batchnum
            PSNR=10*math.log10(R**2/mses)
            result = [threshold, round(PSNR,2)]
        with open(result_csv,"a",newline = '') as f:
            wr = csv.writer(f)
            wr.writerow(result)



srdir_resnet = "ML_project/SRResNet/manga109_srresnet"
srdir_srgan = "ML_project/SRGAN/result/manga109"
gtdir_resnet = "ML_project/dataset/task2/Manga109/GTmod12"
ranksrgan = "ML_project/RankSRGAN/manga109_x4_bic_to_Ranksrgan"

result_csv = "newresult/srgan_proposediqa_manga109.csv"


threshold = 35
print("threshold:",threshold)
PSNR_HJS(gtdir_resnet, ranksrgan,threshold, result_csv)