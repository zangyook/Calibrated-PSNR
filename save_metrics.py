from metrics import PSNR_score, calculate_ssim,NIQE,LPIPSscore,FID
import os
import csv

hrdirroot = "ML_project/dataset/task2/Manga109/GTmod12"
srdirroot = "ML_project/RankSRGAN/manga109_x4_bic_to_Ranksrgan"
results = []
save_dir = "ML_project/RankSRGAN/results/result_ranksrgan_manga.csv"


for file in os.listdir(srdirroot):
    imagename = file
    #jpegstr = imagename.replace('.png','.jpg')

    srimageroot = os.path.join(srdirroot, imagename)
    hrimageroot = os.path.join(hrdirroot, imagename)

    psnr_score = PSNR_score(hrimageroot, srimageroot)
    ssim_score = calculate_ssim(hrimageroot, srimageroot)
    NIQE_score = NIQE(srimageroot)
    LPIPS_score = LPIPSscore(srimageroot, hrimageroot)
    
    result = [imagename, psnr_score,ssim_score,NIQE_score,LPIPS_score]
    results.append(result)
    l = len(os.listdir(srdirroot))
    print("Get metrics!  remain : ",l-len(results))
    


listname = ["imagename","psnr","ssim","niqe","lpips","fid"]
with open(save_dir,"a",newline = '') as f:
        wr = csv.writer(f)
        wr.writerow(listname)

for i in range(len(results)):
    if i == len(results)-1:
        FID_score = FID(srdirroot, hrdirroot)
        results[i].append(FID_score)
        with open(save_dir,"a",newline = '') as f:
            wr = csv.writer(f)
            wr.writerow(results[i])
    with open(save_dir,"a",newline = '') as f:
        wr = csv.writer(f)
        wr.writerow(results[i])







