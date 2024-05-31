import os
import pyiqa
import numpy as np
import torchvision.transforms as T
from PIL import Image
import cv2
import math
from lpips_pytorch import LPIPS, lpips


######################################################
################ PSNR ###############################
#####################################################

def PSNR_score(hrimageroot, srimageroot):
        srimage = Image.open(srimageroot)
        hrimage = Image.open(hrimageroot)

        srimage = np.array(srimage)
        hrimage = np.array(hrimage)

        mse = np.mean((hrimage-srimage)**2)
        if mse ==0:
            return ("Can't calculate / mse = 0")
        else:
            return 20* math.log10(255.0 / math.sqrt(mse))



#########################################################3
###################### SSIM ###############################
##########################################################

def ssim(hrimage, srimage):
    C1= (0.01 *255)**2
    C2 = (0.03 * 255)**2
 
    hrimage = hrimage.astype(np.float64)
    srimage = srimage.astype(np.float64)

    kernel = cv2.getGaussianKernel(11,1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(hrimage, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(srimage, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(hrimage**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(srimage**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(hrimage * srimage, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()




def calculate_ssim(hrimageroot, srimageroot):
    srimage = Image.open(srimageroot)
    hrimage = Image.open(hrimageroot)

    srimage = np.array(srimage)
    hrimage = np.array(hrimage)

    if not hrimage.shape == srimage.shape:
        print("'Input images must have the same dimensions")
    if hrimage.ndim == 2:
        return ssim(hrimage, srimage)
    elif hrimage.ndim == 3:
        if hrimage.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(hrimage,srimage))
            return np.array(ssims).mean()
        elif hrimage.shape[2] == 1:
            return ssim(np.squeeze(hrimage), np.squeeze(srimage))

#######################################################################
####################### LPIPS #########################################
#######################################################################



def LPIPSscore(srroot, hrroot):
    srimage = Image.open(srroot)
    hrimage = Image.open(hrroot)

    srtensor = T.ToTensor()(srimage)
    hrtensor = T.ToTensor()(hrimage)

    criterion = LPIPS( net_type='vgg',  version='0.1')

    loss = criterion(srtensor, hrtensor)
    loss = lpips(srtensor, hrtensor, net_type='vgg', version='0.1')

    return loss.item()


#######################################################################
########################## NIQE #######################################
#######################################################################

def NIQE(srroot, device = "cuda:3"):
    srimage = Image.open(srroot)
    srtensor = T.ToTensor()(srimage)
    srtensor = srtensor.unsqueeze(0)

    niqe = pyiqa.create_metric('niqe', device = device)
    niqe_score = niqe(srtensor, color_space = 'ycbcr')

    return niqe_score.item()

##################################################################
##################### FID #######################################
#################################################################

def FID(srdirroot, hrdirroot, device = "cuda:3"):
    fid = pyiqa.create_metric('fid', device = device)
    fid_score = fid(srdirroot, hrdirroot)
    
    return(fid_score.item())
