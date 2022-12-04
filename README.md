# Calibrated-PSNR_2022_12
## Dataset 
 다음 링크에서 다운로드 받을 수 있다.

## SRResNet 
 다음 링크의 소스를 사용하였다. [SRGAN-PyTorch](https://github.com/dongheehand/SRGAN-PyTorch.git)
다음의 깃허브 레포지토리를 복제하면된다.
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
1. Rank 데이터셋을 생성  [./datasets/generate_rankdataset/](datasets/generate_rankdataset)
2.다음과 같은 명령어를 입력하라.
```c++
python train_rank.py -opt options/train/train_Ranker.yml
```

### Train RankSRGAN

1. 구성파일에서 팡리 목적에 맞게 수정한다.  `options/train/train_RankSRGAN.json`
2. 다음의 명령어를 입력하면 된다.
```c++
python train_niqe.py -opt options/train/train_RankSRGAN.yml
```

## PULSE 
 다음 링크의 알고리즘을 사용하였다. 사용 방법은 링크의 Readme.md 를 이용하면 된다.

## How to use Metrics 
### Sources
LPIPS, FID, NIQE, MA, MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI 등의 이미지 품질 평가 지표 소스는 다음 링크에서 받을 수 있다.
IQA-Pytorch install
[chaofengc/IQA-PyTorch: PyTorch Toolbox for Image Quality Assessment, including LPIPS, FID, NIQE, NRQM(Ma), MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI and more... (github.com)](https://github.com/chaofengc/IQA-PyTorch)
본 프로젝트에서는 LPIPS 코드를 다음 링크에서 따와 사용하였다. 
- lpips-pytorch install 
[S-aiueo32/lpips-pytorch: A simple and useful implementation of LPIPS. (github.com)](https://github.com/S-aiueo32/lpips-pytorch)

### save_metrics.py
 원본 고화질 영상과 복원시킨 영상이 저장된 파일 경로를 각각 hrdirroot, srdirroot에 적어주고 metric 수치를 기록할 csv파일 경로를 save_dir에 입력해주면 된다.


# Calibrated-PSNR_2022_12
### How to Use 
 *(파일 이름)의 파일을 이용하면 된다.
