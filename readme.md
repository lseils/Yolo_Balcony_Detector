# YOLO Balcony Detector


![Example](images/Framework.png)




Lydia Seils
M.S. Architecture (Computational Design) - Georgia Tech 
www.linkedin.com/in/lydia-seils
Lydiamseils@gmail.com
https://lseils.github.io/


--------
## Overview

This Repository includes a Detection Model for Balconies specifically

This is a YOLOv8 trained model with BFA-YOLO architecture



## About

This model was trained for the purpose of being used in other research: A Computational Framework for Assessing Balcony Plug-and-Play Solar Photovoltaic Potential at the Neighborhood Scale

To see this research: https://github.com/SustainableUrbanSystemsLab/ARCH-8833-Lydia


This is a YOLOv8 trained model with BFA-YOLO architecure. BFA-YOLO is a trained model specifically for detection of facade elements. Although their is a balcony class, the dataset and other dependencies are not made available requiring the need for training for balconies with available data that would work for the research. The reason for training YOLOv8 is for its benefits, like it's massive ecosystem, active maintenance, simple API, and easy export options. The value in training the model with BFA-YOLO architecture is it's FBSM (Feature Balanced Spindle Module), TDATH (Target Dynamic Alignment Task Detection Head), and PMESA (Position Memory Enhanced Self-Attention). FBSM handles the fact that balconies vary widly in size across and image. TDATH catches balconies even when part of them is hidden or cut off. PMESA helps the model remember context and position avoiding false positives since non balcony railings can look just like balcony railings. 

To see BFA-YOLO: https://github.com/CVEO/BFA-YOLO


## Methods 

1. Image Collection

  Since the use of this model is for a research project uses google street view images, it was important that the data was at the same type of quality. So the images for training were taken from going around on google maps, finding balconies on buildings, and taking screenshots. In this process, multiple shots of each building were taken so that there would be different FOV, Angles, Lighting, Scale, and portions of the building. Including more variables helps the model to be more robust. 400 images were collected
    

2. AnyLabeling

  AnyLabeling was used to label all of the photos. Polygons were drawn around each balcony. AnyLabeling then output JSON files of the labeled data.

  To see Label Anything: https://anylabeling.nrl.ai/


3. Data Conversion

  AnyLabeling outputs JSON but traing data requires a specific file type. Bounding boxes were generated around the polygons within the JSON files, then output as txt files which is the correct data type that the model needs to be trained.

  To see repo that did this conversion: https://github.com/lseils/AnythingLabeling


4. Actual Training


## Usage




To Detect: *details*
```
commands
```


## Results



## Discussion



## References




