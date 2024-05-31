# 2022 Fall: Machine Learning(2) Team_Project 
#
# What is Calibrated-PSNR? 
### Abstract 
 SISR(Single Image Super Resolution)에서 적대적 생성모델(Generative adversarial networks) 기반의 알고리즘은 이외의 알고리즘보다 일반적으로 평가점수에서는 밀리지만 사람이 인지하기에는 차이가 없거나 오히려 더 좋을 수 있다. 이러한 현상은 기존 평가지표들의 평가방식에 어느정도 문제점이 있다는 것을 의미한다. 특히 PSNR은 픽셀 단위로 계산하며 MSE가 낮을 수록 좋기 때문에 MSE가 아닌 손실함수를 사용하는 GAN 알고리즘들은 기본적으로 감점요인을 가지고 있을 수 밖에서 없다. 따라서 우리는 GAN 기반의 알고리즘의 특성을 어느정도 고려한 새로운 평가지표 Calibrated_PSNR을 제안한다.

### Method 
아래 표와 그림을 통해 SRResNet 모델이 SRGAN 모델보다 단색 공간에서 더 높은 PSNR 점수를 받는다는 것을 확인할 수 있다. (1번은 단색 이미지의 좌측 상단, 2번은 우측 상단, 3번은 좌측 하단, 4번은 우측 하단 이미지이다.)
이를 개선하기 위해 Calibrated-PSNR에서는 이미지를 32*32로 등분한 후 각 블록의 PSNR 점수가 35 이상인 경우 배제하여 PSNR을 구한다. 
![image](https://github.com/zangyook/Calibrated-PSNR/assets/100524867/295ae1e4-ff2d-4012-bc6b-2c0a4f6719e7)
![image](https://github.com/zangyook/Calibrated-PSNR/assets/100524867/cddd0872-98d3-459e-a445-356fc5ab3aec)

### Results 
PSNR 지표와 제안한 평가지표를 비교하면, SRResNet과 SRGAN 간의 차이가 줄어든 것을 확인할 수 있다. Calibrated-PSNR 방법론을 통해 단색 공간의 영향력을 줄일 수 있다. 
![image](https://github.com/zangyook/Calibrated-PSNR/assets/100524867/80987054-e59a-4245-9c41-5a0916efe9f6)


# How to use Calibrated-PSNR metric
### How to Use 
- Proposed_metric.py 파일 이용.
- SR root와 HR root 경로를 바꾸어 이용하면 된다.

# Implement details
## Dataset 
 다음 링크에서 다운로드 받을 수 있다.
### Train
- [DIV2k](https://www.kaggle.com/datasets/joe1995/div2k-dataset)
### Test
- [Set5, Set14, BSD100, Manga109](https://cvnote.ddlee.cc/2019/09/22/image-super-resolution-datasets)
- [CelebA-HQ](https://www.kaggle.com/datasets/lamsimon/celebahq)


### GT to LR
GT2LR.py 파일을 실행하면 된다.

## Requirement
- Python 3.6.5
- PyTorch 1.1.0 
- Pillow 5.1.0
- numpy 1.14.5
- scikit-image 0.15.0

## SRResNet 
 다음 링크의 소스를 사용하였다. [SRGAN-PyTorch](https://github.com/dongheehand/SRGAN-PyTorch.git)
<br>다음의 깃허브 레포지토리를 복제하면된다.

```
git clone https://github.com/dongheehand/SRGAN-PyTorch.git
```
### Train & Test
 Train 
```
python main.py --LR_path ./LR_imgs_dir --GT_path ./GT_imgs_dir
```
Test
```
python main.py --mode test_only --LR_path ./LR_imgs_dir --generator_path ./model/SRResNet.pt
```

## SRGAN
 SRResNet과 같은 소스를 사용하였다. 훈련과 검정은 아래와 같은 명령어를 입력하면 된다.
### Train & Test
 Train 
```
python main.py --LR_path ./LR_imgs_dir --GT_path ./GT_imgs_dir
```
Test
```
python main.py --mode test_only --LR_path ./LR_imgs_dir --generator_path ./model/SRGAN.pt
```

## RankSRGAN
 논문 저자의 github 소스를 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.
 [XPixelGroup/RankSRGAN](https://github.com/XPixelGroup/RankSRGAN.git)

### How to Test 
1. 다음의 깃허브 레포지토리를 복제한다. 
```
git clone https://github.com/WenlongZhang0724/RankSRGAN.git
```
2. './LR' 폴더에 복원할 저해상도 이미지를 둔다.
3. 다음의 링크에서 사전훈련된 모델들을 다운받을 수 있다. 3가지 종류의 Ranker(NIQE, Ma, PI)와 3가지 종류으 모델(SRGAN, SRResNet, RankSRGAN)을 제공한다. [Google Drive](https://drive.google.com/drive/folders/1_KhEc_zBRW7iLeEJITU3i923DC6wv51T?usp=sharing). 모델은 './experiments/pretrained_models/'에 두어야 한다.
5. test.py 파일에서 옵션을 구성하고 검정할 수 있다.
```
python test.py -opt options/test/test_RankSRGAN.yml
```
5. 결과는 './results' 폴더에 저장된다.

### Train Ranker
1. Rank 데이터셋 생성  [./datasets/generate_rankdataset/](datasets/generate_rankdataset)
2. 명령어 입력
```c++
python train_rank.py -opt options/train/train_Ranker.yml
```

### Train RankSRGAN

1. 구성파일에서 파일 목적에 맞게 수정  `options/train/train_RankSRGAN.json`
2. 명령어 입력
```c++
python train_niqe.py -opt options/train/train_RankSRGAN.yml
```

## PULSE 
 논문 저자의 github 소스를 사용하였다. 사용 방법은 링크의 Readme.md 를 참조할 수 있다.
 [adamian98/pulse](https://github.com/adamian98/pulse)

 ### Sources
LPIPS, FID, NIQE, MA, MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI 등의 이미지 품질 평가 지표 소스는 다음 링크에서 받을 수 있다.
IQA-Pytorch install
[chaofengc/IQA-PyTorch: PyTorch Toolbox for Image Quality Assessment, including LPIPS, FID, NIQE, NRQM(Ma), MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI and more... (github.com)](https://github.com/chaofengc/IQA-PyTorch)
본 프로젝트에서는 LPIPS 계산을 위해 다음을 참조하였다.
- lpips-pytorch install 
[S-aiueo32/lpips-pytorch: A simple and useful implementation of LPIPS. (github.com)](https://github.com/S-aiueo32/lpips-pytorch)

### save_metrics.py
 원본 고화질 영상과 복원시킨 영상이 저장된 파일 경로를 각각 hrdirroot, srdirroot에 적어주고 metric 수치를 기록할 csv파일 경로를 save_dir에 입력해주면 된다.

