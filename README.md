<div align="center">

# Modfied version of SAMURAI made to run on Mac machines of the M series

[Cheng-Yen Yang](https://yangchris11.github.io), [Hsiang-Wei Huang](https://hsiangwei0903.github.io/), [Wenhao Chai](https://rese1f.github.io/), [Zhongyu Jiang](https://zhyjiang.github.io/#/), [Jenq-Neng Hwang](https://people.ece.uw.edu/hwang/)

[Information Processing Lab, University of Washington](https://ipl-uw.github.io/) 
</div>
This repository is the modified implementation of SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory

## Getting Started

#### SAMURAI Installation 

SAM 2 needs to be installed first before use. The code requires `python>=3.10`, as well as `torch>=2.3.1` and `torchvision>=0.18.1`. Please follow the instructions [here](https://github.com/facebookresearch/sam2?tab=readme-ov-file) to install both PyTorch and TorchVision dependencies. You can install **the SAMURAI version** of SAM 2 on a M series machine using:
```
cd sam2
pip install -e .
```

Please see [INSTALL.md](https://github.com/facebookresearch/sam2/blob/main/INSTALL.md) from the original SAM 2 repository for FAQs on potential issues and solutions.

Install other requirements:
```
pip install matplotlib==3.7 tikzplotlib jpeg4py opencv-python lmdb pandas scipy loguru
```

#### SAM 2.1 Checkpoint Download

```
cd checkpoints && \
./download_ckpts.sh && \
cd ..
```

#### Data Preparation

Please prepare the data in the following format:
```
data/LaSOT
├── airplane/
│   ├── airplane-1/
│   │   ├── full_occlusion.txt
│   │   ├── groundtruth.txt
│   │   ├── img
│   │   ├── nlp.txt
│   │   └── out_of_view.txt
│   ├── airplane-2/
│   ├── airplane-3/
│   ├── ...
├── basketball
├── bear
├── bicycle
...
├── training_set.txt
└── testing_set.txt
```

#### Main Inference
```
python scripts/main_inference.py 
```

## Demo on Custom Video

To run the demo with your custom video or frame directory, use the following examples:

**Note:** The `.txt` file contains a single line with the bounding box of the first frame in `x,y,w,h` format while the SAM 2 takes `x1,y1,x2,y2` format as bbox input.

### Input is Video File

```
python scripts/demo.py --video_path <your_video.mp4> --txt_path <path_to_first_frame_bbox.txt>
```

### Input is Frame Folder
```
# Only JPG images are supported
python scripts/demo.py --video_path <your_frame_directory> --txt_path <path_to_first_frame_bbox.txt>
```

## FAQs
**Question 1:** Does this project need configuration?

**Answer 1:** Yes, I don't know how this thing is even running, I just know it is partialy working based on my tests.

**Question 2:** It doesn't work on my machine.

**Answer 2:** Good fucking luck, I will try to help but I spent days just to debug some of this stuff, and also, I'm a kid, I don't know shit.

**Question 3:** I got an error because of the aten::upsample_bicubic2d.out is not supported.

**Answer 3:** Unfortunately, as I'm writing this the torch does not have implemented this so you have to set the variable PYTORCH_ENABLE_MPS_FALLBACK to 1 with the command:
```
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

**Question 4:** What is the average time to run the program?

**Answer 4:** It depends, on the tests that I run on an M4 with 16GB of ram it runs in 9 minutes.

## Acknowledgment

This project is built on top of [SAMURAI](https://github.com/yangchris11/samurai) by yangchris11

SAMURAI is built on top of [SAM 2](https://github.com/facebookresearch/sam2?tab=readme-ov-file) by Meta FAIR.

The VOT evaluation code is modifed from [VOT Toolkit](https://github.com/votchallenge/toolkit) by Luka Čehovin Zajc.

## Citation

The original authors of the SAMURAI project and the base project SAM2
```
@article{ravi2024sam2,
  title={SAM 2: Segment Anything in Images and Videos},
  author={Ravi, Nikhila and Gabeur, Valentin and Hu, Yuan-Ting and Hu, Ronghang and Ryali, Chaitanya and Ma, Tengyu and Khedr, Haitham and R{\"a}dle, Roman and Rolland, Chloe and Gustafson, Laura and Mintun, Eric and Pan, Junting and Alwala, Kalyan Vasudev and Carion, Nicolas and Wu, Chao-Yuan and Girshick, Ross and Doll{\'a}r, Piotr and Feichtenhofer, Christoph},
  journal={arXiv preprint arXiv:2408.00714},
  url={https://arxiv.org/abs/2408.00714},
  year={2024}
}

@misc{yang2024samurai,
  title={SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory}, 
  author={Cheng-Yen Yang and Hsiang-Wei Huang and Wenhao Chai and Zhongyu Jiang and Jenq-Neng Hwang},
  year={2024},
  eprint={2411.11922},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2411.11922}, 
}
```
