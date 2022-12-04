# PSNR-HJS-All-he-did

### Metrics 파일
-IQA-Pytorch install
[chaofengc/IQA-PyTorch: PyTorch Toolbox for Image Quality Assessment, including LPIPS, FID, NIQE, NRQM(Ma), MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI and more... (github.com)](https://github.com/chaofengc/IQA-PyTorch)
-lpips-pytorch install 
[S-aiueo32/lpips-pytorch: A simple and useful implementation of LPIPS. (github.com)](https://github.com/S-aiueo32/lpips-pytorch)
-save_metrics.py
 원본 고화질 영상과 복원시킨 영상이 저장된 파일 경로를 각각 hrdirroot, srdirroot에 적어주고 metric 수치를 기록할 csv파일 경로를 save_dir에 입력해준다. 

### Dataset 파일
-	GT2LR,py
고화질의 원본 영상만 존재하는 데이터세트의 저화질 영상을 만듦.
hr_root는 고화질 원본 영상만 있는 파일 경로이고 save_root는 저화질 영상을 저장할 파일 경로를 설정해주면 된다.

### SRGAN파일
-	Srgan_config
Upscale_factor와 mode(train or test), device를 정해준다. 
Train시 pretrained_g_model_weights_path를 SRGAN_x4-ImageNet-8c4a7569.pth.tar 로 설정해준다. 해당 pretrain weight는 [Lornatang/SRGAN-PyTorch: A simple and complete implementation of super-resolution paper. (github.com)](https://github.com/Lornatang/SRGAN-PyTorch) 에서 다운받을 수 있다. 
Test 시 저화질 영상과 고화질 영상, 복원 영상이 저장된 파일경로들을 각각 lr_dir, sr_dir, gt_dir에 적용해준다. G_model_weights_path는 train후 저장된 weight 중 g_best.pth.tar을 적용한다.  
