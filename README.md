# Calibrated-PSNR_2022_12
#
## How to use Metrics 
### Sources
LPIPS, FID, NIQE, MA, MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI 등의 이미지 품질 평가 지표 소스는 다음 링크에서 받을 수 있다.
IQA-Pytorch install
[chaofengc/IQA-PyTorch: PyTorch Toolbox for Image Quality Assessment, including LPIPS, FID, NIQE, NRQM(Ma), MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI and more... (github.com)](https://github.com/chaofengc/IQA-PyTorch)
본 프로젝트에서는 LPIPS 코드를 다음 링크에서 따와 사용하였다. 
- lpips-pytorch install 
[S-aiueo32/lpips-pytorch: A simple and useful implementation of LPIPS. (github.com)](https://github.com/S-aiueo32/lpips-pytorch)

### Metrics
- metrics.py 파일을 이용하여 결과를 내면 된다.
- save_metrics.py
 원본 고화질 영상과 복원시킨 영상이 저장된 파일 경로를 각각 hrdirroot, srdirroot에 적어주고 metric 수치를 기록할 csv파일 경로를 save_dir에 입력해주면 된다.
#  
## Dataset 
 다음 링크에서 다운로드 받을 수 있다.
#
## SRResNet 
 다음 링크의 알고리즘을 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.

## SRGAN
 다음 링크의 알고리즘을 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.

## RankSRGAN
 다음 링크의 소스를 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.

### How to train
- Training Ranker
- Training RankSRGAN 

### How to test

## PULSE 
 다음 링크의 알고리즘을 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.

# Calibrated-PSNR_2022_12
### How to Use 
- Proposed_metric.py 파일 이용.
- SR root와 HR root 경로를 바꾸어 이용하면 된다.
 
