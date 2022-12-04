# PSNR-HJS-All-he-did
#
### Metrics 파일
- IQA-Pytorch install
[chaofengc/IQA-PyTorch: PyTorch Toolbox for Image Quality Assessment, including LPIPS, FID, NIQE, NRQM(Ma), MUSIQ, NIMA, DBCNN, WaDIQaM, BRISQUE, PI and more... (github.com)](https://github.com/chaofengc/IQA-PyTorch)
- lpips-pytorch install 
[S-aiueo32/lpips-pytorch: A simple and useful implementation of LPIPS. (github.com)](https://github.com/S-aiueo32/lpips-pytorch)
- save_metrics.py
 원본 고화질 영상과 복원시킨 영상이 저장된 파일 경로를 각각 hrdirroot, srdirroot에 적어주고 metric 수치를 기록할 csv파일 경로를 save_dir에 입력해준다. 
#  
### Dataset 파일
-	GT2LR,py
고화질의 원본 영상만 존재하는 데이터세트의 저화질 영상을 만듦.
hr_root는 고화질 원본 영상만 있는 파일 경로이고 save_root는 저화질 영상을 저장할 파일 경로를 설정해주면 된다.
#  
### SRGAN파일
-	Srgan_config
Upscale_factor와 mode(train or test), device를 정해준다. 
Train시 pretrained_g_model_weights_path를 SRGAN_x4-ImageNet-8c4a7569.pth.tar 로 설정해준다. 해당 pretrain weight는 [Lornatang/SRGAN-PyTorch: A simple and complete implementation of super-resolution paper. (github.com)](https://github.com/Lornatang/SRGAN-PyTorch) 에서 다운받을 수 있다. 
Test 시 저화질 영상과 고화질 영상, 복원 영상이 저장된 파일경로들을 각각 lr_dir, sr_dir, gt_dir에 적용해준다. G_model_weights_path는 train후 저장된 weight 중 g_best.pth.tar을 적용한다.  
### RankSRGAN
자세한 사항은 [XPixelGroup/RankSRGAN](https://github.com/XPixelGroup/RankSRGAN) 참조 
## How to Test  
1. Clone this github repo. 
```
git clone https://github.com/WenlongZhang0724/RankSRGAN.git
cd RankSRGAN
```
2. Place your own **low-resolution images** in `./LR` folder.
3. Download pretrained models from [Google Drive](https://drive.google.com/drive/folders/1_KhEc_zBRW7iLeEJITU3i923DC6wv51T?usp=sharing). Place the models in `./experiments/pretrained_models/`. We provide three Ranker models and three RankSRGAN models  (see [model list](experiments/pretrained_models)).
4. Run test. We provide RankSRGAN (NIQE, Ma, PI) model and you can config in the `test.py`.
```
python test.py -opt options/test/test_RankSRGAN.yml
```
5. The results are in `./results` folder.

## How to Train
## Train Ranker
1. Download [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/) and [Flickr2K](https://github.com/LimBee/NTIRE2017) from [Google Drive](https://drive.google.com/drive/folders/1B-uaxvV9qeuQ-t7MFiN1oEdA6dKnj2vW?usp=sharing) or [Baidu Drive](https://pan.baidu.com/s/1CFIML6KfQVYGZSNFrhMXmA)
2. Generate rank dataset [./datasets/generate_rankdataset/](datasets/generate_rankdataset)
3. Run command:
```c++
python train_rank.py -opt options/train/train_Ranker.yml
```
### Train RankSRGAN
We use a PSNR-oriented pretrained SR model to initialize the parameters for better quality.

1. Prepare datasets, usually the DIV2K dataset. 
2. Prerapre the PSNR-oriented pretrained model. You can use the `mmsr_SRResNet_pretrain.pth` as the pretrained model that can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1_KhEc_zBRW7iLeEJITU3i923DC6wv51T?usp=sharing). 
3. Modify the configuration file  `options/train/train_RankSRGAN.json`
4. Run command: 
```c++
python train.py -opt options/train/train_RankSRGAN.yml
```
or

```c++
python train_niqe.py -opt options/train/train_RankSRGAN.yml
```
Using the train.py can output the convergence curves with PSNR; Using the train_niqe.py can output the convergence curves with NIQE and PSNR.


