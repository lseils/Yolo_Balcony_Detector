import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
# F:\0528shiyanjieguo\kunnan\train-yuanshi0514222222222\exp2\weights\best.pt
if __name__ == '__main__':
    model = YOLO('runs/detect/train3/weights/best.pt') # select your model.pt path
    model.predict(source='input/images', # input folder
                  imgsz=640,
                  project='detections',
                  name='exp',
                  show_labels=True,
                  save=True,
                  # conf=0.2,
                  # visualize=True # visualize model features maps
                )
    
# show_labels: 在显示时是否显示类别标签。

# show_conf: 在显示时是否显示置信度得分。
    

