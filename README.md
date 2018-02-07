# A magnetic field cloak for charged particle beams.

This is the analysis code for the EIC Detector R&D project to build and test a magnetic field for charged particle beams.

The Python macros that were used for the final analysis and plotting of the measurements (as published in our [article](https://www.sciencedirect.com/science/article/pii/S0168900217310045) in Nuclear Instruments and Methods in Physics Research) are located in the following folders:

* [pycloak/shielding_pub17](pycloak/shielding_pub17)
* [pycloak/ferromagnet_pub17](pycloak/ferromagnet_pub17)
* [pycloak/cloaking_pub17](pycloak/cloaking_pub17)

### How to get the data:

* In parent directory (```cd ..```), clone https://github.com/SBU-DetectorRnD/magcloak-data-calib

* If you want to calibrate data yourself, also clone https://github.com/SBU-DetectorRnD/magcloak-data


### How to calibrate data:

* ```cd calibration```

* ```cd data``` and copy files from Dropbox here if they are missing 

* ```cd -``` (i.e. go back to MagCloak_Analysis/calibration)

* edit file <filelist> with list of data files you want to calibrate

* run one of these depending on code used to record data:
 * ```ipython3 calibrateData_Gaussmeter.py <filelist>```
 * ```ipython3 calibrateData_MegaVIEW.py <filelist>```


