# Above-or-average (AOA) thresholding method

Implementation of a novel thresholding method based on the Otsu threshold specifically for the determination of the fiber volume content (FVC) of low contrast CT images of carbon fiber reinforced polyamide 6. 

## Disclaimer 
The BibTeX citation of the paper describing the scientific background and the methods underlying this repository is: 

<span style="color:gray">

    @article{BLARR2024103067,   
    title = {Novel thresholding method and convolutional neural network for fiber volume content determination from 3D μCT images},   
    journal = {NDT & E International},   
    volume = {144},   
    pages = {103067},   
    year = {2024},   
    issn = {0963-8695},   
    doi = {https://doi.org/10.1016/j.ndteint.2024.103067},   
    url = {https://www.sciencedirect.com/science/article/pii/S096386952400032X},   
    author = {Juliane Blarr and Philipp Kunze and Noah Kresin and Wilfried V. Liebig and Kaan Inal and Kay A. Weidenmann},   
    keywords = {X-ray tomography, Carbon fiber reinforced polymers, Thermoplastics, Low contrast, Deep learning},   
    abstract = {In order to determine fiber volume contents (FVC) of low contrast CT images of carbon fiber reinforced polyamide 6, a novel thresholding method and a convolutional neural network are implemented with absolute deviations from experimental values of 2.7% and, respectively, 1.46% on average. The first method is a sample thickness     based adjustment of the Otsu threshold, the so-called “average or above (AOA) thresholding”, and the second is a mixed convolutional neural network (CNN) that directly takes 3D scans and the experimentally determined FVC values as input. However, the methods are limited to the specific material combination, process-dependent microstructure     and scan quality but could be further developed for different material types.}   
    }

</span>

If you use the code in this repository, please cite the paper accordingly.

## Content

CT scans of glass fiber reinforced polymers are used to determine the fiber volume content (FVC) through image processing. However, in the case of carbon fiber reinforced polymers (CFRP), the contrast between the polymer matrix existing of C-atoms and the carbon fibers existing of C-atoms is very low. Additionally, as carbon fibers have a small diameter of 5-7 µm, the resolution has to be high in order to resolve the fibers. Both effects lead to noisy images. As the histograms of low contrast CT images do not show two peaks for the two materials but rather one single distribution, simple thresholding does not lead to good segmentation results (determined FVC had been compared to experimental values). Hence, a sample thickness-based adjustment of the Otsu threshold, the so-called "above or average (AOA) thresholding" has been implemented in this code. It is based on an empirical approach of a binary decision between the single slice Otsu threshold and the average stack Otsu threshold. Please consider the above-mentioned paper for more details.

<p align="center">
  <img src="https://github.com/jewelsbla/AOA_thresholding/blob/main/images/aoa_graphic.png?raw=true">
</p>

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
