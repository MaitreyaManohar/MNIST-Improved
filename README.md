

# MNIST Improved
 An improved version of MNIST with an aim to achieve 99.4% accuarcy on the validation dataset

## How to run

Just create a python environment with the libraries and packages in the starting import. Then run the ipynb, alternatively you could upload this notebook on colab and run it. Reached 99.4 accuracy

## Model Parameters

### Model Summary

| Layer (type) | Output Shape | Param # |
|---|---|---|
| Conv2d-1 | [-1, 128, 26, 26] | 1,280 |
| BatchNorm2d-2 | [-1, 128, 26, 26] | 256 |
| Dropout2d-3 | [-1, 128, 26, 26] | 0 |
| Conv2d-4 | [-1, 4, 28, 28] | 516 |
| Conv2d-5 | [-1, 16, 28, 28] | 592 |
| BatchNorm2d-6 | [-1, 16, 28, 28] | 32 |
| Dropout2d-7 | [-1, 16, 28, 28] | 0 |
| MaxPool2d-8 | [-1, 16, 14, 14] | 0 |
| Conv2d-9 | [-1, 16, 14, 14] | 2,320 |
| BatchNorm2d-10 | [-1, 16, 14, 14] | 32 |
| Dropout2d-11 | [-1, 16, 14, 14] | 0 |
| Conv2d-12 | [-1, 32, 14, 14] | 4,640 |
| BatchNorm2d-13 | [-1, 32, 14, 14] | 64 |
| MaxPool2d-14 | [-1, 32, 7, 7] | 0 |
| Conv2d-15 | [-1, 16, 7, 7] | 528 |
| Conv2d-16 | [-1, 20, 7, 7] | 2,900 |
| BatchNorm2d-17 | [-1, 20, 7, 7] | 40 |
| Conv2d-18 | [-1, 32, 7, 7] | 5,792 |
| BatchNorm2d-19 | [-1, 32, 7, 7] | 64 |
| Conv2d-20 | [-1, 10, 7, 7] | 330 |
| AvgPool2d-21 | [-1, 10, 1, 1] | 0 |

### Model Statistics

| Stat | Value |
|---|---|
| Total params | 19,386 |
| Trainable params | 19,386 |
| Non-trainable params | 0 |
| Input size (MB) | 0.00 |
| Forward/backward pass size (MB) | 2.54 |
| Params size (MB) | 0.07 |
| Estimated Total Size (MB) | 2.62 |
