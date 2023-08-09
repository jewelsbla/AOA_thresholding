# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:53:52 2022

@author: Juliane Blarr (juliane.blarr@kit.edu), Noah Kresin
"""

import cv2
import SimpleITK as sitk
import numpy as np
from matplotlib import pyplot as plt
import matplotlib


def density(img):
    """Calculates the density. "img" is an image file with applied thresholding filter, so a binary image."""
    pixel_ges = img.shape[0] * img.shape[1]
    val = np.count_nonzero(img)
    return val / pixel_ges


def filtering(image, i, kernel_size):
    """Determination of the fiber volume content of the image."""

    denoised = cv2.medianBlur(image, kernel_size)
    ret, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    """Uncomment these three functions to get histograms of the original image, the filtered image and the thresholded (first stage) image."""
    """
    if i == 40:
        
        plt.hist(image.ravel(),bins=256);plt.title('Original')
        plt.ylabel('Quantity');plt.xlabel('Grey-level');plt.xlim((0,255))
        plt.savefig('plots_ntp/Original_hist.png',dpi=150, bbox_inches = "tight")
        plt.show()
        plt.clf();
        
        plt.hist(denoised.ravel(), bins=256)
        plt.ylim((0, 150000))
        # plt.title('Filtered')
        plt.ylabel("Quantity")
        plt.xlabel("Grey-level intensity")
        plt.xlim((0, 255))
        plt.savefig("Filtered_hist.png", dpi=150, bbox_inches="tight")
        plt.show()
        plt.clf()
        
        plt.imshow(image);plt.title('Original Image')
        ax = plt.gca();ax.axes.xaxis.set_ticks([]);ax.axes.yaxis.set_ticks([])
        plt.savefig('plots_ntp/Original.png',dpi=150, bbox_inches = "tight")
        plt.show()
        plt.clf();plt.imshow(thresh);plt.title('First Stage')
        ax = plt.gca();ax.axes.xaxis.set_ticks([]);ax.axes.yaxis.set_ticks([])
        plt.savefig('plots_ntp/First_Stage.png',dpi=150, bbox_inches = "tight")
        plt.show()
        plt.clf()
        
    """
    return ret


def filtering2(image, T, i, kernel_size):
    """Determination of the FVC of the image (second stage)."""

    denoised = cv2.medianBlur(image, kernel_size)
    ret, thresh = cv2.threshold(denoised, T, 255, cv2.THRESH_BINARY)
    brightness = np.sum(image) / (np.shape(image)[0] * np.shape(image)[1])

    """Uncomment to see the visualization of one particular image after second stage thresholding."""
    """
    if i == 40:
        plt.imshow(thresh)
        plt.title("Second Stage")
        ax = plt.gca()
        ax.axes.xaxis.set_ticks([])
        ax.axes.yaxis.set_ticks([])
        # plt.savefig('plots_ntp/Second_Stage.png',dpi=150, bbox_inches = "tight")
        plt.show()
        plt.clf()
    """

    return density(thresh), brightness


if __name__ == "__main__":
    twoStages = True
    result_file = False
    kernel_size = 23
    """Change kernel size of 23 above to 15 for FLD_1, FLD_2, FLD_3, FLD_10, FLD_11 and FLD_12."""
    # kernel_size = 15

    file = "C1_8bit.mhd"
    # file = sys.argv[1]

    plt.rcParams.update(plt.rcParamsDefault)
    matplotlib.rcParams["mathtext.fontset"] = "stix"
    matplotlib.rcParams["font.family"] = "STIXGeneral"
    matplotlib.rcParams.update({"font.size": 28})  # 18

    itk_image = sitk.ReadImage(file)
    image_array = sitk.GetArrayViewFromImage(itk_image)
    print(file[0:-4])
    print(image_array.shape)

    T = []
    for i in range(0, image_array.shape[0]):
        T.append(filtering(image_array[i], i, kernel_size))

    T_av = int(sum(T) / len(T))
    T_max = max(T)
    print(T_max, T_av)
    T_new = []
    FVC_cur = []
    brightness = []
    T_normed = []
    for i in range(0, len(T)):
        if twoStages == True:
            T_akt = max(T[i], T_av)
        elif twoStages == False:
            T_akt = T[i]
        T_new.append(T_akt)
        FVC_im, brightness_im = filtering2(image_array[i], T_akt, i, kernel_size)
        FVC_cur.append(FVC_im)
        brightness.append(brightness_im / 255)
        T_normed.append(T_akt / brightness_im)
    FVC_final = sum(FVC_cur) / len(FVC_cur)
    print("FVC:", FVC_final)

    # Plot threshold value.
    plt.clf()
    plt.plot(T)
    plt.plot([0, len(T)], [T_av, T_av])
    plt.plot(T_new)
    plt.xlabel("Slices/-")
    plt.ylabel("Threshold Values/-")
    plt.title(file[0:-4])
    plt.savefig("{}_value.png".format(file[0:-9]), dpi=150, bbox_inches="tight")
    # plt.show()

    # Plot FVC.
    plt.clf()
    plt.plot(FVC_cur)
    plt.plot([0, len(FVC_cur)], [FVC_final, FVC_final])
    plt.xlabel("Slices/-")
    plt.ylabel("FVC/-")
    # plt.suptitle('FVC: {:.5f}'.format(FVC_final))
    plt.title("{};  FVC: {:.5f}".format(file[0:-4], FVC_final))
    plt.savefig("{}_fvc.png".format(file[0:-9]), dpi=150, bbox_inches="tight")
    # plt.show()
    plt.clf()

    """Uncomment the following part in order to get brightness plots across the stack and the brightness-normed threshold values."""
    """
    #Plot Brightness
    plt.clf()
    plt.plot(brightness)
    plt.ylim((0,0.8))
    plt.xlabel('Slices/-')
    plt.ylabel('Brightness/-')
    plt.title(file[0:-4])
    plt.savefig('{}_brightness.png'.format(file[0:-9]),dpi=150, bbox_inches = "tight")
    #plt.show()
    
    #Plot normed Fiber Volume Content
    plt.clf()
    plt.plot(T_normed)
    #plt.ylim((0,2))
    plt.xlabel('Slices/-')
    plt.ylabel('Threshold Values/Brightness / -')
    plt.title(file[0:-4])
    plt.savefig('{}_value_normed.png'.format(file[0:-9]),dpi=150, bbox_inches = "tight")
    #plt.show()
    plt.clf()
    """

    if result_file == True:
        with open("results.txt", "a") as f:
            print("{}: {}".format(file[0:-9], FVC_final), file=f)
