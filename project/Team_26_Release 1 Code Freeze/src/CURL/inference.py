import matplotlib
from pyparsing import ParseExpression
matplotlib.use('agg')
from util import ImageProcessing
import matplotlib.pyplot as plt
from data import Adobe5kDataLoader, Dataset
import time
import torch
import torchvision.transforms as transforms
from torch.autograd import Variable
import logging
import argparse
import torch.optim as optim
import numpy as np
import datetime
import os.path
import os
import metric
import model
import sys
from PIL import Image

def main() :
    FILE_NAME = './adobe5k_dpe/curl_example_test_input/a2803-060810_075208_GM6A0020_input.png'
    MODEL = 'pretrained_models/adobe_dpe/curl_validpsnr_23.073045286204017_validloss_0.0701291635632515_testpsnr_23.584083321292365_testloss_0.061363041400909424_epoch_510_model.pt'
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    OUT_PATH = './adobe5k_dpe/curl_example_test_inference/'

    net = model.CURLNet()
    checkpoint = torch.load(MODEL, map_location=DEVICE)
    net.load_state_dict(checkpoint['model_state_dict'])
    net.eval()
    net.to(DEVICE)
    
    # img = cv2.imread(FILE_NAME)
    normaliser=2 ** 8 - 1
    print(np.shape(Image.open(FILE_NAME).convert('RGB')))
    img = ImageProcessing.normalise_image(np.array(Image.open(FILE_NAME).convert('RGB')), normaliser)
    print(np.shape(img))
    transform=transforms.Compose([transforms.ToTensor()])
    
    t_img = torch.clamp(transform(img), 0, 1)
    t_img = t_img.unsqueeze(0)
    
    
    print(np.shape(t_img))
    
    with torch.no_grad():
        output = net(t_img)

    

if __name__ == "__main__":
    main()